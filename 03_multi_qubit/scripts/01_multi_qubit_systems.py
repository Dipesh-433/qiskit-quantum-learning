from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, DensityMatrix, partial_trace
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 01 — INTRODUCTION TO MULTI-QUBIT SYSTEMS
# ============================================================

print("=" * 70)
print("MODULE 03 — MULTI-QUBIT SYSTEMS")
print("=" * 70)

print("""
A quantum computer can work with multiple qubits.

For n qubits, the quantum state is represented using:

    2^n amplitudes

Examples:

    1 qubit  -> 2 amplitudes
    2 qubits -> 4 amplitudes
    3 qubits -> 8 amplitudes
    4 qubits -> 16 amplitudes

This module explores:
- Two-qubit systems
- Tensor products
- Computational basis states
- CNOT
- Bell states
- Entanglement
- Multi-qubit measurement
- Statevectors
""")


input("\nPress Enter to continue...")


# ============================================================
# 02 — TWO-QUBIT SYSTEM
# ============================================================

print("\n" + "=" * 70)
print("02 — TWO-QUBIT SYSTEM")
print("=" * 70)

qc = QuantumCircuit(2)

print("\nInitial two-qubit circuit:")
print(qc.draw())

state = Statevector.from_instruction(qc)

print("\nInitial statevector:")
print(state)

print("\nInitial probabilities:")
print(state.probabilities_dict())


input("\nPress Enter to continue...")


# ============================================================
# 03 — COMPUTATIONAL BASIS STATES
# ============================================================

print("\n" + "=" * 70)
print("03 — COMPUTATIONAL BASIS STATES")
print("=" * 70)

print("""
For two qubits, there are four computational basis states:

    |00>
    |01>
    |10>
    |11>

Therefore, a two-qubit state requires 4 amplitudes.
""")

basis_states = ["|00>", "|01>", "|10>", "|11>"]

for state_name in basis_states:
    print(state_name)

print("\nCreating each computational basis state...")


# |00>
qc_00 = QuantumCircuit(2)
state_00 = Statevector.from_instruction(qc_00)

print("\n|00> statevector:")
print(state_00)

# |01>
qc_01 = QuantumCircuit(2)
qc_01.x(0)
state_01 = Statevector.from_instruction(qc_01)

print("\n|01> statevector:")
print(state_01)

# |10>
qc_10 = QuantumCircuit(2)
qc_10.x(1)
state_10 = Statevector.from_instruction(qc_10)

print("\n|10> statevector:")
print(state_10)

# |11>
qc_11 = QuantumCircuit(2)
qc_11.x(0)
qc_11.x(1)
state_11 = Statevector.from_instruction(qc_11)

print("\n|11> statevector:")
print(state_11)


input("\nPress Enter to continue...")


# ============================================================
# 04 — TENSOR PRODUCT
# ============================================================

print("\n" + "=" * 70)
print("04 — TENSOR PRODUCTS")
print("=" * 70)

print("""
When combining quantum systems, we use the tensor product.

For example:

    |0> ⊗ |0> = |00>

    |0> ⊗ |1> = |01>

    |1> ⊗ |0> = |10>

    |1> ⊗ |1> = |11>

The tensor product allows individual qubits
to be represented as one combined quantum system.
""")

zero = np.array([1, 0])
one = np.array([0, 1])

state_00_tensor = np.kron(zero, zero)
state_01_tensor = np.kron(zero, one)
state_10_tensor = np.kron(one, zero)
state_11_tensor = np.kron(one, one)

print("\n|0> ⊗ |0> =")
print(state_00_tensor)

print("\n|0> ⊗ |1> =")
print(state_01_tensor)

print("\n|1> ⊗ |0> =")
print(state_10_tensor)

print("\n|1> ⊗ |1> =")
print(state_11_tensor)


input("\nPress Enter to continue...")


# ============================================================
# 05 — SUPERPOSITION IN TWO QUBITS
# ============================================================

print("\n" + "=" * 70)
print("05 — TWO-QUBIT SUPERPOSITION")
print("=" * 70)

