from flask import Flask, render_template, Response, request
from camera import VideoCamera
import time
import threading
import os

import threading
from time import sleep
import ultrasonic
import motor

pi_camera = VideoCamera(flip=True)  # flip pi camera if upside down.

# App Globals (do not edit)
app = Flask(__name__)

@app.before_first_request
def activate_job():
    def run_job():
            while True:
                sleep(1)
                #print("Run recurring task")
                uDist = ultrasonic.distance()
                ultrasonic.alarm(uDist)
                print("%.1f" % uDist)
                templateData = {
                    'dist' : uDist
                }
                #return render_template('index.html', **templateData)

    threadU = threading.Thread(target=run_job)
    threadU.start()

@app.route('/')
def index():
    return render_template('index.html')  # you can customze index.html here


@app.route("/<action>")
def act(action):
    if action == "beep":
        ultrasonic.beep(1)
        sleep(1)
        ultrasonic.beep(0)
    elif action == "forward":
            motor.forward()
    elif action == "backward":
            motor.backward()
    elif action == "left":
            motor.left()
    elif action == "right":
            motor.right()
    elif action == "stop":
            motor.stop()
    else:
        print("action is not defined")

    return render_template('index.html')


def gen(camera):
    # get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port='8000', debug=False)
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("~~Stopped by User~~")
