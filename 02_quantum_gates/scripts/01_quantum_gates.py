from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt
import numpy as np


# ============================================================
# QISKIT QUANTUM LEARNING
# Module 02: Quantum Gates
# ============================================================
#
# Topics covered:
# 1. Quantum gate matrices
# 2. Pauli X gate
# 3. Pauli Y gate
# 4. Pauli Z gate
# 5. Hadamard gate
# 6. Phase gates: S and T
# 7. Rotation gates: RX, RY, RZ
# 8. Controlled gates: CX and CZ
# 9. SWAP gate
# 10. Gate combinations
# 11. Statevector experiments
# 12. Bloch sphere visualization
#
# Learning philosophy:
# Understand → Implement → Experiment → Observe → Analyze
# ============================================================


# ============================================================
# 1. INTRODUCTION
# ============================================================

print("=" * 65)
print("QISKIT QUANTUM LEARNING")
print("MODULE 02: QUANTUM GATES")
print("=" * 65)

print("""
Quantum gates are operations that change the state of qubits.

Classical logic gates:
    AND, OR, NOT, XOR

Quantum gates:
    X, Y, Z, H, S, T, RX, RY, RZ, CX, CZ, SWAP, ...

Most quantum gates are represented using unitary matrices.
""")

input("\nPress Enter to continue...")


# ============================================================
# 2. COMMON QUANTUM GATE MATRICES
# ============================================================

print("\n" + "=" * 65)
print("2. COMMON QUANTUM GATE MATRICES")
print("=" * 65)

X_matrix = np.array([
    [0, 1],
    [1, 0]
], dtype=complex)

Y_matrix = np.array([
    [0, -1j],
    [1j, 0]
], dtype=complex)

Z_matrix = np.array([
    [1, 0],
    [0, -1]
], dtype=complex)

H_matrix = (1 / np.sqrt(2)) * np.array([
    [1, 1],
    [1, -1]
], dtype=complex)

S_matrix = np.array([
    [1, 0],
    [0, 1j]
], dtype=complex)

T_matrix = np.array([
    [1, 0],
    [0, np.exp(1j * np.pi / 4)]
], dtype=complex)


print("\nPauli-X matrix:")
print(X_matrix)

print("\nPauli-Y matrix:")
print(Y_matrix)

print("\nPauli-Z matrix:")
print(Z_matrix)

print("\nHadamard matrix:")
print(H_matrix)

print("\nS matrix:")
print(S_matrix)

print("\nT matrix:")
print(T_matrix)

input("\nPress Enter to continue...")


# ============================================================
# 3. PAULI X GATE
# ============================================================

print("\n" + "=" * 65)
print("3. PAULI X GATE")
print("=" * 65)

print("""
The Pauli-X gate is similar to the classical NOT gate.

    X|0> = |1>
    X|1> = |0>

Matrix:

    [0 1]
    [1 0]
""")

x_circuit = QuantumCircuit(1)

print("\nInitial circuit:")
print(x_circuit.draw())

initial_state = Statevector.from_instruction(x_circuit)

print("\nInitial state:")
print(initial_state)

x_circuit.x(0)

print("\nCircuit after X gate:")
print(x_circuit.draw())

x_state = Statevector.from_instruction(x_circuit)

print("\nState after X gate:")
print(x_state)

print("\nProbabilities:")
print(x_state.probabilities_dict())

input("\nPress Enter to continue...")


# ============================================================
# 4. PAULI Y GATE
# ============================================================

print("\n" + "=" * 65)
print("4. PAULI Y GATE")
print("=" * 65)

print("""
The Pauli-Y gate changes both the state and phase.

    Y|0> = i|1>
    Y|1> = -i|0>

Matrix:

    [0  -i]
    [i   0]
""")

y_circuit = QuantumCircuit(1)

y_circuit.y(0)

print("\nCircuit:")
print(y_circuit.draw())

y_state = Statevector.from_instruction(y_circuit)

