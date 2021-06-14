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
import numpy
import math
#from sympy
from sympy.abc import x # This makes it so x is always defined symbolically
from sympy import latex, exp, diff, pi, sqrt, cbrt, integrate, real_root
from sympy import solve
from sympy import sin, cos
#from math import pi

from sympy.geometry.util import idiff # implicit differentiation

from sympy import nan, ln
from sympy import atan, acos, asin

from cbefunctions import *

'''
Helper function for q4
Function types:
0: axcos(bx)
1: axsin(bx)
2: a + cos(bx)
3: a + sin(bx)
4: ax^2
'''
def q4RandomFunction():
	ftype = random.randint(0, 4)
	a = randomCoeff(6, allowFracs=False)
	b = randomCoeff(6, allowFracs=False)
	if ftype == 0:
		return a * x * cos(b * x)
	elif ftype == 1:
		return a * x * sin(b * x)
	elif ftype == 2:
		return a + cos(b * x)
	elif ftype == 3:
		return a + sin(b * x)
	elif ftype == 4:
		return a * (x ** 2)
	else:
		raise ValueError("Issue with ftype")
	
'''
Generates two polynomials who share a single root, a.

Asks the students to evaluate the limit of the quotient of
those polynomials approaching that root, which can be evaluated
using L'Hopital's rule (using sympy's diff function here)

CSV Parameters:
f: the numerator
g: the denominator
r: the shared root
l: lim_{x -> r} f / g
'''
def q1(desiredNumSolutions, write, prnt, outputFile="cbe5q1.csv"):
	print("\n\nQuestion 1:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,g,r,l")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,g,r,l\n")
	while numSols < desiredNumSolutions:
		usedroots = {}
		fRoots = []
		gRoots = []
		# Get roots for polynomials
		for i in range(random.randint(2, 3)):
			fRoots.append(getUnique2(usedroots))
			gRoots.append(getUnique2(usedroots))
		if bool(random.getrandbits(1)):
			commonRoot = 0
		else:
			commonRoot = getUnique(usedroots)
		# Create common root issue
		fRoots.append(commonRoot)
		gRoots.append(commonRoot)
		flist = list(polyFromRoots(fRoots))
		glist = list(polyFromRoots(gRoots))
		# Get common denominator for algebraic simplicity
		fcd = commonDenominator(flist)
		ggcd = commonDenominator(glist) # ggcd so as not to clash with sympy.gcd
		for i in range(len(flist)):
			flist[i] *= fcd
		for i in range(len(glist)):
			glist[i] *= ggcd
		f = arrToSymb(flist)
		g = arrToSymb(glist)
		fl = latex(f)
		gl = latex(g)
		k = fl + ':' + gl
		if k in solhashs:
			continue
		solhashs[k] = True
		fPrime = diff(f)
		gPrime = diff(g)
		l = sympy.Rational(fPrime.subs(x, commonRoot) / gPrime.subs(x, commonRoot)) # If error, exception will be thrown here.
		ltex = latex(l)
		if len(ltex) > 12:
			continue
		numSols += 1
		if prnt:
			print(fl + ',' + gl + ',' + latex(commonRoot) + ',' + ltex)
		if write:
			csvfile.write(fl + ',' + gl + ',' + latex(commonRoot) + ',' + ltex + '\n')
	if write:
		csvfile.close()
'''
Generates questions of the form

lim f / g
Where f = a + (sin or cos)(b x) and g = cx
Find the limit as x -> 0. Uses l'hopital's rule.

CSV parameters:
f : latex of f
g : latex of g
l : limit
'''
def q2(desiredNumSolutions, write, prnt, outputFile="cbe5q2.csv"):
	print("\n\nQuestion 2:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,g,l")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,g,l\n")
	while numSols < desiredNumSolutions:
		# Get a single random solution.
		a = randomCoeff(5, allowFracs=False)
		b = randomCoeff(5, allowFracs=False)
		c = randomCoeff(5, allowFracs=False)
		d = randomCoeff(5, allowFracs=False)
		if bool(random.getrandbits(1)):
			f = a + b * sin(c * x)
		else:
			f = a + b * cos(c * x)
		g = d * x
		fx = latex(f)
		gx = latex(g)
		k = fx + gx
		if k in solhashs:
			continue
		# We have a solution
		solhashs[k] = True
		l = latex(diff(f).subs(x, 0) / d)
		numSols += 1
		if prnt:
			print(fx + ',' + gx + ',' + l)
		if write:
			csvfile.write(fx + ',' + gx + ',' + l + '\n')
		
	if write:
		csvfile.close()
		
'''
Question 3

Generates two polynomials (max quadratic), both with a root of 1 or -1
The answer is the limit of the quotient of the two as we approach a common root.

This one doesn't care if multiple roots are shared

TODO: the original had some really easy limits. This one requires at least some factoring
or L'Hoptial's. Ask Greg if he wants the easy ones, too.
'''

