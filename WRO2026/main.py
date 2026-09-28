#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Port, Button
from pybricks.tools import wait

ev3 = EV3Brick()
gyro = GyroSensor(Port.S1)
gyro.reset_angle(0)

while True:
    # Press the center button to zero the angle
    if Button.CENTER in ev3.buttons.pressed():
        gyro.reset_angle(0)
        ev3.speaker.beep()

    angle = gyro.angle()  # degrees

    ev3.screen.clear()
    ev3.screen.print("Gyro test")
    ev3.screen.print("Angle:", angle)

    print("angle:", angle)
    wait(100)