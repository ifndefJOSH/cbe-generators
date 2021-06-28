'''
Author: Josh Jeppson

Disclaimer: if you're from Dr. Wheeler's Math 1210 class and you've come to the code thinking that you can
get solutions, you can't. They're automatically generated. That's the point of these scripts. Plus, because
of heavy use of the sympy and numpy libraries, you'll have to understand how the math works to even really
read the code. Too badddd.....no way for you to cheat without actually understanding the math in the first 
place, which is the point of the CBEs anyway. :/
'''

import random
import csv
import sympy
#from sympy
from sympy.abc import x # This makes it so x is always defined symbolically
from sympy import latex, exp, diff, pi, sqrt, cbrt
#from math import pi

from sympy.geometry.util import idiff # implicit differentiation

from sympy import nan, ln
from sympy import atan, acos, asin

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
def q1(desiredNumSolutions, write, prnt, outputFile="cbe3q1.csv"):
	print("\n\nQuestion 1:\n")
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
			htype = 0
			gtype = 0
			# Yes its a lot of "or"s. Too bad.
			while h == 0 or g == 0 or h == g or htype == 3 or htype == 4 or gtype == 3 or gtype == 4:
				[h, htype] = randomSymbolic(0, 7, 1, True)
				[g, gtype] = randomSymbolic(0, 7, 1, True)
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
			S = fPrime.subs(x, B)
			if S.is_infinite or S == nan:
				#print("Skipping infinite solution")
				continue
			numSols += 1
			if prnt:
				print(k + ',' + latex(B) + ',' + latex(S))
			if write:
				csvfile.write(k + ',' + latex(B) + ',' + latex(S) + '\n')
	if write:
		csvfile.close()
				
