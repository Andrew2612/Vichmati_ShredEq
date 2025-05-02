from Models.world_parametrs import WorldParameters as WP
from Models.hamiltonian import Hamiltonian
from Systems.single_particle import SingleParticle
from Visualization.single_particle_visualization import VisualizationSingleParticle1D
from Systems.potential import Potential


def main():
    particles = SingleParticle()
    potential, theoretical_energies = Potential().choose_potential(particles.m)

    H = Hamiltonian(particles=particles,
                    potential=potential,
                    N=512, extent=20*WP.Å)

    eigenstates = H.solve(max_states=30)

    print(eigenstates.energies)

    if len(eigenstates.energies) == 0:
        print("No states found")
        return

    print("Теоретические значения")
    for i, x in enumerate(theoretical_energies(n=len(eigenstates.energies)), 1):
        print(f"{x:10}", end="\n" if i % 6 == 0 else " ")

    visualization = VisualizationSingleParticle1D(eigenstates, potential)
    visualization.slider_plot()


if __name__ == "__main__":
    main()
