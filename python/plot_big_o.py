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
I_MAX = 25

# Generate data
x = pylab.arange(I_MAX)

import math

# Set up data plot
pylab.figure(1)
pylab.clf()
axes = pylab.axes([0.125,0.2,0.95-0.125,0.95-0.2])

##############################################################################
# Plot!

# log n
y1 = pylab.arange(I_MAX, dtype=float)

# n
y2 = pylab.arange(I_MAX, dtype=float)

# n \log n
y3 = pylab.arange(I_MAX, dtype=float)

# n^2
y4 = pylab.arange(I_MAX, dtype=float)

# 2^n
y5 = pylab.arange(I_MAX, dtype=float)


for i in range(1,I_MAX):
	y1[i] = math.log(i,2)
	y2[i] = i
	y3[i] = i * math.log(i,2)
	y4[i] = i**2
	y5[i] = 2**i
	
#axes.set_yscale('log')

pylab.plot(x,y1,'g-',label='$\log n$')
pylab.plot(x,y2,'g.',label='$n$')
pylab.plot(x,y3,'go',label='$n\log n$')
pylab.plot(x,y4,'gx',label='$n^2$')
#pylab.plot(x,y5,'g+',label='$2^n$')

pylab.legend(loc='lower right', bbox_to_anchor=(1.0, 0.0),
             ncol=1, fancybox=True, shadow=True)

##############################################################################
# Finish the plot

pylab.xlabel('input size')
pylab.ylabel('function')
pylab.savefig('big-o.eps')
