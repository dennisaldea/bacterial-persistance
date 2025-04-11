class Population:
    """
    Represents a cell population consisting of susceptible, resistant, and persister cells.

    Attributes
    ----------
    cfg : dict
        Configuration dictionary containing simulation parameters.
    s : float
        Number of susceptible cells.
    r : float
        Number of resistant cells.
    p : float
        Number of persister cells.
    """
    def __init__(self, cfg):
        self.cfg = cfg
        self.s = cfg['n0']
        self.r = 0
        self.p = 0

    def update(self, drug, immune, muP):
        """
        Update the population dynamics for one time step.

        Parameters
        ----------
        drug : float
            Drug concentration affecting the population.
        immune : float
            Immune-mediated killing rate.
        muP : float
            Mutation rate for persister cells.
        """
        s, r, p = self.s, self.r, self.p
        dt = self.cfg['dt']

        # Calculate switching and mutation from susceptible to other types
        sw = self.cfg['kSwitch'] * s * dt
        mut = self.cfg['mu'] * s * dt
        mutP = muP * self.p * self.cfg['dt']

        # Apply switching and mutation
        s -= sw + mut
        p += sw
        r += mut + mutP

        # Growth contributions
        sg = s * self.cfg['g'] * dt
        rg = r * self.cfg['g'] * dt
        pg = p * self.cfg['gP'] * dt

        # Death contributions
        sd = s * (self.cfg['d'] + drug + immune) * dt
        rd = r * (self.cfg['d'] + immune) * dt
        pd = p * (self.cfg['dP'] + drug / 10 + immune) * dt
        
        # Update populations
        self.s = max(s + sg - sd, 0)
        self.r = max(r + rg - rd, 0)
        self.p = max(p + pg - pd, 0)

    def total(self):
        """
        Get total population size.

        Returns
        -------
        float
            Total number of cells (susceptible + resistant + persisters).
        """
        return self.s + self.r + self.p

    def isResistant(self):
        """
        Check if the resistant population exceeds the resistance threshold.

        Returns
        -------
        bool
            True if resistant population exceeds threshold, else False.
        """
        return self.r > self.cfg['rThresh']
