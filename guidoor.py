import pygame
import threading
import sys

class GuiDoor(threading.Thread):

  def __init__(self, threadID, door):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.door = door
    self.running = True
    self.images = {}
    self.lock = threading.RLock()
    print("Init door. ThreadID: ", threadID);

  def getDoorImage(self):
    if self.door.isLocked():
      return 'assets/door_locked.jpg'
    elif self.door.isOpen():
      return 'assets/door_open_.jpg'
    else:
      return 'assets/door_close_.jpg'

  def getDoorDrawable(self):
    doorAsset = self.getDoorImage();
    if(not(doorAsset in self.images)):
      #self.images[doorAsset] = pygame.image.load(doorAsset).convert();
      self.images[doorAsset] = pygame.image.load(doorAsset);
    return self.images[doorAsset];

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
    self.displaysurf = pygame.display.set_mode((156, 256))

    count = 0
    image = self.getDoorDrawable();
    while self.isRunning():
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
      #self.displaysurf.fill((255, 255, 255))
      self.displaysurf.fill((0, 0, 0))

      self.displaysurf.blit(image, (0, 0))
        
      if count > 10:
        count = 0;
        image = self.getDoorDrawable();

      count += 1

      pygame.display.flip()
