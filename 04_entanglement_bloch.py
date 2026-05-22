from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib

# Force Matplotlib to use the standard Windows graphical interface
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt

# 1. Initialize a circuit with 2 qubits
qc = QuantumCircuit(2)

# 2. Create the standard Bell State (Entanglement)
qc.h(0)           
qc.cx(0, 1)       

# 3. Extract the theoretical quantum state BEFORE measurement
state = Statevector(qc)

# 4. Attempt to visualize the state on two separate Bloch spheres
fig = plot_bloch_multivector(state, title="Bloch Representation of Entangled Qubits")

# 5. Display the graph window
plt.show()