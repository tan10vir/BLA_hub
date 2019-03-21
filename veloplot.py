# Packages 
import numpy as np
from astropy.io import ascii
from astropy.table import Table
#
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator 

# from itertools import islice
# import os
# import subprocess, sys

font = {'family' : 'serif', 'weight' : 'normal', 'size'   : 18}
plt.rc('font', **font)


mpl.rcParams['mathtext.fontset'] = 'custom'
mpl.rcParams['mathtext.cal'] =  'Norican'
mpl.rcParams['mathtext.bf'] =  'Crimson Text:bold'

# opener ="open" if sys.platform == "darwin" else "evince"
#

# file = 'pg1116_normdata.txt'

# store the file names in a list to be able to iterate over them:
# removing . dat from filenames
files = ['HIa_newc', 'HIb', 'NII_nc', 'CIIa','OVIa_newc', 'HIa_newc','SiIIa', 'SiIIb',
         'SiIIc', 'SiIII', 'OVIa_newc', 'OVIb', 'CIVa', 'CIVb', 'NVa_nc']

# making a function

def read_file(filename):
        w, f, e = np.loadtxt(filename, unpack=True,skiprows=1)
        return w, f, e

c = 3e5
gray = '#e5e8e8'


#reading the file
# w, f, e=np.loadtxt(file, unpack=True) 



# zabs 
# z=[0.138527] # redshift for v_rel = 0 kms ; Danforth
z = [0.1384984413] # v_rel = 0 km/s corresponding to NII fit 'z'

