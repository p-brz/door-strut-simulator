import requests


class DoorStrut:

    def __init__(self):

        self.observers = []
        self.server = 'localhost:8080'
        self.hash = '5273148ba316de3ef878971745bb7a222660ca42'

        self.has_changed = False

        self.configs = {
            'type': 'door'
        }

        self.services = [
            {
                'name': 'abrir',
                'method': self.matchKey('open'),
                'params': []
            },
            {
                'name': 'fechar',
                'method': self.matchKey('close'),
                'params': []
            },
            {
                'name': 'trancar',
                'method': self.matchKey('lock'),
                'params': []
            },
            {
                'name': 'destrancar',
                'method': self.matchKey('unlock'),
                'params': []
            }
        ]

        self.status = {
            'open': 0,
            'locked': 0
        }

    def isOpen(self):
        return self.status['open'] != 0
    def isLocked(self):
        return self.status['locked'] != 0

    def callService(self, service, params=None):
        print("Call services: " + service)
        valid = False
        method = None
        for appService in self.services:
            if appService['name'] == service:
                print("match with service: ", service)
                valid = True
                method = appService['method']

        if not valid:
            print("service not valid")
            return False

        method(params)
        for observer in self.observers:
            observer.on_change(self)

        return True

    def matchKey(self, method):

        def open(params=None):
            if(not(self.isLocked())):
                print('Opening')
                self.status['open'] = 1
            
        def close(params=None):
            if(self.isOpen()):
                print('Closing')
                self.status['open'] = 0
        
        def lock(params=None):
            if(not(self.isOpen())):
                print('Locking')
                self.status['locked'] = 1
        
        def unlock(params=None):
            print("try unlock");
            print("can unlock:", not(self.isOpen()) and self.isLocked())
            if(not(self.isOpen()) and self.isLocked()):
                print('unLocking')
                self.status['locked'] = 0

        if method == 'open':
            return open
        elif method == 'close':
            return close
        elif method == 'lock':
            return lock
        elif method == 'unlock':
            return unlock

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
