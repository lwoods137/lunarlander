#Listen up Astronauts! 
#This simulation was designed to help prepare you for a lunar landing
#To use this simulation you will be dealing with multiple variables
#Orientation- this is anywhere from 0-360 degrees, 90deg is completly vertical etc etc
#Distance - this is how close you are to the ground
#Speed - how fast you're going, use more rocket power to slow down
#Fuel - how much gas you got left in the tank, correction and rocket power drains this 
#rocket power -  you lose 1.25(n percent you decide to use) of fuel
#rocket power contd - but you'll lose (0.88 n percent) from your speed
#correction - you lose 0.15(n degrees you decide to correct) of fuel 
# You will be given randomly generated variables to use at first, then you use your new values
# until you land
#Each 'turn' is equal to one second
#To land successfully you must be have your distance be equal to or less than zero
#Have your speed less than 20 and your orientation between 80 and 97 degrees 

import random

#initial variable values
orientation_rand = random.randint(0,360)
distance_rand = random.randint(100,250)
speed_rand = random.randint(10,50)
fuel = 100

# displaying values
print("Current Orientation is " + str(orientation_rand) + " degrees")
print("Current distance to lunar surface is " + str(distance_rand)+"m")
print("Current speed is "+str(speed_rand) +"m/s")
print("Current fuel level is " + str(fuel) + "%")

# variables are given values
orientation = input("Enter current orientation or your values from before.")
distance = input("Enter current distance or your values from before.")
speed = input("Enter current speed or your values from before.")
fuel = input("Enter 100 for fuel or your value from before.")

#math of fuel level
correction = input("How much would you like to correct?")
rocket = input("What percent of rocket power would you like to use?")
speedlost = round((float(speed)- (0.88 * int(rocket))),2)
corrected = int(orientation) + int(correction)
correctionfuel = float(fuel) - (0.15*abs(int(correction)))
rocketfuel = correctionfuel - (1.25* int(rocket))
newdistance =  round((float(distance) - speedlost),2)


# landing fxn
def landing_outcomes(newdistance,speedlost,corrected,rocketfuel):  
    if (newdistance<=0) and (speedlost <= 20) and (corrected >=80 ) and (corrected<=97):
        print("LANDING SUCCESSFUL") 
   
    if (rocketfuel <= 0):
        print("YOU'RE OUT OF FUEL MISSION FAILED")        
        
    if (corrected > 360) or (corrected < 0):
        print('ERROR ORIENTATION OVER 360 DEGREES OR UNDER 0 DEGREES')
        
    if (newdistance<=0) and (speedlost>20):
        print("YOU HAVE CRASHED, MISSION FAILED, SPEED IS OVER 20 M/S")
    if (newdistance <= 0) and (corrected > 97) or (corrected < 80):
         print("YOU HAVE CRASHED, MISSION FAILED, ORIENTATION IS LESS THAN 80 OR MORE THAN 97")

landing_outcomes(newdistance,speedlost,corrected,rocketfuel)


# Displaying variables
print("New speed is " + str(speedlost)+'m/s')
print("Fuel level remaining "+str(rocketfuel)+'%')
print('New orientation ' +str(corrected)+' degrees')
print("New distance to lunar surface is " + str(newdistance))

















