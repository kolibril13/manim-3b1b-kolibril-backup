
import scipy as sci
from manimlib.imports import *
class TwoBody(ThreeDScene):
    def construct(self):
        #Define universal gravitation constant
        axes=ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES,theta=45 * DEGREES)

        self.add(axes)
        #self.begin_ambient_camera_rotation(rate=0.2)
        G=6.67408e-11 #N-m2/kg2#Reference quantities
        m_nd=1.989e+30 #kg #mass of the sun
        r_nd=5.326e+12 #m #distance between stars in Alpha Centauri
        v_nd=30000 #m/s #relative velocity of earth around the sun
        t_nd=79.91*365*24*3600*0.51 #s #orbital period of Alpha Centauri#Net constants
        K1=G*t_nd*m_nd/(r_nd**2*v_nd)
        K2=v_nd*t_nd/r_nd
        #Define masses
        m1=1.1 #Alpha Centauri A
        m2=0.907 #Alpha Centauri B#Define initial position vectors
        r1=[-0.5,0,0] #m
        r2=[0.5,0,0] #m#Convert pos vectors to arrays
        A=Sphere(pos=r1)
        B=Sphere(pos=r2)
        A.scale(0.1)
        B.scale(0.1)
        A.set_color(BLUE_E)
        B.set_color(RED_E)
        r1=sci.array(r1,dtype="float64")
        r2=sci.array(r2,dtype="float64")#Find Centre of Mass
        r_com=(m1*r1+m2*r2)/(m1+m2)#Define initial velocities
        v1=[0.01,0.01,0] #m/s
        v2=[-0.05,0,-0.1] #m/s#Convert velocity vectors to arrays
        v1=sci.array(v1,dtype="float64")
        v2=sci.array(v2,dtype="float64")#Find velocity of COM
        v_com=(m1*v1+m2*v2)/(m1+m2)
        #A function defining the equations of motion
        #Package initial parameters
        def TwoBodyEquations(w,t,G,m1,m2):
            r1=w[:3]
            r2=w[3:6]
            v1=w[6:9]
            v2=w[9:12]

            r=sci.linalg.norm(r2-r1) #Calculate magnitude or norm of vector

            #self.camera_frame.set_height(r,rate_func=smooth)
            dv1bydt=K1*m2*(r2-r1)/r**3
            dv2bydt=K1*m1*(r1-r2)/r**3
            dr1bydt=K2*v1
            dr2bydt=K2*v2
            r_derivs=sci.concatenate((dr1bydt,dr2bydt))
            derivs=sci.concatenate((r_derivs,dv1bydt,dv2bydt))
            return derivs
        init_params=sci.array([r1,r2,v1,v2]) #create array of initial params
        init_params=init_params.flatten() #flatten array to make it 1D
        time_span=sci.linspace(0,8,300) #8 orbital periods and 500 points
        #Run the ODE solver
        import scipy.integrate
        two_body_sol=sci.integrate.odeint(TwoBodyEquations,init_params,time_span,args=(G,m1,m2))
        r1_sol=two_body_sol[:,:3]
        r2_sol=two_body_sol[:,3:6]
        Path_A=VMobject()
        Path_B=VMobject()
        Path_B.set_points_smoothly(r2_sol)
        Path_A.set_points_smoothly(r1_sol)
        Path_A.set_color(RED_E)
        Path_B.set_color(BLUE_E)
        a_temp=Path_A.copy()
        b_temp=Path_B.copy()
        a_temp.set_style(stroke_opacity=0)
        b_temp.set_style(stroke_opacity=0)
        self.add(A,B)
        self.play(MoveAlongPath(A,a_temp),MoveAlongPath(B,b_temp),ShowCreation(Path_A),ShowCreation(Path_B),run_time=3)
    def Sphere(pos=[0,0,0],color=RED):
        Sphere=ParametricSurface(
            lambda u, v: np.array([
                pos[0]+1.5*np.cos(u)*np.cos(v),
                pos[1]+1.5*np.cos(u)*np.sin(v),
                pos[2]+1.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[f"{color}_D", f"{color}_E"],
            resolution=(15, 32))
        return Sphere

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "TwoBody"
    os.system(command_A + command_B)

