# Qiskit Quantum Learning ⚛️

A structured, hands-on journey through quantum computing using **Qiskit 2.x** and **Qiskit Aer**.

Each topic follows the workflow: **Understand → Implement → Experiment → Observe → Analyze**

Every module contains matching `.py` scripts and `.ipynb` notebooks — scripts for clean execution, notebooks for rich theory with LaTeX math and inline visualizations.

---

## 🛠️ Tech Stack

| Tool | Version |
|---|---|
| Python | 3.11 |
| Qiskit | 2.x |
| Qiskit Aer | 0.17+ |
| NumPy | 1.24+ |
| Matplotlib | 3.7+ |
| Jupyter Notebook | 7.0+ |

---

## 📁 Repository Structure

```text
qiskit-quantum-learning/
│
├── 01_fundamentals/
│   ├── notebooks/
│   │   ├── 01_first_quantum_circuit.ipynb
│   │   ├── 02_qubit_and_quantum_states.ipynb
│   │   └── 03_bloch_sphere.ipynb
│   └── scripts/
│       ├── 01_first_quantum_circuit.py
│       ├── 02_qubit_and_quantum_states.py
│       └── 03_bloch_sphere.py
│
├── 02_quantum_gates/
│   ├── notebooks/
│   │   └── 01_quantum_gates.ipynb
│   └── scripts/
│       └── 01_quantum_gates.py
│
├── 03_multi_qubit/
│   ├── notebooks/
│   │   └── 01_multi_qubit_systems.ipynb
│   └── scripts/
│       └── 01_multi_qubit_systems.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📚 Learning Path & Progress

### ✅ 01 — Quantum Fundamentals

Core building blocks of quantum computation.

| # | Topic | Script | Notebook |
|---|---|---|---|
| 01 | First Quantum Circuit — H gate, AerSimulator, measurement | `01_first_quantum_circuit.py` | `01_first_quantum_circuit.ipynb` |
| 02 | Qubit & Quantum States — computational basis, superposition, statevectors | `02_qubit_and_quantum_states.py` | `02_qubit_and_quantum_states.ipynb` |
| 03 | Bloch Sphere — geometric visualization of single-qubit states | `03_bloch_sphere.py` | `03_bloch_sphere.ipynb` |

---

### ✅ 02 — Quantum Gates

Single-qubit and two-qubit gate operations with matrix representations and Bloch sphere visualization.

| # | Topic | Script | Notebook |
|---|---|---|---|
| 01 | Quantum Gates — Pauli X/Y/Z, H, S, T, Rotations RX/RY/RZ, CX, CZ, SWAP | `01_quantum_gates.py` | `01_quantum_gates.ipynb` |

---

### ✅ 03 — Multi-Qubit Systems

Tensor products, entanglement, Bell states, and density matrices.

| # | Topic | Script | Notebook |
|---|---|---|---|
| 01 | Multi-Qubit Systems — CNOT, Bell states, GHZ, entanglement, DensityMatrix, partial trace | `01_multi_qubit_systems.py` | `01_multi_qubit_systems.ipynb` |

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Dipesh-433/qiskit-quantum-learning.git
cd qiskit-quantum-learning
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running Scripts

```powershell
python 01_fundamentals/scripts/01_first_quantum_circuit.py
python 03_multi_qubit/scripts/01_multi_qubit_systems.py
```

## 📓 Running Notebooks

```powershell
jupyter notebook
```

Then open any `.ipynb` from the corresponding `notebooks/` directory.

---

## 🧠 What Makes This Different

- **Modular & reusable code**: Each algorithm is broken into clean, documented Python functions — not a single monolithic script.
- **Step-by-step statevector analysis**: Each algorithm tracks the quantum state evolution at every stage (before oracle, after diffuser, after QFT), not just the final histogram.
- **Qiskit 2.x idioms**: Uses modern `QFTGate`, `qc.if_test()` dynamic feed-forward, `Statevector`, and `plot_distribution` APIs throughout.
- **Deep theory in notebooks**: Notebooks include LaTeX math derivations, truth tables, quantum resource exchange comparisons, and interference proofs — not just code.
- **Verified outputs**: All notebooks are pre-executed via `nbconvert` so circuit diagrams, histograms, and plots are visible without re-running.

---

## 👨‍💻 Author

**Dipesh Arjun Shinde**
Integrated Computer Science & Engineering
Dr. Babasaheb Ambedkar Technological University, Lonere

Interests:
- Quantum Computing
- Quantum Machine Learning
- Quantum Algorithms
- Quantum Optimization
- Artificial Intelligence

---

⭐ If you find this repository useful, consider giving it a star.
