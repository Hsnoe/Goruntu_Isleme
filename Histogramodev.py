import cv2
import numpy as np
from matplotlib import pyplot as plt


fotograf = cv2.imread('ev.jpg', 0)


hist = np.zeros(256)
[w, h] = np.shape(fotograf)

for v in range(0, h):
    for u in range(0, w):
        i = fotograf[u, v]
        hist[i] += 1

for i in range(256):
    print(f"{i} = {hist[i]}")


plt.plot(hist, color='#000000')
plt.show()