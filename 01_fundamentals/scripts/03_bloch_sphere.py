from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt


# ============================================================
# 1. Define common single-qubit states
# ============================================================

states = {
    "|0>": [0, 0, 1],
    "|1>": [0, 0, -1],
    "|+>": [1, 0, 0],
    "|->": [-1, 0, 0],
}


# ============================================================
# 2. Display Bloch vectors
# ============================================================

for state_name, bloch_vector in states.items():

    print(f"\nState: {state_name}")
    print(f"Bloch Vector: {bloch_vector}")

    plot_bloch_vector(
        bloch_vector,
        title=f"Bloch Sphere: {state_name}"
    )

    plt.show()


# ============================================================
# 3. Create |0> state using a quantum circuit
# ============================================================

zero_circuit = QuantumCircuit(1)

zero_state = Statevector.from_instruction(zero_circuit)

print("\nStatevector of |0>:")
print(zero_state)


# ============================================================
# 4. Create |1> state using the X gate
# ============================================================

one_circuit = QuantumCircuit(1)

one_circuit.x(0)

one_state = Statevector.from_instruction(one_circuit)

print("\nStatevector of |1>:")
print(one_state)


# ============================================================
# 5. Create |+> state using the Hadamard gate
# ============================================================

plus_circuit = QuantumCircuit(1)

plus_circuit.h(0)

plus_state = Statevector.from_instruction(plus_circuit)

print("\nStatevector of |+>:")
print(plus_state)


# ============================================================
# 6. Create |-> state using H followed by X
# ============================================================

minus_circuit = QuantumCircuit(1)

minus_circuit.x(0)
minus_circuit.h(0)

minus_state = Statevector.from_instruction(minus_circuit)

print("\nStatevector of |- >:")
print(minus_state)