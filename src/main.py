import numpy as np
from itertools import compress      
from bumpfunction import BumpFunction

# Concatenating the charts into 3 pairs
pair1 = np.concatenate((chart1, chart2), axis=0)
pair2 = np.concatenate((chart3, chart4), axis=0)
pair3 = np.concatenate((chart5, chart6), axis=0)

# To check if a Bump Function is compactly supported in a particular given chart;
# should be contained in closure of chart
# returns support 
def check(chart, bumpfunction, return_support=False):
	boolarray = []
	for i, point in chart.iteritems():
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

# union of supports of function should cover the whole set / manifold
def check_for_union_of PoU(list_of_charts):
	support1,support2,support3,support4 = (set() for _ in range(4))
	bumpfunctionclass = BumpFunction()
	for chart in list_of_charts:
		for index, datpoint in chart.iteritems():
			res1 = np.prod(bumpfunctionclass.bumpfunction1(datpoint))
			res2 = np.prod(bumpfunctionclass.bumpfunction2(datpoint))
			res3 = np.prod(bumpfunctionclass.bumpfunction3(datpoint))
			res4 = np.prod(bumpfunctionclass.bumpfunction4(datpoint)) 
			if res1!= 0:
				support1.add(index)
			if res2!=0:
				support2.add(index)
			if res3!=0:
				support3.add(index)
			if res4!=0:
				support4.add(index)
	# Union of all supports should be equal to open cover or manifold
	opencover = support1.union(support2, support3, support4)

def calculation(chart, functionlist):
	numDataPoints, numBumpFunc = len(chart), len(functionlist)
	matrix = np.zeros((numDataPoints, numBumpFunc))
	for i, bumpfunction in enumerate(functionlist):
		vectorized = np.vectorize(bumpfunction)
		result = map(lambda z : np.prod(vectorized(z)), chart)
		matrix[:,i] = result
	normalizing_denominators = np.sum(matrix, 1)
	final_matrix = matrix / normalizing_denominators[:, np.newaxis]

def calculate(input_data_point, set_of_bumpfunctions):


# Number of partitions required as the number of dimension of the manifold 
# or the number of sets in open cover of manifold (here charts) ?? 
#  How do we prove, either of them?

# Think of various scalar valued functions i.e. ( f : R^n -> R )that can be used instead of linear regression on charts
# Bump function in 'n' variables is defined by taking the product of individual functions


# How to choose adaptive neighbourhood sizes

# After experimenting not all points are getting included in the union of the supports
	# Things to cross-verify:
	#	(2) Does the support have to be taken on all the points in original space or just individual charts?? 
	# 	(4) We can also check the locally finite condition by creating neighbourhoods for each point and testing 
	# 		 whether it intersects finitely many :  sets from {supp(phi_alpha)} (collection of supports of functions)
	#	 (6) In general : there is PoU subordinate to an open cover of a Manifold. Here we are taking the sets in 
	#	 	 open cover to be coordinate patches of a atlas.

# EXTRA CODE 

def homeomorphism(x):
	return np.reciprocal(x)