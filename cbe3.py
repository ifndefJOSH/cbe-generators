import random
import csv
import sympy
#from sympy
from sympy.abc import x # This makes it so x is always defined symbolically
from sympy import latex, exp, diff, pi
#from math import pi

from cbefunctions import *

'''
Question 1

Either does something in the format
f(x) = e^(g(x) h(x))
OR
f(x) = e^(g(x))(sin(ax) OR cos(ax))

Parameters: A, B, S
A = f(x)
B = constant
S = f'(B)
'''
def q1(desiredNumSolutions, write, prnt, outputFile="cbe3q3.csv"):
	print("\n\nQuestion 5:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("A,B,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("A,B,S\n")
	while numSols < desiredNumSolutions:
		# Get a single solution
		if bool(random.getrandbits(1)):
			h = 0
			g = 0
			while h == 0 or g == 0 or h == g:
				h = randomSymbolic(0, 7)
				g = randomSymbolic(0, 7)
			f = exp(h * g)
			B = random.randint(0, 9)
		else:
			g = randomSymbolic(0, 7)
			a = random.randint(1, 9)
			B = pi * random.randint(0, 9) / random.randint(1, 9)
			if bool(random.getrandbits(1)):
				f = exp(g) * sympy.cos(a * x)
			else:
				f = exp(g) * sympy.sin(a * x)
				
		# f(x) is now defined
		k = latex(f)
		if not k in solhashs:
			solhashs[k] = True
			fPrime = diff(f)
			S = #TODO
			
			if S.is_infinite or S == nan:
				#print("Skipping infinite solution")
				continue
			numSols += 1