print("\nState after Y gate:")
print(y_state)

print("\nProbabilities:")
print(y_state.probabilities_dict())

input("\nPress Enter to continue...")


# ============================================================
# 5. PAULI Z GATE
# ============================================================

print("\n" + "=" * 65)
print("5. PAULI Z GATE")
print("=" * 65)

print("""
The Pauli-Z gate performs a phase flip.

    Z|0> = |0>
    Z|1> = -|1>

Matrix:

    [1   0]
    [0  -1]
""")

z_circuit = QuantumCircuit(1)

z_circuit.z(0)

print("\nCircuit:")
print(z_circuit.draw())

z_state = Statevector.from_instruction(z_circuit)

print("\nState after Z gate:")
print(z_state)

print("\nProbabilities:")
print(z_state.probabilities_dict())

input("\nPress Enter to continue...")


# ============================================================
# 6. HADAMARD GATE
# ============================================================

print("\n" + "=" * 65)
print("6. HADAMARD GATE")
print("=" * 65)

print("""
The Hadamard gate creates superposition.

    H|0> = (|0> + |1>) / sqrt(2)

    H|1> = (|0> - |1>) / sqrt(2)

Matrix:

    1       [1   1]
    ---  *
    sqrt(2) [1  -1]
""")

h_circuit = QuantumCircuit(1)

h_circuit.h(0)

print("\nCircuit:")
print(h_circuit.draw())

h_state = Statevector.from_instruction(h_circuit)

print("\nState after H gate:")
print(h_state)

print("\nProbabilities:")
print(h_state.probabilities_dict())

input("\nPress Enter to continue...")


# ============================================================
# 7. PHASE GATES: S AND T
# ============================================================

print("\n" + "=" * 65)
print("7. PHASE GATES: S AND T")
print("=" * 65)

print("""
S gate:

    S = diag(1, i)

It adds a phase of pi/2 to |1>.

T gate:

    T = diag(1, exp(i*pi/4))

It adds a phase of pi/4 to |1>.
""")

s_circuit = QuantumCircuit(1)
s_circuit.s(0)

print("\nS gate circuit:")
print(s_circuit.draw())

s_state = Statevector.from_instruction(s_circuit)

print("\nState after S gate:")
print(s_state)


t_circuit = QuantumCircuit(1)
t_circuit.t(0)

print("\nT gate circuit:")
print(t_circuit.draw())

t_state = Statevector.from_instruction(t_circuit)

print("\nState after T gate:")
print(t_state)

input("\nPress Enter to continue...")


# ============================================================
# 8. ROTATION GATES
# ============================================================

print("\n" + "=" * 65)
print("8. ROTATION GATES")
print("=" * 65)

print("""
Rotation gates rotate a qubit state around the Bloch sphere.

RX(theta):
    Rotation around the X-axis.

RY(theta):
    Rotation around the Y-axis.

RZ(theta):
    Rotation around the Z-axis.
""")

theta = np.pi / 2

rx_circuit = QuantumCircuit(1)
rx_circuit.rx(theta, 0)

ry_circuit = QuantumCircuit(1)
ry_circuit.ry(theta, 0)

rz_circuit = QuantumCircuit(1)
rz_circuit.rz(theta, 0)

print("\nRX(pi/2) circuit:")
print(rx_circuit.draw())

print("\nRY(pi/2) circuit:")
print(ry_circuit.draw())

print("\nRZ(pi/2) circuit:")
print(rz_circuit.draw())

rx_state = Statevector.from_instruction(rx_circuit)
ry_state = Statevector.from_instruction(ry_circuit)
rz_state = Statevector.from_instruction(rz_circuit)

print("\nState after RX(pi/2):")
print(rx_state)

print("\nState after RY(pi/2):")
print(ry_state)

print("\nState after RZ(pi/2):")
print(rz_state)

input("\nPress Enter to continue...")


# ============================================================
# 9. CONTROLLED-X / CNOT GATE
# ============================================================

