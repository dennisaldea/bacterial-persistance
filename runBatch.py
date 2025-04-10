from batchRunner import runGrid
from plotFigB import plotFigB

persistVals = [1e-4, 1e-3, 5e-3]
muCombos = [(1.5e-8, 1.5e-4), (3e-8, 6e-4)]

results = runGrid(persistVals, muCombos)
plotFigB(results)
