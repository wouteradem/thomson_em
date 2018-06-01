import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import ellipk
from scipy.special import ellipe
from scipy.constants import mu_0

"""
      Calculates B for symmetric plane through z-axis and computes the field 
      from two thin loops of radius a, located at z - +d and -d and current i.
"""
if __name__ == '__main__':

      fig = plt.figure()
      ax = plt.axes(projection='3d')

      LN = 128  # Number of turns in the loops.
      I = 0.697
      a = 0.15  # Radius of the coil.
      d = 0.065  # Distance between the coils.

      # Define the plane over which fields are computed.
      # N must be odd to include the point (0,0).
      M = 26  # No. of points along the rho axis.
      N = 51  # No. of points along the z axis.
      p = np.linspace(-a, a, M)
      # p = np.concatenate([p1[::-1][:-1], p1])  # Make it symmetric.
      z = np.linspace(-d, d, N)
      p, z = np.meshgrid(p, z)  # Create grid of (p,z).

      # Determine modulus and Elliptic integrals.
      denominator = (np.power((a+np.abs(p)), 2) + np.power((z-d), 2))
      k1 = (4 * a * np.abs(p)) / denominator
      K1 = ellipk(k1)
      E1 = ellipe(k1)
      k2 = (4 * a * np.abs(p)) / (np.power((a+np.abs(p)), 2) + np.power((z+d), 2))
      K2 = ellipk(k2)
      E2 = ellipe(k2)

      # Compute B-rho fields.
      bp1 = ((z-d)/(np.abs(p) * np.sqrt(np.power(a+np.abs(p), 2) + np.power(z-d, 2)))) * \
            (((np.power(a, 2) + np.power(np.abs(p), 2) + np.power(z-d, 2)) / (np.power(a-np.abs(p), 2) + np.power(z-d, 2))) * E1 - K1)
      bp2 = ((z+d)/(np.abs(p) * np.sqrt(np.power(a+np.abs(p), 2) + np.power(z+d, 2)))) * \
            (((np.power(a, 2) + np.power(np.abs(p), 2) + np.power(z+d, 2)) / (np.power(a-np.abs(p), 2) + np.power(z+d, 2))) * E2 - K2)
      bp = ((LN * mu_0 * I)/(2 * np.pi)) * (bp1 + bp2)  # 100% correct until here! But throws some calc errors.

      # Compute B-z fields.
      bz1 = (1 / np.sqrt(np.power(a+np.abs(p), 2) + np.power(z-d, 2))) * \
            (((np.power(a, 2) - np.power(np.abs(p), 2) - np.power(z-d, 2)) / (np.power(a-np.abs(p), 2) + np.power(z-d, 2))) * E1 + K1)
      bz2 = (1 / np.sqrt(np.power(a+np.abs(p), 2) + np.power(z+d, 2))) * \
            (((np.power(a, 2) - np.power(np.abs(p), 2) - np.power(z+d, 2)) / (np.power(a-np.abs(p), 2) + np.power(z+d, 2))) * E2 + K2)
      bz = ((LN * mu_0 * I)/(2 * np.pi)) * (bz1 + bz2)  # 100% correct until here! But throws some calc errors.

      # Compute the total B field.
      bt = np.sqrt(np.power(bz, 2) + np.power(bp, 2))
      # Test along the z axis where we know the solution.
      #t1 = np.sqrt(np.power(np.power(a, 2) + np.power(z-d, 2), 3))
      #t2 = np.sqrt(np.power(np.power(a, 2) + np.power(z+d, 2), 3))
      #bzz = 1 / t1 + 1 / t2
      #bzz = 0.5 * LN * mu0 * I * np.power(a, 2) * bzz

      ax.contour3D(z, p, bt, 200, cmap='coolwarm')
      ax.scatter(-d, -a, 0.001953, c='r', marker='o')
      ax.scatter(d, -a, 0.001953, c='r', marker='o')
      ax.scatter(-d, a, 0.001953, c='r', marker='o')
      ax.scatter(d, a, 0.001953, c='r', marker='o')

      ax.scatter(0, -a, 0.000329, c='r', marker='o')
      ax.scatter(0, a, 0.000329, c='r', marker='o')

      ax.scatter(0, 0, 0.000621, c='r', marker='o')

      ax.scatter(-d, 0, 0.000581, c='r', marker='o')
      ax.scatter(d, 0, 0.000581, c='r', marker='o')

      ax.scatter(-d/2, -a/2, 0.000630, c='r', marker='o')
      ax.scatter(-d/2, -a/2, 0.000630, c='r', marker='o')
      ax.scatter(-d/2, -a/2, 0.000630, c='r', marker='o')
      ax.scatter(-d/2, -a/2, 0.000630, c='r', marker='o')

      plt.xlabel('Z(m)')
      plt.ylabel('R(m)')
      ax.set_zlabel('B([$\mu$]T)')
      plt.show()
