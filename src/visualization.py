from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.ticker as ticker

from create_charts import * 

tick_spacing=0.5

# Visualize spherical manifold S^2 in R^3
fig1 = plt.figure(figsize=(7,7)) #7" * 7 " fig
ax = fig1.add_subplot(111, projection='3d')
ax.scatter(xi, yi, zi, s=10, c='b')
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.zaxis.set_major_locator(ticker.MultipleLocator(0.5)) 
fig1.savefig('../images/sphere_manifold.png')


# Visualize individual charts of the manifold 
fig2 = plt.figure(figsize=(7,7)) #7" * 7 " fig

#Chart1
xs1 = list(zip(*chart1.values())[0])
ys1 = list(zip(*chart1.values())[1])
ax1 = fig2.add_subplot(321, projection='3d')
ax1.scatter(xs1, ys1, s=0.5, c='r')
ax1.text2D(0.05, 0.95, "charts in x-y plane", transform=ax1.transAxes)
ax1.tick_params(width=1)
ax1.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
ax1.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
ax1.zaxis.set_major_locator(ticker.MultipleLocator(tick_spacing)) 

#Chart2
xs2 = list(zip(*chart2.values())[0])
ys2 = list(zip(*chart2.values())[1])
ax2 = fig2.add_subplot(322, projection='3d')
ax2.scatter(xs2, ys2, s=0.5, c='g')
ax2.set_xlabel('X Axis')
ax2.set_ylabel('Y Axis')
ax2.set_zlabel('Z Axis')
ax2.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
ax2.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
ax2.zaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

#Chart3
xs3 = list(zip(*chart3.values())[0])
zs3 = list(zip(*chart3.values())[1])
ax3 = fig2.add_subplot(323, projection='3d')
ax3.scatter(xs3, np.zeros(len(xs3)), zs3, s=0.5, c='r')
ax3.text2D(0.05, 0.95, "charts in x-z plane", transform=ax3.transAxes) 
ax3.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
ax3.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
ax3.zaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

#Chart4
xs4 = list(zip(*chart4.values())[0])
zs4 = list(zip(*chart4.values())[1])
ax4 = fig2.add_subplot(324, projection='3d')
ax4.scatter(xs4, np.zeros(len(xs4)), zs4, s=0.5, c='g')
ax4.set_xlabel('X Axis')
ax4.set_ylabel('Y Axis')
ax4.set_zlabel('Z Axis')
ax4.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
ax4.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
ax4.zaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

#Chart5
ys5 = list(zip(*chart5.values())[0])
zs5 = list(zip(*chart5.values())[1])
ax5 = fig2.add_subplot(325, projection='3d')
ax5.scatter(np.zeros(len(ys5)), ys5, zs5, s=0.5, c='r')
ax5.text2D(0.05, 0.95, "charts in y-z plane", transform=ax5.transAxes) 
ax5.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
ax5.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
ax5.zaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

#Chart6
ys6 = list(zip(*chart6.values())[0])
zs6 = list(zip(*chart6.values())[1])
ax6 = fig2.add_subplot(326,projection='3d')
ax6.scatter(np.zeros(len(ys6)), ys6, zs6, s=0.5, c='g')
ax6.set_xlabel('X Axis')
ax6.set_ylabel('Y Axis')
ax6.set_zlabel('Z Axis')
ax6.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
ax6.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
ax6.zaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

fig2.savefig('../images/charts.png')
plt.show()