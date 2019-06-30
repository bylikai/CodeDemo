
import numpy as np
import theano.tensor as tt

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import  pymc3 as pm
import seaborn as sns


sns.set_context('notebook')
plt.style.use('seaborn-darkgrid')

lambda_ = pm.Exponential("poisson_param", 1)
data_generator = pm.Poisson("data_generator", lambda_)

data_plus_one = data_generator+1

print(lambda_.value)
print(data_generator.value)
print(data_plus_one.value)


