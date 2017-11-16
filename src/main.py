import numpy as np
import pprint
from datetime import datetime
from itertools import compress   

from bumpfunction import BumpFunction
from regression import fit_locally
from create_charts import dictionary_of_charts, dictionary_datapoints, CreateCharts

# To check if a Bump Function is compactly supported in a particular given chart
def check_for_Bumpfunction_support(chart, bumpfunction, return_support=False):
	boolarray = []
	for i, point in chart.iteritems():
		res = bumpfunction(point)  
		if res != 0:
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

# union of supports of bump functions should cover the whole set / manifold
def check_for_union_of_supports(list_of_charts):
	support1,support2 = (set() for _ in range(2))
	bfobject = BumpFunction()
	for chart in list_of_charts:
		for index, datpoint in chart.iteritems():
			res1 = bfobject.bumpfunction1(datpoint)
			res2 = bfobject.bumpfunction2(datpoint)
			if res1!= 0:
				support1.add(index)
			if res2!=0:
				support2.add(index)
	
	# Union of all supports should be equal to open cover or manifold
	opencover = support1.union(support2)

# Now deprecated function; calculates the normalized values of bump functions at different datapoints
# This function is currently superceded by functionality added in 'main()' function
def calculation(chart, functionlist):
	numDataPoints, numBumpFunc = len(chart), len(functionlist)
	matrix = np.zeros((numDataPoints, numBumpFunc))
	for i, bumpfunction in enumerate(functionlist):
		vectorized = np.vectorize(bumpfunction)
		result = map(lambda z : np.prod(vectorized(z)), chart)
		matrix[:,i] = result
	normalizing_denominators = np.sum(matrix, 1)
	final_matrix = matrix / normalizing_denominators[:, np.newaxis]

def set_of_charts(datapoint_index, dictionary_of_charts):
	"""
	Returns all the chart names in which the datapoint lies
	in. (currently: 3 charts at a time for a single datapoint)
	"""
	included_charts = []
	for chart_name, chart in dictionary_of_charts.iteritems():
		if datapoint_index in chart:
			included_charts.append(chart_name)
	return included_charts

# Create an object of the BumpFunction class 
bumpfunctionobj = BumpFunction()

# Caller dispatch; the bump functions corresponding to the each chart
chart_to_bumpfunc = {
	'chart1' : bumpfunctionobj.bumpfunction1,
	'chart2' : bumpfunctionobj.bumpfunction2,
	'chart3' : bumpfunctionobj.bumpfunction1,
	'chart4' : bumpfunctionobj.bumpfunction2,
	'chart5' : bumpfunctionobj.bumpfunction1,
	'chart6' : bumpfunctionobj.bumpfunction2 
	}

def global_approximation(set_of_points, regression_params):
	"""
	Returns a list of globally approximated values of the given set of points 
	by using partitions of unity on locally fitted linear functions

	args:
	-----------------------
	set_of_points : A dictionary of datapoints and its indices
	regression_params : A dictionary of chart names and their respective

	"""
	global_values = dict() 
	
	#Looping over the 'set_of_points' lying on the embedded spherical manifold 
	for index, data_point in set_of_points.iteritems(): 
		included_charts = set_of_charts(index, dictionary_of_charts)
		bumpfunc_values = []
		linearfunc_values = []
		
		# There will be only 3 charts in 'included_charts' and 
		# hence only 3 bump functions will be non-zero for a single datapoint
		for chart_name in included_charts:
			respective_data_point = dictionary_of_charts[chart_name][index]
			func_value = chart_to_bumpfunc[chart_name](respective_data_point) 
			bumpfunc_values.append(func_value)
		
			reg = regression_params[chart_name]
			mul = np.dot(reg, respective_data_point.reshape(2,1)) #Reshape to make it 
			                                                      #suitable for multiplication
			linearfunc_values.append(np.asscalar(mul)) 
		
		# Converting the bumpfunction list to a numpy array to make them compatible for multiplication
		bumpfunc_values = np.asarray(bumpfunc_values)
		
		# Normalizing the bump function values to fulfill PoU's conditions
		normalized_bumpfunc = bumpfunc_values / np.sum(bumpfunc_values) 
		local_function_products = np.multiply(normalized_bumpfunc, linearfunc_values)
		
		# Global value of the locally fitted function
		global_function_value = np.sum(local_function_products)
		global_values[index] = global_function_value
	
	return global_values
	#pprint.pprint(global_values)
	
def f_true(testing_set):
	"""
	Returns the value to be compared with the approximated value for evaluation on testing set 
	Here we take:
		f_true(x1, x2, x3) = x1 
	where,
		(x1, x2, x3) is a sample from our embedded manifold with the 3 values as the coordinates in 3D space
	"""
	true_function_values = dict()
	for point_index, point in testing_set.iteritems():
		value = point[0]  
		true_function_values[point_index] = value
	return true_function_values

def holdout_method():
	"""
	Dividing the dataset (training and testing) in 80:20 ratio according to Pareto principle 
	"""
	training_set = dict(dictionary_datapoints.items()[:80])
	testing_set = dict(dictionary_datapoints.items()[80:])
	chart_1, chart_2, chart_3, chart_4, chart_5, chart_6 = CreateCharts(training_set, return_for_evaluating=True)
	regression_params = fit_locally(chart_1, chart_2, chart_3, chart_4, chart_5, chart_6)

	true_function_vals = f_true(testing_set)
	
	#Calculating time
	start_time = datetime.now()
	global_vals = global_approximation(testing_set, regression_params)
	end_time = datetime.now()

	#Calculating mean of the sum of squared loss and standard deviation
	loss_array = []
	for (true, approximated) in zip(true_function_vals.values(), global_vals.values()):
			loss_array.append(true - approximated)
	total_loss = np.sum(np.abs(loss_array))
	average_loss = np.mean(loss_array)
	mean_squared_loss = np.mean(np.square(loss_array))
	standard_deviation = np.sqrt(np.mean(map(lambda x : np.square(x - average_loss), loss_array)))
	 
	print ("Total loss for the testing dataset is : {}, \n"
			"Average loss for the testing dataset is : {}, \n"
			"Mean Squared error/ loss : {} \n"
			"Standard Deviation : +/- {} \n"
			"Time taken for fitting function : {} seconds").format(total_loss, average_loss, mean_squared_loss, \
												standard_deviation, (end_time - start_time).total_seconds())
	
	#Printing the global values for testing dataset
	print "The global approximated values for the local fitted functions are : "
	pprint.pprint(global_vals)

if __name__=="__main__":
	holdout_method()