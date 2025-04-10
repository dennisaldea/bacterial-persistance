from simulation import run
from config import config as baseCfg
import pandas as pd
import numpy as np

def runGrid(persistVals, muVals):
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
