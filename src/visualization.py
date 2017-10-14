from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d

from create_charts import *

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