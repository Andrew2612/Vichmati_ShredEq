class Eigenstates:
    def __init__(self, energies, array, extent, N):
        self.energies = energies
        self.array = array
        self.number = len(array)
        self.extent = extent
        self.N = N