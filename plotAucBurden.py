def plotAucBurden(results):
    from scipy.integrate import simps

    rows = []
    for df in results:
        auc = simps(df['s'] + df['r'] + df['p'], df['t'])
        rows.append({'a': df['a'].iloc[0], 'muG': df['muG'].iloc[0], 'muP': df['muP'].iloc[0], 'auc': auc})

    dfAuc = pd.DataFrame(rows)
    sns.heatmap(dfAuc.pivot('a', 'muG', 'auc'), annot=True, fmt='.1e', cmap='magma')
    plt.title('Total Bacterial Burden (AUC)')
    plt.xlabel('Mutation rate (growing)')
    plt.ylabel('Persistence switching rate (a)')
    plt.show()
