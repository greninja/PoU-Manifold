import numpy as np 
from matplotlib import pyplot as plt 

class BumpFunction():
	"""
	This class contains all the bump functions used for PoU
	----------
	x : a single data point
	"""
	def __init__(self):
		pass
	
	# Prerequisite smooth functions 
	def f(self, t):
		if t>0:
			return np.exp(-float(1)/t)
		return 0

	def g(self, t):
		return self.f(t)/(self.f(t) + self.f(1-t))

	def h(self, t):
		return self.g(t-1)

	def k(self, t):
		tsquare = np.square(t)
		return self.h(tsquare)

	def rho(self, t):
		return 1 - self.k(t)

	# Non-negative C-infinite bump functions essential for Partition of unity

	def bumpfunction1(self, x): 				# Has compact support between [-1,1]
		self.output = []
		for i in x:
			if i > -1  and i < 1:
				self.output.append(np.exp(1/(i**2-1)))
			else :
				self.output.append(0)
		return self.output

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

	def bumpfunction2(self, x):
		self.output = []
		self.output = list(map(lambda i : self.f(1+i) * self.f(1-i), x))
		return self.output
	
	"""
	def bumpfunction4(self, x):
		self.output = []
		for i in x:
		 	self.output.append(self.rho(i))
		return self.output
	"""
	"""
	def bumpfunction3(self, x):
		self.output=[]
		for i in x:
			if np.abs(i) < 1:
				self.output.append(1 - np.square(i))
			else:
				self.output.append(0)
		return self.output
	"""
	def bumpfunction3(self, x):
		self.output=[]
		for i in x:
			numerator1 = np.square(i) + 1
			numerator2 = np.exp(4*i/(np.square(i)-1), dtype=np.float128)
			denominator1 = np.square(i) - 1
			denominator2 = 1 + numerator2
			final = (numerator1 * numerator2) /  np.square(denominator1 * denominator2)
			self.output.append(final)
		return self.output

def plot_main():
	bumpfunctionobj = BumpFunction() 
	x = np.linspace(-1, 1, 1000)
	y1 = bumpfunctionobj.bumpfunction1(x)
	y2 = bumpfunctionobj.bumpfunction2(x)
	y3 = bumpfunctionobj.bumpfunction3(x)
 
	plt.figure(1,figsize=(14,14))
	
	plt.subplot(221)
	plt.plot(x,y1)
	
	plt.subplot(222)
	plt.plot(x,y2)
	
	plt.subplot(223)
	plt.plot(x,y3)
	
	plt.show()
	
if __name__=="__main__":
	plot_main()