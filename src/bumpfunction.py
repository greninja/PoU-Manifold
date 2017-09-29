import numpy as np 

class BumpFunctions():
	"""
	This class contains all the bump functions used for PoU
	----------
	x : a single data point
	"""
	def __init__():
		output = []
	
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
			for i in x:
				if i > -1  and i < 1:
					output.append(np.exp(1/(i**2-1)))
				else :
					output.append(0)
			return output

		def bumpfunction2(x):
			absolute_value = np.abs(x)
			for i in absolute_value:
				if  i <= 1:
						output.append(1)
				elif i >= 2:
						output.append(0)
				else:
						term_1 = f(2 - i)
						term_2 = f(i + 1)
						output.append(term_1/(term_1 + term_2))
			return output

		def bumpfunction3(x):
			output = list(map(lambda i : f(1+i) * f(1-i), x))
			return output

		def bumpfunction4(x):
			for i in x:
			 	output.append(rho(i))
			return output

		def bumpfunction5(x):
			for i in x :
				if i <= -1 or i >= 1:
					output.append(0)
				else:
					oper = np.square(np.cos((np.pi * x)/2))
					output.append(oper)