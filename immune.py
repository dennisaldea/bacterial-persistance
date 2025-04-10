class Immune:
    def __init__(self, cfg):
        self.cfg = cfg
        self.active = False

    def getKill(self, pop):
        if not self.active and pop > self.cfg['iThresh']:
            self.active = True
        return self.cfg['kImmune'] if self.active else 0
