from waitingthread import *
import time

class LampConsumption(WaitingThread):

  def __init__(self, lamp, publishConsumptionTime=8, measureTime = 5):
    WaitingThread.__init__(self, measureTime)
    self.lamp = lamp
    self.timeToPublish = publishConsumptionTime
    self.lastPublication = time.time()
    self.consumptionAccumulator = 0
    self.consumptionHistory = []
    self.consumptionObservers = []

  def addConsumptionObserver(self, observer):
    self.consumptionObservers.add(observer)
  def removeConsumptionObserver(self, observer):
    self.consumptionObservers.remove(observer)

  def getConsumptionHistory(self):
    return self.consumptionHistory

  def execute(self, deltaTime):
    consumption = self.calculateConsumption(deltaTime)
    self.consumptionAccumulator += consumption
    #print("Consumption: " + consumption + ". Accumulated consumption: " + self.consumptionAccumulator)

    now = time.time()
    if self.isTimeToPublish(now):
      self.publishConsumption(now)

  def calculateConsumption(self, deltaTime):
    if(not self.lamp.isOn()):
      return 0
    deltaTimeInHours = self.secondsToHours(deltaTime)
    consumptionWattHours = self.lamp.getPower() * deltaTimeInHours
    return consumptionWattHours

  def secondsToHours(self, seconds):
    return seconds / (3600.0)

  def isTimeToPublish(self, now):
    deltaTime = now - self.lastPublication
    publish = deltaTime > self.timeToPublish
    if(publish):
      self.lastPublication = now
    return publish

  def publishConsumption(self, now):
    consumptionEvent = {}
    consumptionEvent['value'] = self.consumptionAccumulator
    consumptionEvent['time'] = now
    self.consumptionAccumulator = 0
    self.consumptionHistory.append(consumptionEvent)
    print("notify consumption: ", consumptionEvent)
    for observer in self.consumptionObservers :
      observer.onConsumption(consumptionEvent)
  
