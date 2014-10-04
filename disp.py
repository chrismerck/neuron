import sys, ctypes
import numpy as np
from sdl2 import *
import sdl2.ext

def main():
  screen = Screen(1025,1536)
  screen.wait_quit()
  screen.quit()

class Screen(object):
  def __init__(self,xmax,ymax):
    self.xmax = xmax
    self.ymax = ymax
    SDL_Init(SDL_INIT_VIDEO)
    self.window = SDL_CreateWindow(b"Neuron Display",
        SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
        self.xmax,self.ymax,SDL_WINDOW_SHOWN)
    self.surf = SDL_GetWindowSurface(self.window).contents

  def redraw(self):
    SDL_UpdateWindowSurface(self.window)

  def get_pix(self):
    p = sdl2.ext.pixels2d(self.surf)
    return p

  def wait_quit(self):
    running = True
    event = SDL_Event()
    while running:
      while SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == SDL_QUIT:
          running = False
          break

  def quit(self):
    SDL_DestroyWindow(self.window)
    SDL_Quit()
    sys.exit(0)

  def img_vh(self,left,top,img):
    p = self.get_pix()
    (img_xmax,img_ymax)=img.shape
    img_xmax = 1000
    img_ymax = 1000
    for i in range(img_xmax):
      for j in range(img_ymax):
        w = max(min(img[i][j]*256/4096,255),0)
        x = j+top
        y = i+left
        if x < self.xmax and y < self.ymax:
          p[j+top][i+left] = w + w*256 + w*256*256
    self.redraw()

  '''
  def img_vh(self,left,top,img):
    p = self.get_pix()
    (img_xmax,img_ymax)=img.shape
    w = img*256/4096
    c = w + w*256 + w*256*256
    np.copyto(p,c)
    self.redraw()
  '''

#sdl2.ext.pixels2d

if __name__=="__main__":
  main()


