import numpy as np

class Treatment:
    def __init__(self, cfg):
        self.cfg = cfg

    def getDrug(self, t):
        times = np.arange(0, self.cfg['tMax'], self.cfg['doseInt'])
        if any(abs(t - ti) < self.cfg['dt'] / 2 for ti in times):
            return self.cfg['doseAmt']
        return 0
