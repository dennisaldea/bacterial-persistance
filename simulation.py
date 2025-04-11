from config import config as cfg
from population import Population
from treatment import Treatment
from immune import Immune
from recorder import Recorder

def run(cfg, muPersisters=None):
    """
    Run a single simulation of population dynamics under treatment and immune response.

    Parameters
    ----------
    cfg : dict
        Dictionary containing simulation parameters, such as time step (`dt`), total time (`tMax`), 
        switching rate (`kSwitch`), mutation rate (`mu`), and resistance threshold (`rThresh`).
    muPersisters : float, optional
        Mutation rate for persister cells. If None, defaults to `cfg['mu']`.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the simulation results over time with columns for time ('t'), 
        susceptible ('s'), resistant ('r'), persisters ('p'), and the parameters used: 'a', 
        'muG', 'muP', and 'rThresh'.
    """
    t = 0
    pop = Population(cfg)
    drug = Treatment(cfg)
    imm = Immune(cfg)
    rec = Recorder()
    muP = muPersisters if muPersisters is not None else cfg['mu']
    while t < cfg['tMax']:
        d = drug.getDrug(t)
        ik = imm.getKill(pop.total())
        pop.update(d, ik, muP)
        rec.log(t, pop)
        if pop.isResistant():
            break
        t += cfg['dt']
        
    df = rec.toDf()
    
    df['a'] = cfg['kSwitch']
    df['muG'] = cfg['mu']
    df['muP'] = muP
    df['rThresh'] = cfg['rThresh']
    return df

if __name__ == '__main__':
    df = run(cfg)
    print(df.tail())
    df.to_csv('results.csv', index=False)