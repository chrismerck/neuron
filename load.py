import numpy as np
import array

def load(filename):
  with open(filename,'rb') as h:
    s = h.read()
  arr = array.array('H',s)
  arr.byteswap()
  img = np.array(arr,dtype='uint16').reshape(1024,1536)
  return img


if __name__=="__main__":
  import disp
  IMG_XMAX = 1024
  IMG_YMAX = 1536
  screen = disp.Screen(IMG_XMAX,IMG_YMAX)
  img = load('data/imk00001.iml')
  screen.img_vh(left=0,top=0,img=img)

