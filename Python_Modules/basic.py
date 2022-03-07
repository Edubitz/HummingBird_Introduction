from BirdBrain import Hummingbird # importing the HummingBird object from the BirdBrain library
from time import sleep # importing the sleep function from the time library

bird = Hummingbird('A') # Declare a HummingBird object with the device identifier 

bird.setLED(1, 100) # Turn the LED at port 1 of the HummingBird to 100 intensity. Intensity range is 0 - 100
sleep(1) # Wait for 1 second

bird.stopAll() # Stop the program