qc = QuantumCircuit(2)

qc.h(0)
qc.h(1)

print("\nCircuit:")
print(qc.draw())

state = Statevector.from_instruction(qc)

print("\nStatevector:")
print(state)

print("\nProbabilities:")
print(state.probabilities_dict())

print("""
Each computational basis state has approximately equal probability:

    |00> ≈ 25%
    |01> ≈ 25%
    |10> ≈ 25%
    |11> ≈ 25%
""")


input("\nPress Enter to continue...")


# ============================================================
# 06 — MEASUREMENT OF TWO QUBITS
# ============================================================

print("\n" + "=" * 70)
print("06 — MEASUREMENT OF TWO QUBITS")
print("=" * 70)

measurement_qc = QuantumCircuit(2, 2)

measurement_qc.h(0)
measurement_qc.h(1)

measurement_qc.measure([0, 1], [0, 1])

print("\nMeasurement circuit:")
print(measurement_qc.draw())

simulator = AerSimulator()

job = simulator.run(
    measurement_qc,
    shots=1024
)

result = job.result()

counts = result.get_counts()

print("\nMeasurement results:")
print(counts)

print("\nTotal shots:")
print(sum(counts.values()))

plot_histogram(counts)
plt.show()


input("\nPress Enter to continue...")


# ============================================================
# 07 — CNOT GATE
# ============================================================

print("\n" + "=" * 70)
print("07 — CNOT / CONTROLLED-X GATE")
print("=" * 70)

print("""
CNOT has two qubits:

    Control qubit
          |
          v
        ──●──
          |
          X
          |
        ──⊕──

The target qubit flips only when
the control qubit is |1>.
""")

cnot_qc = QuantumCircuit(2)

cnot_qc.x(0)
cnot_qc.cx(0, 1)

print("\nCircuit:")
print(cnot_qc.draw())

cnot_state = Statevector.from_instruction(cnot_qc)

print("\nFinal statevector:")
print(cnot_state)

print("\nProbabilities:")
print(cnot_state.probabilities_dict())

print("""
The initial state was:

    |00>

After X on qubit 0:

    |01>

After CNOT:

    |11>
""")


input("\nPress Enter to continue...")


# ============================================================
# 08 — CNOT TRUTH TABLE
# ============================================================

print("\n" + "=" * 70)
print("08 — CNOT TRUTH TABLE")
print("=" * 70)

print("""
Control    Target    Output
----------------------------
   0          0         00
   0          1         01
   1          0         11
   1          1         10
""")

cnot_inputs = [
    ("00", []),
    ("01", [("x", 0)]),
    ("10", [("x", 1)]),
    ("11", [("x", 0), ("x", 1)])
]

for label, operations in cnot_inputs:

    circuit = QuantumCircuit(2)

    for gate, qubit in operations:
        if gate == "x":
            circuit.x(qubit)

    circuit.cx(0, 1)

    final_state = Statevector.from_instruction(circuit)

    print(f"Input |{label}> -> {final_state.probabilities_dict()}")


input("\nPress Enter to continue...")


# ============================================================
# 09 — BELL STATE 1
# ============================================================

print("\n" + "=" * 70)
print("09 — BELL STATE |Φ+>")
print("=" * 70)

print("""
Bell states are maximally entangled two-qubit states.

The first Bell state is:

        |00> + |11>
|Φ+> = --------------
             √2

We create it using:

    H on qubit 0
    CNOT with qubit 0 as control
""")

bell_phi_plus = QuantumCircuit(2)

bell_phi_plus.h(0)
bell_phi_plus.cx(0, 1)

print("\nBell circuit:")
print(bell_phi_plus.draw())

bell_state = Statevector.from_instruction(bell_phi_plus)

print("\nBell statevector:")
print(bell_state)

print("\nProbabilities:")
print(bell_state.probabilities_dict())


input("\nPress Enter to continue...")


# ============================================================
# 10 — MEASURING THE BELL STATE
# ============================================================

