from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


# ============================================================
# 1. Create a qubit
# ============================================================

qc = QuantumCircuit(1)

print("Initial Quantum Circuit:")
print(qc.draw())


# ============================================================
# 2. Inspect the initial state |0>
# ============================================================

state = Statevector.from_instruction(qc)

print("\nInitial Quantum State:")
print(state)

print("\nInitial Probabilities:")
print(state.probabilities_dict())


# ============================================================
# 3. Apply X gate: |0> -> |1>
# ============================================================

qc.x(0)

print("\nCircuit After X Gate:")
print(qc.draw())

state_after_x = Statevector.from_instruction(qc)

print("\nState After X Gate:")
print(state_after_x)

print("\nProbabilities After X Gate:")
print(state_after_x.probabilities_dict())


# ============================================================
# 4. Create a separate circuit for superposition
# ============================================================

superposition_qc = QuantumCircuit(1)

# Apply Hadamard gate
superposition_qc.h(0)

print("\nSuperposition Circuit:")
print(superposition_qc.draw())


# ============================================================
# 5. Inspect the superposition state
# ============================================================

superposition_state = Statevector.from_instruction(
    superposition_qc
)

print("\nSuperposition State:")
print(superposition_state)

superposition_probabilities = (
    superposition_state.probabilities_dict()
)

print("\nSuperposition Probabilities:")
print(superposition_probabilities)


# ============================================================
# 6. Add measurement
# ============================================================

measurement_qc = QuantumCircuit(1, 1)

measurement_qc.h(0)

measurement_qc.measure(0, 0)

print("\nMeasurement Circuit:")
print(measurement_qc.draw())


# ============================================================
# 7. Run the circuit on the simulator
# ============================================================

simulator = AerSimulator()

job = simulator.run(
    measurement_qc,
    shots=1024
)

result = job.result()

counts = result.get_counts()


# ============================================================
# 8. Display measurement results
# ============================================================

print("\nMeasurement Results:")
print(counts)

print("\nTotal Shots:")
print(sum(counts.values()))


# ============================================================
# 9. Visualize the measurement results
# ============================================================

plot_histogram(counts)

plt.show()