import matplotlib.pyplot as plt
import matplotlib.lines as ln
import numpy as np


x = np.linspace(-50,50,100)
y = 2*x+1


plt.plot(x, y)


plt.grid()
plt.show()