print("\n" + "=" * 70)
print("10 — MEASURING THE BELL STATE")
print("=" * 70)

bell_measurement = QuantumCircuit(2, 2)

bell_measurement.h(0)
bell_measurement.cx(0, 1)

bell_measurement.measure([0, 1], [0, 1])

print("\nCircuit:")
print(bell_measurement.draw())

job = simulator.run(
    bell_measurement,
    shots=1024
)

result = job.result()

bell_counts = result.get_counts()

print("\nMeasurement results:")
print(bell_counts)

print("""
Notice:

    |00> appears
    |11> appears

But:

    |01> and |10>

do not appear.

The two qubits are strongly correlated.
""")


plot_histogram(bell_counts)
plt.show()


input("\nPress Enter to continue...")


# ============================================================
# 11 — OTHER BELL STATES
# ============================================================

print("\n" + "=" * 70)
print("11 — ALL FOUR BELL STATES")
print("=" * 70)

print("""
The four Bell states are:

|Φ+> = (|00> + |11>) / √2

|Φ-> = (|00> - |11>) / √2

|Ψ+> = (|01> + |10>) / √2

|Ψ-> = (|01> - |10>) / √2
""")


# Phi+
phi_plus = QuantumCircuit(2)
phi_plus.h(0)
phi_plus.cx(0, 1)

phi_plus_state = Statevector.from_instruction(phi_plus)

print("\n|Φ+>:")
print(phi_plus_state)


# Phi-
phi_minus = QuantumCircuit(2)
phi_minus.h(0)
phi_minus.cx(0, 1)
phi_minus.z(0)

phi_minus_state = Statevector.from_instruction(phi_minus)

print("\n|Φ->:")
print(phi_minus_state)


# Psi+
psi_plus = QuantumCircuit(2)
psi_plus.h(0)
psi_plus.cx(0, 1)
psi_plus.x(1)

psi_plus_state = Statevector.from_instruction(psi_plus)

print("\n|Ψ+>:")
print(psi_plus_state)


# Psi-
psi_minus = QuantumCircuit(2)
psi_minus.h(0)
psi_minus.cx(0, 1)
psi_minus.x(1)
psi_minus.z(0)

psi_minus_state = Statevector.from_instruction(psi_minus)

print("\n|Ψ->:")
print(psi_minus_state)


input("\nPress Enter to continue...")


# ============================================================
# 12 — ENTANGLEMENT
# ============================================================

print("\n" + "=" * 70)
print("12 — ENTANGLEMENT")
print("=" * 70)

print("""
Entanglement means that the quantum state of a
multi-qubit system cannot always be described as
independent states of each qubit.

For example:

        |00> + |11>
|Φ+> = --------------
             √2

The complete two-qubit system has a well-defined
joint state, but the individual qubits do not have
independent pure states.

This is one of the most important concepts
in quantum computing.
""")

print("\nBell state:")
print(bell_state)


input("\nPress Enter to continue...")


# ============================================================
# 13 — REDUCED STATE / PARTIAL TRACE
# ============================================================

print("\n" + "=" * 70)
print("13 — REDUCED STATE")
print("=" * 70)

print("""
We can examine one qubit of an entangled system
using a partial trace.

For the Bell state |Φ+>, the individual qubits
are described by mixed states.

This is different from a classical bit
being simply 0 or 1.
""")

# Convert the Bell state into a density matrix
density_matrix = DensityMatrix(bell_state)

print("\nFull two-qubit density matrix:")
print(density_matrix)

# Trace out qubit 1 to obtain the reduced state of qubit 0
reduced_qubit_0 = partial_trace(density_matrix, [1])

# Trace out qubit 0 to obtain the reduced state of qubit 1
reduced_qubit_1 = partial_trace(density_matrix, [0])

print("\nReduced state of qubit 0:")
print(reduced_qubit_0)

print("\nReduced state of qubit 1:")
print(reduced_qubit_1)


input("\nPress Enter to continue...")


