from gpiozero import DistanceSensor, Buzzer
from time import sleep

import motor

dSensor = DistanceSensor(echo="BOARD7", trigger="BOARD12")
bz = Buzzer("BOARD29")
obj_Dist = 10.0


def beep(status):
    if status == 1:
        bz.on()
        print("alarm On")
    else:
        bz.off()
        print("alarm Off")


def isClose(dist):
    if dist <= obj_Dist:
        print("obstacle is Close")
        return True
    else:
        return False


def alarm(dist):
    if dist <= obj_Dist:
        print("obstacle detected")
        # call alarm
        beep(1)
        motor.stop()
    else:
        beep(0)


def distance():
    distance = (dSensor.distance * 100)
    return distance


if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print("Measured Distance = %.1f cm" % dist)
            alarm(dist)
            sleep(1)

    except KeyboardInterrupt:
        print("Measurement stopped by User")
