import RPi.GPIO as GPIO
from time import sleep
# GPIO Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

Motor_A_Pin1 = 11
Motor_A_Pin2 = 13
Motor_B_Pin1 = 16
Motor_B_Pin2 = 18
Motor_A_EN = 15
Motor_B_EN = 22
global pwmA
global pwmB

GPIO.setup(Motor_A_Pin1, GPIO.OUT)  # IN1
GPIO.setup(Motor_A_Pin2, GPIO.OUT)  # IN2
GPIO.setup(Motor_B_Pin1, GPIO.OUT)  # IN3
GPIO.setup(Motor_B_Pin2, GPIO.OUT)  # IN4
GPIO.setup(Motor_A_EN, GPIO.OUT)  # PWM1
GPIO.setup(Motor_B_EN, GPIO.OUT)  # PWM2
pwmA = GPIO.PWM(Motor_A_EN, 100)
pwmB = GPIO.PWM(Motor_B_EN, 100)
pwmA.start(0)
pwmB.start(0)
#print("GPIO Set")


def inti():
    # GPIO Setup
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    Motor_A_Pin1 = 11
    Motor_A_Pin2 = 13
    Motor_B_Pin1 = 16
    Motor_B_Pin2 = 18
    Motor_A_EN = 15
    Motor_B_EN = 22
    global pwmA
    global pwmB

    GPIO.setup(Motor_A_Pin1, GPIO.OUT)  # IN1
    GPIO.setup(Motor_A_Pin2, GPIO.OUT)  # IN2
    GPIO.setup(Motor_B_Pin1, GPIO.OUT)  # IN3
    GPIO.setup(Motor_B_Pin2, GPIO.OUT)  # IN4
    GPIO.setup(Motor_A_EN, GPIO.OUT)  # PWM1
    GPIO.setup(Motor_B_EN, GPIO.OUT)  # PWM2
    #pwmA = GPIO.PWM(Motor_A_EN, 100)
    #pwmB = GPIO.PWM(Motor_B_EN, 100)
    pwmA.start(0)
    pwmB.start(0)
    #print("GPIO Set")


def forward(speed):
    inti()
    # Motor1
    GPIO.output(Motor_A_Pin1, False)
    GPIO.output(Motor_A_Pin2, True)
    # Motor2
    GPIO.output(Motor_B_Pin1, True)
    GPIO.output(Motor_B_Pin2, False)

    pwmA.ChangeDutyCycle(speed)
    pwmB.ChangeDutyCycle(speed)
    GPIO.output(Motor_A_EN, True)
    GPIO.output(Motor_B_EN, True)
    #print("forward Set")


def backward(speed):
    inti()
    # Motor1
    GPIO.output(Motor_A_Pin1, True)
    GPIO.output(Motor_A_Pin2, False)
    # Motor2
    GPIO.output(Motor_B_Pin1, False)
    GPIO.output(Motor_B_Pin2, True)

    pwmA.ChangeDutyCycle(speed)
    pwmB.ChangeDutyCycle(speed)
    GPIO.output(Motor_A_EN, True)
    GPIO.output(Motor_B_EN, True)
    #print("backward Set")


def left(speed):
    inti()
    # Motor1
    GPIO.output(Motor_A_Pin1, False)
    GPIO.output(Motor_A_Pin2, False)
    # Motor2
    GPIO.output(Motor_B_Pin1, False)
    GPIO.output(Motor_B_Pin2, False)

    pwmA.ChangeDutyCycle(speed)
    pwmB.ChangeDutyCycle(speed)
    GPIO.output(Motor_A_EN, True)
    GPIO.output(Motor_B_EN, True)
    #print("backward Set")


def right(speed):
    inti()
    # Motor1
    GPIO.output(Motor_A_Pin1, False)
    GPIO.output(Motor_A_Pin2, False)
    # Motor2
    GPIO.output(Motor_B_Pin1, False)
    GPIO.output(Motor_B_Pin2, False)

    pwmA.ChangeDutyCycle(speed)
    pwmB.ChangeDutyCycle(speed)
    GPIO.output(Motor_A_EN, True)
    GPIO.output(Motor_B_EN, True)
    #print("backward Set")


def stop():
    inti()
    GPIO.output(Motor_A_Pin1, False)
    GPIO.output(Motor_A_Pin2, False)
    GPIO.output(Motor_B_Pin1, False)
    GPIO.output(Motor_B_Pin2, False)
    #GPIO.output(Motor_A_EN, False)
    #GPIO.output(Motor_B_EN, False)
    # pwmA.ChangeDutyCycle(0)
    # pwmB.ChangeDutyCycle(0)
    #rint("Stop Set")


def end():
    inti()
    stop()
    GPIO.output(Motor_A_EN, False)
    GPIO.output(Motor_B_EN, False)
    pwmA.stop()
    pwmB.stop()
    GPIO.cleanup()
    #print("END Set")


def speedTest():
    inti()
    try:
        while True:
            for dutyCycle in range(0, 100, 5):
                pwmA.ChangeDutyCycle(dutyCycle)
                pwmB.ChangeDutyCycle(dutyCycle)
                sleep(0.1)

            for dutyCycle in range(100, 0, -5):
                pwmA.ChangeDutyCycle(dutyCycle)
                pwmB.ChangeDutyCycle(dutyCycle)
                sleep(0.1)

    except KeyboardInterrupt:
        pwmA.stop()
        pwmB.stop()


def main():
    inti()
    forward(20)
    sleep(1)
    speedTest()
    sleep(1)
    stop()
    end()


if __name__ == "__main__":
    try:
        main()
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
