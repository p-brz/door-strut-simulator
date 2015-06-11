#flask/bin/python


from flask import Flask, jsonify, request
from door import *
from guidoor import *

app = Flask(__name__)
appliance = DoorStrut()

@app.route('/')
def index():
    return jsonify(appliance.getJson())

@app.route('/services/abrir/', methods=['GET'])
def abrir():
    appliance.callService('abrir')
    return jsonify(appliance.getJsonStatus())

@app.route('/services/fechar/', methods=['GET'])
def fechar():
    appliance.callService('fechar')
    return jsonify(appliance.getJsonStatus())
    
@app.route('/services/trancar/', methods=['GET'])
def trancar():
    appliance.callService('trancar')
    return jsonify(appliance.getJsonStatus())
    
@app.route('/services/destrancar/', methods=['GET'])
def destrancar():
    appliance.callService('destrancar')
    return jsonify(appliance.getJsonStatus())


@app.route('/services/', methods=['GET'])
def getServices():
    return jsonify(appliance.getJsonServices())

@app.route('/status/', methods=['GET'])
def status():
    return jsonify(appliance.getJsonStatus())


if __name__ == '__main__':

    gui = GuiDoor(1, appliance)
    gui.start()

    app.config['SERVER_NAME'] = 'localhost:5001'
    app.run(debug=True, use_reloader=False)

    #stop other threads
    gui.stop()
    gui.join()
  
