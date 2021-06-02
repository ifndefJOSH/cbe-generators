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
		for i in range(random.randint(2, 4)):
			fRoots.append(getUnique(usedroots))
			gRoots.append(getUnique(usedroots))
		commonRoot = getUnique(usedroots)
		fRoots.append(commonRoot)
		gRoots.append(commonRoot)
		f = arrToSymb(list(polyFromRoots(fRoots)))
		g = arrToSymb(list(polyFromRoots(gRoots)))
		fl = latex(f)
		gl = latex(g)
		k = fl + ':' + gl
		if k in solhashs:
			continue
		solhashs[k] = True
		numSols += 1
		fPrime = diff(f)
		gPrime = diff(g)
		l = sympy.Rational(fPrime.subs(x, commonRoot) / gPrime.subs(x, commonRoot)) # If error, exception will be thrown here.
		if prnt:
			print(fl + ',' + gl + ',' + latex(commonRoot) + ',' + latex(l))
		if write:
			csvfile.write(fl + ',' + gl + ',' + latex(commonRoot) + ',' + latex(l) + '\n')
	if write:
		csvfile.close()
		
		
if __name__=='__main__':
	numSols = int(input("How many solutions do you want for each question: "))
	q1(numSols, False, True)
