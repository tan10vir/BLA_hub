from bayesvp.mcmc_setup import bvp_mcmc as mcmc
from bayesvp.config import DefineParams
from bayesvp.scripts import bvp_process_model


config_file = '/home/vikram/BLA_hub/test_vikram/hi_config.dat'

# the mcmc fit
mcmc(config_file, print_config = True)

# after the chains
x = DefineParams(config_file)
op=bvp_process_model.ProcessModel(x)
op.plot_model_comparison(0.081, 400)
op.write_model_summary()
op.write_model_spectrum()
op.plot_gr_indicator()
op.corner_plot()
