#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.nxtdevices import LightSensor
from pybricks.parameters import Port, Button, Color
from pybricks.tools import wait


"""" This code was completely created by Amin Salman.
 Provided you subscribe to my Youtube channel, you are
 allowed to modify it and use it in competitions as you
 wish. If you have any questions, leave them in the
 comments on my channel.
"""

# Initialize the motors.

left_motor_two = Motor(Port.B)
right_motor_two = Motor(Port.D)

print("motors done")

# Initialize the color sensor.
s1 = LightSensor(Port.S4)
s2 = LightSensor(Port.S3)
s3 = LightSensor(Port.S2)
s4 = LightSensor(Port.S1)

print("sensors done")

# Initialize Ev3
ev3 = EV3Brick()

threshold = 40
kP = 0.25
kI = 0.002
kD = 5
PIDspeed = 100
turnSpeed = 100
straightSpeed = 90

# Reset Variables
P, I, D, PID, lastError, error, = 0, 0, 0, 0, 0, 0
global right_speed, left_speed
left_speed = 0
right_speed = 0
locked = 0

def getSensors():
    s1_status = (int(s1.reflection() < threshold))
    s2_status = (int(s2.reflection() < threshold))
    s3_status = (int(s3.reflection() < threshold))
    s4_status = (int(s4.reflection() < threshold))
    sensors = [s1_status, s2_status, s3_status, s4_status]
    return sensors

def turnRight():
    global left_speed, right_speed, turnSpeed
    right_speed = 0
    left_speed = turnSpeed
    applySpeeds()
    return

def turnLeft(): 
    global left_speed, right_speed, turnSpeed
    left_speed = 0
    right_speed = turnSpeed
    applySpeeds()
    return

def moveStraight(): 
    global left_speed, right_speed, straightSpeed
    left_speed = straightSpeed
    right_speed = straightSpeed
    applySpeeds()
    return

def applySpeeds():
    global left_speed, right_speed

    left_motor_two.dc(-1*left_speed)
    right_motor_two.dc(right_speed)


ev3.screen.clear()

if locked == 1:
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
    print(EV3Brick().buttons.pressed())
    if EV3Brick().buttons.pressed() == [Button.CENTER]:
            break     
           
ev3.screen.clear()
ev3.screen.draw_text(40, 50, "UNLOCKED", Color.BLACK, None)


while True:
    sensorsList = getSensors()    

    if (sensorsList == [1, 0, 0, 0]) or (sensorsList == [1, 1, 0, 0]) or (sensorsList == [1, 1, 1, 0]) or (sensorsList == [1, 1, 0, 1]) :
        #print("R")
        turnLeft()
        applySpeeds()
        while True:         #wait until line detected
            sensorsList = getSensors()
            if ((sensorsList[1] == 1) or (sensorsList[2] == 1)) and (sensorsList[3] == 0):
                break
                      
    elif (sensorsList == [0, 0, 0, 1]) or (sensorsList == [0, 0, 1, 1]) or (sensorsList == [0, 1, 1, 1]) or (sensorsList == [1, 0, 1, 1]) :
        #print("L")
        turnRight()   
        while True:         #wait until line detected
            sensorsList = getSensors()
            if ((sensorsList[1] == 1) or (sensorsList[2] == 1)) and (sensorsList[3] == 0):
                break           
      

    else:
        error = (s3.reflection() - s2.reflection())
        P = kP * error
        I = kI * (error + I)
        D = kD * (error - lastError)
        PID = P+I+D    
        left_speed = PIDspeed - PID
        right_speed = PIDspeed + PID
        left_motor_two.dc(-1*left_speed)
        right_motor_two.dc(right_speed)    
        lastError = error
        wait(8)       






