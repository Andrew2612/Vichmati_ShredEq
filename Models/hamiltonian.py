import numpy as np
from scipy.sparse import diags
import time
from scipy.sparse.linalg import eigsh


class Hamiltonian:
    def __init__(self, particles, potential, N, extent, E_min=0):

        self.N = N
        self.extent = extent
        self.dx = extent / N
        self.particle_system = particles
        self.particle_system.H = self

        self.T = self.particle_system.get_kinetic_matrix(self)

        self.potential = potential
        self.E_min = E_min

        # self.particle_system.get_observables(self)
        self.particle_system.build_matrix_operators(self)
        self.V = self.get_potential_matrix()

    def get_potential_matrix(self):
        if self.potential == None:
            self.E_min = 0.
            V = 0.
            return V
        else:
            V = self.potential(self.particle_system.x)
            self.Vgrid = V
            self.E_min = np.amin(V)
            V = V.reshape(self.N)
            V = diags([V], [0])
            return V


    def solve(self, max_states: int):
        """
        Diagonalize the hamiltonian and retrieve eigenstates
        """

        H = self.T + self.V

        t0 = time.time()

        eigenvalues, eigenvectors = eigsh(H, k=max_states, which='LM', sigma=min(0, self.E_min))

        self.eigenstates = self.particle_system.get_eigenstates(self, max_states, eigenvalues, eigenvectors)

        print("Took", time.time() - t0)
        return self.eigenstates