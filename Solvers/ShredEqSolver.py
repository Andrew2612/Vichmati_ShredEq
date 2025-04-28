import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.linalg import eigsh
from Models.world_parametrs import WorldParameters as WP

from Models.potential import Potential

class ShredEqSolver:
    @staticmethod
    def solve(potential: Potential):

        # hbar^2/(2m*dx^2) * (psi[i+1]) + hbar^2/2m * (1/dx^2 + V[i])psi[i]
        #               - hbar^2/(2m*dx^2) * (psi[i-1]) = E*psi[i]

        a = -WP.h**2 / (2 * WP.m * WP.dx**2)

        H = np.zeros((WP.nx, WP.nx))

        for i in range(1, WP.nx - 1):
            H[i, i-1] = H[i, i+1] = a
            H[i, i] = 2 * a * potential.get_potential(WP.dx * (i - WP.nx/2))

        H[0, 0] = 2 * a * potential.get_potential(WP.dx * (-WP.nx/2))
        H[-1, -1] = 2 * a * potential.get_potential(WP.dx * WP.nx/2)
        H[0, 1] = H[1, 0] = H[-1, -2] = H[-2, -1] = a

        energies, wavefunctions = eigsh(H, k=3, which='LM', sigma=min(0, 0))

        plt.figure(figsize=(10, 6))
        x = np.linspace(-WP.dx*WP.nx/2, WP.dx*WP.nx/2, WP.nx)
        for i in range(3):  # Plot first 3 wavefunctions
            plt.plot(x, wavefunctions[:, i] + energies[i], label=f'E = {energies[i]:.2f}')
        plt.title('Wavefunctions')
        plt.xlabel('Position (x)')
        plt.ylabel('Wavefunction (ψ)')
        plt.axhline(0, color='black', lw=0.5, ls='--')
        plt.legend()
        plt.grid()
        plt.show()

        return 0


