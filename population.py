class Population:
    def __init__(self, cfg):
        self.cfg = cfg
        self.s = cfg['n0']
        self.r = 0
        self.p = 0

    def update(self, drug, immune, muP):
        s, r, p = self.s, self.r, self.p
        dt = self.cfg['dt']
        sw = self.cfg['kSwitch'] * s * dt
        mut = self.cfg['mu'] * s * dt
        mutP = muP * self.p * self.cfg['dt']
        s -= sw + mut
        p += sw
        r += mut + mutP
        sg = s * self.cfg['g'] * dt
        rg = r * self.cfg['g'] * dt
        sd = s * (self.cfg['d'] + drug + immune) * dt
        rd = r * (self.cfg['d'] + immune) * dt
        pg = p * self.cfg['gP'] * dt
        pd = p * (self.cfg['dP'] + drug / 10 + immune) * dt
        self.s = max(s + sg - sd, 0)
        self.r = max(r + rg - rd, 0)
        self.p = max(p + pg - pd, 0)

    def total(self):
        return self.s + self.r + self.p

    def isResistant(self):
        return self.r > self.cfg['rThresh']
