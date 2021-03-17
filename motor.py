from gpiozero import Robot
from time import sleep

import curses


# Broadcom (BCM) pin
robot = Robot(left=(27, 17), right=("BOARD16", "BOARD15"))


def forward(self, speed=0.25):
    robot.forward(speed)


def backward(self, speed=0.25):
    robot.forward(speed)


def left(self, speed=0.25):
    robot.forward(speed)


def right(self, speed=0.25):
    robot.forward(speed)


def stop():
    robot.stop()


def test():
    for i in range(4):
        robot.forward()
        sleep(1)
        robot.backward()
        sleep(1)
        robot.stop()
    try:
        while True:
            for speed in range(0, 100, 5):
                robot.forward(speed/100)
                sleep(0.1)

            for speed in range(100, 0, -5):
                robot.forward(speed/100)
                sleep(0.1)

    except KeyboardInterrupt:
        robot.stop()


# for keyCon
actions = {
    curses.KEY_UP:    robot.forward,
    curses.KEY_DOWN:  robot.backward,
    curses.KEY_LEFT:  robot.left,
    curses.KEY_RIGHT: robot.right,
}


def keyCon(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            # KEY PRESSED
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action(0.25)
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY RELEASED
            robot.stop()


if __name__ == "__main__":
    try:
        curses.wrapper(keyCon)
        # main()
    except KeyboardInterrupt:
        print("Stopped by User")
