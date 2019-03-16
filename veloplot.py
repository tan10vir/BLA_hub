# Packages 
import numpy as np
from astropy.io import ascii
from astropy.table import Table
#
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator 

font = {'family' : 'serif', 'weight' : 'normal', 'size'   : 18}
plt.rc('font', **font)


mpl.rcParams['mathtext.fontset'] = 'custom'
mpl.rcParams['mathtext.cal'] =  'Norican'
mpl.rcParams['mathtext.bf'] =  'Crimson Text:bold'

#

# file = 'pg1116_normdata.txt'
# store the file names in a list to be able to iterate over them:

files = ['HIa_nc.dat', 'HIb.dat', 'CIIa.dat','CIIb.dat', 'NII_nc.dat','SiIIa.dat', 'SiIIb.dat', 'SiIIc.dat', 'SiIII.dat', 'OVIa.dat', 'OVIb.dat', 'CIVa.dat', 'CIVb.dat', 'NVa.dat', 'NVb.dat']

# making a function

def read_file(filename):
        w, f, e = np.loadtxt(filename, unpack=True,skiprows=1)
        return w, e, f

    c = 3e5
    gray = '#e5e8e8'


#reading the file
# w, f, e=np.loadtxt(file, unpack=True) 



# zabs 
# z=[0.138527] # redshift for v_rel = 0 kms ; Danforth

    z = [0.1384840678] # two component HI fit
    z2 = 0.1386364296

    for z1 in z:

        fig, ((ax1, ax6, ax11), (ax2, ax7, ax12), (ax3, ax8, ax13), (ax4, ax9, ax14), (ax5, ax10, ax15),)=plt.subplots(5, 3, sharex=False, sharey=True, figsize=(11, 8))
        lam=[1215.6701, 1025.7223, 1334.5323, 1036.3367, 1083.9937, 1260.4221, 1193.2897, 1190.4158, 1206.5, 1031.9261, 1037.6167, 1548.1949, 1550.77, 1238.8210, 1242.8040]
    
        name=['HI', 'HI', 'CII', 'CII', 'NII', 'SiII', 'SiII', 'SiII', 'SiIII','OVI', 'OVI', 'CIV', 'CIV', 'NV', 'NV']

        # zc = [0.3257065, 0.3255469] # redshift for two components
        # fit=['vpfit_chunk001.txt', 'vpfit_chunk002.txt', 'vpfit_chunk003.txt', 'vpfit_chunk004.txt', 'vpfit_chunk005.txt', 'vpfit_chunk006.txt', 'vpfit_chunk007.txt'] # vpfit fit profiles

        for ax, l1, n1, filename in zip((ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10, ax11, ax12, ax13, ax14, ax15), lam, name, files):
            
            label= n1 + '  ${\lambda}$' + '{:d}'.format(int(l1)) 
            w, e, f=read_file(filename)
            ax.plot((((w/(1.0+z1))-l1)/l1)*c, f, linestyle='-', linewidth=2.0,  color='k',drawstyle='steps-mid')

            # for ft in fit:
                # u, x=np.loadtxt(ft,usecols=(0,3), comments='!', unpack=True)
                # ax.plot((((u/(1.0+z1))-l1)/l1)*c, x, linestyle='-', linewidth=1.75,  color='r')

            ax.set_xlim(-200,200)
            ax.set_ylim(-0.2,1.2)
            ax.tick_params(direction='in', length=7, width=1.5)
            ax.tick_params(direction='in', which='minor', length=3.5, width=1.5)
            ax.xaxis.set_ticks_position('both')
            ax.yaxis.set_ticks_position('both')
            # ax.yaxis.set_label_coords(-0.05, 0.65)

        #
            for axt in (ax1, ax2, ax3, ax4, ax6, ax7, ax8, ax9, ax11, ax12, ax13, ax14):
                plt.setp(axt.get_xticklabels(), visible=False)    

            for axp in (ax5, ax10, ax15):
                axp.set_xlabel(r'Velocity (km s$^{-1}$)', fontsize=18)#, fontweight='bold')  
                axp.locator_params(tight=True, nbins=4)
                ax5.set_xticks([-200, -100, 0, 100, ])
                ax10.set_xticks([-100, 0, 100])
                ax15.set_xticks([-100, 0, 100, 200])
            
                axp.xaxis.set_minor_locator(AutoMinorLocator(4))
        
               
            for axi in (ax1, ax2, ax3, ax4, ax5):
            # axi.set_yticks([0,1])
                manual_ylabels =['0',' ','1']
                axi.set_yticks([0, 0.5, 1])
                axi.set_yticklabels(manual_ylabels, minor=False, fontsize=18)
                ax3.set_ylabel(r'Normalized Flux', fontsize=18)

        # ax4.set_ylabel(r'Normalized Flux', fontsize=13)#, fontweight='bold')

            ax.annotate(label, xy=(60, 0.05), color='r', fontweight='bold', fontsize=13)
            ax.axhline(y=0, linewidth=1.25, color='g', linestyle='--')
            ax.axhline(y=1, linewidth=1.25, color='g', linestyle='--')


            ax.axvline((z1-z1)*c/(1.+((z1+z1)/2.)), linewidth=1.05, color='b', linestyle='-.')
            ax.axvline((z2-z1)*c/(1.+((z2+z1)/2.)), linewidth=1.05, color='b', linestyle='-.')
        # 
            for axis in ['top','bottom','left','right']:
                ax.spines[axis].set_linewidth(1.75)

        #
            fig.suptitle(r'PG 1116+215 :: z$_{\mathrm{abs}} =$'+ str(z1)[:8], fontsize=15)
            fig.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
            fig.subplots_adjust(top=0.94, hspace=0,wspace=0)
            fig.savefig(r'PG1116_veloplot_' +str(z1)[:8] +'.pdf')
plt.close(fig)
