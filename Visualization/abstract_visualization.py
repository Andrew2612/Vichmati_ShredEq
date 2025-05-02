from abc import abstractmethod


class Visualization:
    @abstractmethod
    def __init__(self, eigenstates):
        pass

    @abstractmethod
    def slider_plot(self):
        pass



