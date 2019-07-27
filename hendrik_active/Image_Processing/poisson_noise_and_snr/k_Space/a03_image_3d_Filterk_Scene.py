from manimlib.imports import *
import cmath
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.FLOWER import FLOWER
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.a01_image_3d_main import K_Space,Realspace
global k_plane_size
k_plane_size=0.7


class Nearly_Empty_Fourier(ThreeDScene):
    CONFIG = {
        "flower_value_start": 0,
        "flower_value_end": 360
    }

    def construct(self):

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES) #2.5D
        self.begin_ambient_camera_rotation(rate=0.01)  # Start move camera

        def get_amp_array(z):
            return abs(z)

        def get_phi_array(z):
            phi=[[cmath.phase(z_row) for z_row in z_col] for z_col in z]
            return np.rad2deg(phi)
        #setup the sizes and arrays
        pixels=7
        k_space_ar= np.zeros((pixels, pixels), dtype=complex)
        ##
        def get_angle_phi(phi_deg):
            all= VGroup()
            r=255
            phi=phi_deg
            z=r * np.exp(1j * phi)
            k_space_ar[4,3]=z

            amp_ar=get_amp_array(k_space_ar)
            phi_ar=get_phi_array(k_space_ar)
            # print(phi_ar)
            k_space_ar_shift= np.fft.ifftshift(k_space_ar)
            real_out_ar =  np.fft.ifft2(k_space_ar_shift)

            # setup the k_plane
            k_plane = K_Space(pixel_len=pixels)
            k_plane.set_x(0)
            k_plane.set_y(0)
            k_plane.set_z(-0.01)
            k_plane.fill_k_space(amp_ar, dots_lines=True)
            k_plane.set_phase_flowers(amp_ar,phi_ar)
            k_plane.scale_about_point(9 / pixels * k_plane_size, ORIGIN)
            k_plane.set_shade_in_3d(True)
            all.add(k_plane)
            # setup the real_out_plane
            real_out_plane = Realspace(pixel_len=pixels)
            real_out_plane.fill_real_space(real_out_ar.real)
            real_out_plane.scale(9 / pixels * k_plane_size * 0.4).to_edge(UR)
            all2=real_out_plane
            return all,all2
        flow_tracker=ValueTracker(0)

        def flower_updater_a(a1):
            a2,b2=get_angle_phi(flow_tracker.get_value())
            a1.become(a2)

        def flower_updater_b(b1):
            a2,b2=get_angle_phi(flow_tracker.get_value())
            b1.become(b2)

        a1,b1=get_angle_phi(0)
        self.add(a1)
        self.add_fixed_in_frame_mobjects(b1)
        a1.add_updater(flower_updater_a)
        b1.add_updater(flower_updater_b)

        self.play(flow_tracker.set_value, self.flower_value_end ,run_time=5)


class More_Filled_Fourier(ThreeDScene):
    CONFIG = {
        "flower_value_start": 0,
        "flower_value_end": 360
    }

    def construct(self):

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES) #2.5D
        self.begin_ambient_camera_rotation(rate=0.01)  # Start move camera
        self.camera.frame_center.shift(2 * OUT)

        def get_amp_array(z):
            return abs(z)

        def get_phi_array(z):
            phi=[[cmath.phase(z_row) for z_row in z_col] for z_col in z]
            return np.rad2deg(phi)
        #setup the sizes and arrays
        pixels=7
        raster_size= (pixels,pixels)
        # k_space_ar= np.zeros((pixels, pixels), dtype=complex)
        r = np.random.uniform(0, 255, raster_size)  # setup function
        phi_rad = np.full(raster_size, 5)
        img_k_space = r * np.exp(1j * phi_rad)
        img_kamp = np.abs(img_k_space)
        img_kph = (np.angle(img_k_space, deg=True))
        ##
        def get_angle_phi(phi_deg):
            all= VGroup()
            r=255
            phi=phi_deg
            z=r * np.exp(1j * phi)
            img_k_space[4,3]=z

            amp_ar=get_amp_array(img_k_space)
            phi_ar=get_phi_array(img_k_space)
            # print(phi_ar)
            k_space_ar_shift= np.fft.ifftshift(img_k_space)
            real_out_ar =  np.fft.ifft2(k_space_ar_shift)

            # setup the k_plane
            k_plane = K_Space(pixel_len=pixels)
            k_plane.set_x(0)
            k_plane.set_y(0)
            k_plane.set_z(-0.01)
            k_plane.fill_k_space(amp_ar, dots_lines=True)
            k_plane.set_phase_flowers(amp_ar,phi_ar)
            k_plane.scale_about_point(9 / pixels * k_plane_size, ORIGIN)
            k_plane.set_shade_in_3d(True)
            all.add(k_plane)
            # setup the real_out_plane
            real_out_plane = Realspace(pixel_len=pixels)
            real_out_plane.fill_real_space(real_out_ar.real)
            real_out_plane.scale(9 / pixels * k_plane_size * 0.4).to_edge(UR)
            all2=real_out_plane
            return all,all2
        flow_tracker=ValueTracker(0)

        def flower_updater_a(a1):
            a2,b2=get_angle_phi(flow_tracker.get_value())
            a1.become(a2)

        def flower_updater_b(b1):
            a2,b2=get_angle_phi(flow_tracker.get_value())
            b1.become(b2)

        a1,b1=get_angle_phi(0)
        self.add(a1)
        self.add_fixed_in_frame_mobjects(b1)
        a1.add_updater(flower_updater_a)
        b1.add_updater(flower_updater_b)

        self.play(flow_tracker.set_value, self.flower_value_end ,run_time=5)



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -l  -p  -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"More_Filled_Fourier"
    os.system(command_A + command_B)