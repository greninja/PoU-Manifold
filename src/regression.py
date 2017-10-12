from sklearn import linear_model  
from sklearn import PolynomialFeatures
try:
	import cPickle as pickle 
except:
	import pickle

# Linear/ Polynomial regression
def regression(X, targets, polynomial=False):
	beta = np.random.rand(2,1) # dimension of the manifold is 2
	
	# Gaussian noise with mean 0 and standard deviation 1
	epsilon = np.asarray([[np.random.normal(0,1)]  for i in range(100)]) 
	
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
	saved_params = pickle.dumps(reg.coef_)
	return saved_params