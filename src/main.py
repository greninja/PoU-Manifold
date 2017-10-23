import numpy as np
import pprint
import time 
from itertools import compress   

from bumpfunction import BumpFunction
from regression import Regression, regression_params
from create_charts import dictionary_of_charts, dictionary_datapoints

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
def check_for_union_of_PoU(list_of_charts):
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
	Returns all the overlapping charts in which the given data point falls into.
	"""
	included_charts = []
	for chart_name, chart in dictionary_of_charts.iteritems():
		if index_of_point in chart:
			included_charts.append(chart_name)
	return included_charts

bumpfunctionobj = BumpFunction()

# Caller dispatch
chart_to_bumpfunc = {
	'chart1' : bumpfunctionobj.bumpfunction1,
	'chart2' : bumpfunctionobj.bumpfunction1,
	'chart3' : bumpfunctionobj.bumpfunction2,
	'chart4' : bumpfunctionobj.bumpfunction2,
	'chart5' : bumpfunctionobj.bumpfunction3,
	'chart6' : bumpfunctionobj.bumpfunction3 
	}

# Returns a list of global approximation of locally fitted linear functions
def main():
	global_values = []
	start_time = time.time()
	# Calculating the global approximated value for all the 
	# datapoints lying on the sphere
	for index, data_point in dictionary_datapoints.iteritems(): 
		included_charts = set_of_charts(index, dictionary_of_charts)
		bumpfunc_values = []
		linearfunc_values = []
		for chart_name in included_charts:
			respective_data_point = dictionary_of_charts[chart_name][index]
			output_array = chart_to_bumpfunc[chart_name](respective_data_point)
			func_value = np.prod(output_array)
			bumpfunc_values.append(func_value)
		
			reg = regression_params[chart_name]
			mul = np.dot(reg, respective_data_point.reshape(2,1)) #Reshape to make it 
			                                                      #suitable for multiplication
			linearfunc_values.append(np.asscalar(mul)) 
		
		bumpfunc_values = np.asarray(bumpfunc_values)
		# Normalizing the bump function values to fulfill PoU's conditions
		normalized_bumpfunc = bumpfunc_values / np.sum(bumpfunc_values) 
		local_function_products = np.multiply(normalized_bumpfunc, linearfunc_values)
		
		# Global value of the locally fitted function
		global_function_value = np.sum(local_function_products)
		global_values.append(global_function_value)
	end_time = time.time()
	print pprint.pprint(global_values)
	print end_time - start_time
	
if __name__=="__main__":
	main()
# Alternate Scalar valued functions
# How to choose adaptive neighbourhood sizes
# We can also check the locally finite condition by creating neighbourhoods for each point and testing 
# whether it intersects finitely many :  sets from {supp(phi_alpha)} (collection of supports of functions)