#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Button, Color
from pybricks.tools import StopWatch, wait
from sys import exit

# This code is specifically adjusted for round 2
# If you see 10 #s remove this line before usng this code for another round


ev3, timer = EV3Brick(), StopWatch()  # Initialize the hub, motors and sensors.
motorL1, motorL2, motorR1, motorR2 = Motor(Port.A), Motor(Port.B), Motor(Port.C), Motor(Port.D)
s1, s2, s3, s4 = ColorSensor(Port.S4), ColorSensor(Port.S3), ColorSensor(Port.S2), ColorSensor(Port.S1)

kP, kI, kD = 0.13, 0.002, 3	# Set k-values for PID algorithm
P, I, D, PID, lastError, error = 0, 0, 0, 0, 0, 0	# Reset PID variables
black_thres, x, n = 28, 80, 0		# Set threshold, default PID speed, and n counter
speedList = [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x]
speedList_len = len(speedList)  # Speed every second for optimization

PID_speed, turnSpeed, straightSpeed = 84, 87, 100  # PID speed, hard turns speed, and straight speed.
nega_turn = -28

timer.pause() # Pause stopwatch for accurate reseting
timer.reset() # Reset stopwatch for speed indexing

def start_motors(left_speed, right_speed): 	# Starts the motors at % of voltage 
    motorL1.dc(left_speed)	
    motorL2.dc(left_speed)    
    motorR1.dc(-1*right_speed)
    motorR2.dc(-1*right_speed)
 
def getSensors():		# Encode all sensors in a single integer. Returns 0 to 15, a total of 16 states
    return ((int(s1.reflection() < black_thres) * 8) + (int(s2.reflection() < black_thres) * 4) + (int(s3.reflection() < black_thres) * 2) + (int(s4.reflection() < black_thres) * 1))

def locker(locked):	# Lock system to allow only me to activate the robot
    if not locked:
        ev3.screen.draw_text(8, 5, "Note: Only Amin", Color.BLACK, None)
        ev3.screen.draw_text(17, 30, "can activate the", Color.BLACK, None)
        ev3.screen.draw_text(65, 60, "robot.", Color.BLACK, None)
        ev3.screen.draw_text(1, 102, "Please Provide PIN", Color.BLACK, None)

        while True:
            if EV3Brick().buttons.pressed() == [Button.RIGHT]:
                if EV3Brick().buttons.pressed() == [Button.LEFT, Button.RIGHT]:
                    break

        ev3.screen.clear()
        ev3.screen.draw_text(50, 50, "PASS 1", Color.BLACK, None)

        while True:
            if EV3Brick().buttons.pressed() == [Button.UP]:
                if EV3Brick().buttons.pressed() == [Button.UP, Button.DOWN]:
                    break

        ev3.screen.clear()
        ev3.screen.draw_text(50, 50, "PASS 2", Color.BLACK, None)
        while True:
            if EV3Brick().buttons.pressed() == [Button.RIGHT]:                
                break

        ev3.screen.clear()
        ev3.screen.draw_text(50, 50, "PASS 3", Color.BLACK, None)

    ev3.screen.clear()
    ev3.screen.draw_text(40, 50, "UNLOCKED", Color.BLACK, None)
    while True:
        if EV3Brick().buttons.pressed() == [Button.CENTER]:
            break
    

start_motors(0, 0)	# Ensure motors are off
locker(1)		# Start up the locking system



timer.resume()		# Resume stopwatch after robot is unlocked

while True:
    sensorState = getSensors()	# Save the sensor configuration in a variable and update every time
    time = timer.time()/1000  # Capture current time from stopwatch      
    n += 1   				# Increase experimental counter by 1

    if time < 2.6:
        PID_speed = 78
        turnSpeed = 86
        nega_turn = -28
    elif time > 2.8 and time < 6:
        PID_speed = 40
        turnSpeed = 100
        nega_turn = -63
    elif time > 4 and time < 7.3:
        PID_speed = 70
        turnSpeed = 86   
        nega_turn = -28
    elif time > 7.7 and time < 8.3:
        PID_speed = 53
        turnSpeed = 100   
        nega_turn = -60     
    elif time > 8.4 and time < 11.5: 
        PID_speed = 55
        turnSpeed = 86   
        nega_turn = -33    
    else:
        PID_speed = 70
        turnSpeed = 86   
        nega_turn = -30 


    if time > 30:             # Check if x seconds have passed
        start_motors(0, 0)      # Then stop motors
        exit()                  # Then exit the program

    if sensorState in [3,7]:	# Check if list contains current state

        start_motors(nega_turn, turnSpeed)	# Turn left sharply

        while True:
            sensorState = getSensors()     # Update sensor state
            if sensorState in [2, 4]:  # Check if either middle or all sensors detect black  
                start_motors(30, 30)
                break				 # If so, exit loop (i.e. stop turning)

    elif sensorState in [12, 14]:  # Check if list contains current state

        start_motors(turnSpeed,  nega_turn)  # Turn right sharply
        
        while True:				
            sensorState = getSensors()     # Update sensor state
            if sensorState in [2, 4]:  # Check if either middle or all sensors detect black  
                start_motors(30, 30)
                break				 # If so, exit loop (i.e. stop turning)

    elif sensorState == 15:	# Check if all sensors are black
        start_motors(straightSpeed, straightSpeed)	# Then start moving straight forward
        
    else:        			          
        error = (s3.reflection() - s2.reflection())	# Set error to difference between sensors        
        P = kP * error						# Set P correction
        I = kI * (error + I)					# Set I correction
        D = kD * (error - lastError)			# Set D correction
        PID = P+I+D 						# Add the 3 corrections

        #if (time < (speedList_len)):			# Check if time in seconds is less than the speed list's length
        #    PID_speed = speedList[time]   		# Set speed to corresponding item in the list

        left_speed = int(PID_speed) + PID
        right_speed = int(PID_speed) - PID
        start_motors(left_speed, right_speed) 		# Apply motor speeds
        lastError = error					# Save error as lastError
        wait(8)     						# Wait 8 milliseconds before repeating the loop
        