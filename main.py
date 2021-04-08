# import Libraries
from flask import Flask, render_template, Response, request, jsonify
from camera import VideoCamera
import time
import threading
import os
from time import sleep

import ultrasonic
import motor
import datetime

pi_camera = VideoCamera(flip=True)  # flip pi camera if upside down.

# App Globals (do not edit)
app = Flask(__name__)

running = True  # to control loop in thread
value = 0

# thread for ultrasonic.distance


@app.before_first_request
def activate_job():
    def run_job():
        global value
        while True:
            sleep(0.5)
            uDist = ultrasonic.distance()
            ultrasonic.alarm(uDist)
            value = "Distance: " + "{:.2f}".format(uDist)
            #print("%.1f" % uDist)

    threadU = threading.Thread(target=run_job)
    threadU.start()

# routing


# root


@app.route('/')
def index():
    return render_template('index.html')  # you can customze index.html here

# action


@app.route("/<action>")
def act(action):
    if action == "beep":
        ultrasonic.beep(1)
        sleep(1)
        ultrasonic.beep(0)
    elif action == "forward":
        motor.forward()
        print("forward")
    elif action == "backward":
        motor.backward()
        print("backward")
    elif action == "left":
        motor.left()
        print("left")
    elif action == "right":
        motor.right()
        print("right")
    elif action == "stop":
        motor.stop()
        print("stop")
    else:
        print("")

    return render_template('index.html')

# update


@app.route('/update', methods=['POST'])
def update():
    return jsonify({
        'value': value,
        'time': datetime.datetime.now().strftime("%H:%M:%S"),
    })

# handler for camera


def gen(camera):
    # get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# video steram


@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera), mimetype='multipart/x-mixed-replace; boundary=frame')


# run main
if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port='8000', debug=False)
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("~~Stopped by User~~")
