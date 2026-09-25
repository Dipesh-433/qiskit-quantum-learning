from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


# ============================================================
# 1. Create a quantum circuit
# ============================================================

qc = QuantumCircuit(1, 1)

# Apply Hadamard gate
qc.h(0)

# Display circuit before measurement
print("Quantum Circuit:")
print(qc.draw())


# ============================================================
# 2. Calculate the statevector
# ============================================================

state = Statevector.from_instruction(qc)

print("\nQuantum State:")
print(state)

print("\nTheoretical Probabilities:")
print(state.probabilities_dict())


# ============================================================
# 3. Add measurement
# ============================================================

qc.measure(0, 0)


# ============================================================
# 4. Run the quantum simulator
# ============================================================

simulator = AerSimulator()

job = simulator.run(qc, shots=1024)

result = job.result()

counts = result.get_counts()


# ============================================================
# 5. Display measurement results
# ============================================================

print("\nMeasurement Results:")
print(counts)

print("\nTotal Shots:")
print(sum(counts.values()))


# ============================================================
# 6. Visualize measurement results
# ============================================================

plot_histogram(counts)
plt.show()