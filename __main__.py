import numpy as np
from scipy.constants import mu_0
import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import ellipk
from scipy.special import ellipe

# Like loops.u but symmetric plane through z axis
# Computes the a field from 2 thin loops of radium a,
# located at z - +d and -d, (d-a/2, Helmholtz Coils), and
# current 1.

#fig = plt.figure()
#ax = Axes3D(fig)

LN = 48  # Number of turns in the loops.
I = 0.019052
a = 0.6096
d = a/2

# Define the plane over which fields are computed.
# N must be odd to include the point (0,0).
M = 26  # No. of points along the rho axis.
N = 51  # No. of points along the z axis.
p1 = np.linspace(0, a, M)
p = np.concatenate([p1[::-1][:-1], p1])  # Make it symmetric.
z = np.linspace(-d, d, N)
p, z = np.meshgrid(p, z)  # Create grid of (p,z).

# Determine modulus and Elliptic integrals.
denominator = (np.power((a+p), 2) + np.power((z-d), 2))
k1 = (4 * a * p) / denominator
K1 = ellipk(k1)
E1 = ellipe(k1)
k2 = (4 * a * p) / (np.power((a+p), 2) + np.power((z+d), 2))
K2 = ellipk(k2)
E2 = ellipe(k2)

# Compute B-rho fields
bp1 = ((z-d)/(p * np.sqrt(np.power(a+p, 2) + np.power(z-d, 2)))) * \
      (((np.power(a, 2) + np.power(p, 2) + np.power(z-d, 2)) / (np.power(a-p, 2) + np.power(z-d, 2))) * E1 - K1)
bp2 = ((z+d)/(p * np.sqrt(np.power(a+p, 2) + np.power(z+d, 2)))) * \
      (((np.power(a, 2) + np.power(p, 2) + np.power(z+d, 2)) / (np.power(a-p, 2) + np.power(z+d, 2))) * E2 - K2)
bp = ((LN * mu_0 * I)/(2 * np.pi)) * (bp1 + bp2)  # 100% correct until here! But throws some calc errors.

# Compute B-z fields
bz1 = (1 / np.sqrt(np.power(a+p, 2) + np.power(z-d, 2))) * \
      (((np.power(a, 2) - np.power(p, 2) - np.power(z-d, 2)) / (np.power(a-p, 2) + np.power(z-d, 2))) * E1 + K1)
bz2 = (1 / np.sqrt(np.power(a+p, 2) + np.power(z+d, 2))) * \
      (((np.power(a, 2) - np.power(p, 2) - np.power(z+d, 2)) / (np.power(a-p, 2) + np.power(z+d, 2))) * E2 + K2)
bz = ((LN * mu_0 * I)/(2 * np.pi)) * (bz1 + bz2)  # 100% correct until here! But throws some calc errors.

# Compute the total B field
bt = np.sqrt(np.power(bz, 2) + np.power(bp, 2))
#print(bt)

# Test along the z axis where we know the solution
#t1 = np.sqrt(np.power(np.power(a, 2) + np.power(z-d, 2), 3))
#t2 = np.sqrt(np.power(np.power(a, 2) + np.power(z+d, 2), 3))
#bzz = 1 / t1 + 1 / t2
#bzz = 0.5 * LN * mu0 * I * np.power(a, 2) * bzz

#ax.plot_surface(z, p, bt, cmap=plt.cm.YlGnBu_r)
##ax.set_xlabel(r'$\z-axis(m)$')
##ax.set_ylabel(r'$\p-axis(m)$')
##ax.set_zlabel(r'$B(\z)magnitude(mT)$')

# plt.show()