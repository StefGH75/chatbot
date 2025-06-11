# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(0,10,51)
# plt.plot(x,np.sin(x), "b", x, np.cos(x), "r")
# plt.legend(["sin(x)","cos(x)"])
# plt.title("Sinus und Cosinus")
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.show()

#Histogramm:
# from numpy.random import randint
# import matplotlib.pyplot as plt
# wuerfe = randint(1, 7, 100) + randint(1, 7, 100)
# bins = range(2, 14)
# plt.hist(wuerfe, bins, facecolor="b")
# plt.grid()
# plt.show()

#Heatmap:
import matplotlib.pyplot as plt
a = [[0, 1, 1, 0],
     [1, 2, 7, 2],
     [3, 10, 9, 3],
     [2, 4, 5, 11]]
plt.imshow(a, cmap="hot")
plt.show()