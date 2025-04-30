from Models.potential import PositionedPit
from Models.potential import Potential
from Models.world_parametrs import WorldParameters as WP

delta_pit = PositionedPit(depth=1, x=0, length=WP.Å)
potential = Potential(pits=[])


from Models.hamiltonian import Hamiltonian
from Models.single_particle import SingleParticle

def harmonic_oscillator(particle):
    k = 100 * WP.eV / WP.Å**2
    return 0.5 * k * particle.x**2


H = Hamiltonian(particles=SingleParticle(),
                potential=harmonic_oscillator,
                spatial_ndim=1, N=512, extent=20*WP.Å)

eigenstates = H.solve(max_states=30)

print(eigenstates.energies)



