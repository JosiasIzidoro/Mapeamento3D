from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import math

%matplotlib qt
    
d = np.random.randint(0,21600,21600)
d = d.reshape(60, 360)

ah = np.linspace(0,360, 360)
av = np.linspace(0, 60, 60)

xa = []
ya = []
za = []

for i in range(60):
    
    for j in range(360):
        
        print(j)    
        x1 = np.cos(np.radians(ah[j])) * d[i][j]
        xa.append(x1)
        
        y1 = np.sin(np.radians(ah[j])) * d[i][j]
        ya.append(y1)


    
for i in av:
    
    for j in range(360):
        
        z1 = i
        za.append(z1)
        
xa = np.array(xa)
xa = xa.reshape(60, 360)
#x = x.reshape(2, 10)
ya = np.array(ya)
ya = ya.reshape(60, 360)
#y = y.reshape(2, 10)
za = np.array(za)
za = za.reshape(60, 360)

fig = plt.figure(figsize = (10, 5))
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(xa, ya, za, rstride=1, cstride=1)

x = np.array([[1, 2, 3], [1, 2, 3]])
y = np.array([[1, 2, 3], [2, 3, 4]])
z = np.array([[1],[1]])
fig = plt.figure(figsize = (10, 5))
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x, y, z, rstride=1, cstride=1)