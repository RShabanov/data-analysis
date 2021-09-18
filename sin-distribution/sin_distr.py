import matplotlib.pyplot as plt
import numpy as np


SIZE = 1000

x = np.linspace(-np.pi, np.pi, SIZE)
hist = plt.hist(np.sin(x), density=True, histtype='step', label='Sin(x) distribution', bins=100)
plt.show()