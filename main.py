from Models.world_parametrs import WorldParameters as WP
from Models.hamiltonian import Hamiltonian
from Systems.single_particle import SingleParticle
from Visualization.single_particle_visualization import VisualizationSingleParticle1D
from Systems.potential import Potential

potential = Potential.choose_potential()

H = Hamiltonian(particles=SingleParticle(),
                potential=potential,
                N=512, extent=20*WP.Å)

eigenstates = H.solve(max_states=30)

print(eigenstates.energies)

visualization = VisualizationSingleParticle1D(eigenstates, potential)
visualization.slider_plot()