print("\n" + "=" * 65)
print("9. CONTROLLED-X / CNOT GATE")
print("=" * 65)

print("""
The CNOT gate uses two qubits.

    Control qubit ──●──
                    │
    Target qubit  ──X──

The X gate is applied to the target only when
the control qubit is |1>.
""")

cx_circuit = QuantumCircuit(2)

cx_circuit.x(0)
cx_circuit.cx(0, 1)

print("\nCNOT circuit:")
print(cx_circuit.draw())

cx_state = Statevector.from_instruction(cx_circuit)

print("\nState after CNOT:")
print(cx_state)

print("\nProbabilities:")
print(cx_state.probabilities_dict())

input("\nPress Enter to continue...")


# ============================================================
# 10. CONTROLLED-Z GATE
# ============================================================

print("\n" + "=" * 65)
print("10. CONTROLLED-Z GATE")
print("=" * 65)

print("""
The CZ gate applies a Z operation to the target qubit
when the control qubit is |1>.
""")

cz_circuit = QuantumCircuit(2)

cz_circuit.x(0)
cz_circuit.h(1)
cz_circuit.cz(0, 1)

print("\nCZ circuit:")
print(cz_circuit.draw())

cz_state = Statevector.from_instruction(cz_circuit)

print("\nState after CZ:")
print(cz_state)

input("\nPress Enter to continue...")


# ============================================================
# 11. SWAP GATE
# ============================================================

print("\n" + "=" * 65)
print("11. SWAP GATE")
print("=" * 65)

print("""
The SWAP gate exchanges the states of two qubits.

    q0 ──X──
        │
    q1 ──X──
""")

swap_circuit = QuantumCircuit(2)

swap_circuit.x(0)

print("\nBefore SWAP:")
print(swap_circuit.draw())

swap_circuit.swap(0, 1)

print("\nAfter SWAP:")
print(swap_circuit.draw())

swap_state = Statevector.from_instruction(swap_circuit)

print("\nState after SWAP:")
print(swap_state)

print("\nProbabilities:")
print(swap_state.probabilities_dict())

input("\nPress Enter to continue...")


# ============================================================
# 12. GATE COMBINATIONS
# ============================================================

print("\n" + "=" * 65)
print("12. GATE COMBINATIONS")
print("=" * 65)

print("""
Quantum gates can be combined to create more complex operations.

Example:

    |0> → H → Z → H → |1>

The sequence H-Z-H is equivalent to X.
""")

combination = QuantumCircuit(1)

combination.h(0)
combination.z(0)
combination.h(0)

print("\nH-Z-H circuit:")
print(combination.draw())

combination_state = Statevector.from_instruction(combination)

print("\nFinal state:")
print(combination_state)

print("\nProbabilities:")
print(combination_state.probabilities_dict())

input("\nPress Enter to continue...")


# ============================================================
# 13. GATE INVERSE / SELF-INVERSE EXPERIMENT
# ============================================================

print("\n" + "=" * 65)
print("13. GATE INVERSE / SELF-INVERSE EXPERIMENT")
print("=" * 65)

print("""
Some quantum gates are self-inverse.

Examples:

    X² = I
    Y² = I
    Z² = I
    H² = I

Applying the same gate twice returns the original state.
""")

inverse_circuit = QuantumCircuit(1)

inverse_circuit.x(0)
inverse_circuit.x(0)

print("\nX followed by X:")
print(inverse_circuit.draw())

inverse_state = Statevector.from_instruction(inverse_circuit)

print("\nFinal state:")
print(inverse_state)

input("\nPress Enter to continue...")


# ============================================================
# 14. BLOCH SPHERE VISUALIZATION
# ============================================================

print("\n" + "=" * 65)
print("14. BLOCH SPHERE VISUALIZATION")
print("=" * 65)

print("""
The Bloch sphere provides a geometric representation
of a single-qubit state.

Common states:

    |0>  → +Z axis
    |1>  → -Z axis
    |+>  → +X axis
    |->  → -X axis
""")

