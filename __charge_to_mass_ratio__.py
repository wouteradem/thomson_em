import numpy as np
from scipy.constants import mu_0

"""
      Calculates the ration q/m.
"""
def magnetic_induction(radius, current):
    mi = (mu_0 * np.power(0.065, 2) * current) / \
         (2 * (np.power((np.power(radius, 2) + np.power(0.065, 2)), 1.5)))
    return mi


def e_m(anode_voltage, radius, magnetic_field):
    #print(" Radius = {}".format(radius))
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
            r.append(float(columns[2])/2)
        f.close()
    # Step 1: Calculate the e/m ration.
    for current_index in range(len(i)):
        initial_speed = np.sqrt(2 * 175882002411 * 175)
        #magnetic_field = 0.000862 * i[current_index]
        magnetic_field = 0.00089263 * i[current_index]
        # magnetic_field = 0.00058 * i[current_index]
        #magnetic_field = 0.000780 * i[current_index]
        #print(" Magnetic field = {}".format(magnetic_field))
        #em = e_m(200, (r[current_index] * 0.01), magnetic_field)
        #print(em)
        #print(r[current_index] * 0.01)
        #magnetic_field = NR_OF_COILS * magnetic_induction((r[current_index] * 0.01), i[current_index])
        #print(" Magnetic field = {}".format(magnetic_field))
        em = e_m(150, (r[current_index] * 0.01), magnetic_field)
        #em = initial_speed / (r[current_index] * 0.01 * magnetic_field)
        print(em)
