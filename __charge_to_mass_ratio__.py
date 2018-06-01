import numpy as np
from scipy.constants import mu_0

"""
      Calculates the ration q/m.
"""
def magnetic_induction(radius, current):
    # return mu_0 * np.power(0.8, 1.5) * NR_OF_COILS * current * (1./radius) -> Wrong formula!
    factor = (mu_0 * NR_OF_COILS * np.power(radius, 2)) / \
           (np.power((np.power(radius, 2) + np.power(0.065, 2)), 1.5))
    return factor * current


def e_m(anode_voltage, radius, magnetic_field):
    return (2 * anode_voltage) / (np.power(magnetic_field, 2) * np.power(radius, 2))


if __name__ == '__main__':

    # Constants.
    NR_OF_COILS = 128
    anode_voltages = ['150']

    # Step 0: Read data into arrays.
    for a_v in anode_voltages:
        f = open('data/current_voltage_' + a_v, 'r')
        i, v, r = [], [], []
        for line in f:
            line = line.strip()
            columns = line.split()
            i.append(float(columns[0]))
            v.append(float(columns[1]))
            r.append(float(columns[2]))
        f.close()

    # Step 1: Calculate the e/m ration.
    for current_index in range(len(i)):
        #magnetic_field = 0.000858 * i[current_index] * 0.001
        magnetic_field = magnetic_induction(0.15, i[current_index])
        em = e_m(v[current_index], r[current_index], magnetic_field * 0.001)
        print(em)
