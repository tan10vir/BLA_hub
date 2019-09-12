import astropy.table as tab
#tab.Table.read('pg1116_data.spec')
#tab.Table.read('pg1116_data.spec', format= 'ascii')
import matplotlib.pyplot as plt
data=tab.Table.read('pg1116_data.spec', format= 'ascii')
plt.plot(data['Wavelength'], data['Flux'])
plt.show()
