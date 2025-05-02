import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from Visualization.abstract_visualization import Visualization
from Models.world_parametrs import WorldParameters as WP


class VisualizationSingleParticle1D(Visualization):
    def __init__(self, eigenstates, potential):
        self.eigenstates = eigenstates
        self.potential = potential

    def slider_plot(self, xlim=None):
        plt.style.use("dark_background")

        eigenstates_array = self.eigenstates.array
        energies = self.eigenstates.energies

        fig = plt.figure(figsize=(16 / 9 * 5.804 * 0.9, 5.804))

        grid = plt.GridSpec(2, 2, width_ratios=[5, 1], height_ratios=[1, 1], hspace=0.1, wspace=0.2)
        ax1 = fig.add_subplot(grid[0:2, 0:1])
        ax2 = fig.add_subplot(grid[0:2, 1:2])

        ax1.set_xlabel("x [Å]")

        ax2.set_title('Energy Level')
        ax2.set_facecolor('black')

        ax2.set_ylabel('$E_N$ [eV]')
        ax2.set_xticks(ticks=[])
        if xlim != None:
            ax1.set_xlim(np.array(xlim) / WP.Å)

        ymax = np.amax(eigenstates_array)
        ymin = np.amin(eigenstates_array)
        ax1.set_ylim([ymin * 1.2, ymax * 1.2])

        for E in energies:
            ax2.plot([0, 1], [E, E], color='gray', alpha=0.5)

        x = np.linspace(-self.eigenstates.extent / 2, self.eigenstates.extent / 2, self.eigenstates.N)

        eigenstate_plot = ax1.plot(x / WP.Å, np.real(eigenstates_array[0]))
        ax1.plot(x/WP.Å,self.potential(x)*max(abs(ymin),abs(ymax))/np.amax(np.abs(self.potential(x))))

        line = ax2.plot([0, 1], [energies[1], energies[1]], color='yellow', lw=3)

        plt.subplots_adjust(bottom=0.2)
        from matplotlib.widgets import Slider
        slider_ax = plt.axes([0.2, 0.05, 0.7, 0.05])
        slider = Slider(slider_ax,  # the axes object containing the slider
                        'state',  # the name of the slider parameter
                        0,  # minimal value of the parameter
                        len(eigenstates_array) - 1,  # maximal value of the parameter
                        valinit=0,  # initial value of the parameter
                        valstep=1,
                        color='#5c05ff'
                        )

        def update(state):
            state = int(state)
            eigenstate_plot[0].set_ydata(np.real(eigenstates_array[state]))

            line[0].set_ydata([energies[state], energies[state]])

        slider.on_changed(update)
        plt.show()
