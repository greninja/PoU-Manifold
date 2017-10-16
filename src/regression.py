import numpy as np 
from sklearn import linear_model  
from sklearn.preprocessing import PolynomialFeatures
from create_charts import chart1, chart2, chart3, chart4, chart5, chart6

# Linear/ Polynomial regression
def Regression(X, polynomial=False):
	beta = np.random.rand(2,1) # dimension of the manifold is 2
	
	# Gaussian noise with mean 0 and standard deviation 1
	epsilon = np.asarray([[np.random.normal(0,1)]  for _ in range(len(X))]) 
	
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
	reg.fit(X, targets) # reg.coef_ consists of the estimated parameters

	# Storing the parameters
	saved_params = reg.coef_
	return saved_params

chart1_params = Regression(chart1.values())
chart2_params = Regression(chart2.values())
chart3_params = Regression(chart3.values())
chart4_params = Regression(chart4.values())
chart5_params = Regression(chart5.values())
chart6_params = Regression(chart6.values())

# A dictionary for storing the parameters
regression_params = {
	'chart1' : chart1_params,
	'chart2' : chart2_params,
	'chart3' : chart3_params,
	'chart4' : chart4_params,
	'chart5' : chart5_params,
	'chart6' : chart6_params,
}