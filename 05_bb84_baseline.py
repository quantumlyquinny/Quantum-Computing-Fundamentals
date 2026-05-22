from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit_aer import AerSimulator
import numpy as np

num_bits = 32
print(f"--- Starting BB84 QKD Protocol ({num_bits} bits) [BASELINE] ---")

# 1. Random Arrays (No Eve)
alice_bits = np.random.randint(2, size=num_bits)
alice_bases = np.random.randint(2, size=num_bits)
bob_bases = np.random.randint(2, size=num_bits)

# 2. Setup Registers
qr = QuantumRegister(num_bits, name="q")
cr_bob = ClassicalRegister(num_bits, name="bob_c")
qc = QuantumCircuit(qr, cr_bob)

# 3. Alice Encodes
for i in range(num_bits):
    if alice_bits[i] == 1:
        qc.x(i)
    if alice_bases[i] == 1:
        qc.h(i)

qc.barrier()

# 4. Bob Measures Directly
for i in range(num_bits):
    if bob_bases[i] == 1:
        qc.h(i)
    qc.measure(i, cr_bob[i])

# 5. Execute Simulation
simulator = AerSimulator()
job = simulator.run(qc, shots=1, memory=True)
result = job.result()
bob_str = result.get_memory()[0]
bob_bits = [int(b) for b in reversed(bob_str)]

# 6. Sifting Phase
sifted_alice = []
sifted_bob = []
for i in range(num_bits):
    if alice_bases[i] == bob_bases[i]:
        sifted_alice.append(alice_bits[i])
        sifted_bob.append(bob_bits[i])

# 7. QBER Calculation (Should always be 0.00% here)
errors = sum(1 for a, b in zip(sifted_alice, sifted_bob) if a != b)
qber = (errors / len(sifted_alice)) * 100 if len(sifted_alice) > 0 else 0

print("-----------------------------------")
print(f"Total Sifted Bits Retained: {len(sifted_alice)}")
print(f"Errors Detected:            {errors}")
print(f"Quantum Bit Error Rate:     {qber:.2f}%")
print("-----------------------------------")

if qber == 0:
    print("SUCCESS: Transmission secure. Perfect key generated.")
else:
    print("WARNING: Errors detected.")