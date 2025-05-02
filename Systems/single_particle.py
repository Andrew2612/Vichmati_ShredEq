import numpy as np
from scipy.sparse import diags
from scipy.sparse import eye
from Models.abstract_particle_system import AbstractParticleSystem
from Models.world_parametrs import WorldParameters as WP
from Models.eigenstates import Eigenstates


def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


class SingleParticle(AbstractParticleSystem):
    def __init__(self, m=WP.m_e, spin=None):
        self.m = m
        self.spin = spin

    def get_observables(self, H):
        self.x = np.linspace(-H.extent / 2, H.extent / 2, H.N)


    def build_matrix_operators(self, H):
        self.x = np.linspace(-H.extent / 2, H.extent / 2, H.N)
        diff_x = diags([-1., 0., 1.], [-1, 0, 1], shape=(H.N, H.N)) * 1 / (2 * H.dx)
        self.px = - WP.hbar * 1j * diff_x

        self.I = eye(H.N)

    def get_kinetic_matrix(self, H):
        T = diags([-2., 1., 1.], [0, -1, 1], shape=(H.N, H.N)) * -WP.k / (self.m * H.dx ** 2)
        return T

    def get_eigenstates(self, H, max_states, eigenvalues, eigenvectors):
        energies = eigenvalues
        eigenstates_array = np.moveaxis(eigenvectors.reshape(*[H.N], max_states), -1, 0)

        eigenstates_array = eigenstates_array / np.sqrt(H.dx)
        # проверка что энергии лежат ниже пределов потенциала на бесконечности
        F = min(abs(derivative(H.potential,H.extent/2)),abs(derivative(H.potential, -H.extent/2)))
        if F < 1e-5:
            Emax = max(H.potential(H.extent/2),H.potential(-H.extent/2))
            mask = energies <= Emax
            energies = energies[mask]
            eigenstates_array = eigenstates_array[mask]

        eigenstates = Eigenstates(energies / WP.eV, eigenstates_array, H.extent, H.N)
        return eigenstates
