#!/usr/bin/env pybricks-micropython
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import StopWatch, wait


"""" This code was completely created by Amin Salman.
 Provided you subscribe to my Youtube channel, you are
 allowed to modify it and use it in competitions as you
 wish. If you have any questions, leave them in the
 comments on my channel.
"""

timer = StopWatch()  # Initialize the hub, motors and sensors.
motorL, motorR = Motor(Port.A), Motor(Port.B)
s1, s2, s3, s4 = ColorSensor(Port.C), ColorSensor(Port.E), ColorSensor(Port.F), ColorSensor(Port.D)

kP, kI, kD = 0.15, 0.0015, 3.5	# Set k-values for PID algorithm
P, I, D, PID, lastError, error = 0, 0, 0, 0, 0, 0	# Reset PID variables
black_thres, x, n = 35, 80, 0		# Set threshold, default PID speed, and n counter

PID_speed, turnSpeed, straightSpeed = 100, 100, 100  # PID speed, hard turns speed, and straight speed.

timer.pause() # Pause stopwatch for accurate reseting
timer.reset() # Reset stopwatch for speed indexing

def start_motors(left_speed, right_speed): 	# Starts the motors at % of voltage 
    motorR.dc(-1*left_speed)	
    motorL.dc(right_speed) 
 
def getSensors():		# Encode all sensors in a single integer. Returns 0 to 15, a total of 16 states
    return ((int(s1.reflection() < black_thres) * 8) + (int(s2.reflection() < black_thres) * 4) + (int(s3.reflection() < black_thres) * 2) + (int(s4.reflection() < black_thres) * 1))

start_motors(0, 0)	# Ensure motors are off
timer.resume()		# Resume stopwatch after robot is unlocked

while True:
    sensorState = getSensors()	# Save the sensor configuration in a variable and update every time
    time = timer.time()/1000  # Capture current time from stopwatch      
    if sensorState in [1,3,7]:	# Check if list contains current state
        start_motors(0, turnSpeed)	# Turn left sharply
        while True:
            sensorState = getSensors()     # Update sensor state
            if sensorState in [2, 4, 15]:  # Check if either middle or all sensors detect black  
                start_motors(80, 80)
                break				 # If so, exit loop (i.e. stop turning)

    elif sensorState in [8, 12, 14]:  # Check if list contains current state     
            
        start_motors(turnSpeed, 0)  # Turn right sharply
        while True:				
            sensorState = getSensors()     # Update sensor state
            if sensorState in [2, 4, 15]:  # Check if either middle or all sensors detect black  
                start_motors(80, 80)
                break				 # If so, exit loop (i.e. stop turning)

    elif sensorState == 15:	# Check if all sensors are black
        start_motors(straightSpeed, straightSpeed)	# Then start moving straight forward
        
    else:        			          
        error = (s3.reflection() - s2.reflection())	# Set error to difference between sensors        
        P = kP * error						# Set P correction
        I = kI * (error + I)					# Set I correction
        D = kD * (error - lastError)			# Set D correction
        PID = P+I+D 						# Add the 3 corrections
        left_speed = int(PID_speed) + PID
        right_speed = int(PID_speed) - PID
        start_motors(left_speed, right_speed) 		# Apply motor speeds
        lastError = error					# Save error as lastError
        wait(8)     						# Wait 8 milliseconds before repeating the loop
        