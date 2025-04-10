from config import config as cfg
from population import Population
from treatment import Treatment
from immune import Immune
from recorder import Recorder

def run(cfg, muPersisters=None):
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
    return rec.toDf()

if __name__ == '__main__':
    df = run(cfg, muPersisters=muP)
    print(df.tail())
    df.to_csv('results.csv', index=False)