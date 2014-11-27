import pygame
import threading
import sys

class GuiLamp(threading.Thread):

  def __init__(self, threadID, lamp):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.lamp = lamp
    self.running = True
    self.images = {}
    self.lock = threading.RLock()
    print("Init lamp. ThreadID: ", threadID);

  def getLampImage(self):
    lampStatus = self.lamp.status['ligada']
    if lampStatus == 1:
      return 'assets/lampOn.png'
    else:
      return 'assets/lampOff.png'

  def getLampDrawable(self):
    lampAsset = self.getLampImage();
    if(not(lampAsset in self.images)):
      #self.images[lampAsset] = pygame.image.load(lampAsset).convert();
      self.images[lampAsset] = pygame.image.load(lampAsset);
    return self.images[lampAsset];
  
  #Por: http://www.nerdparadise.com/tech/python/pygame/blitopacity/
  def blit_alpha(self, target, source, location, opacity):
      x = location[0]
      y = location[1]
      temp = pygame.Surface((source.get_width(), source.get_height())).convert()
      temp.blit(target, (-x, -y))
      temp.blit(source, (0, 0))
      temp.set_alpha(opacity)        
      target.blit(temp, location)

  def isRunning(self):
    self.lock.acquire()
    isRunningNow = self.running
    self.lock.release()
    return isRunningNow

  def stop(self):
    self.lock.acquire()
    self.running = False
    self.lock.release()

  def run(self):
    print("run");
    pygame.init()
    self.displaysurf = pygame.display.set_mode((256, 256))

    count = 0
    image = self.getLampDrawable();
    while self.isRunning():
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
      #self.displaysurf.fill((255, 255, 255))
      self.displaysurf.fill((0, 0, 0))


      if(self.lamp.status['ligada']):
        alpha = 255 * (self.lamp.status['brilho']/100.0)
        self.blit_alpha(self.displaysurf, image, (0,0), alpha)
        #image.set_alpha(alpha)
      else:
        #image.set_alpha(255)
        self.displaysurf.blit(image, (0, 0))

      if count > 10:
        count = 0;
        image = self.getLampDrawable();

      count += 1

      pygame.display.flip()
