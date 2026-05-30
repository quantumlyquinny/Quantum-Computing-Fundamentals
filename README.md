# Quantum Computing Fundamentals: BB84 QKD & Threat Simulation

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Qiskit](https://img.shields.io/badge/Qiskit-IBM-6929EE.svg)
![JavaScript](https://img.shields.io/badge/Visualizer-Vanilla%20JS-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-purple.svg)

⚡ **[Launch the Interactive BB84 Visualizer →](https://quantumlyquinny.github.io/Quantum-Computing-Fundamentals/visualizer/)**

A progressive quantum computing sandbox built with IBM's Qiskit framework, culminating
in a simulation of the BB84 Quantum Key Distribution (QKD) protocol with a live
eavesdropper threat model. Presented in an academic setting as an introduction to
quantum cryptographic principles.

## What This Covers

The repository builds from single-qubit fundamentals to applied quantum cryptography
in six progressive scripts:

| Script | Concept |
|---|---|
| `01_superposition.py` | Hadamard gate + statistical measurement |
| `02_entanglement_bell_state.py` | Bell State via H + CNOT gates |
| `03_superposition_bloch.py` | Pre-measurement state vector visualisation |
| `04_entanglement_bloch.py` | Mixed states + No-Cloning theorem |
| `05_bb84_baseline.py` | Secure BB84 transmission — 0.00% QBER |
| `06_bb84_eavesdropper.py` | Intercept-resend attack + automatic abort |

## The Eavesdropper Threat Model

The core insight of BB84 is that eavesdropping is **physically detectable**.

When Eve intercepts a qubit, she must measure it — which forces a quantum state collapse.
Since she guesses the correct measurement basis only ~50% of the time, she permanently
corrupts ~25% of transmitted qubits before forwarding them to Bob.

During the classical sifting phase, Alice and Bob compare a subset of their keys.
A Quantum Bit Error Rate (QBER) above ~11% statistically proves the channel is compromised.
`06_bb84_eavesdropper.py` simulates this end-to-end and **automatically aborts the
protocol** when the QBER threshold is exceeded.

## Interactive Visualizer

The [live demo](https://quantumlyquinny.github.io/Quantum-Computing-Fundamentals/visualizer/)
is a custom vanilla JS front-end that visualises quantum state collapses and QBER
detection in real time — no installation required.

## Setup

```bash
git clone https://github.com/quantumlyquinny/Quantum-Computing-Fundamentals
cd Quantum-Computing-Fundamentals
pip install qiskit qiskit-aer matplotlib pylatexenc numpy

# Run the full BB84 eavesdropper simulation
python 06_bb84_eavesdropper.py
```

## Background Reading

If you're new to QKD, these resources build the intuition well:
- [IBM Qiskit Textbook — Quantum Protocols](https://learn.qiskit.org)
- [BB84 original paper — Bennett & Brassard, 1984](https://arxiv.org/abs/2003.06557)
