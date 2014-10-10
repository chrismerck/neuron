import numpy as np
from neuron_hu import *
from neuron_plot import *
from neuron_load import *
import matplotlib.animation as ani

def sparse_pixels(n):
  return np.random.exponential(scale=1.0,size=n*n).reshape((n,n))

def normalize(img):
  return img / np.max(np.abs(img))

def test_hu_of():
  patch_size = 16
  hu = HuNeuron(M=patch_size*patch_size,T=1000*50)
  cmax = 1000
  c = 0
  while c < cmax:
    print 
    print "*"*80
    patch = sparse_pixels(patch_size)
    #print patch
    #plot_patch(normalize(patch))
    #continue
    x=np.ravel(patch) # convert to 1D view
    y = hu.update(x)
    '''print "x=\n%s"%str(x)
    print "y=\n%s"%str(y)
    print "x_smooth=\n%s"%str(hu.x_smooth)
    print "u=\n%s"%str(hu.u)
    print "w=\n%s"%str(hu.w)
    print "Y=\n%s"%str(hu.Y)'''
    c += 1
    if c % 10 == 0:
      print "patch #%06d"%c
      w = np.reshape(hu.w,(patch_size,patch_size))
      plot_patch(w,savefile='patch%06d.png'%c)

def test_hu():
  patch_size = 16
  step = 16 # overlap = patch - step
  hu = HuNeuron(M=patch_size*patch_size,T=1000*50)
  c = 0
  for k in range(1,1+1):
    # load a vanHateren image
    vh = load_vh(k)
    for left in range(0,vh.shape[0]-patch_size,step):
      for top in range(0,vh.shape[1]-patch_size,step):
        patch = vh[left:left+patch_size,top:top+patch_size]
        #plot_vh(patch)
        x=np.ravel(patch) # convert to 1D view
        hu.update(x)
        c += 1
        if c % 100 == 0:
          print "patch #%06d"%c
          w = np.reshape(hu.w,(patch_size,patch_size))
          plot_patch(w,savefile='patch%06d.png'%c)

if __name__=="__main__":
  test_hu()