# ============================================================
# 14 — ENTANGLED VS SEPARABLE STATES
# ============================================================

print("\n" + "=" * 70)
print("14 — ENTANGLED VS SEPARABLE STATES")
print("=" * 70)

print("""
A separable state can be written as:

    |ψ> = |a> ⊗ |b>

An entangled state cannot be written
as a single tensor product of two independent
single-qubit states.

Example separable state:

    |00>

Example entangled state:

    (|00> + |11>) / √2
""")


# Separable state
separable = QuantumCircuit(2)
separable.h(0)
separable.h(1)

separable_state = Statevector.from_instruction(separable)

print("\nSeparable superposition:")
print(separable_state)

print("\nProbabilities:")
print(separable_state.probabilities_dict())

print("\nEntangled Bell state:")
print(bell_state)

print("\nProbabilities:")
print(bell_state.probabilities_dict())


input("\nPress Enter to continue...")


# ============================================================
# 15 — THREE-QUBIT SYSTEM
# ============================================================

print("\n" + "=" * 70)
print("15 — THREE-QUBIT SYSTEM")
print("=" * 70)

three_qubit = QuantumCircuit(3)

three_qubit.h(0)
three_qubit.cx(0, 1)
three_qubit.cx(0, 2)

print("\nThree-qubit circuit:")
print(three_qubit.draw())

three_state = Statevector.from_instruction(three_qubit)

print("\nThree-qubit statevector:")
print(three_state)

print("\nProbabilities:")
print(three_state.probabilities_dict())

print("""
This creates a three-qubit GHZ-type state:

    |000> + |111>
    -------------
         √2
""")


input("\nPress Enter to continue...")


# ============================================================
# 16 — THREE-QUBIT MEASUREMENT
# ============================================================

print("\n" + "=" * 70)
print("16 — THREE-QUBIT MEASUREMENT")
print("=" * 70)

ghz_measurement = QuantumCircuit(3, 3)

ghz_measurement.h(0)
ghz_measurement.cx(0, 1)
ghz_measurement.cx(0, 2)

ghz_measurement.measure([0, 1, 2], [0, 1, 2])

print("\nGHZ measurement circuit:")
print(ghz_measurement.draw())

job = simulator.run(
    ghz_measurement,
    shots=1024
)

result = job.result()

ghz_counts = result.get_counts()

print("\nMeasurement results:")
print(ghz_counts)

plot_histogram(ghz_counts)
plt.show()


input("\nPress Enter to continue...")


# ============================================================
# 17 — FINAL MULTI-QUBIT EXPERIMENT
# ============================================================

print("\n" + "=" * 70)
print("17 — FINAL EXPERIMENT")
print("=" * 70)

final_circuit = QuantumCircuit(3, 3)

final_circuit.h(0)
final_circuit.cx(0, 1)
final_circuit.cx(1, 2)

final_circuit.measure([0, 1, 2], [0, 1, 2])

print("\nFinal circuit:")
print(final_circuit.draw())

job = simulator.run(
    final_circuit,
    shots=1024
)

result = job.result()

final_counts = result.get_counts()

print("\nFinal measurement results:")
print(final_counts)

plot_histogram(final_counts)
plt.show()


# ============================================================
# 18 — FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("MODULE 03 COMPLETE")
print("=" * 70)

print("""
You learned:

1. Two-qubit systems
2. Computational basis states
3. Tensor products
4. Two-qubit superposition
5. Multi-qubit measurement
6. CNOT / controlled-X
7. CNOT truth table
8. Bell states
9. Bell-state measurement
10. Entanglement
11. Reduced states
12. Separable vs entangled states
13. Three-qubit systems
14. GHZ-type states
15. Multi-qubit experiments

Key idea:

    More qubits
        ↓
    Larger state space
        ↓
    Tensor products
        ↓
    Controlled operations
        ↓
    Entanglement
        ↓
    Powerful quantum algorithms
""")

print("\nLearning philosophy:")
print("Understand → Implement → Experiment → Observe → Analyze")

print("\nNext module: Quantum Information")