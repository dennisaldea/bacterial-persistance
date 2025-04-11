import pandas as pd

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
        """
        Convert the recorded data to a pandas DataFrame.

        Returns
        -------
        pandas.DataFrame
            DataFrame containing columns 't', 's', 'r', and 'p' for time, susceptible, resistant,
            and persister cells respectively.
        """
        return pd.DataFrame({
            't': self.t,
            's': self.s,
            'r': self.r,
            'p': self.p
        })
