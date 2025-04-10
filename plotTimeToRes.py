def plotTimeToResistance(results):
    import seaborn as sns
    import pandas as pd

    rows = []
    for df in results:
        tResist = df[df['r'] > df['rThresh'].iloc[0]]['t'].min()
        if pd.isna(tResist): tResist = df['t'].max()
        rows.append({'a': df['a'].iloc[0], 'muG': df['muG'].iloc[0], 'muP': df['muP'].iloc[0], 'timeToResist': tResist})

    dfHeat = pd.DataFrame(rows)
    pivot = dfHeat.pivot('a', 'muG', 'timeToResist')
    sns.heatmap(pivot, annot=True, fmt='.1f', cmap='viridis')
    plt.title('Time to Resistance')
    plt.xlabel('Mutation rate (growing)')
    plt.ylabel('Persistence switching rate (a)')
    plt.show()