bloch_states = {
    "|0>": [0, 0, 1],
    "|1>": [0, 0, -1],
    "|+>": [1, 0, 0],
    "|->": [-1, 0, 0],
}

for state_name, vector in bloch_states.items():

    print(f"\nBloch vector of {state_name}: {vector}")

    fig = plot_bloch_vector(
        vector,
        title=f"Bloch Sphere: {state_name}"
    )

    plt.show()


input("\nPress Enter to continue...")


# ============================================================
# 15. PAULI GATE BLOCH-SPHERE EXPERIMENT
# ============================================================

print("\n" + "=" * 65)
print("15. PAULI GATE BLOCH-SPHERE EXPERIMENT")
print("=" * 65)

print("""
We now visualize the effect of X, Y and Z on |0>.

X:
    |0> → |1>

Y:
    |0> → i|1>

Z:
    |0> → |0>
    but changes the phase of |1>.
""")

# X applied to |0>
x_bloch = [0, 0, -1]

fig = plot_bloch_vector(
    x_bloch,
    title="After X Gate: |0> → |1>"
)

plt.show()


# Y applied to |0>
y_bloch = [0, 0, -1]

fig = plot_bloch_vector(
    y_bloch,
    title="After Y Gate: |0> → i|1>"
)

plt.show()


# Z applied to |0>
z_bloch = [0, 0, 1]

fig = plot_bloch_vector(
    z_bloch,
    title="After Z Gate: |0> → |0>"
)

plt.show()


# ============================================================
# 16. GATE COMPARISON
# ============================================================

print("\n" + "=" * 65)
print("16. QUANTUM GATE COMPARISON")
print("=" * 65)

print("""
Gate      Main effect
------------------------------------------------
X         Bit flip
Y         Bit + phase change
Z         Phase flip
H         Creates superposition
S         Adds pi/2 phase
T         Adds pi/4 phase
RX        Rotation around X-axis
RY        Rotation around Y-axis
RZ        Rotation around Z-axis
CX        Controlled-X operation
CZ        Controlled-Z operation
SWAP      Exchanges two qubit states
""")

input("\nPress Enter to continue...")


# ============================================================
# 17. FINAL EXPERIMENT: GATE SEQUENCE
# ============================================================

print("\n" + "=" * 65)
print("17. FINAL EXPERIMENT: QUANTUM GATE SEQUENCE")
print("=" * 65)

print("""
Let's create a complete quantum circuit using
multiple different gates.
""")

final_circuit = QuantumCircuit(2)

# Create superposition on qubit 0
final_circuit.h(0)

# Entangle with qubit 1
final_circuit.cx(0, 1)

# Apply phase operation
final_circuit.z(1)

# Apply another Hadamard
final_circuit.h(0)

print("\nFinal quantum circuit:")
print(final_circuit.draw())

final_state = Statevector.from_instruction(final_circuit)

print("\nFinal statevector:")
print(final_state)

print("\nFinal probabilities:")
print(final_state.probabilities_dict())


# ============================================================
# 18. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 65)
print("MODULE 02 COMPLETE")
print("=" * 65)

print("""
You have studied:

✓ Pauli X gate
✓ Pauli Y gate
✓ Pauli Z gate
✓ Hadamard gate
✓ S gate
✓ T gate
✓ RX gate
✓ RY gate
✓ RZ gate
✓ CNOT / CX gate
✓ CZ gate
✓ SWAP gate
✓ Gate combinations
✓ Self-inverse gates
✓ Statevectors
✓ Bloch sphere representation
✓ Multi-qubit gate operations

Important idea:

Quantum gates are mathematical operations that transform
quantum states while preserving the total probability.

Learning flow:

Quantum State
      ↓
Quantum Gate
      ↓
State Transformation
      ↓
Statevector
      ↓
Measurement / Visualization
      ↓
Observation
""")

print("=" * 65)
print("End of Module 02: Quantum Gates")
print("=" * 65)