# %%
import sys
import os
import bayesvp
from astropy.io import ascii
from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from bayesvp.scripts import bvp_write_config as wc
from bayesvp import likelihood as lk

from bayesvp.mcmc_setup import bvp_mcmc as mcmc
from bayesvp.mcmc_setup import _create_walkers_init as int
from bayesvp.mcmc_setup import bvp_mcmc_single as mc_single


from bayesvp.config import DefineParams
from bayesvp.utilities import get_bayesvp_Dir

from bayesvp.vp_model import general_intensity
from bayesvp.vp_model import wavelength_array
from bayesvp.vp_model import simple_spec

# %% testing the code on OVI.spec to get a Voigt fitted profile 


sys.path.append('/home/tanvir/BLA_project/bayesvp/')

spectrum_path = '/home/tanvir/BLA_project/DATA/20_selected/pg1116/bayesvp_tutorial/'

# create a config file uncomment below
# %%
# config = wc.WriteBayesVPConfig().print_to_file()
# %%

config_fname = spectrum_path + 'bvp_configs/config_OVI.dat'

# code_path = get_bayesvp_Dir()
config_params = DefineParams(config_fname)

# %%
print (config_params)
# %%
config_fname = spectrum_path + 'bvp_configs/config_OVI.dat'
config_params = DefineParams(config_fname)
int(config_params)
mc_single(config_params)

# %%

mcmc(config_fname)
# %%
from bayesvp.config import DefineParams as param
config_fname = spectrum_path + 'bvp_configs/config_OVI.dat'
config_params = DefineParams(config_fname)
# %%
from bayesvp import likelihood as lk
config_fname = spectrum_path + 'bvp_configs/config_OVI.dat'
config_params = DefineParams(config_fname)
output = lk.Posterior(config_params)

# %%
print(output)
# %%

import bayesvp.vp_model as pm
# output = pm.ProcessModel(config_fname)
# %%
redshift = 0; dv = 300

# %%
from bayesvp.utilities import determine_autovp as autovp
autovp(config_fname)

# %%
