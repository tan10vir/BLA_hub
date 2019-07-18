

Tutorial on BayesVP
===================

``bayesvp`` is python package developed by `Cameron Liang <jwliang@oddjob.uchicago.edu>`_ & Andrey Kravtsov. It implements a Bayesian approach for modeling absorption lines with the Voigt profile. The package can be used to simultaneously fit multiple absorption components to constrain column density, Doppler parameter, and redshift of the absorbing gas. The parameter constraints are derived in the form of marginalized posterior distributions, which allows for uniform treatment of the non-detections (i.e., upper limits) and detections in subsequent analyses, model fits, and comparisons of observations with simulations.

.. ``bayesvp`` package is set up to use the affine-invariant MCMC method implemented in the MCMC emcee_ package and the kernel-density-estimate-based ensemble sampler kombine_ to efficiently sample the posterior distributions of highly correlated parameters. It also provides useful utilities, such as convolution with instrumental line spread function (LSF), explicit control of parameter priors, Bayesian model comparison criteria, and sampling convergence check.

``bayesvp`` package is designed to have a simple user interface with a single configuration file. The main functionality is the MCMC Voigt profile fitting (``bvpfit``) where the user supplies a configuration file that specifies parameters for the fitting. These include parameter priors, number of walkers, parallel threads, line spread function, continuum model, Bayesian model comparisons, and etc. There are utility functions that allow users to quickly create an example configuration file, process and plot the chains, process and plot the best fit models and more. For details on the how code works and more, refer to the papers `Liang & Kravtsov 2017 <https://arxiv.org/abs/1710.09852>`_ and `Liang et al. 2017 <https://arxiv.org/abs/1710.00411>`_.


Acknowledgements
----------------
|
  This tutorial is written based on the examples in `Liang & Kravtsov 2017 <https://arxiv.org/abs/1710.09852>`_.


Installation instructions
-------------------------

.. toctree::
  :maxdepth: 2

  install.rst

Documentation
-------------

.. toctree::
  :maxdepth: 2

  documentation.rst



.. _kombine: https://github.com/bfarr/kombine
.. _emcee: https://github.com/dfm/emcee
