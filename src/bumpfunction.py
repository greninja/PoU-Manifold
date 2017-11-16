import numpy as np 
from matplotlib import pyplot as plt 
from scipy.spatial.distance import euclidean
from mpl_toolkits.mplot3d import Axes3D

from create_charts import sample_spherical

class BumpFunction():
	"""
	This class contains all the bump functions used for PoU
	----------
	x : a single data point
	"""
	def __init__(self):
		self.ORIGIN = [0,0]
	
	# Prerequisite smooth functions 
	def f(self, t):
		if t>0:
			return np.exp(-float(1)/t)
		return 0

	# Non-negative C-infinite bump functions

	#Has compact support between [-1,1]
	def bumpfunction1(self, x): 				
		norm = euclidean(x, self.ORIGIN) # Calculating the euclidean norm of the point on S^2 
		if norm < 1:
				return np.exp(1/(norm**2 - 1))
		else :
				return 0.0
		
	def bumpfunction2(self, x):
		norm = euclidean(x, self.ORIGIN)
		return self.f(1+norm) * self.f(1-norm)

	"""
	def bumpfunction2(self, x):
		self.output = []
		absolute_value = np.abs(x)
		for i in absolute_value:
			if  i <= 1:
					self.output.append(1)
			elif i >= 2:
					self.output.append(0)
			else:
					term_1 = self.f(2 -i) 
					term_2 = self.f(i + 1)
					self.output.append(term_1/(term_1 + term_2))
		return self.output
	"""
	
	"""
	def bumpfunction3(self, x):
		self.output=[]
		for i in x:
			if i > -1 and i < 1:
				numerator1 = np.square(i) + 1
				numerator2 = np.exp(4*i/(np.square(i)-1), dtype=np.float128)
				denominator1 = np.square(i) - 1
				denominator2 = 1 + numerator2
				final = (numerator1 * numerator2) /  np.square(denominator1 * denominator2)
				self.output.append(final)
			else:
				self.output.append(0.0)
		return self.output
	"""

def plot_main():
	fig = plt.figure(figsize=plt.figaspect(0.5))
	bumpfunctionobj = BumpFunction() 
	xi, yi, zi = sample_spherical(500)
	merged_sample_points = zip(xi, yi)
	
	# For 2 bump functions
	z1, z2 = [], []
	for point in merged_sample_points:
		z1.append(bumpfunctionobj.bumpfunction1(point))
		z2.append(bumpfunctionobj.bumpfunction2(point))
	
	ax1 = fig.add_subplot(121, projection='3d')
	ax1.scatter(xi, yi, z1, color='b')
	ax1.text2D(0.05, 0.95, "Bump Function 1", transform=ax1.transAxes)
	ax1.set_xlabel('X Axis')
	ax1.set_ylabel('Y Axis')
	ax1.set_zlabel('Z Axis')

	ax2 = fig.add_subplot(122, projection='3d')
	ax2.scatter(xi, yi, z2, color='r')
	ax2.text2D(0.05, 0.95, "Bump Function 2", transform=ax2.transAxes)
	ax2.set_xlabel('X Axis')
	ax2.set_ylabel('Y Axis')
	ax2.set_zlabel('Z Axis')

	fig.savefig('../images/bumpfunctions.png')
	plt.show()
	
if __name__=="__main__":
	plot_main()