def q1Symbolic(desiredNumSolutions, write, prnt, outputFile="cbe3q1s.csv"):
	print("\n\nQuestion 1:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("A,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("A,S\n")
	while numSols < desiredNumSolutions:
		# Get a single solution
		if bool(random.getrandbits(1)):
			h = 0
			g = 0
			htype = 0
			gtype = 0
			# Yes its a lot of "or"s. Too bad.
			while h == 0 or g == 0 or h == g or htype == 3 or htype == 4 or gtype == 3 or gtype == 4:
				[h, htype] = randomSymbolic(0, 7, 1, True)
				[g, gtype] = randomSymbolic(0, 7, 1, True)
			f = exp(h * g)
			#B = random.randint(0, 9)
		else:
			gtype = 0
			g = 0
			while g == 0 or gtype == 3 or gtype == 4:
				[g, gtype] = randomSymbolic(0, 7, 1, True)
			a = random.randint(1, 9)
			#B = pi * random.randint(0, 9) / random.randint(1, 9)
			if bool(random.getrandbits(1)):
				f = exp(g) * sympy.cos(a * x)
			else:
				f = exp(g) * sympy.sin(a * x)
				
		# f(x) is now defined
		k = latex(f).replace("log", "ln")
		if not k in solhashs:
			solhashs[k] = True
			fPrime = diff(f)
			S = fPrime
			if S.is_infinite or S == nan:
				#print("Skipping infinite solution")
				continue
			numSols += 1
			if prnt:
				print(k + ',' + latex(S).replace("log", "ln")) # In sympy (unlike in written math) log is ln, not log10
			if write:
				csvfile.write(k + ',' + latex(S).replace("log", "ln") + '\n')
	if write:
		csvfile.close()
		
def q2RandomFunction(c=1):
	fType = random.randint(1, 3)
	if fType == 1:
		return [(c * x), fType]
	elif fType == 2:
		return [exp(c * x), fType]
	elif fType == 3:
		return [sqrt(c * x), fType]
	else:
		raise ValueError("Something went wrong in q2RandomFunction()")
'''
Question 2:

f(x) = ln(h(x) / g(x))

Solution = f'(x) 

This one is still generating some rather hairy, albeit correct solutions.
'''
def q2Symbolic(desiredNumSolutions, write, prnt, outputFile="cbe3q2s.csv"):
	print("\n\nQuestion 2:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("A,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("A,S\n")
	while numSols < desiredNumSolutions:
		[h, htype, g, gtype] = [0, 0, 0, 0] 
		while htype == gtype or ln(h / g) == 0:
			[h, htype] = q2RandomFunction() #randomSymbolic(0, 6, 3, True, 3)
			[g, gtype] = q2RandomFunction() # randomSymbolic(0, 6, 3, True, 3)
			#if htype != 
			if bool(random.getrandbits(1)):
				h += random.randint(1, 3)
			else:
				h -= random.randint(1, 3)
			if bool(random.getrandbits(1)):
				g += random.randint(1, 3)
			else: 
				g -= random.randint(1, 3)
				
		# Now we have something we can use.
		f = ln(h / g) 
		k = latex(f).replace("log", "ln")
		if not k in solhashs:
			solhashs[k] = True
			fPrime = diff(f)
			if fPrime.is_infinite:
				continue
			S = latex(fPrime).replace("log", "ln")
			numSols += 1
			if prnt:
				print(k + ',' + S)
			if write:
				csvfile.write(k + ',' + S + '\n')
	if write:
		csvfile.close()
'''
Question 3

Chain rule. Either

f(x) = sqrt(randomPolynomial)
 OR
f(x) = cuberoot(randomPolynomial)

Solution: derivative
'''
def q3Symbolic(desiredNumSolutions, write, prnt, outputFile="cbe3q3s.csv"):
	print("\n\nQuestion 3:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("A,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("A,S\n")
	while numSols < desiredNumSolutions:
		h = randomSymbolic(0, 0, 3) + random.randint(1, 5)
		if bool(random.getrandbits(1)):
			f = sqrt(h)
		else:
			f = cbrt(h)
		k = latex(f)
		if not k in solhashs:
			solhashs[k] = True
			fPrime = diff(f)
			if fPrime.is_infinite:
				continue
			S = latex(fPrime)
			numSols += 1
			if prnt:
				print(k + ',' + S)
			if write:
				csvfile.write(k + ',' + S + '\n')
	if write:
		csvfile.close()
'''
Question 4: Logarithmic Differentiation

Either

t^(randomPolynomial)

Or randomPolynomial^(at)

Find the derivative
'''
def q4Symbolic(desiredNumSolutions, write, prnt, outputFile="cbe3q4s.csv"):
	print("\n\nQuestion 4:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("A,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("A,S\n")
	while numSols < desiredNumSolutions:
		if bool(random.getrandbits(1)):
			f = (randomSymbolic(0, 0, 2) + random.randint(1, 5)) ** (random.randint(1, 3) * x)
		else:
			f = x ** randomSymbolic(0, 0, 2)
		k = latex(f.subs(x, t))
		if not k in solhashs:
			solhashs[k] = True
			fPrime = diff(f)
			if fPrime.is_infinite:
				continue
			S = latex(fPrime.subs(x, t))
			S= S.replace("log", "ln")
			numSols += 1
			if prnt:
				print(k + ',' + S)
			if write:
				csvfile.write(k + ',' + S + '\n')
	if write:
		csvfile.close()
	
'''
Question 5:

Question is of the form:

v(x) = A trig^{-1}(f(x))

Where
f(x) is a random function. The solution is the derivative.
'''
def q5Symbolic(desiredNumSolutions, write, prnt, outputFile="cbe3q5s.csv"):
	print("\n\nQuestion 5:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("A,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("A,S\n")
	while numSols < desiredNumSolutions:
		f = randomSymbolic(0, 2, 3, False) * randomCoeff() # To give us some fractional coefficients
		A = randomCoeff(20)
		# Select a random type of trig function
		trigType = random.randint(1, 3) # 1 - 3
		if trigType == 1:
			v = A*atan(f)
		elif trigType == 2:
			v = A*acos(f)
		else:
			v = A*asin(f)
		v = v.subs(x, t)
		k = latex(v)
		k = k.replace("\\operatorname{atan}", "\\tan^{-1}")
		k = k.replace("\\operatorname{acos}", "\\cos^{-1}")
		k = k.replace("\\operatorname{asin}", "\\sin^{-1}")
		if not k in solhashs:
			solhashs[k] = True
			vPrime = diff(v)
			if vPrime.is_infinite:
				continue
			S = latex(vPrime.subs(x, t))
			S = S.replace("\\operatorname{atan}", "\\tan^{-1}")
			S = S.replace("\\operatorname{acos}", "\\cos^{-1}")
			S = S.replace("\\operatorname{asin}", "\\sin^{-1}")
			numSols += 1
			if prnt:
				print(k + ',' + S)
			if write:
				csvfile.write(k + ',' + S + '\n')
	if write:
		csvfile.close()
			
'''
Question 6:

Form: find the slope of the tangent line at a specific point using implicit differentiation.

This just uses sympy's idiff function

CSV Parameters:
A: f(x, y) == 0
x = value of x
y = value of y
S: dy / dx at (x,y)

For some reason (probably idiff) this one takes a while to run
'''
def q6Symbolic(desiredNumSolutions, write, prnt, outputFile="cbe3q6s.csv"):
	print("\n\nQuestion 5:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("A,x,y,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("A,x,y,S\n")
	while numSols < desiredNumSolutions:
		# Get random coefficients
		a = randomCoeffOrZero()
		b = randomCoeff()
		c = randomCoeff()
		d = randomCoeff()
		e = randomCoeffOrZero()
		g = randomCoeff()
		# f(x, y) = 0 = ax^3 + bx^2y + cxy^2 + dxy + ey^3 + g
		# For 
		f = a * (x ** 3) + b * (x ** 2) * y + c * x * (y ** 2) + d * x * y + e * (y ** 3) + g
		dy_dx = idiff(f, y, x) #.simplify()
		k = latex(f)
		if not k in solhashs:
			solhashs[k] = True
			if dy_dx.is_infinite:
				continue # Skip oo solution
			# Get a random x, y
			xVal = randomCoeff()
			yVal = randomCoeff()
			slope = dy_dx.subs(x, xVal).subs(y, yVal)
			S = latex(xVal) + "," + latex(yVal) + "," + latex(slope)
			numSols += 1
			if prnt:
				print(k + ',' + S)
			if write:
				csvfile.write(k + ',' + S + '\n')
	if write:
		csvfile.close()
if __name__=='__main__':
	numSols = int(input("How many solutions do you want for each question: "))
	# q1(numSols, False, True)
	# q1Symbolic(numSols, False, True)
	q2Symbolic(numSols, False, True)
	# q3Symbolic(numSols, False, True)
	# q4Symbolic(numSols, False, True)
	# q5Symbolic(numSols, False, True)
	#q6Symbolic(numSols, False, True)
