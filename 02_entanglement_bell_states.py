from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# 1. Initialize a circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# 2. Create the Bell State (Entanglement)
qc.h(0)           # Put Qubit 0 in superposition
qc.cx(0, 1)       # CNOT gate: Qubit 0 controls Qubit 1

# 3. Measure both qubits
qc.measure([0, 1], [0, 1])

# 4. Execute the simulation
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts(qc)

print("Measurement outcomes for Entanglement (1000 shots):")
print(counts)