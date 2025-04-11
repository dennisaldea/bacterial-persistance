import matplotlib.pyplot as plt

def plotFigB(allResults):
    """
    Plot population dynamics from multiple simulation results.

    Parameters
    ----------
    allResults : list of pandas.DataFrame
        A list of DataFrames, each containing simulation data with columns 't', 's', 'r', 'p',
        and metadata: 'a', 'muG', 'muP'.
    """
    fig, axs = plt.subplots(3, 2, figsize=(10, 12), sharex=True, sharey=True)
    axs = axs.flatten()

    for i, df in enumerate(allResults):
        ax = axs[i]

        # Plot wild type population (s + p) and resistant population (r)
        ax.plot(df['t'], df['s'] + df['p'], label='Wild type', color='blue')
        ax.plot(df['t'], df['r'], label='Resistant', color='red')

        # Use log scale for y-axis
        ax.set_yscale('log')
        ax.set_xlim([0, 140])
        ax.set_ylim([1, 1e9])
        # Add parameter values
        inset = f"a = {df['a'].iloc[0]:.0e}\nμ₉ = {df['muG'].iloc[0]:.1e}\nμₚ = {df['muP'].iloc[0]:.1e}"
        ax.text(0.95, 0.95, inset, transform=ax.transAxes, fontsize=10,
                verticalalignment='top', horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        # Add legend to first subplot only
        if i == 0:
            ax.legend()

    fig.supxlabel('Time (h)', fontsize=12)
    fig.supylabel('Number of cells', fontsize=12)
    plt.tight_layout()
    # plt.show()
    fig.savefig('figB.png', dpi=300)