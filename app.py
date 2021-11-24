import numpy as np
import matplotlib.pyplt as plt
from ypstruct import structure
import random
import ga

def sphere(x):
    return -(sum(x**.5))
    
# problem definetion
problem = structure()
problem.costfunc = sphere
problem.nvar = 3
problem.varmin = 0
problem.varmax = random.randint(1,30)


# ga parameters
params = structure()
params.maxit = 100
params.npop = 30
params.pc = 1
params.gamma = 0.1
params.mu = 0.2
params.sigma = 0.1

# run ga
out = ga.run(problem,params)

# results















