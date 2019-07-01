# ```bayesvp```: Tutorial

```bayesvp``` is a Bayesian MCMC parallel Voigt profile fitting routine written by Cameron Liang (jwliang@oddjob.uchicago.edu; cameron.liang@gmail.com) & Andrey Kravtsov.

```bayesvp``` provides a number of helpful executable scripts that work with command line arguments (saved in your environment ```PATH```). The main functionality is the MCMC Voigt profile fitting (bvpfit) where the user supplies a config file that specifies parameters for the fitting. These include parameter priors, number of walkers, parallel threads, line spread function, continuum model, Bayesian model comparisons, and etc. There are utility functions that allow users to quickly create an example config file, process and plot the chains, process and plot the best fit models and more. For details on the code, refer to the papers [Liang & Kravtsov 2017](https://arxiv.org/abs/1710.09852) and [Liang et al. 2017](https://arxiv.org/abs/1710.00411).

The following is a short tutorial on how to use ```bayesvp``` fitting routine.

## Installation

Install ```bayesvp``` using pip with the ```--user``` flag:

```
pip install bayesvp --user
```

For users with Python 3 and above, you need to convert the ```bayesvp``` scripts written originally in Python 2.7 to Python 3 using the Python package [```2to3```](https://pypi.org/project/2to3/). 

After installing ```bayesvp``` we should run its unit tests to ensure the package works as expected. The simplest way to do this is inside a python shell:

```
from bayesvp.tests import run_tests

```
The output should look something like this:

```
The output should look something like this:

test_config_file_exists (bayesvp.tests.test_config.TCConfigFile) ... ok
test_default_no_continuum_params (bayesvp.tests.test_config.TCConfigFile) ... ok
test_example_mcmc_params (bayesvp.tests.test_config.TCConfigFile) ... ok
...
test_prior (bayesvp.tests.test_likelihood.TCPosterior) ... ok
test_general_intensity (bayesvp.tests.test_model.TCSingleVP) ... ok
test_simple_spec (bayesvp.tests.test_model.TCSingleVP) ... ok

----------------------------------------------------------------------
Ran 13 tests in 3.654s

OK
```
This would ensure ```bayesvp``` package is installed.

## Fit a simple absorption line with ```bayesvp```

We describe a simple tutorial on how to use ```bayesvp``` package. It can be run in an interactive python session or using a python script.

To start ```bayesvp```, first we need to setup a configuration file. ```bayesvp``` is meant to run with this file in background as it can take few minutes for MCMC sampling depending on the chosen number of walkers, steps, and parallel processes.

Below we illustrate a simple interactive use of the code and setting up of a configuration file.

### Setup a 'config file'

Let us first import ```bayesvp```. Next we import an object,
```bvp_write_config```, that interactively asks the user a few questions to create a config file.

```
In [1]: import bayesvp

In [2]: from bayesvp.scripts import bvp_write_config as wc

```
Let us assume that the spectrum in question is located in the
following directory:

```
In [3]: spectrum_path = '/home/<username>/bayesvp_tutorial/codes/examples/'
```
Suppose the file name of the example spectrum is ```OVI.spec``` with three of columns of data: wave, flux, error. We can use the ```bvp_write_config``` routine to set up the config file as:

```
In [4]: config_writer = wc.WriteBayesVPConfig().print_to_file("-i")
```
On executing the above command, the routine will ask the user few questions:

_The questions are on the left while, on the right, as an example, the answers are written. These answers can change based on different user preferences._

```Path to spectrum: ``` /home/\<username>\/bayesvp_tutorial/codes/examples

```Spectrum filename:``` OVI.spec

```filename for output chain:``` o6

_Enter the name of the ion to be fitted: first atom name, next its  ionization state_

```atom:``` O

```state:``` VI

_Enter the number of components to used in the fitting routine. If you wish to use more components then type in the number_

```Maximum number of components to try:``` 1

_Enter the observed wavelength region to be used in the fitting routine_

```Starting wavelength(A):``` 1030

```Ending wavelength(A):``` 1033


```Enter the priors:```

_Enter the assumed minimum and maximum values of column density for the absorption feature to be fitted_

```min logN [cm^-2] = ``` 10

```max logN [cmˆ-2] =``` 18

_Similarly, enter the assumed minimum and maximum values of Doppler b parameter for the absorption feature to be fitted_

```min b [km/s] =``` 0

```max b [km/s] =``` 100

_Enter the central redshift of the absorption feature corresponding to the ion to be fitted_

```central redshift =``` 0

```velocity range [km/s] = ```300

_Here we enter parameters to be used for MCMC sampling_

```Enter the MCMC parameters:```

```Number of walkers:``` 400

```Number of steps:``` 2000

```Number of processes:``` 8

```Model selection method bic(default),aic,bf:``` bic

```MCMC sampler kombine(default), emcee:``` kombine

_On completion of the above step, the **config file** is automatically written within a subdirectory where the spectrum is located._

```Written config file:``` /home/\<username>\/bayesvp_tutorial/codes/examples/bvp_configs/config_OVI.dat

### Run a MCMC fit
