from typing import List
from Models.world_parametrs import WorldParameters as WP


class PositionedPit:
    depth: float          # pit depth
    length: float         # pit length
    x: float              # pit position

    def __init__(self, depth, x, length):
        self.depth = depth
        self.x = x
        self.length = length


class Potential:
    pits: List[PositionedPit]

    def __init__(self, pits: List[PositionedPit]):
        self.pits = self.verify_data(pits)

    @staticmethod
    def verify_data(pits: List[PositionedPit]) -> List[PositionedPit]:
        if len(pits) == 0:
            return pits

        pits = sorted(pits, key=lambda pit: pit.x)

        if abs(pits[0].x) > WP.dx * (WP.nx / 2 - 1):
            raise Exception('Pit is positioned out of world')

        for i in range(1, len(pits)):
            if abs(pits[i].x) > WP.dx * (WP.nx / 2 - 1):
                raise Exception('Pit is positioned out of world')

            if pits[i].x - pits[i].length/2 < pits[i-1].x + pits[i-1].length/2:
                raise Exception('Pits are positioned too close to each other')

        return pits

    def get_potential(self, x: float) -> float:
        if abs(x) > WP.dx * (WP.nx/2 - 1):
            return 1e15

        for i, pit in enumerate(self.pits):
            if abs(x - pit.x) < pit.length/2:
                return -pit.depth

        return 0
