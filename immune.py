class Immune:
    """
    Represents the immune system's effect on the population.

    Attributes
    ----------
    cfg : dict
        Configuration dictionary containing simulation parameters, including immune response strength.
    """
    def __init__(self, cfg):
        self.cfg = cfg
        self.active = False

    def getKill(self, pop):
        """
        Compute the immune-mediated killing rate based on the total population size.

        Parameters
        ----------
        pop : float
            Current total number of cells in the population.

        Returns
        -------
        float
            Immune killing rate as provided in the config dict when immune is active, else 0.
        """
        if not self.active and pop > self.cfg['iThresh']:
            self.active = True
        return self.cfg['kImmune'] if self.active else 0