for z1 in z:

    plotfile = r'PG1116_veloplot_' + str(z1)[:8] + '.pdf'

    fig, ((ax1, ax6, ax11), (ax2, ax7, ax12), (ax3, ax8, ax13),
          (ax4, ax9, ax14), (ax5, ax10, ax15),) = plt.subplots(5, 3, sharex=False, sharey=True, figsize=(11, 8))
    lam = [1215.6701, 1025.7223, 1083.9937, 1334.5323, 1031.9261, 1215.6701, 1260.4221, 1193.2897, 1190.4158, 1206.5, 1031.9261, 1037.6167, 1548.1949, 1550.77, 1238.8210, 1242.8040]

    name = ['HI', 'HI', 'NII', 'CII', 'OVI', 'HI', 'SiII', 'SiII', 'SiII', 'SiIII', 'OVI', 'OVI', 'CIV', 'CIV', 'NV']

    zhi  = [0.1386581793]  # second component for HI (b=5.05\pm2.26)
    zsi2 = [0.1384821575]  # fitting redshift for SiII
    zsi3 = [0.1384875538]  # fitting redshift for SiIII
    zo6  = [0.138609]      # 2nd component for fit to OVI
    zc4  = [ 0.1384779044 ] #redshift comp for CIV 1548; CIV 1550 is taken into fitting
    zn5  = [0.1384946797 ] 

    
    # fit = ['Lya_vpfit_old.txt', 'Lyb_vpfit_old.txt', 'CIIa_tied_NII_vpfit.txt', 'CIIb_disp_tied_NII_vpfit.txt', 'NII_vpfit.txt', 'SiIIa_vpfit.txt', 'SiIIb_vpfit.txt',  'SiIIc_vpfit.txt', 'SiIII_vpfit.txt']  # vpfit fit profiles

    for ax, l1, n1, filename in zip((ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10, ax11, ax12, ax13, ax14, ax15), lam, name, files):

        label = n1 + '  ${\lambda}$' + '{:d}'.format(int(l1))
        w, f, e = read_file(filename+'.dat')

        ax.plot((((w / (1.0 + z1)) - l1) / l1) * c, f, linestyle='-', linewidth=2.0, color='k', drawstyle='steps-mid')

        # do following
        # best way is to make sure that the fit files have same file naming structure as below
        # read the fit files (changes made as you have suggested)

        fitfile=filename+'_vpfit.txt'

        try:
            u, x = np.loadtxt(fitfile, usecols=(0, 3), comments='!', unpack=True)
            ax.plot((((u / (1.0 + z1)) - l1) / l1) * c, x, linestyle='-', linewidth=1.75, color='r')
        except:
            print("file {} does not exist".format(fitfile))

        #remove this
        #for ft in fit[2:]:
        #    u, x = np.loadtxt(ft, usecols=(0, 3), comments='!', unpack=True)
        #    ax.plot((((u / (1.0 + z1)) - l1) / l1) * c, x, linestyle='-', linewidth=1.75, color='r')

        ax.set_xlim(-200, 200)
        ax.set_ylim(-0.2, 1.2)
        ax.tick_params(direction='in', length=7, width=1.5)
        ax.tick_params(direction='in', which='minor', length=3.5, width=1.5)
        ax.xaxis.set_ticks_position('both')
        ax.yaxis.set_ticks_position('both')
        # ax.yaxis.set_label_coords(-0.05, 0.65)

        #
        for axt in (ax1, ax2, ax3, ax4, ax6, ax7, ax8, ax9, ax11, ax12, ax13, ax14):
            plt.setp(axt.get_xticklabels(), visible=False)

        for axp in (ax5, ax10, ax15):
            ax10.set_xlabel(r'Relative Velocity (km s$^{-1}$)', fontsize=17)  # , fontweight='bold')
            axp.locator_params(tight=True, nbins=4)
            ax5.set_xticks([-200, -100, 0, 100, ])
            ax10.set_xticks([-100, 0, 100])
            ax15.set_xticks([-100, 0, 100, 200])

            axp.xaxis.set_minor_locator(AutoMinorLocator(4))

        for axi in (ax1, ax2, ax3, ax4, ax5):
            # axi.set_yticks([0,1])
            manual_ylabels = ['0', ' ', '1']
            axi.set_yticks([0, 0.5, 1])
            axi.set_yticklabels(manual_ylabels, minor=False, fontsize=18)
            ax3.set_ylabel(r'Normalized Flux', fontsize=18)

        # ax4.set_ylabel(r'Normalized Flux', fontsize=13)#, fontweight='bold')

        ax.annotate(label, xy=(60, 0.05), color='r', fontweight='bold', fontsize=13)
        ax.axhline(y=0, linewidth=1.25, color='g', linestyle='--')
        ax.axhline(y=1, linewidth=1.25, color='g', linestyle='--')

        #Tick marks to represent velocity centroid corresponding to z_abs
        for axl in (ax1, ax2, ax3, ax4, ax5, ax6, ax11, ax12):
            zero = (z1 - z1) * c / (1. + ((z1 + z1) / 2.))
            axl.plot([zero, zero], [1.2, 1.0], color='c', linewidth=2.00)


        #Tick marks to represent velocity centroid for other components 
        for zh, z2, z3, zovi, zciv, znv in zip(zhi, zsi2, zsi3, zo6, zc4, zn5):
            si2 = (z2 - z1) * c / (1. + ((z2 + z1) / 2.))
            for axk in (ax7, ax8, ax9):
                # ax.axvline((z2-z1)*c/(1.+((z2+z1)/2.)), linewidth=1.25, color='b', linestyle='--')
                # ax.annotate(xy=(comp, 1.05), )
                axk.plot([si2, si2], [1.2, 1.0], color='c', linewidth=2.00)
            si3 = (z3 - z1) * c / (1. + ((z3 + z1) / 2.))
            ax10.plot([si3, si3], [1.2, 1.0], color='c', linewidth=2.00)
            #
            hi2 = (zh - z1) * c / (1. + ((zh + z1) / 2.))
            for axh in (ax1, ax2, ax6):
                axh.plot([hi2, hi2], [1.2, 1.0], color='c', linewidth=2.00)
            #
            ovi2 = (zovi - z1) * c / (1. + ((zovi + z1) / 2.))
            for axh in (ax5, ax11, ax12):
                axh.plot([ovi2, ovi2], [1.2, 1.0], color='c', linewidth=2.00)
            #
            c4i  = (zciv - z1) * c / (1. + ((zciv + z1) / 2.))
            for axb in (ax13, ax14):
                axb.plot([c4i, c4i], [1.2, 1.0], color='c', linewidth=2.00)
            #
            nf  = (znv - z1) * c / (1. + ((znv + z1) / 2.))
            ax15.plot([nf, nf], [1.2, 1.0], color='c', linewidth=2.00)


        # ax.axvline((z2-z1)*c/(1.+((z2+z1)/2.)), linewidth=1.05, color='b', linestyle='-.')
        #
        for axis in ['top', 'bottom', 'left', 'right']:
            ax.spines[axis].set_linewidth(1.75)

        #
        fig.suptitle(
            r'PG 1116+215 :: v$_{\mathrm{rel}}=0$ $\mathrm{km/s}$ $\mathrm{for}$ z$_{\mathrm{abs}} =$' + str(z1)[:8],
            fontsize=15)
        fig.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
        fig.subplots_adjust(top=0.94, hspace=0, wspace=0)
        fig.savefig(plotfile)
        # os.startfile(plotfile) 
plt.close(fig)
# os.startfile(plotfile) 
# subprocess.call([opener, plotfile], shell=True)