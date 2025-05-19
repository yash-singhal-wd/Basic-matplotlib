import matplotlib.pyplot as plt
import numpy as np

#data to plot
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

plt.plot(x,y)
plt.xlabel('x something')
plt.ylabel('y something')
plt.title("Some plot")
plt.grid()
plt.show()