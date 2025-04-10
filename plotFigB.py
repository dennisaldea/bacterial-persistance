import matplotlib.pyplot as plt
import numpy as np

def plotFigB(allResults):
    fig, axs = plt.subplots(3, 2, figsize=(10, 12), sharex=True, sharey=True)
    axs = axs.flatten()

    for i, df in enumerate(allResults):
        ax = axs[i]
        ax.plot(df['t'], df['s'] + df['p'], label='Wild type', color='blue')
        ax.plot(df['t'], df['r'], label='Resistant', color='red')
        ax.set_yscale('log')
        ax.set_xlim([0, 140])
        ax.set_ylim([1, 1e9])
        inset = f"a = {df['a'].iloc[0]:.0e}\nμ₉ = {df['muG'].iloc[0]:.1e}\nμₚ = {df['muP'].iloc[0]:.1e}"
        ax.text(0.95, 0.95, inset, transform=ax.transAxes, fontsize=10,
                verticalalignment='top', horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        if i == 0:
            ax.legend()

    fig.supxlabel('Time (h)', fontsize=12)
    fig.supylabel('Number of cells', fontsize=12)
    plt.tight_layout()
    plt.show()
    fig.savefig('figB.png', dpi=300)