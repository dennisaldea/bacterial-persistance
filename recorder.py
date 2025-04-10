class Recorder:
    def __init__(self):
        self.t = []
        self.s = []
        self.r = []
        self.p = []

    def log(self, t, pop):
        self.t.append(t)
        self.s.append(pop.s)
        self.r.append(pop.r)
        self.p.append(pop.p)

    def toDf(self):
        import pandas as pd
        return pd.DataFrame({
            't': self.t,
            's': self.s,
            'r': self.r,
            'p': self.p
        })
