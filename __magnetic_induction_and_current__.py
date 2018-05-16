import numpy as np
import matplotlib.pyplot as plt

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
print("MIN = {}".format(imin))
print("MAX = {}".format(imax))

Polynomial = np.polynomial.Polynomial
pfit, stats = Polynomial.fit(i, bt, 1, full=True, window=(imin, imax), domain=(imin, imax))

A0, m = pfit
resid, rank, sing_val, rcond = stats
rms = np.sqrt(resid[0]/len(bt))

plt.plot(i, bt, 'o', color='k')
plt.plot(i, pfit(i), color='k')

plt.plot()
plt.style.use('seaborn-whitegrid')
plt.xlabel("Stroom (mA)")
plt.ylabel("Magnetisch veld (mT)")

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
print("MIN = {}".format(imin))
print("MAX = {}".format(imax))

Polynomial = np.polynomial.Polynomial
pfit, stats = Polynomial.fit(i, bt, 1, full=True, window=(imin, imax), domain=(imin, imax))

A0, m = pfit
resid, rank, sing_val, rcond = stats
rms = np.sqrt(resid[0]/len(bt))

plt.plot(i, bt, 'o', color='r')
plt.plot(i, pfit(i), color='r')

plt.plot()
plt.style.use('seaborn-whitegrid')
plt.xlabel("Stroom (mA)")
plt.ylabel("Magnetisch veld (mT)")
plt.show()