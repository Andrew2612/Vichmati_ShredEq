import scipy.special

from Models.world_parametrs import WorldParameters as WP
from Models.hamiltonian import Hamiltonian
from Systems.single_particle import SingleParticle
from Visualization.single_particle_visualization import VisualizationSingleParticle1D
from Systems.potential import Potential
import numpy as np


def main():
    potentialClass=Potential()
    potential=potentialClass.choose_potential()

    H = Hamiltonian(particles=SingleParticle(),
                    potential=potential,
                    N=512, extent=20*WP.Å)

    eigenstates = H.solve(max_states=30)

    print(eigenstates.energies)

    if len(eigenstates.energies) == 0:
        print("No states found")
        return
    m = H.particle_system.m
    print("Теоретические значения")
    theoretical_energies = []
    if potentialClass.potential_type=="oscillator":
        theoretical_energies=[0.5*potentialClass.omega*i for i in range(1,len(eigenstates.energies))]
    if potentialClass.potential_type=="sech2":
        U0 = potentialClass.U0
        a = potentialClass.a
        s=0.5*(-1+np.sqrt(1+8*m*U0*a**2))
        theoretical_energies=[float(-(2*m*a**2)**(-1) * (s-i)**2) for i in range(0,int(s-(1e-5))+1)]
    if potentialClass.potential_type=="linear":
        F=potentialClass.F
        nAiprimezeros=int(-0.1+len(eigenstates.energies)/2)+1
        nAizeros=len(eigenstates.energies)-nAiprimezeros
        Aizeros,Aiprimezeros=scipy.special.ai_zeros(nAiprimezeros)[:2]
        for i in range(nAizeros):
            theoretical_energies.append(float((F**2/(2*m))**(1/3)*abs(Aiprimezeros[i])))
            theoretical_energies.append(float((F**2/(2*m))**(1/3)*abs(Aizeros[i])))
        if nAiprimezeros>nAizeros:
            theoretical_energies.append(float((F**2/(2*m))**(1/3)*abs(Aiprimezeros[-1])))
    for i, x in enumerate(theoretical_energies, 1):
        print(f"{x:10}", end="\n" if i % 6 == 0 else " ")
    visualization = VisualizationSingleParticle1D(eigenstates, potential)
    visualization.slider_plot()


if __name__ == "__main__":
    main()
