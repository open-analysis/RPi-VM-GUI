#! /usr/bin/env python3

import threading
import json
from flask import Flask, request, jsonify
import mixer
import utils

app = Flask(__name__)



def runServer():
    app.run(debug=True, threaded=True, use_reloader=False, port=5000, host="192.168.1.142")

# Return the queue of commands to the PC
@app.get("/queue")
def getQueue():
    queue = []
    with open("queue.txt", "r") as f:
        lines = f.readlines()
        queue = [line.strip() for line in lines]

    # Clear the file
    open("queue.txt", 'w').close()
    json_queue = jsonify(queue)
    return json_queue

# Add/Update/Delete programs
@app.post("/programs")
def add_program():
    tmp_prog = json.loads(str(request.get_data(True))[2:-1])
    utils.updateProgs(tmp_prog)
    return ["Success"], 200

# Add/Update/Delete devices
@app.post("/devices")
def add_device():
    tmp_dev = json.loads(str(request.get_data(True))[2:-1])
    utils.updateDevices(tmp_dev)
    return ["Success"], 200

def updateQueue(action: str):
    with open("queue.txt", "a") as f:
        f.writelines(action)
        f.write('\n')


if __name__ == '__main__':

    t1 = threading.Thread(target=runServer)
    
    t1.start()
    
    mixer.start()
