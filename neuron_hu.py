import numpy as np
from math import *

def ST(f,lam):
  # soft threshold
  lam_arr = np.ones(f.shape)*lam
  fplus = f + lam_arr
  fmin = f - lam_arr
  temp = np.zeros(f.shape)
  temp = np.where(f > lam_arr, fmin, temp)
  temp = np.where(f < -lam_arr, fplus, temp)
  return temp

class HuNeuron(object):
  def __init__(self,M,beta=exp(-1/10.),lam_y=0.4,lam_w1=0.002,lam_w2=0.002,T=50000):
    # M = number of upstream neurons
    # beta = smoothing factor 0<beta<1 (higher beta means slower change)
    # lam_y = output (l-1) regularization parameter
    # lam_w1 = weight l-1 regularization parameter
    # lam_w2 = weight l-2 regularization parameter
    # T = total timesteps (smaller means more adaptable, larger means longer memory)

    # save parameters
    self.M = M
    self.beta = beta
    self.lam_y = lam_y
    self.lam_w1 = lam_w1
    self.lam_w2 = lam_w2
    self.T = T
    self.t = 0

    # random initialization
    self.u = np.random.random(self.M)-0.5 #np.random.normal(size=self.M)
    self.w = np.random.random(self.M)-0.5 #np.random.normal(size=self.M)
    self.Y = 0.0 #np.random.normal()
    self.x_smooth = np.random.random(self.M)*0.1 #np.random.normal(size=self.M)

  def update(self,x,reps=50):
    # input: unsmoothed vector x of inputs
    #        reps = number of times to apply inputs
    # output: neuron output y
    assert reps > 0
    assert x.shape == (self.M,)

    for rep in range(reps):
      # smooth input (leaky integration at synapses)
      self.t += 1
      self.x_smooth = self.beta * self.x_smooth + (1-self.beta)*x

      # compute output
      w_norm = (np.linalg.norm(self.w,ord=2)**2)
      if w_norm == 0.0:
        print "WARNING: hu.w norm underflow"
        w_norm = 0.0001
      y = ST(np.dot(self.w,self.x_smooth),self.lam_y)/w_norm

      # recompute weights
      self.Y = self.Y + y**2
      self.u = self.u + y*(self.x_smooth - self.u*y)/self.Y
      lam_w_eff = self.t*self.lam_w1/(self.Y+self.t*self.lam_w2)
      #print "lam_w_eff=",lam_w_eff
      self.w = ST(self.u,lam_w_eff)

    return y

