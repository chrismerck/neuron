from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import numpy as np

def plot_vh(img,greymax=4096,savefile=None):
  # input: img = 2D numpy array to plot
  # output: image shown on screen
  fig = plt.figure()
  plt.imshow(img)
  plt.show()
