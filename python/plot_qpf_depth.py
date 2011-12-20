# This produces eps graphs with LaTeX math text for inclusion into LaTeX.

import pylab
from pylab import arange,pi,sin,cos,sqrt
fig_width_pt = 346.0  # Get this from LaTeX using \showthe\columnwidth
inches_per_pt = 1.0/72.27               # Convert pt to inch
golden_mean = (sqrt(5)-1.0)/2.0         # Aesthetic ratio
fig_width = fig_width_pt*inches_per_pt  # width in inches
fig_height = fig_width*golden_mean      # height in inches
fig_size =  [fig_width,fig_height]
params = {'backend': 'ps',
          'axes.labelsize': 8,
          'text.fontsize': 10,
          'legend.fontsize': 10,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'figure.figsize': fig_size}
pylab.rcParams.update(params)

STEP = 50000
# Data range
I_MAX = 2**20 / STEP

# Generate data
x = pylab.arange(I_MAX)

import math

# Set up data plot
pylab.figure(1)
pylab.clf()
axes = pylab.axes([0.125,0.2,0.95-0.125,0.95-0.2])

##############################################################################
# Plot!

# 2D NTC
y1 = pylab.arange(I_MAX, dtype=float)

# 1D NTC
y2 = pylab.arange(I_MAX, dtype=float)

for i in range(1,I_MAX+1):
	L = i*STEP
	x[i-1] = L
	a1 = math.ceil(218*L*math.log(L, 1.5))
	a2 = 373
	y1[i-1] = a1 + a2

	b1 = 12*L**2
	b2 = 60*L*(math.log(L, 2)**2)
	b3 = L*math.log(L,2)
	y2[i-1] = b1 + b2 + b3
	
pylab.plot(x,y1,'g-',label='2D NTC')
pylab.plot(x,y2,'g.',label='1D NTC')

axes.set_yscale('log')

pylab.legend(loc='lower right', bbox_to_anchor=(1.0, 0.0),
             ncol=1, fancybox=True, shadow=True)

##############################################################################
# Finish the plot

pylab.xlabel('Modulus size (bits)')
pylab.ylabel('Circuit depth (NTC timesteps)')
pylab.savefig('qpf-depth.eps')
