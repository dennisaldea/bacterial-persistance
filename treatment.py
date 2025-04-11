import numpy as np

class Treatment:
    """
    Represents the drug treatment schedule and dosage.

    Attributes
    ----------
    cfg : dict
        Configuration dictionary with treatment parameters including dosage interval (`doseInt`), 
        amount (`doseAmt`), and total simulation time (`tMax`).
    """
    def __init__(self, cfg):
        self.cfg = cfg

    def getDrug(self, t):
        """
        Determine the drug concentration at a given time point.

        Parameters
        ----------
        t : float
            Current time in the simulation.

        Returns
        -------
        float
            Drug concentration (dose amount) if time is at a dosage point, else 0.
        """
        times = np.arange(0, self.cfg['tMax'], self.cfg['doseInt'])
        if any(abs(t - ti) < self.cfg['dt'] / 2 for ti in times):
            return self.cfg['doseAmt']
        return 0
