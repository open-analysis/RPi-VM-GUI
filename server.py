from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

queue = []

def updateQueue(action):
    queue.append(action)

# Return the queue of commands to the PC
@app.get("/queue")
def getQueue():
    global queue 
    json_queue = jsonify(queue)
    queue.clear()
    return json_queue

# Add/Update/Delete programs
@app.post("/programs")
def add_program():
    if request.is_json:
        tmp_progs = request.get_json()
        print(f"Adding {tmp_progs}")
        # utils.importProgs(tmp_progs)

@app.put("/programs")
def update_program():
    if request.is_json:
        tmp_progs = request.get_json()
        print(f"Updating {tmp_progs}")
        # utils.importProgs(tmp_progs)

@app.delete("/programs")
def del_program():
    if request.is_json:
        tmp_progs = request.get_json()
        print(f"Deleting {tmp_progs}")
        # utils.removeProgs(tmp_progs)

# Add/Update/Delete devices
@app.post("/devices")
def add_device():
    if request.is_json:
        tmp_devs = request.get_json()
        print(f"Adding {tmp_devs}")
        # utils.importDevices(tmp_devs)

@app.put("/devices")
def update_device():
    if request.is_json:
        tmp_devs = request.get_json()
        print(f"Updating {tmp_devs}")
        # utils.importDevices(tmp_devs)

@app.delete("/devices")
def remove_device():
    if request.is_json:
        tmp_devs = request.get_json()
        print(f"Deleting {tmp_devs}")
        # utils.removeDevice(tmp_devs)
