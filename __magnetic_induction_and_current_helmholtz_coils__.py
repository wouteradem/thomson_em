import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

"""
      Calculates B field from ASCII data.
"""

# Orientation North - South.
f = open('data/ascii/MAG2AA.AAF', 'r')
bt = np.empty(51)
i = np.empty(51)
counter = 0
for line in f:
    line = line.strip()
    columns = line.split()
    i[counter] = float(columns[0])
    bt[counter] = float(columns[1])
    counter += 1
f.close()

imin, imax = min(i), max(i)
Polynomial = np.polynomial.Polynomial
pfit, stats = Polynomial.fit(i, bt, 1, full=True, window=(imin, imax), domain=(imin, imax))

A0, m = pfit
resid, rank, sing_val, rcond = stats
rms = np.sqrt(resid[0]/len(bt))

slope, intercept, r_value, p_value, std_err = linregress(i, bt)
print("SLOPE North-South = {}".format(slope))

plt.plot(i, bt, 'o', color='k')
plt.plot(i, pfit(i), color='k')

plt.plot()
plt.style.use('seaborn-whitegrid')
plt.xlabel("Stroom (mA)")
plt.ylabel("Magnetisch veld (\microT)")

# Orientation East - West.
f = open('data/ascii/MAG2AA.AAE', 'r')
bt = np.empty(51)
i = np.empty(51)
counter = 0
for line in f:
    line = line.strip()
    columns = line.split()
    i[counter] = float(columns[0])
    bt[counter] = float(columns[1])
    counter += 1
f.close()

imin, imax = min(i), max(i)
Polynomial = np.polynomial.Polynomial
pfit, stats = Polynomial.fit(i, bt, 1, full=True, window=(imin, imax), domain=(imin, imax))

A0, m = pfit
resid, rank, sing_val, rcond = stats
rms = np.sqrt(resid[0]/len(bt))
slope, intercept, r_value, p_value, std_err = linregress(i, bt)
print("SLOPE East-West = {}".format(slope))

plt.plot(i, bt, 'o', color='r')
plt.plot(i, pfit(i), color='r')

plt.plot()
plt.style.use('seaborn-whitegrid')
plt.xlabel("Stroom (mA)")
plt.ylabel("Magnetisch veld ($\mu$T)")
plt.show()
