
.. _documentation:

=====================================
Absorption line fit using ``bayesvp``
=====================================

We describe an example on how to fit a simple absorption line using ``bayesvp``.  The fitting routine can run in an interactive python session or using a python script.

To start ``bayesvp``, first we need to setup a configuration file. ``bayesvp`` is meant to run with this file in background as it can take few minutes for MCMC sampling depending on the chosen number of walkers, steps, and parallel processes.

Below we illustrate a simple interactive use of the code and setting up of a configuration file to fit an O VI transition with rest wavelength of 1031.926 Å.

Setup a config file
--------------------

First step is to import ``bayesvp`` package. Next we import an object, ``bvp_write_config``, that interactively asks the user a few questions
to create a config file.

::

    In [1]: import bayesvp

    In [2]: from bayesvp.scripts import bvp_write_config as wc

Let us assume that the spectrum in question is located in the following directory:

::

    In [3]: spectrum_path = '/home/<username>/bayesvp_tutorial/codes/examples/'

Suppose the file name of the example spectrum is ``OVI.spec`` with three of columns of data: wave, flux, error. We can use the ``bvp_write_config`` routine to set up the config file as:

::

    In [4]: config_writer = wc.WriteBayesVPConfig().print_to_file("-i")

On executing the above command, the routine will ask the user few questions:

*The questions are on the left, while on the right, as an example, the answers are written. These answers can change based on different user
preferences.*

``Path to spectrum:`` /home/<username>/bayesvp\_tutorial/codes/examples

``Spectrum filename:`` OVI.spec

``filename for output chain:`` o6

*Enter the name of the ion to be fitted: first atom name, next its ionization state*

``atom:`` O

``state:`` VI

*Enter the number of components to used in the fitting routine. If you wish to use more components then type in the number*

``Maximum number of components to try:`` 1

*Enter the observed wavelength region to be used in the fitting routine*

``Starting wavelength(A):`` 1030

``Ending wavelength(A):`` 1033

``Enter the priors:``

*Enter the assumed minimum and maximum values of column density for the absorption feature to be fitted*

``min logN [cm^-2] =`` 10

``max logN [cmˆ-2] =`` 18

*Similarly, enter the assumed minimum and maximum values of Doppler b-parameter for the absorption feature to be fitted*

``min b [km/s] =`` 0

``max b [km/s] =`` 100

*Enter the central redshift of the absorption feature corresponding to the ion to be fitted*

``central redshift =`` 0

``velocity range [km/s] =``\ 300

*Here we enter parameters to be used for MCMC sampling*

``Enter the MCMC parameters:``

``Number of walkers:`` 400

``Number of steps:`` 2000

``Number of processes:`` 8

``Model selection method bic(default),aic,bf:`` bic

``MCMC sampler kombine(default), emcee:`` kombine

*On completion of the above step, the configuration file is automatically written within a sub-directory where the spectrum is located.*

``Written config file:``
/home/<username>/bayesvp\_tutorial/codes/examples/bvp\_configs/config\_OVI.dat

The saved configuration file 'config\_OVI.dat' will look like the following:

::

    spec_path /home/<username>/bayesvp_tutorial/codes/examples
    output o6
    mcmc 400 2000 8 bic kombine
    %% OVI.spec 1030.000000 1033.000000
    % O VI 15 30 0.000000
    logN 10.00 18.00
    b    0.00 100.00
    z    0.000000 300.00


For HST/COS data
~~~~~~~~~~~~~~~~~~~~

To deal with HST/COS data, which requires incorporation of line-spread-functions (LSFs), the above saved **config_OVI.dat** needs to be modified as such:

::

    spec_path /home/<username>/bayesvp_tutorial/codes/examples
    output o6
    mcmc 400 2000 8 bic kombine
    %% OVI.spec 1030.000000 1033.000000
    % O VI 15 30 0.000000
    lsf COS_res<central_wavel>.dat
    logN 10.00 18.00
    b    0.00 100.00
    z    0.000000 300.00

*Note the changes made above. An additional statement:* ``lsf <LSF kernel at the central wavelength>`` *is added.*

The `HST/COS LSFs <http://www.stsci.edu/hst/instrumentation/cos/performance/spectral-resolution>`_ should be saved in a sub-directory (named **database**) where the spectrum is located.


MCMC fit
--------------

We can now run MCMC fit. To start we first supply the full path to the **config file** created as a command line argument.

.. Using this config file and parameters stored in it, we can run ``bayesvp`` MCMC fit.

::

    In [5]: config_fname = spectrum_path + 'bvp_configs/config_OVI.dat'

Next we import the MCMC fit object ``bvp_mcmc`` and run the fit as shown below.

.. The output is one or more chains for each MCMC run.

::

    In [6]: from bayesvp.mcmc_setup import bvp_mcmc

    In [7]: bvp_mcmc(config_fname, print_config = True)

``bvp_mcmc`` runs a fixed number of component fit as specified by the config file or make copies of the configs and run upto the maximum number of components specified until the best model is found. For each MCMC run, one or more chain is produced as an output. Setting ``print_config = True`` will save the configuration used in the run in a sub-directory where the spectrum is located.

The the fitting process is completed after the above step produces an output chain saved in a sub-directory (named **chains**) where the spectrum is located. The output chain is a binary file (ends with .npy) which contains all the information that we need. 

.. ``bayesvp`` will print to screen the relevant information from the config file
.. ``DefineParams`` reads and defines fitting parameters from *config file* created.
