from abc import ABC, abstractmethod
from Models.hamiltonian import Hamiltonian

class AbstractParticleSystem(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_observables(self, H: Hamiltonian):
        pass

    @abstractmethod
    def build_matrix_operators(self, H: Hamiltonian):
        pass

    @abstractmethod
    def get_kinetic_matrix(self, H: Hamiltonian):
        pass

    @abstractmethod
    def get_eigenstates(self, H: Hamiltonian, max_states, eigenvalues, eigenvectors):
        pass
