import random
import csv
import sympy
import numpy
#from sympy
from sympy.abc import x # This makes it so x is always defined symbolically
from sympy import latex, exp, diff, pi, sqrt, cbrt
from sympy import solve
#from math import pi

from sympy.geometry.util import idiff # implicit differentiation

from sympy import nan, ln
from sympy import atan, acos, asin

from cbefunctions import *

# Questions 1-3 are graphical questions, which in the interest of hard disk space + difficulty using in AA,
# are questions that I don't want to autogenerate.

'''
Question 4:
Absolute min or maximum.

CSV params:
A: The function.
B: The domain
C: The word "minimum" or "maximum"
S: f(x_max/min)
S2: x_max/min

P.S., there is a less computationally expensive way of doing this using arrays, but
I've chosen not to do this seeing as this is a script to be run very infrequently.
'''
def q4(desiredNumSolutions, write, prnt, outputFile="cbe4q4.csv"):
	print("\n\nQuestion 4:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("A,B,C,S,S2")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("A,B,C,S,S2\n")
	while numSols < desiredNumSolutions:
		# Get a single solution
		f = randomPolynomial2(random.randint(3, 5)) # quadratic, cubic, or quartic polynomial
		k = latex(f)
		if k in solhashs:
			continue # Skip used or infinite solution
		# Is max of min (True = maximum, False = minimum)
		isMax = bool(random.getrandbits(1))
		if isMax:
			C = "maximum"
		else:
			C = "minimum"
		# Get bounds.
		bound1 = 0
		bound2 = 0
		while bound1 == bound2 or abs(bound1 - bound2) < 3:
			bound1 = randomCoeffOrZero(5)
			bound2 = randomCoeffOrZero(5)
			if bound1 > bound2:
				bounds = [bound2, bound1]
			else:
				bounds = [bound1, bound2]
		B = latex(bounds[0]) + " \\leq x \\leq " + latex(bounds[1])
		fPrime = diff(f)
		extrema = solve(fPrime) # Finds the roots of fPrime
		# Eliminate roots outside of the bounds.
		points = [bounds[0]]
		for i in range(len(extrema)):
			if extrema[i].is_real and extrema[i] > bounds[0] and extrema[i] < bounds[1]:
				points.append(extrema[i])
		points.append(bounds[1])
		if len(points) == 2:
			# print("[ERROR]: no real roots")
			continue
		# Get all of the y-values corresponding to index
		# yVals = []
		desiredIndex = 0
		bestValue = f.subs(x, 0)
			
		for i in range(1, len(points)):
			xVal = points[i]
			yVal = f.subs(x, xVal) 
			if isMax and yVal > bestValue:
				bestValue = yVal
				desiredIndex = i
			elif yVal < bestValue and not isMax: # If we are looking for minimum
				bestValue = yVal
				desiredIndex = i
				
		S = latex(bestValue)
		S2 = latex(points[i])
		numSols += 1
		if prnt:
			print(k + ',' + B + ',' + C + ',' + S + ',' + S2)
		if write:
			csvfile.write(k + ',' + B + ',' + C + ',' + S + ',' + S2 + '\n')
'''
A better version of Q4 that starts with roots and then builds a problem from there.

This one uses numpy
'''
def q4Optimized(desiredNumSolutions, write, prnt, outputFile="cbe4q4.csv"):
	pass
	# Todo
	
if __name__=='__main__':
	numSols = int(input("How many solutions do you want for each question: "))
	q4(numSols, False, True)
