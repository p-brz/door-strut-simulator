import requests

class NetworkConsumptionObserver:

  def __init__(self, params):
    self.port    = None if (params is None) else int(params['port'])
    self.address = None if (params is None) else params['address']

  def onConsumption(self, consumptionEvent):
    try:
      url = "http://" + str(self.address) + ":" + str(self.port)
      print("Sending consumption: " + str(consumptionEvent) + " to address: " + url)
      response = requests.get(url, data=consumptionEvent)
      print(str(response))
    except Exception, e: 
      #TODO: se requisição falhar (X vezes ?), para de enviar
      print e
  
