from Models.potential import PositionedPit
from Models.potential import Potential
from Models.world_parametrs import WorldParameters as WP


delta_pit = PositionedPit(depth=1, x=0, length=WP.Å)
potential = Potential(pits=[])

import numpy as np
from Models.hamiltonian import Hamiltonian
from Models.single_particle import SingleParticle
from Visualization.abstract_visualization import init_visualization


def choose_oscillator(omega):
    def oscillator(x):
        # k = 100 * WP.eV / WP.Å**2
        # omega=1
        return 0.5 * 1 * (omega ** 2) * x ** 2
    return oscillator


def choose_sech2(a,U0):
    def sech2(x):
        # a = 1
        # U0 = 14 / 2
        return -U0 / (np.cosh(x / a)) ** 2
    return sech2

print("Выберите тип потенциала: 1 - осциллятор, 2 - sech2")
inp = input()
print("Введите массу частицы в атомных единицах, ")
chosen_mass = float(input())
if inp=="1":
    print("Введите частоту осциллятора в атомных единицах")
    chosen_omega=float(input())
    chosen_potential = choose_oscillator(chosen_omega)
else:
    print("Введите характерное расстояние a в атомных единицах")
    choosen_a = float(input())
    print("Введите глубину потенциала U0 в атомных единицах")
    choosen_U0=float(input())
    chosen_potential=choose_sech2(choosen_a,choosen_U0)


H = Hamiltonian(particles=SingleParticle(),
                potential=chosen_potential,
                spatial_ndim=1, N=512, extent=20*WP.Å)

eigenstates = H.solve(max_states=30)

print(eigenstates.energies)

visualization = init_visualization(eigenstates,chosen_potential)
visualization.slider_plot()



