# Quantum Computing Fundamentals: BB84 QKD & Threat Simulation

This repository serves as a foundational sandbox for quantum computing concepts, culminating in a simulation of the **BB84 Quantum Key Distribution (QKD) protocol** and an applied eavesdropper threat model.

Built using IBM's Qiskit framework, the project demonstrates the mathematical principles of quantum state preparation, superposition, entanglement, and cryptographic key sifting.

## Project Architecture

The repository progresses from fundamental single-qubit operations to composite entangled systems, and finally to applied quantum cryptography:

1. `01_superposition.py`: Demonstrates basic Hadamard gate application and statistical measurement.
2. `02_entanglement_bell_state.py`: Generates a standard Bell State using H and CNOT gates.
3. `03_superposition_bloch.py`: Visualizes pre-measurement state vectors mathematically.
4. `04_entanglement_bloch.py`: Visualizes perfectly mixed states to demonstrate the No-Cloning theorem.
5. `05_bb84_baseline.py`: Simulates a secure, peer-to-peer BB84 QKD transmission resulting in a perfect shared key (0.00% QBER).
6. `06_bb84_eavesdropper.py`: Injects an intercept-resend attack (Man-in-the-Middle) into the transmission.

## Threat Detection (QBER)

The eavesdropper simulation explicitly models the physics of a quantum attack. Because an eavesdropper (Eve) must measure the traveling qubits to read them, she forces the quantum state to collapse. 

When she guesses the incorrect measurement basis (which happens ~50% of the time), she permanently alters the qubit before passing it to Bob. This mathematically guarantees an approximate **25-35% Quantum Bit Error Rate (QBER)** during the classical sifting phase. The `06_bb84_eavesdropper.py` script automatically calculates this QBER and triggers a protocol abort if the channel is compromised.

## Requirements

To run these simulations locally, ensure you have Python installed alongside the following dependencies:
* `qiskit`
* `qiskit-aer`
* `matplotlib`
* `pylatexenc` (Required for Matplotlib circuit visualizations)
* `numpy`