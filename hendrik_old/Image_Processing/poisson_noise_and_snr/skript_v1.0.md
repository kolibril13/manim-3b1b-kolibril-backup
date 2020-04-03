#Possion Noise, SNR and the brilliance of human eyes

Ideas: for who is this video?
Science interested people, who must not have a physiciscist background
Which language?
First of all German, but in more general in english.
How long?
about 5 minutes.





## Szene 1

Let's see too images:
One of it at sunlight:
the object is perfectly visible
Second one:
Same at nightlight:
The image is kind of blurry, less details with the camera, while we still can see quite good at night.
**TODO find out how many photons from moon**
From the moon we recive ### photons per second per squaremeter, so why can't we make good pictures?
And when can we actually capture good pictures?

> Picture bright,
> Picture dark

## Szene 2
Lets consider this exerimental setup: a constant light source, a directed light beam to the right side, where we assume that 
* light goes only in z direction (no transverse  light component in x or y direction )
* The light source is an exendend plane (e.g.can be thought of as an arry 32x32 LEDs), which emits exactly 10 photons per second per squarecentimeter.
* the detector is perfect and can detect every single photon.

--> When we read now the signal from all detctors, we would recive an image that looks perfectly like the original.
> 1 Experimental setup with all equal

Now we can also introduce the histogram of the image, on the x-axis we see the intensity of the pixel (from 0 to 255) and on the y axis the amount of pixels that have this discrete value.

> 2 Variation of the intensity level 

*TODO: IDEA Maybe add also white noise with different volume*

ok, now it is time to add some more power to the light source: the result: the intensity in the histogram is increasing and decreasing.

## Szene 3
 
 But now lets consider a more realistic scenrio.
 Due to the quantum nature of light, we have  an uncertanty in the flux of photons. 
 
 The process of photon creation is a random process, and in reality we can't say: a photon flux of 10 photons per second.
 
 It is only possible to say: in *average* 10 photons per second.
 
 To go deeper into this statsitics, we can compare the creation of a photon with a coin flip experiment.
 The creation of a photon can be assicioated with "head", and the case of no creation with "tail".
 
 > coin sides
 
 When we start to throw 20 coins, we would expect 10 head and 10 tail, however reaility 
 it might be 11:9, 8:12 or similar.
 
 
 > Insert images
 
 But let's just do this experiment!
 Or more convinent: look in the internet if someone already made this experiment.
 And yes, a ##TODO: Look up the details, the Statistiker was looked up by the Nazis in a prison and made this experiment over and over. The results of his coin flip experiments can be found in this book.
 
 Now it is time to throw 100 times 20 coins and add every single coin experiment to an histogram.
 
 And we see.. a poisson distribution
 
 >  Insert Poisson image from wiki
 
 #Szene 4
 
 The same laws apply when we consider the creation of photons, which can be seen on the screen as poisson noise.
 
 > Every single has an other value for time t=0s
 
 > Every single has another value for t=1s
 
 Lets run it for a few seconds, increase and decrease the power of the light source
 
 #Szene 5 
 
 Ok, with this assumptions, we can now capute an object. Easiest case: an round scheibe, which absorbs 3 % of the light and transmitts the rest 97 %.
 When we have a low light power, the poisson disribution is dominant for the overall image, but the more intensity we add, the more contrast we add to our image.
 
 #Szene 6
 We can see now: more light power means more contrast, and not we only miss something to physialisch feslegen, we are looking for a parameter which tells us when something is visible. 
 This is the sound to noise ratio.
 And it is quite intuitive: we take a squre in the middle of the object, and devide this by a squre in the middle of the background.
 
 # Szene 7
 Other noise creation in detectors
 1. photon noise, poisson noise
 2. shot noise
 3. thermal noise
 4. 1/f noise
 
 # Szene 8
 Comparision: to the human eye
 
 
 
 
 
 