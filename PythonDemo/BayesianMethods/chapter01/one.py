
import numpy as np

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import theano.tensor as tt
import pymc3 as pm
import seaborn as sns



sns.set_context('notebook')
plt.style.use('seaborn-darkgrid')
print('Running on PyMC3 v{}'.format(pm.__version__))


with pm.Model() as model:
    mu = pm.Normal('mu', mu=0, sigma=1)
    obs = pm.Normal('obs', mu=mu, sigma=1, observed=np.random.randn(100))

print(model.basic_RVs)

print(model.free_RVs)

print(model.observed_RVs)

print(model.logp({'mu': 0}))