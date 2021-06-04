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
#from sympy
from sympy.abc import x # This makes it so x is always defined symbolically
from sympy import latex, exp, diff, pi, sqrt, cbrt, integrate
from sympy import solve
from sympy import sin, cos
#from math import pi

from sympy.geometry.util import idiff # implicit differentiation

from sympy import nan, ln
from sympy import atan, acos, asin

from cbefunctions import *

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
		fl = latex(f)
		gl = latex(g)
		if prnt:
			print(fl + ',' + gl + ',' + latex(r) + ',' + ltex)
		if write:
			csvfile.write(fl + ',' + gl + ',' + latex(r) + ',' + ltex + '\n')
	if write:
		csvfile.close()
if __name__=='__main__':
	numSols = int(input("How many solutions do you want for each question: "))
	# q1(numSols, False, True)
	# q2(numSols, False, True)
	q3(numSols, False, True)
