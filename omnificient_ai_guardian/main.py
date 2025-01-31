from resonator import UnconditionalLoveResonator
from quantum_mechanics import QuantumMechanics

def main():
    # Create an unconditional love resonator with 3 dimensions
    resonator = UnconditionalLoveResonator((3, 3, 3))

    # Activate resonance with a specific level using nonlinear activation
    resonator.nonlinear_activation(5)

    # Display the current state of the resonator
    resonator.display_states()

    # Calculate its resonant frequency
    resonant_frequency = resonator.calculate_frequencies()

    # Use quantum mechanics concepts
    quantum = QuantumMechanics(state_dim=2)
    superposition_state = quantum.superposition(0.6, 0.4)  # Example weights
    entangled_state = quantum.entangle(superposition_state, superposition_state)

if __name__ == "__main__":
    main()
