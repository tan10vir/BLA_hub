#-------------------------------------------------------------
# BayesVP: Author: Cameron Liang & Andrey V. Kravtsov
# Reference: arxiv 1710.09852
# See Appendix of the paper for an example.
#-------------------------------------------------------------
# Code to fit a single absorption line
# Tested on Apr 8 2019 @ 23:04 on Python3

import bayesvp

# from astropy.io import ascii
# from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

#---------- Important BayesVP functions ----------------
from bayesvp.scripts import bvp_write_config as wc
from bayesvp.mcmc_setup import bvp_mcmc_single as mc_single
from bayesvp.mcmc_setup import bvp_mcmc as mcmc
from bayesvp.scripts import bvp_process_model as pm
from bayesvp.config import DefineParams


#---- Additional packages/functions for trial-----------------------
# from bayesvp import likelihood as lk
# from bayesvp.mcmc_setup import _create_walkers_init as int
# from bayesvp.utilities import get_bayesvp_Dir
# from bayesvp.vp_model import general_intensity
# from bayesvp.vp_model import wavelength_array
# from bayesvp.vp_model import simple_spec



#----------- Path of the spectrum ---------------------------------------

spectrum_path = '/home/tanvir/BLA_project/DATA/20_selected/pg1116/bayesvp_tutorial/'

# create a config file

config = wc.WriteBayesVPConfig().print_to_file()

# Load the config file

config_fname = spectrum_path + 'bvp_configs/config_NII.dat'

# code_path = get_bayesvp_Dir()

# Extract all of the relevant information using the DefineParams function
config_params = DefineParams(config_fname)

# print (config_params)

#-------- run the MCMC fit --------------------------
# Fitting log is written in 'config.log' file.
#
# int(config_params)
mc_single(config_params)
#
mcmc(config_fname)

# The fitting process after the step is completed. The output chain is a binary file which ends with .npy
# contains all the information that we need.

#--------------------------------------------~~_--------------------------------------------------------
# Note: Example in Liang2017 paper shows that using only "mcmc(config_fname)" will complete the fitting process.
# However, I found that in my cases, before "mcmc(config_fname)", I need to run the following commands:
# 1. config_params = DefineParams(config_fname)
# 2. "mc_single(config_params)"
# and then run
# 3. mcmc(config_fname)
#------------------------------------------------~~------------------------------------------

#------Plot the results and write the best fit spectrum into a file-------------

output = pm.ProcessModel(config_params)

redshift = 0.138498; dv = 200;
output.plot_model_comparison(redshift, dv)
output.write_model_summary()
output.write_model_spectrum()
output.plot_gr_indicator()
output.corner_plot()

#-- Output are written in a subdirectory "bvp_output_z<redshift>"
#-- Plots are in "bvp_output_z<redshift>/data_products/plots"
