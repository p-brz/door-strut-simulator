import requests


class NetworkConsumptionObserver:

    def __init__(self, params, lp):
        self.port = None if (params is None) else int(params['port'])
        self.address = None if (params is None) else params['address']
        self.lamp = lp

    def onConsumption(self, consumptionEvent):
        try:
            url = "http://" + str(self.address) + ":" + str(self.port) + '/appliances/' + self.lamp.hash + '/extras/'
            url += self.lamp.consumption_key + '/'
            print("Sending consumption: " + str(consumptionEvent) + " to address: " + url)
            response = requests.post(url, data=consumptionEvent)
            print(str(response))
        except Exception, e:
            print e