class LampStrut:

  def __init__(self):

    self.configs = {
      'type' : 'lamp'
    }

    self.services = [
      {
        'name' : 'ligar',
        'method' : self.matchKey('turnOn')
      },
      {
        'name' : 'desligar',
        'method' : self.matchKey('turnOff')
      }
    ]

    self.status = {
      'ligada' : 0
    }

  def callService(self, service):
    valid = False
    method = None
    for appService in self.services:
      if appService['name'] == service:
        valid = True
        method = appService['method']

    if not valid:
      return False


    method()
    return True

  def matchKey(self, method):

    def turnOn():
      print('Turning on')
      self.status['ligada'] = 1

    def turnOff():
      print('Turning off')
      self.status['ligada'] = 0

    if method == 'turnOn':
      return turnOn

    elif method == 'turnOff':
      return turnOff

  def getJsonServices(self):
    json = {}
    for service in self.services:
      json.update({service['name'] : 0})

    return json

  def getJsonStatus(self):
    return self.status

  def getJsonConfigs(self):
    return self.configs

  def getJson(self):
    json = {
      'configs' : self.getJsonConfigs(),
      'services' : self.getJsonServices(),
      'status' : self.getJsonStatus()
    }

    return json
