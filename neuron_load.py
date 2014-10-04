import numpy as np
import array
from neuron_plot import *

def load_vh(n):
  filename = 'data/imk%05d.iml'%n
  with open(filename,'rb') as h:
    s = h.read()
  arr = array.array('H',s)
  arr.byteswap()
  img = np.array(arr,dtype='uint16').reshape(1024,1536)
  img = img[:,2:-2]
  return img

if __name__=="__main__":
  i = 1
  img = load_vh(i)
  plot_vh(img)

