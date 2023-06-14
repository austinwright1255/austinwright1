import numpy as np

def apply_hadamard_gate(qubit):
    hadamard_matrix = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    return np.dot(hadamard_matrix, qubit)

def apply_pauli_x_gate(qubit):
    pauli_x_matrix = np.array([[0, 1], [1, 0]])
    return np.dot(pauli_x_matrix, qubit)

def measure_qubit(qubit):
    probabilities = np.abs(qubit) ** 2
    outcome = np.random.choice([0, 1], p=probabilities)
    measured_state = np.zeros_like(qubit)
    measured_state[outcome] = 1.0
    return measured_state

def main():
    # Initialize a qubit in the |0⟩ state
    qubit = np.array([1, 0])

    print("Initial qubit state:", qubit)

    # Apply the Hadamard gate
    qubit = apply_hadamard_gate(qubit)
    print("After applying the Hadamard gate:", qubit)

    # Apply the Pauli-X gate
    qubit = apply_pauli_x_gate(qubit)
    print("After applying the Pauli-X gate:", qubit)

    # Measure the qubit
    measured_qubit = measure_qubit(qubit)
    print("Measured qubit state:", measured_qubit)

if __name__ == "__main__":
    main()
