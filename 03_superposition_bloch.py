from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

# 1. Initialize a circuit with 1 qubit
qc = QuantumCircuit(1)

# 2. Apply a Hadamard (H) gate to create a superposition
qc.h(0)

# 3. Extract the quantum state BEFORE measurement
# (Measuring collapses the state to 0 or 1, destroying the visual!)
state = Statevector(qc)

# 4. Visualize the state on a Bloch Sphere
fig = plot_bloch_multivector(state, title="Superposition State")

# 5. Display the graph window
plt.show()