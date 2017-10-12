"""
The data points are uniformly distributed on a unit sphere.
To generate these 3-dimensional points, we first generate standard
normally distributed points as vectors lying in 3d space, and then
normalize these vectors (X:= X / ||X||) to make it lie on a sphere
(S^2) which acts as our manifold. 
"""
import numpy as np 
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def sample_spherical(npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    return vec
"""
phi = np.linspace(0, np.pi, 20)
theta = np.linspace(0, 2 * np.pi, 40)
x = np.outer(np.sin(theta), np.cos(phi))
y = np.outer(np.sin(theta), np.sin(phi))
z = np.outer(np.cos(theta), np.ones_like(phi))
"""
xi, yi, zi = sample_spherical(100)
data_points = []
map(lambda x,y,z : data_points.append((x,y,z)), xi,yi,zi)     
dictionary_datapoints = {k:np.array(v) for k,v in enumerate(data_points)}
chart1, chart2, chart3, chart4, chart5, chart6 = (dict() for _ in range(6))

# Creating the 6 charts of a sphere
for i, point in dictionary_datapoints.iteritems():
        if point[2] > 0 :
            chart1[i] = point[:2] 
        else:
        	chart2[i] = point[:2]
        if point[1] > 0:
        	chart3[i] = point[::len(point)-1]
        else:
        	chart4[i] = point[::len(point)-1]
        if point[0] > 0:
        	chart5[i] = point[1:]
        else:
        	chart6[i] = point[1:]

# Visualize spherical manifold S^2 in R^3
fig1 = plt.figure(figsize=(7,7)) #7" * 7 " fig
ax = fig1.add_subplot(111, projection='3d')
ax.scatter(xi, yi, zi, s=10, c='b')

# Visualize individual charts of the manifold 
fig2 = plt.figure(figsize=(7,7)) #7" * 7 " fig

#Chart1
xs1 = list(zip(*chart1.values())[0])
ys1 = list(zip(*chart1.values())[1])
ax1 = fig2.add_subplot(321, projection='3d')
ax1.scatter(xs1, ys1, c='r') 

#Chart2
xs2 = list(zip(*chart2.values())[0])
ys2 = list(zip(*chart2.values())[1])
ax2 = fig2.add_subplot(322, projection='3d')
ax2.scatter(xs2, ys2, c='g')

#Chart3
xs3 = list(zip(*chart3.values())[0])
zs3 = list(zip(*chart3.values())[1])
ax3 = fig2.add_subplot(323, projection='3d')
ax3.scatter(xs3, np.zeros(len(xs3)), zs3, c='r')

#Chart4
xs4 = list(zip(*chart4.values())[0])
zs4 = list(zip(*chart4.values())[1])
ax4 = fig2.add_subplot(324, projection='3d')
ax4.scatter(xs4, np.zeros(len(xs4)), zs4, c='g')

#Chart5
ys5 = list(zip(*chart5.values())[0])
zs5 = list(zip(*chart5.values())[1])
ax5 = fig2.add_subplot(325, projection='3d')
ax5.scatter(np.zeros(len(ys5)), ys5, zs5, c='r')

#Chart6
ys6 = list(zip(*chart6.values())[0])
zs6 = list(zip(*chart6.values())[1])
ax6 = fig2.add_subplot(326,projection='3d')
ax6.scatter(np.zeros(len(ys6)), ys6, zs6, c='g')

plt.show()