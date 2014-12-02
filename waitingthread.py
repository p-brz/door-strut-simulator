import threading
import sys
import time


class WaitingThread(threading.Thread):

    def __init__(self, lp,  waitTime = 5):
        threading.Thread.__init__(self)
        self.running = True
        self.waitCondition = threading.Condition(threading.RLock())
        self.waitTime = waitTime
        self.lastTime = None

    def setWaitTime(self, time):
        self.waitCondition.acquire()
        self.waitTime = time
        self.waitCondition.release()

    def isRunning(self):
        self.waitCondition.acquire()
        isRunningNow = self.running
        self.waitCondition.release()
        return isRunningNow

    def stop(self):
        self.waitCondition.acquire()
        self.running = False
        self.waitCondition.notify()
        self.waitCondition.release()

    def run(self):
        now = time.time()
        self.lastTime = now
        self.doWork(now)
        while self.isRunning():
            self.onstep()
            now = time.time()
            timeToWait = (self.lastTime + self.waitTime) - now
            if(timeToWait <= 0):
                self.doWork(now)
            else:
                print("Sleep: ", timeToWait," seconds")
                self.waitCondition.acquire()
                self.waitCondition.wait(timeToWait)
                self.waitCondition.release()

    def doWork(self, now):
        deltaTime = now - self.lastTime
        self.execute(deltaTime)
        self.lastTime = now

    def getLastTime(self):
        return self.lastTime

    def execute(self, deltaTime):
        pass

    def onstep(self):
        pass

