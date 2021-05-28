import random
import csv
import sympy
import numpy
#from sympy
from sympy.abc import x # This makes it so x is always defined symbolically
from sympy import latex, exp, diff, pi, sqrt, cbrt, integrate
from sympy import solve
#from math import pi

from sympy.geometry.util import idiff # implicit differentiation

from sympy import nan, ln
from sympy import atan, acos, asin

from cbefunctions import *

# Some tiny value

epsilon = 0.001

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
		S2 = latex(bestPoint)
		numSols += 1
		if prnt:
			print(k + ',' + B + ',' + C + ',' + S + ',' + S2)
		if write:
			csvfile.write(k + ',' + B + ',' + C + ',' + S + ',' + S2 + '\n')
	if write:
		csvfile.close()
'''
A better version of Q4 that starts with roots and then builds a problem from there.

This one uses numpy
'''
def q4Optimized(desiredNumSolutions, write, prnt, outputFile="cbe4q4.csv"):
	print("\n\nQuestion 4 (or 5):\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("A,B,C,S,S2")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("A,B,C,S,S2\n")
	while numSols < desiredNumSolutions:
		# Get roots of random derivative.
		roots = []
		for i in range(random.randint(3, 4)):
			newRoot = randomCoeff()
			# if not newRoot in roots:
			roots.append(newRoot)
		roots.sort()
		# Bounds always contain roots.
		bounds = [roots[0] - 1, roots[len(roots) - 1] + 1]
		fPrime = numpy.poly1d(roots, True)
		f = numpIntCoeff(fPrime)
		# Check for stuff like \frac{6004799503160661}{18014398509481984} and the like...
		meanCoeff = False
		for c in f:
			if not isNiceRational(c, 15):
				meanCoeff = True
				break
		if meanCoeff:
			continue
		A = numTex(f)
		if A in solhashs:
			continue
		B = latex(bounds[0]) + " \\leq x \\leq " + latex(bounds[1])
		isMax = bool(random.getrandbits(1))
		if isMax:
			C = "maximum"
		else:
			C = "minimum"
		# Get solutions
		points = roots.copy()
		points.insert(0, bounds[0])
		points.append(bounds[1])
		bestPoint = points[0]
		bestYValue = numEval(f, bestPoint)
		ys = [bestYValue]
		for i in range(1, len(points)):
			point = points[i]
			yValue = numEval(f, point)
			ys.append(yValue)
			if isMax and (yValue > bestYValue):
				bestYValue = yValue
				bestPoint = point
			elif (not isMax) and (yValue < bestYValue):
				bestYValue = yValue
				bestPoint = point
			else:
				pass # DO nothing
		# Test
		if isMax and max(ys) != bestYValue:
			print("[ERROR]: Max was found incorrectly. Should have got: " + str(max(ys)) + " but got " + str(bestYValue))
		elif (not isMax) and min(ys) != bestYValue:
			print("[ERROR]: Min was found incorrectly")
		S = latex(bestYValue)
		S2 = latex(bestPoint)
		numSols += 1
		if prnt:
			print(A + ',' + B + ',' + C + ',' + S + ',' + S2)
		if write:
			csvfile.write(A + ',' + B + ',' + C + ',' + S + ',' + S2 + '\n')
	if write:
		csvfile.close()
			
# Q5 is the same as Q4
'''
Generates a random polynomial and locates the number of relative maxima in minima.

if the double derivative evaluated at xVal is positive, then it is a min.

else if it's negative, then it's a max.

else (if it's zero) then it's an inflection point.

(CSV) Parameters:
y: the function
mins: the number of mins
maxs: the number of maxes
tinfs: the *total* number of inflection points
'''
def q6(desiredNumSolutions, write, prnt, outputFile="cbe4q6.csv"):
	print("\n\nQuestion 6:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("y,mins,maxs,tinfs")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("y,mins,maxs,tinfs\n")
	while numSols < desiredNumSolutions:
		# Get a single solution
		f = randomPolynomial2(random.randint(2, 5), 9, False)
		y = latex(f)
		if y in solhashs:
			continue
		solhashs[y] = True
		# Get derivatives
		fPrime = diff(f)
		fDoublePrime = diff(fPrime)
		criticalPoints = sympy.roots(fPrime)
		mins = 0
		maxs = 0
		tinfs = 0 # Handle imaginary roots
		ipointCandidates = sympy.roots(fDoublePrime)
		for ip in ipointCandidates:
			if ip.is_real:
				tinfs += 1
		# If you wanted, we could rewrite this so that it asks them *for* the
		# critical points.
		for point in criticalPoints:
			# Ignore imaginary or complex roots
			if not point.is_real:
				continue
			ddVal = fDoublePrime.subs(x, point)
			# print("[INFO] ddVal = " + str(ddVal) + " \nand point = " + str(point))
			if ddVal > 0:
				# It is a minimum
				mins += 1
			elif ddVal < 0:
				# It is a maximum
				maxs += 1
			else:
				# It is an inflection point and we must do epsilon analysis
				dd1 = fPrime.subs(x, point - epsilon)
				dd2 = fPrime.subs(x, point + epsilon)
				if dd1 > 0 and dd2 < 0:
					# Positive to negative derivative = max
					maxes += 1
				elif dd1 < 0 and dd2 > 0:
					# Negative to positive derivative = min
					mins += 1
				elif dd1 == dd2:
					print("[ERROR]: epsilon analysis failed")
				# Else it is neither
		if mins == 0 and maxs == 0:
			# SKip this solution, since we want one where there are at least one min or max
			continue
		numSols += 1
		if prnt:
			print(y + ',' + str(mins) + ',' + str(maxs) + ',' + str(tinfs))
		if write:
			csvfile.write(y + ',' + str(mins) + ',' + str(maxs) + ',' + str(tinfs) + '\n')
	if write:
		csvfile.close()
			
'''
Generates a function with only one inflection point, asks where that inflection point is

CSV Params:
f: the function
ipoint: the x value of the inflection point
'''
def q7(desiredNumSolutions, write, prnt, outputFile="cbe4q7.csv"):
	print("\n\nQuestion 7:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,ipoint")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,ipoint\n")
	while numSols < desiredNumSolutions:
		f, ipoint = oneInflection() # See cbefunctions.py for implementation of oneInflection()
		k = latex(f)
		if k in solhashs:
			continue
		solhashs[k] = True
		numSols += 1
		if prnt:
			print(k + ',' + str(ipoint))
		if write:
			csvfile.write(k + ',' + str(ipoint) + '\n')
	if write:
		csvfile.close()

'''
Asks students to determine the interval where the function is concave up/down
f: the function
u: up/down
iv: the interval (solution)
'''
def q8(desiredNumSolutions, write, prnt, outputFile="cbe4q8.csv"):
	print("\n\nQuestion 8:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,u,iv1,iv2")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,u,iv1,iv2\n")
	while numSols < desiredNumSolutions:
		b1 = randomCoeff()
		b2 = randomCoeff()
		if b1 > b2:
			b1, b2 = b2, b1
		# b1 is now lower bound, b2 is upper bound.
		k = str(b1) + '->' + str(b2)
		if k in solhashs:
			continue
		solhashs[k] = True
		numSols += 1
		iv = latex(b1) + "," + latex(b2)
		# Generate function
		c = randomCoeff()
		# If leading coeff on 2nd derivative is negative, this will be a concave up interval
		if c < 0:
			u = "up"
		else:
			u = "down"
		fDoublePrime = c*(x - b1)*(x - b1)
		fPrime = integrate(fDoublePrime) + randomCoeffOrZero()
		f = integrate(fPrime) + randomCoeff()
		fl = latex(f)
		if prnt:
			print(fl + ',' + u + ',' + iv)
		if write:
			csvfile.write(fl + ',' + u + ',' + iv + '\n')
	if write:
		csvfile.close()
	
if __name__=='__main__':
	numSols = int(input("How many solutions do you want for each question: "))
	# q4Optimized(numSols, False, True)
	# q4Optimized(numSols, False, True, "cbe4q5.csv") # Q5 is the same as Q4
	q6(numSols, False, True)
	# q7(numSols, False, True)
	# q8(numSols, False, True)
