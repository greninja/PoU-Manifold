import numpy as np
from itertools import compress      

from bumpfunction import BumpFunction
from regression import Regression 
from create_charts import dictionary_of_charts, dictionary_datapoints

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

def set_of_charts(index_of_point, dictionary_of_charts):
	"""
	Returns the chart the given data point falls in
	"""
	included_charts = []
	for chart_name, chart in dictionary_of_charts.iteritems():
		if index_of_point in chart:
			included_charts.append(chart_name)
	return included_charts

chart_to_bumpfunc = {
	'chart1' : 'bumpfunction1',
	'chart2' : 'bumpfunction1',
	'chart3' : 'bumpfunction2',
	'chart4' : 'bumpfunction2',
	'chart5' : 'bumpfunction3',
	'chart6' : 'bumpfunction3',
}

def main():
	bumpfunctionobj = BumpFunction()
	global_values = np.array()
	
	# Calculating the global approximated value for all the 
	# datapoints lying on the sphere
	for index, point in dictionary_datapoints.iteritems(): 
		included_charts = set_of_charts(index, dictionary_of_charts)
		values = []
		for chart_name in included_charts:
			bf = chart_to_bumpfunc[chart_name]
			point = dictionary_of_charts[chart_name][index]
			func_value = bumpfunctionobj.bf(point)
			values.append(func_value)

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