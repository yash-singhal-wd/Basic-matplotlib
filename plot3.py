import matplotlib.pyplot as plt
import numpy as np

#data to plot
x = np.array([0, 1, 2, 3, 4])
y1 = x**2
y2 = x**1.5

plt.plot(x,y1,'ro--', linewidth=5)
plt.plot(x,y2,'gs-')
plt.xlabel("Numbers")
plt.ylabel("f(x)")
plt.title("y=f(x)")
plt.grid()
plt.legend()
plt.show()