#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor, Color
from pybricks.parameters import Port, Button
from pybricks.tools import wait, StopWatch
from typing import Union

"""" This code was completely created by Amin Salman.
 Provided you subscribe to my Youtube channel, you are
 allowed to modify it and use it in competitions as you
 wish. If you have any questions, leave them in the
 comments on my channel.
"""

class Base:
    """
    This is the class responsible for movement. To use this class, you need to specify the left and right motors,
    the wheel circumference, and the distance between the wheels in cm.    """

    def __init__(self, left_motor_port: Port,
                 right_motor_port: Port,
                 wheel_circumference: float,
                 ):
        self.left_motor = Motor(left_motor_port)
        self.right_motor = Motor(right_motor_port)
        self.wheel_circumference = wheel_circumference
        

    def start_tank(self, leftSpeed: int, rightSpeed: int):

        """
        This method gives you control of the speed of each motor separately. The base will start moving and will not
        stop automatically.

        :param leftSpeed: -100 to 100, negative for reverse
        :param rightSpeed: -100 to 100, negative for reverse
        """

        self.left_motor.run(leftSpeed)
        self.right_motor.run(-1 * rightSpeed)
        return


    def stop_and_hold(self):
        """
        Instantly stops the robot and holds the motors at current position.
        """
        self.left_motor.hold()
        self.right_motor.hold()
        return


    def get_avg_motor_deg(self, captured_motor_angles):
        """
        Returns the average number of the wheel motors degrees based on the initial angles' parameter.
        :return: int
        """
        return 


    def move_cm(self, distance_in_cm: float, speed: int):
        """
        Starts moving at the specified speed and stops when the distance specified is reached.
        :param distance_in_cm: Positive Integer
        :param speed: -100 to 100
        """

        self.start_tank(speed, speed)
        captured_angles = [int(self.left_motor.angle()), int(self.right_motor.angle())]
        distance_inDegrees = abs(int((distance_in_cm / self.wheel_circumference) * 360))
        while (int((abs(int(self.right_motor.angle()) - captured_angles[1]) + abs(int(self.left_motor.angle()) - captured_angles[0])) / 2)) < distance_inDegrees:
            pass
        self.stop_and_hold()
        return


class Gyro:
    """
    This class is responsible for any action that utilises the gyro sensor, such as turning accurately and moving
    straight accurately.
    """
    def __init__(self, robotBase: Base,
                 gyroPort: Port):
        self.robotBase = robotBase
        self.sensor = GyroSensor(gyroPort)


    def gyroTurn(self, endAngle: int, speed: int, mode=1):
        """
        This method turns the robot to a specific angle using the gyro sensor. If the robot doesn't turn accurately
        try reconnecting the gyro sensor or restarting the program while the robot is perfectly still. :param
        endAngle: The angle to turn to :param speed: Maximum speed of the wheel motors :param mode: 1 for
        pivoting around the center, 0 for pivoting around a wheel :return: nothing
        """
        if mode not in [0, 1]:
            return
        
        startAngle = self.sensor.angle()

        if endAngle > startAngle:
            while endAngle > self.sensor.angle():
                if abs(startAngle - self.sensor.angle()) > 15:
                    self.robotBase.start_tank(speed, -speed * mode)
                else:
                    self.robotBase.start_tank(15, -15 * mode)

        elif endAngle < startAngle:
            while endAngle < self.sensor.angle():
                if abs(startAngle - self.sensor.angle()) > 15:
                    self.robotBase.start_tank(-speed * mode, speed)
                else:
                    self.robotBase.start_tank(-15 * mode, 15)

        self.robotBase.stop_and_hold()
        return



# Initialize objects:
base = Base(Port.A, Port.B, 4)
gyro = Gyro(base, Port.S3)

# Wait for center button to be pressed:
while EV3Brick().buttons.pressed() != [Button.CENTER]:
    print("Press the center button on the EV3 Brick")

StopWatch().reset() # Start timer and run:

#Actual Run Starts Here:
