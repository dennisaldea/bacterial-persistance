from simulation import run
from config import config as baseCfg


def runGrid(persistVals, muVals):
    """
    Run simulations over a grid of persistence switching rates and mutation rate combinations.

    Parameters
    ----------
    persistVals : list of float
        List of persistence switching rates (kSwitch) to evaluate.
    muVals : list of tuple of float
        List of tuples (muG, muP) representing mutation rates for growing and persister cells, respectively.

    Returns
    -------
    list of pandas.DataFrame
        A list of DataFrames containing simulation results for each parameter combination. Each DataFrame
        includes columns for time ('t'), susceptible ('s'), resistant ('r'), persisters ('p'), and the
        parameters used: 'a', 'muG', 'muP'.
    """
    results = []
    for a in persistVals:
        for muG, muP in muVals:
            cfg = baseCfg.copy()
            cfg['kSwitch'] = a
            cfg['muG'] = muG
            cfg['muP'] = muP
            cfg['mu'] = muG
            df = run(cfg, muPersisters=muP)
            df['a'] = a
            df['muG'] = muG
            df['muP'] = muP
            results.append(df)
    return results
