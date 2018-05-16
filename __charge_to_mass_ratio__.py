import numpy as np
from scipy.constants import mu_0


def average_current(current_voltage):
    a_c = 0.
    i = 0
    v = 0.
    for c_v in current_voltage:
        a_c += c_v[0]
        v = c_v[1]
        i += 1
    return [np.round(a_c/i, 3), v]


# Constants.
NR_OF_COILS = 128
ANODE_VOLTAGE = 150
radii = [8.90, 8.70, 7.00, 5.80]

# Step 1: Calculate the average currents.
currents_voltage_1 = [[0.800, 3.8], [0.743, 3.8], [0.744, 3.8], [0.768, 3.8]]
currents_voltage_2 = [[0.988, 4.7], [0.976, 4.7], [1.000, 4.7], [0.988, 4.7]]
currents_voltage_3 = [[1.217, 5.8], [1.213, 5.8], [1.225, 5.8], [1.230, 5.8]]
currents_voltage_4 = [[1.501, 7.1], [1.487, 7.1], [1.509, 7.1], [1.506, 7.1]]

average_currents_voltages = []
average = average_current(currents_voltage_1)
average_currents_voltages.append(average)
average = average_current(currents_voltage_2)
average_currents_voltages.append(average)
average = average_current(currents_voltage_3)
average_currents_voltages.append(average)
average = average_current(currents_voltage_4)
average_currents_voltages.append(average)
print(average_currents_voltages)

# Step 2: Calculate the magnetic induction.
magnetic_induction = []
c = 0
for a_c_v in average_currents_voltages:
    radius = radii[c] / 2.
    # m_i = mu_0 * np.power(0.8, 1.5) * NR_OF_COILS * a_c_v[0] * (1./radius)
    m_i = 0.000748 * a_c_v[0]
    c += 1
    magnetic_induction.append(m_i)
print(magnetic_induction)

# Step 3: Calculate the e/m -1.758820024 x 10^11 C/kg.
d = 0
for b in magnetic_induction:
    radius = radii[d] / 2.
    q_over_m = (2 * ANODE_VOLTAGE) / (np.power(b, 2) * np.power(radius, 2))
    d += 1
    print(q_over_m)

# Constants.
ANODE_VOLTAGE = 175
radii = [9.20, 7.70, 6.60, 5.80, 5.20]

# Step 1: Calculate the average currents.
currents_voltage_1 = [[0.9980, 4.5], [0.9992, 4.5], [0.9987, 4.5], [0.9973, 4.5]]
currents_voltage_2 = [[1.1982, 5.5], [1.1976, 5.5], [1.1970, 5.5], [1.1967, 5.5]]
currents_voltage_3 = [[1.3946, 6.5], [1.4071, 6.5], [1.4110, 6.5], [1.4122, 6.5]]
currents_voltage_4 = [[1.5997, 7.4], [1.5982, 7.4], [1.5972, 7.4], [1.506, 7.]]
currents_voltage_5 = [[1.7987, 8.3], [1.8002, 8.3], [1.7966, 8.3], [1.7882, 8.3]]

average_currents_voltages = []
average = average_current(currents_voltage_1)
average_currents_voltages.append(average)
average = average_current(currents_voltage_2)
average_currents_voltages.append(average)
average = average_current(currents_voltage_3)
average_currents_voltages.append(average)
average = average_current(currents_voltage_4)
average_currents_voltages.append(average)
average = average_current(currents_voltage_5)
average_currents_voltages.append(average)
print(average_currents_voltages)

# Step 2: Calculate the magnetic induction.
magnetic_induction = []
c = 0
for a_c_v in average_currents_voltages:
    radius = radii[c] / 2.
    # m_i = mu_0 * np.power(0.8, 1.5) * NR_OF_COILS * a_c_v[0] * (1./radius)
    m_i = 0.000748 * a_c_v[0]
    c += 1
    magnetic_induction.append(m_i)
print(magnetic_induction)

# Step 3: Calculate the e/m -1.758820024 x 10^11 C/kg.
d = 0
for b in magnetic_induction:
    radius = radii[d] / 2.
    q_over_m = (2 * ANODE_VOLTAGE) / (np.power(b, 2) * np.power(radius, 2))
    d += 1
    print(q_over_m)

# Constants.
ANODE_VOLTAGE = 200
radii = [10.50, 8.30, 7.00, 6.00, 5.50]

# Step 1: Calculate the average currents.
currents_voltage_1 = [[0.817, 3.8], [0.812, 3.8], [0.815, 3.8], [0.820, 3.8]]
currents_voltage_2 = [[0.972, 4.4], [0.962, 4.4], [0.967, 4.4], [0.968, 4.4]]
currents_voltage_3 = [[1.412, 6.5], [1.407, 6.5], [1.403, 6.5], [1.399, 6.5]]
currents_voltage_4 = [[1.6337, 7.3], [1.6329, 7.3], [1.6305, 7.3], [1.6314, 7.3]]
currents_voltage_5 = [[1.8052, 8.1], [1.8033, 8.1], [1.8026, 8.1], [1.820, 8.1]]

average_currents_voltages = []
average = average_current(currents_voltage_1)
average_currents_voltages.append(average)
average = average_current(currents_voltage_2)
average_currents_voltages.append(average)
average = average_current(currents_voltage_3)
average_currents_voltages.append(average)
average = average_current(currents_voltage_4)
average_currents_voltages.append(average)
average = average_current(currents_voltage_5)
average_currents_voltages.append(average)
print(average_currents_voltages)

# Step 2: Calculate the magnetic induction.
magnetic_induction = []
c = 0
for a_c_v in average_currents_voltages:
    radius = radii[c] / 2.
    # m_i = mu_0 * np.power(0.8, 1.5) * NR_OF_COILS * a_c_v[0] * (1./radius)
    m_i = 0.000748 * a_c_v[0]
    c += 1
    magnetic_induction.append(m_i)
print(magnetic_induction)

# Step 3: Calculate the e/m -1.758820024 x 10^11 C/kg.
d = 0
for b in magnetic_induction:
    radius = radii[d] / 2.
    q_over_m = (2 * ANODE_VOLTAGE) / (np.power(b, 2) * np.power(radius, 2))
    d += 1
    print(q_over_m)

# Test.
b = 0.00089479
radius = 0.0890 / 2
ANODE_VOLTAGE = 150
q_over_m = (2 * ANODE_VOLTAGE) / (np.power(b, 2) * np.power(radius, 2))
print(q_over_m)
