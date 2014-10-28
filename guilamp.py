import pygame
import threading

class GuiLamp(threading.Thread):

  def __init__(self, threadID, lamp):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.lamp = lamp
    self.isRunning = True

  def getLampImage(self):
    lampStatus = self.lamp.status['ligada']
    if lampStatus == 1:
      return 'assets/lampOn.png'
    else:
      return 'assets/lampOff.png'

  def run(self):

    pygame.init()
    self.displaysurf = pygame.display.set_mode((256, 256))

    count = 0
    res = 'assets/lampOn.png';
    while self.isRunning:

      self.displaysurf.fill((255, 255, 255))
      image = pygame.image.load(res)
      self.displaysurf.blit(image, (0, 0))
      if count > 10:
        res = self.getLampImage()

      count += 1

      pygame.display.flip()