def q3(desiredNumSolutions, write, prnt, outputFile="cbe5q3.csv"):
	print("\n\nQuestion 3:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,g,r,l")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,g,r,l\n")
	while numSols < desiredNumSolutions:
		if bool(random.getrandbits(1)):
			r = 1
		else:
			r = -1
		fRoots = [r]
		gRoots = [r]
		# Get roots for polynomials
		if bool(random.getrandbits(1)):
			fRoots.append(randomCoeff(6, allowFracs=False))
			
		if bool(random.getrandbits(1)):
			gRoots.append(randomCoeff(6, allowFracs=False))
		
		f = arrToSymb(polyFromRoots(fRoots, True))
		g = arrToSymb(polyFromRoots(gRoots, True))
		fx = latex(f)
		gx = latex(g)
		k = fx + gx
		if k in solhashs:
			continue
		# We have a solution
		solhashs[k] = True
		numSols += 1
		l = diff(f).subs(x, r) / diff(g).subs(x, r) # exception will be thrown if error
		ltex = latex(l)
		if prnt:
			print(fx + ',' + gx + ',' + latex(r) + ',' + ltex)
		if write:
			csvfile.write(fx + ',' + gx + ',' + latex(r) + ',' + ltex + '\n')
	if write:
		csvfile.close()
		
'''
Question 4
'''
def q4(desiredNumSolutions, write, prnt, outputFile="cbe5q4.csv"):
	print("\n\nQuestion 4:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,g,l")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,g,l\n")
	while numSols < desiredNumSolutions:
		# Get a single random solution.
		f = q4RandomFunction()
		g = q4RandomFunction()
		fx = latex(f)
		gx = latex(g)
		k = fx + gx
		if k in solhashs:
			continue
		# We have a solution
		solhashs[k] = True
		lnum = diff(f).subs(x, 0) 
		lden = (diff(g).subs(x, 0))
		if lden == 0:
			continue
		lVal = lnum / lden
		#if math.isnan(lVal):
			#continue
		l = latex(lVal)
		numSols += 1
		if prnt:
			print(fx + ',' + gx + ',' + l)
		if write:
			csvfile.write(fx + ',' + gx + ',' + l + '\n')
		
	if write:
		csvfile.close()

'''
Question 5:

(ax + b)^cx OR (ax + b)^c/x

c is allowed fractional. a, b, are not.

Solution lim (ax + b)^cx = e^(lim a / c)

Solution limit as we approach 0 from the right:
L'Hopital's rule

l = lim f^g
ln(l) = ln(lim(f^g))
ln(l) = lim gln(f)
l = e^lim(gln(f))

if g = c / x
	l = e^\infty = \infty
else if g = c x
	l = e^0 = 1
'''
def q5(desiredNumSolutions, write, prnt, outputFile="cbe5q5.csv"):
	print("\n\nQuestion 4:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,g,l")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,g,l\n")
	while numSols < desiredNumSolutions:
		# Generate random solution
		a = randomCoeff(5, False)
		b = randomCoeff(5, False)
		c = randomCoeff(5, True)
		k = str(a) + str(b) + str(c)
		# Skip this i
		if k in solhashs:
			continue
		solhashs[k] = True
		f = latex(a * x  + b)
		if bool(random.getrandbits(1)):
			g = latex(c / x)
			l = '\infty'
		else:
			g = latex(c * x)
			l = '1'
		numSols += 1
		if prnt:
			print(f + ',' + g + ',' + l)
		if write:
			csvfile.write(f + ',' + g + ',' + l + '\n')
		
	if write:
		csvfile.close()
		
'''
Generates a function of the form 
f(x) = u(x)v(x) and asks the user to find
int(f(x)) + C
'''
def q6(desiredNumSolutions, write, prnt, outputFile="cbe5q6.csv"):
	print("\n\nQuestion 6:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,g,i")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,g,i\n")
	while numSols < desiredNumSolutions:
		# Get a single random solution.
		f = randomPolynomial2(random.randint(1, 2), 5, False, False)
		g = randomPolynomial2(random.randint(1, 2), 5, False, False)
		fx = latex(f)
		gx = latex(g)
		k = fx + gx
		if k in solhashs:
			continue
		# We have a solution
		solhashs[k] = True
		iVal = integrate(f*g, x)
		i = latex(iVal) + " + C"
		numSols += 1
		if prnt:
			print(fx + ',' + gx + ',' + i)
		if write:
			csvfile.write(fx + ',' + gx + ',' + i + '\n')
		
	if write:
		csvfile.close()
		
