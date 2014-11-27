class LampStrut:

    def __init__(self):

        self.hash = '5273148ba316de3ef878971745bb7a222660ca42'
        self.consumption_key = 'CONSUMPTION'

        self.configs = {
            'type': 'lamp'
        }

        self.services = [
            {
                'name': 'ligar',
                'method': self.matchKey('turnOn'),
                'params': []
            },
            {
                'name': 'desligar',
                'method': self.matchKey('turnOff'),
                'params': []
            },
            {
                'name': 'definir_brilho',
                'method': self.matchKey('setBright'),
                'params': [
                    'brilho'
                ]
            }
        ]

        self.status = {
            'power': 60, #in watts
            'ligada': 0,
            'brilho': 100
        }

    def isOn(self):
        return self.status['ligada'] != 0

    def getPower(self):
        return self.status['power']

    def callService(self, service, params=None):
        valid = False
        method = None
        for appService in self.services:
            if appService['name'] == service:
                valid = True
                method = appService['method']

        if not valid:
            return False


        method(params)
        return True

    def matchKey(self, method):

        def turnOn(params=None):
            print('Turning on')
            self.status['ligada'] = 1

        def turnOff(params=None):
            print('Turning off')
            self.status['ligada'] = 0

        def setBright(params=None):
            print('set Bright. params: ', params)
            if(params and 'brilho' in params):
                self.status['brilho'] = int(params['brilho'])

        if method == 'turnOn':
            return turnOn
        elif method == 'turnOff':
            return turnOff
        elif method == 'setBright':
            return setBright

    def getJsonServices(self):
        json = {}
        for service in self.services:
            json.update({service['name']: service['params']})

        return json

    def getJsonStatus(self):
        return self.status

    def getJsonConfigs(self):
        return self.configs

    def getJson(self):
        json = {
            'configs': self.getJsonConfigs(),
            'services': self.getJsonServices(),
            'status': self.getJsonStatus()
        }

        return json
