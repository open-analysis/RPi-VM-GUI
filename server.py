import threading
import json
from flask import Flask, request, jsonify
import mixer_gui
import utils

app = Flask(__name__)

t1 = threading.Thread(target=mixer_gui.start)

t1.start()

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
    tmp_progs = json.loads(str(request.get_data(True))[2:-1])
    print(f"Adding {tmp_progs}")
    utils.importProgs(tmp_progs)
    return ["Success"], 200

@app.delete("/programs")
def del_program():
    tmp_progs = json.loads(str(request.get_data(True))[2:-1])
    print(f"Deleting {tmp_progs}")
    utils.removeProgs(tmp_progs)
    return ["Success"], 200

# Add/Update/Delete devices
@app.post("/devices")
def add_device():
    tmp_devs = json.loads(str(request.get_data(True))[2:-1])
    print(f"Adding {tmp_devs}")
    utils.importDevices(tmp_devs)
    return ["Success"], 200

@app.delete("/devices")
def remove_device():
    tmp_devs = json.loads(str(request.get_data(True))[2:-1])
    print(f"Deleting {tmp_devs}")
    utils.removeDevice(tmp_devs)
    return ["Success"], 200

def updateQueue(action: str):
    with open("queue.txt", "a") as f:
        f.writelines(action)
        f.write('\n')