'''
Generates a function of the form 
f(x) = u(x)v(x) and asks the user to find
int(f(x)) + C
The only difference between this one and the last one is g(x) is a radical
'''
def q7(desiredNumSolutions, write, prnt, outputFile="cbe5q7.csv"):
	print("\n\nQuestion 7:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,i")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,i\n")
	while numSols < desiredNumSolutions:
		if bool(random.getrandbits(1)):
			exp = 1
		else:
			exp = -1
		# Get a single random solution.
		f = randomCoeff(9, False) * (x ** exp)
		g = sympy.root(x ** random.randint(1, 2), random.randint(2, 4))
		fx = latex(f * g)
		#gx = latex(g)
		k = fx
		if k in solhashs:
			continue
		# We have a solution
		solhashs[k] = True
		iVal = integrate(f*g, x)
		i = latex(iVal) + " + C"
		numSols += 1
		if prnt:
			print(fx + ','  + i)
		if write:
			csvfile.write(fx + ',' + i + '\n')
		
	if write:
		csvfile.close()
'''
Question 8: Same as question 7 but we allow some entropy in the functions
'''
def q8(desiredNumSolutions, write, prnt, outputFile="cbe5q8.csv"):
	print("\n\nQuestion 8:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,i")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,i\n")
	while numSols < desiredNumSolutions:
		# Get a single random solution.
		[f, ftype] = randomSymbolic(0, 6, 4, True)
		if ftype == 0:
			continue
		#gx = latex(g)
		k = latex(f)
		if k in solhashs:
			continue
		k = k.replace("log", "ln")
		# We have a solution
		solhashs[k] = True
		iVal = integrate(f, x)
		i = latex(iVal).replace("log", "ln") + " + C"
		numSols += 1
		if prnt:
			print(k + ','  + i)
		if write:
			csvfile.write(k + ',' + i + '\n')
		# print(numSols)
	if write:
		csvfile.close()
		
'''
Question 9: initial value problem. The following CSV columns are generated:

fpp: f''(x)
fpz: f'(0)
fz: f(0)
f: f(x)
'''
def q9(desiredNumSolutions, write, prnt, outputFile="cbe5q9.csv"):
	print("\n\nQuestion 9:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("fpp,fpz,fz,f")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("fpp,fpz,fz,f\n")
	while numSols < desiredNumSolutions:
		fpp = randomPolynomial2(random.randint(0, 1), allowFracs=False)
		fppx = latex(fpp)
		if fppx in solhashs:
			continue
		solhashs[fppx] = True
		numSols += 1
		# Get the solution for our initial value problem with these initial conditions
		fpz = random.randint(-9, 9)
		fz = random.randint(-9, 9)
		# Integrate twice and include constants of integration c1 and c2, which are determined by initial conditions
		fp = integrate(fpp, x)
		# If f'(0) = [What we got for f'(0)] + C1, then C1 = f'(0) = [What we got for f'(0)]
		c1 = fpz - fp.subs(x, 0)
		fp += c1
		# Second integration
		f = integrate(fp, x)
		# Same deal here with the constants of integration
		c2 = fz - f.subs(x, 0)
		f += c2
		fx = latex(f)
		if prnt:
			print(fppx + ',' + str(fpz) + ',' + str(fz)  + ',' + fx)
		if write:
			csvfile.write(fppx + ',' + str(fpz) + ',' + str(fz)  + ',' + fx + '\n')
	if write:
		csvfile.close()
		
'''
Q10 is exactly like q9 except f''(x) = asin(x) + bcos(x)

fpp: f''(x)
fpz: f'(0)
fz: f(0)
f: f(x)
'''
def q10(desiredNumSolutions, write, prnt, outputFile="cbe5q10.csv"):
	print("\n\nQuestion 10:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("fpp,fpz,fz,f")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("fpp,fpz,fz,f\n")
	while numSols < desiredNumSolutions:
		a = randomCoeff(5, False)
		b = randomCoeff(5, False)
		fpp = a * sin(x) + b * cos(x)
		fppx = latex(fpp)
		if fppx in solhashs:
			continue
		solhashs[fppx] = True
		numSols += 1
		# Get the solution for our initial value problem with these initial conditions
		fpz = random.randint(-9, 9)
		fz = random.randint(-9, 9)
		# Integrate twice and include constants of integration c1 and c2, which are determined by initial conditions
		fp = integrate(fpp, x)
		# If f'(0) = [What we got for f'(0)] + C1, then C1 = f'(0) = [What we got for f'(0)]
		c1 = fpz - fp.subs(x, 0)
		fp += c1
		# Second integration
		f = integrate(fp, x)
		# Same deal here with the constants of integration
		c2 = fz - f.subs(x, 0)
		f += c2
		fx = latex(f)
		if prnt:
			print(fppx + ',' + str(fpz) + ',' + str(fz)  + ',' + fx)
		if write:
			csvfile.write(fppx + ',' + str(fpz) + ',' + str(fz)  + ',' + fx + '\n')
	if write:
		csvfile.close()
if __name__=='__main__':
	numSols = int(input("How many solutions do you want for each question: "))
	# q1(numSols, False, True)
	# q2(numSols, False, True)
	# q3(numSols, False, True)
	# q4(numSols, False, True)
	# q5(numSols, False, True)
	# q6(numSols, False, True)
	# q7(numSols, False, True)
	# q8(numSols, False, True)
	# q9(numSols, False, True)
	q10(numSols, False, True)
