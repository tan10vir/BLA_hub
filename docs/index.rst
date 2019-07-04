

Tutorial on BayesVP
===================

``bayesvp`` is a Bayesian MCMC parallel Voigt profile fitting routine written by Cameron Liang & Andrey Kravtsov.

``bayesvp`` provides a number of helpful executable scripts that work with command line arguments (saved in your environment ``PATH``). The
main functionality is the MCMC Voigt profile fitting (bvpfit) where the user supplies a config file that specifies parameters for the fitting.
These include parameter priors, number of walkers, parallel threads, line spread function, continuum model, Bayesian model comparisons, and
etc. There are utility functions that allow users to quickly create an example configuration file, process and plot the chains, process and plot the best fit models and more. For details on the code, refer to the papers `Liang & Kravtsov 2017 <https://arxiv.org/abs/1710.09852>`_ and `Liang
et al. 2017 <https://arxiv.org/abs/1710.00411>`_.


Acknowledgements
----------------
|
  This tutorial is written based on the examples done by `Cameron Liang <https://github.com/cameronliang/bayesvp.git>`_


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
