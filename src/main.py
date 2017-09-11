import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d

from sklearn import linear_model  
from sklear import PolynomialFeatures

from itertools import compress      

def sample_spherical(npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    return vec

phi = np.linspace(0, np.pi, 20)
theta = np.linspace(0, 2 * np.pi, 40)
x = np.outer(np.sin(theta), np.cos(phi))
y = np.outer(np.sin(theta), np.sin(phi))
z = np.outer(np.cos(theta), np.ones_like(phi))

# Increase the number of points
xi, yi, zi = sample_spherical(100)
data_points = []
map(lambda x,y,z : data_points.append((x,y,z)), xi,yi,zi)     
#fig.show()
chart1, chart2, chart3, chart4, chart5, chart6 = ([] for i in range(6))

# Creating the 6 charts of a sphere
for i in range(len(data_points)):
		if data_points[i][2] > 0:
		 	chart1.append((data_points[i][0], data_points[i][1]))
		else:
		 	chart2.append((data_points[i][0], data_points[i][1]))

		if data_points[i][0] > 0:
		 	chart3.append((data_points[i][1], data_points[i][2]))
		else:
		 	chart4.append((data_points[i][1], data_points[i][2]))
		if data_points[i][1] > 0:
			chart5.append((data_points[i][0], data_points[i][2]))
		else:
			chart6.append((data_points[i][0], data_points[i][2]))

# To visualize charts

xs1 = list(zip(*chart1)[0])
ys1 = list(zip(*chart1)[1])

xs2 = list(zip(*chart2)[0])
ys2 = list(zip(*chart2)[1])

fig = plt.figure(figsize=plt.figaspect(2.))
ax1 = fig.add_subplot(221,projection='3d')

ax1.scatter(xi, yi, zi, s=10, c='g', zorder=10)

# Chart 1
ax2 = fig.add_subplot(222,projection='3d')
ax2.scatter(xs1,ys1,c='r')   

# Chart 2
ax3 = fig.add_subplot(223,projection='3d')
ax3.scatter(xs2,ys2,c='b')   
plt.show()

# Concatenating the charts into 3 pairs
pair1 = np.concatenate((chart1, chart2), axis=0)
pair2 = np.concatenate((chart3, chart4), axis=0)
pair3 = np.concatenate((chart5, chart6), axis=0)

# Linear/ Polynomial regression
def regression(X, targets, polynomial=False):
	beta = np.random.rand(2,1) # 2 because the dimension of the manifold is 2
	epsilon = np.asarray([[np.random.normal(0,1)]  for i in range(100)]) # Gaussian noise with mean 0 and standard deviation 1
	
	if polynomial:
		# For polynomial regression (Manually)
		xquare = map(lambda m : np.square(m), X[:,1])
		X[:,1] = xquare
		targets = np.dot(X, beta) + epsilon
		
		# Using sklearn 
		# poly = PolynomialFeatures(degree=2)
		# X_ = poly.fit_transform(X)
		# clf = linear_model.LinearRegression()
		# clf.fit(X_, targets)

	# Generating the targets i.e. the regressands
	targets = np.dot(X, beta) + epsilon  #  Shape of targets is (100,1)
	reg = linear_model.LinearRegression()
	reg.fit(X, targets) # reg.coef_ will display the coefficients i.e. the estimated beta parameters

# Prerequisite smooth functions 
def f(t):
	if t>0:
		return np.exp(-float(1)/t)
	return 0

def g(t):
	return f(t)/(f(t) + f(1-t))

def h(t):
	return g(t-1)

def k(t):
	tsquare = np.square(t)
	return h(tsquare)

def rho(t):
	return 1 - k(t)

# Non-negative C-infinite bump functions essential for Partition of unity

def bumpfunction1(x): 				# Has compact support between [-1,1]
	if x > -1  and  x < 1:
		return np.exp(1/(x**2-1))
	else :
		return 0

def bumpfunction2(x):
	absolute_value = np.abs(x)
	if  absolute_value <= 1:
		return 1
	elif absolute_value >= 2:
		return 0
	else:
		return f(2 - absolute_value) / (f(2 - absolute_value) + f(absolute_value + 1))

def bumpfunction3(x):
	return f(1+x) * f(1-x)

# From Loring Tu's book
def bumpfunction4(x):
	return rho(x)

# To check if a Bump Function is supported in the given chart; return support 
def check(chart, bumpfunction, return_support=False):
	boolarray = []
	for dim1, dim2 in chart:
		mul =  bumpfunction(dim1) * bumpfunction(dim2)
		if mul != 0:
			boolarray.append(True)
		else:
			boolarray.append(False)
	if any(boolarray):
		print "{} has is supported in the given chart \
				(subset of the cover/ atlas) ".format(bumpfunction)

	# Functionality for returning support of the given bump function
	if return_support:
		support = list(compress(xrange(len(boolarray)), boolarray))
		return support

def calculation(chart, functionlist):
	numDataPoints, numBumpFunc = len(chart), len(functionlist)
	matrix = np.zeros((numDataPoints, numBumpFunc))
	for i, bumpfunction in enumerate(functionlist):
		vectorized = np.vectorize(bumpfunction)
		result = map(lambda z : np.prod(vectorized(z), chart))
		matrix[:,i] = result
	normalizing_denominators = np.sum(matrix, 1)
	final_matrix = matrix / normalizing_denominators[:, np.newaxis]

# PoU -> convolution operation
# Think of various scalar valued functions i.e. ( f : R^n -> R )that can be used instead of linear regression on charts
# Bump function in 'n' variables is defined by taking the product of individual functions
# Polynomial regression