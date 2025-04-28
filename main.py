from Solvers.ShredEqSolver import ShredEqSolver
from Models.potential import PositionedPit
from Models.potential import Potential
from Models.world_parametrs import WorldParameters

delta_pit = PositionedPit(depth=1, x=0, length=WorldParameters.dx)
potential = Potential(pits=[delta_pit])

solver = ShredEqSolver()
solver.solve(potential)


