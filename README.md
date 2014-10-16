<!--# neuron

Exploring Neural Networks-->

## Questions

### Generative Mode

  1. Can a NN be run in a generative mode? I.e. can we obtain plausible inputs for some specified output, up to Gaussian noise?
  2. Applications are to machine creativity as well as evaluating unsupervised classifiers.
  3. Is there an analogous biological mechanism?

For example, suppose we have a network with $n$ input nodes $\{x_1,...,x_n\},$
and $m$ output nodes $\{y_1,...,y_m\}.$ 
I am interested in:

  1. Finding a distribution $P(X|Y)$.
  2. Sampling from this distribution given some output.

For example, if we have a deep autoencoder network with an output node
that has learned to recognize faces from images, sampling in this way
should yield plausible faces.

This is in contrast to the approach taken by Standford ML and Google
in their work, where they show either (1) best fitting training exemplars,
and (2) a blurry grey receptive field.

### Sparse Coding with Hu Neurons

Can an ensemble of Hu neurons (Hu et al 2014) perform sparse coding?

  1. Can single neuron result be replicated? (Hu et al 2014)
  2. Can ensemble output regularization reproduce V1 bases? (Olshausen & Field 1997)
  3. Is this more efficient than RBM or Ng's autoencoder?
  4. Can it reproduce hierarchical computer vision results? (Lee, Grosse et al 2011)

### Time Series Processing

  1. How can time series data be processed by an ANN? E.g. can we improve over Ng's Shift-Invariant Sparse Coding (SISC)?
  2. How is time series information actually processed by biological neurons?
  3. Apply to analysis of audio, video, text, and other time series.

