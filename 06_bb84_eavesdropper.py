from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit_aer import AerSimulator
import numpy as np

# 1. Configuration
num_bits = 32 # Higher bit count for better statistical averages
print(f"--- Starting BB84 QKD Protocol ({num_bits} bits) ---")

# 2. Generate Random Arrays for All Parties
# 0 = Rectilinear Basis (+), 1 = Diagonal Basis (x)
alice_bits = np.random.randint(2, size=num_bits)
alice_bases = np.random.randint(2, size=num_bits)
eve_bases = np.random.randint(2, size=num_bits)
bob_bases = np.random.randint(2, size=num_bits)

# Setup isolated registers for Eve and Bob's measurements
qr = QuantumRegister(num_bits, name="q")
cr_eve = ClassicalRegister(num_bits, name="eve_c")
cr_bob = ClassicalRegister(num_bits, name="bob_c")
qc = QuantumCircuit(qr, cr_eve, cr_bob)

# 3. Alice Encodes the Qubits
for i in range(num_bits):
    if alice_bits[i] == 1:
        qc.x(i) # Flip to |1>
    if alice_bases[i] == 1:
        qc.h(i) # Shift to diagonal basis

qc.barrier() # Visual separator for the circuit

# 4. The Attack: Eve Intercepts the Transmission
print(">> Eve is intercepting the quantum channel...")
for i in range(num_bits):
    if eve_bases[i] == 1:
        qc.h(i)
    
    # Eve measures, forcibly collapsing the quantum wave function
    qc.measure(i, cr_eve[i]) 
    
    # Eve attempts to re-encode the collapsed qubit before sending it to Bob
    if eve_bases[i] == 1:
        qc.h(i)

qc.barrier()

# 5. Bob Receives and Measures
for i in range(num_bits):
    if bob_bases[i] == 1:
        qc.h(i)
    qc.measure(i, cr_bob[i])

print(">> Generating circuit diagram (this may take a few seconds)...")
qc.draw(output='mpl', filename='eve_interception_circuit.png', scale=0.5)

# 6. Execute the Quantum Simulation
simulator = AerSimulator()
job = simulator.run(qc, shots=1, memory=True)
result = job.result()

# Qiskit outputs classical registers separated by a space (Bob Eve)
measured_str = result.get_memory()[0]
bob_str, eve_str = measured_str.split(" ")

# Reverse the strings to match our left-to-right Python arrays
bob_bits = [int(b) for b in reversed(bob_str)]

# 7. The Classical Sifting Phase
sifted_alice = []
sifted_bob = []

for i in range(num_bits):
    # Alice and Bob publicly compare bases. They ignore Eve entirely here.
    if alice_bases[i] == bob_bases[i]:
        sifted_alice.append(alice_bits[i])
        sifted_bob.append(bob_bits[i])

# 8. Security Audit: Calculate Quantum Bit Error Rate (QBER)
errors = 0
for a, b in zip(sifted_alice, sifted_bob):
    if a != b:
        errors += 1

# Calculate the percentage of corrupted bits in the final key
qber = (errors / len(sifted_alice)) * 100 if len(sifted_alice) > 0 else 0

print("-----------------------------------")
print(f"Total Sifted Bits Retained: {len(sifted_alice)}")
print(f"Errors Caused by Eve:       {errors}")
print(f"Quantum Bit Error Rate:     {qber:.2f}%")
print("-----------------------------------")

# 9. Protocol Abort Logic
if qber > 0:
    print("WARNING: Eavesdropper detected! The quantum state was collapsed.")
    print("ACTION: Protocol aborted. Key discarded.")
else:
    print("SUCCESS: Transmission secure. No eavesdropper detected.")