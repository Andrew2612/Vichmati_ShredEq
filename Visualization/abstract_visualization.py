from abc import abstractmethod
from typing import Union, Dict, List
from Models.eigenstates import Eigenstates


class Visualization:
    @abstractmethod
    def __init__(self, eigenstates):
        pass

    @abstractmethod
    def slider_plot(self):
        pass



