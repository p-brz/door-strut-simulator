#flask/bin/python
from flask import Flask, jsonify, request

"""
Um servidor flask que não faz nada.
Utilizado apenas para testar networkConsumptionObserver
"""

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  return jsonify({"Message": "Lorem ipsum", "params" : request.args })

if __name__ == '__main__':
  app.config['SERVER_NAME'] = 'localhost:10000'
  app.run(debug=True, use_reloader=False)
  
