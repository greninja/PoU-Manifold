import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d

from sklearn import linear_model  
from sklearn import PolynomialFeatures

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
xi, yi, zi = sample_spherical(200)
data_points = []
map(lambda x,y,z : data_points.append((x,y,z)), xi,yi,zi)     
dictionary_datapoints = {k:np.array(v) for k,v in enumerate(data_points)}
chart1, chart2, chart3, chart4, chart5, chart6 = (dict() for _ in range(6))


"""
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
        
 """
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

# To check if a Bump Function is compactly supported in the given chart;
# should be contained in closure of chart
# returns support 
def check(chart, bumpfunction, return_support=False):
	boolarray = []
	for point in chart:
		res = bumpfunction(point)  
		mul = np.prod(res) 
		if mul != 0:
			boolarray.append(True)
		else:
			boolarray.append(False)
	if any(boolarray):
		print "{} is supported in the given chart", \
				"(subset of the cover/ atlas) ".format(bumpfunction.func_name)

	# Functionality for returning support of the given bump function
	if return_support:
		support = list(compress(xrange(len(boolarray)), boolarray))
		return support

	# After experimenting not all points are getting included in the union of the supports
	# Things to cross-verify:
	# 	(1) Can we write bumpfunction in 'n' variables as the product of individual bfs
	#	(2) Does the support have to be taken on all the points in original space or just individual charts?? 
	#   (3) Try on the points from the manifold and not random data points
	# 	(4) We can also check the locally finite condition by creating neighbourhoods for each point and testing 
	# 		 whether it intersects finitely many :  sets from {supp(phi_alpha)} (collection of supports of functions)
	# 	 (5) Show Hari visualizations of all bump functions
	#	 (6) In general : there is PoU subordinate to an open cover of a Manifold. Here we are taking the sets in 
	#	 	 open cover to be coordinate patches of a atlas.
"""
def check_alternative(chart_dictionary, bumpfunction):
    chart_list = []
    for chart_name, chart in chart_dictionary.iteritems(): 
        boolarray = []
        for point in chart:
            res = bumpfunction(point)
            mul = np.prod(res)
            if mul != 0:
                boolarray.append(True)
            else:
                boolarray.append(False)
        if any(boolarray):
            chart_list.append(chart_name)
    return chart_list
"""


def calculation(chart, functionlist):
	numDataPoints, numBumpFunc = len(chart), len(functionlist)
	matrix = np.zeros((numDataPoints, numBumpFunc))
	for i, bumpfunction in enumerate(functionlist):
		vectorized = np.vectorize(bumpfunction)
		result = map(lambda z : np.prod(vectorized(z), chart))
		matrix[:,i] = result
	normalizing_denominators = np.sum(matrix, 1)
	final_matrix = matrix / normalizing_denominators[:, np.newaxis]

def check_for_union_of PoU():
	# union of supports of function  should cover the whole set / manifold
	# indexing the list of datapoints using dict(enumerate(datapoints))

def main(x, local_function, bumpfunction):
	global_value = 0
	for bf in "number of bump functions":
		global_value += local_function(x) * bf(x)
	return global_value

# Number of partitions required as the number of dimension of the manifold 
# or the number of sets in open cover of manifold (here charts) ?? 
#  How do we prove, either of them?
# 

# PoU -> convolution operation
# Think of various scalar valued functions i.e. ( f : R^n -> R )that can be used instead of linear regression on charts
# Bump function in 'n' variables is defined by taking the product of individual functions
# Polynomial regression
# We have created individual charts from the dataset
# We explored with using C-inf smooth Bump Functions instead of 'pyramid (max{0, r-(c-x)})'
# Instead of polynomial regression, linear regression we can explore with kernel smoothers
# How to choose adaptive neighbourhood sizes
# We have constructed the overlapping charts/ patches s.t. atmost '4' patches overlap at any given point.
# Shape lying on sphereical manifold dataset