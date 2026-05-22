from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 1. Initialize a circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# 2. Apply a Hadamard (H) gate to create a superposition
qc.h(0)

# 3. Measure the qubit, storing the outcome in the classical bit
qc.measure(0, 0)

# 4. Execute using Qiskit Aer Simulator
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts(qc)

print("Measurement outcomes for Superposition (1000 shots):")
print(counts)

# 5. Visualize the results in a bar chart
fig = plot_histogram(counts, title="Superposition Measurement (1000 Shots)", color='midnightblue')
plt.show()  # This pauses the script and opens the graph window!