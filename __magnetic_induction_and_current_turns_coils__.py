import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.stats import linregress

"""
    Experiment: Determine linear (I, B, n) relation between number of coils.
"""
if __name__ == '__main__':
    turns = ['300', '600', '1200']
    colours = ['k', 'y', 'g']
    slopes = []
    NR_OF_LINES = 51
    bt = np.empty(NR_OF_LINES)
    i = np.empty(NR_OF_LINES)
    colour_index = 0
    for t in turns:
        f = open('data/ascii/MAG2AA_' + t + '_windingen.AAA', 'r')
        counter = 0
        for line in f:
            line = line.strip()
            columns = line.split()
            i[counter] = float(columns[0])
            bt[counter] = float(columns[1])
            counter += 1
        f.close()

        # Process the data.
        imin, imax = min(i), max(i)
        Polynomial = np.polynomial.Polynomial
        pfit, stats = Polynomial.fit(i, bt, 1, full=True, window=(imin, imax), domain=(imin, imax))
        A0, m = pfit
        resid, rank, sing_val, rcond = stats
        rms = np.sqrt(resid[0]/len(bt))
        slope, intercept, r_value, p_value, std_err = linregress(i, bt)
        slopes.append(slope)

        # Plot.
        c = colours[colour_index]
        plt.plot(i, bt, 'o', color=c)
        plt.plot(i, pfit(i), color=c)
        colour_index += 1
        black_patch = mpatches.Patch(color='black', label=t + ' windingen')

    # Determine slope ration's.
    print(slopes)

    # Finally, draw.
    plt.xlabel('Ampere (mA)')
    plt.ylabel('Magnetisch veld ($\mu$T)')
    plt.show()
