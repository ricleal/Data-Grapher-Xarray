from Data import Data
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import stats

d = Data("Data Examples/BioSANS_exp253_scan0010_0001.xml")
d.setup()

data = d.data

plt.figure()
data.plot()

# Axes are inverted!
data = data.T
data = data.rename({'x': 'x_old', 'y': 'y_old'})
data = data.rename({'x_old': 'y', 'y_old': 'x'})

plt.figure()
data.plot()

# tube selection
# Fitting a polynomial of degree 6 to a tube
tube_axis = data.y.values
tube_values = data[dict(x=-50)].values
coefficients = scipy.polyfit(tube_axis,tube_values,6)
tube_fit = scipy.poly1d(coefficients)
# binning the tubes
bin_means, bin_edges, binnumber = stats.binned_statistic(tube_axis, tube_fit(tube_axis), statistic='mean',bins=40)
bin_width = (bin_edges[1] - bin_edges[0])
bin_centers = bin_edges[1:] - bin_width/2


# Plotting tube

plt.figure()
plt.plot(tube_axis, tube_values, 'bo', label="Raw")
plt.plot(tube_axis, tube_fit(tube_axis), 'g-', label="Fit")
plt.plot(bin_centers,bin_means,'r-', label="binning")
plt.legend()


# Pixel selection
# pixel = data[dict(y=-60,x=-50)].values

plt.show()
