#flask/bin/python
from flask import Flask, jsonify, request
from lamp import *
from guilamp import *
import os

app = Flask(__name__)
lp = LampStrut()

@app.route('/')
def index():
  return jsonify(lp.getJson())

@app.route('/services/ligar', methods=['GET'])
def ligar():
  lp.callService('ligar')
  return jsonify(lp.getJsonStatus())

@app.route('/services/desligar', methods=['GET'])
def desligar():
  lp.callService('desligar')
  return jsonify(lp.getJsonStatus())

@app.route('/services/definir_brilho', methods=['GET'])
def set_bright():
  lp.callService('definir_brilho', request.args)
  return jsonify(lp.getJsonStatus())

@app.route('/services', methods=['GET'])
def getServices():
  return jsonify(lp.getJsonServices())

@app.route('/status', methods=['GET'])
def status():
  return jsonify(lp.getJsonStatus())



if __name__ == '__main__':
  print("WERKZEUG_RUN_MAIN: ",os.environ.get("WERKZEUG_RUN_MAIN"))

  gui = GuiLamp(1, lp)
  gui.start()
  print("gui lamp started")
  app.config['SERVER_NAME'] = 'localhost:5000'
  app.run(debug=True, use_reloader=False)
  gui.stop()
  print('after run')
  
