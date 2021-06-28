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
from sympy.abc import x # This makes it so certain vars are always defined symbolically
from sympy import latex, exp, diff, pi, sqrt, cbrt, integrate, real_root
from sympy import solve
from sympy import sin, cos, tan, sec, csc, asin, acos, atan
#from math import pi
from sympy import Rational

from sympy.geometry.util import idiff # implicit differentiation

from sympy import nan, ln
from sympy import atan, acos, asin
from sympy import limit, oo

from cbefunctions import *
'''
Question 1:
f: the function
r: the value to find the limit as f ->
S: lim_{x -> r} f(x)
'''
def q1(desiredNumSolutions, write, prnt, outputFile="cbe1q1.csv"):
	print("\n\nQuestion 1:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,r,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,r,S\n")
	while numSols < desiredNumSolutions:
		# Generate two polynomials, one quadratic and one linear, that share a root
		sharedRoot = random.randint(-5,5)
		additionalRoot = random.randint(-5,5)
		if additionalRoot == sharedRoot:
			continue
		u = polyFromRoots([sharedRoot], False, True)
		v = polyFromRoots([sharedRoot, additionalRoot], False, True)
		# Doesn't matter the direction we approach from
		if bool(random.getrandbits(1)):
			side = '+'
		else:
			side = '-'
		# Randomize numerator or denominator
		if bool(random.getrandbits(1)):
			f = u / v
		else:
			f = v / u
		f *= randomCoeff()
		fTex = latex(f)
		if fTex in solhashs:
			continue
		solhashs[fTex] = True
		s = limit(f, x, sharedRoot)
		# Sanity check
		#if limit(f, x, sharedRoot, '+') != limit(f, x, sharedRoot, '-'):
			#print("Error")
		sTex = latex(s)
		sTex = sTex.replace("log", "ln")
		numSols += 1
		if prnt:
			print(fTex + ',' + latex(sharedRoot) + '^' + side + ',' + sTex)
		if write:
			csvfile.write(fTex + ',' + latex(sharedRoot) + '^' + side + ',' + sTex + '\n')
	if write:
		csvfile.close()

'''
Q2 is extremely similar in format to Q1
'''
def q2(desiredNumSolutions, write, prnt, outputFile="cbe1q2.csv"):
	print("\n\nQuestion 2:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,r,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,r,S\n")
	while numSols < desiredNumSolutions:
		# Generate two polynomials, one quadratic and one linear, that share a root
		keyRoot = random.randint(-10,10)
		krSq = keyRoot ** 2
		if keyRoot == 0:
			continue
		u = x - krSq
		v = sqrt(x) - keyRoot
		# Randomize numerator or denominator
		if bool(random.getrandbits(1)):
			f = u / v
		else:
			f = v / u
		f *= random.randint(1, 5) # so we can generate enough solutions
		fTex = latex(f)
		if fTex in solhashs:
			continue
		solhashs[fTex] = True
		s = limit(f, x, krSq, '+') # Yes I could generalize a solution form, but I'm lazy
		sTex = latex(s)
		sTex = sTex.replace("log", "ln")
		numSols += 1
		if prnt:
			print(fTex + ',' + latex(krSq) + ',' + sTex)
		if write:
			csvfile.write(fTex + ',' + latex(krSq) + ',' + sTex + '\n')
	if write:
		csvfile.close()

'''
Q3 is similar as well, except there is no common root. In this case, we randomize the direction we come from.
Therefore, limit is always + or - infinity
'''
def q3(desiredNumSolutions, write, prnt, outputFile="cbe1q3.csv"):
	print("\n\nQuestion 3:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,r,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,r,S\n")
	while numSols < desiredNumSolutions:
		r = random.randint(-10,10)
		r2 = random.randint(-10,10)
		r3 = random.randint(-10,10)
		if r == r2 or r == r3 or r2 == r3:
			continue
		d = polyFromRoots([r, r2], False, True)
		n = (x - r3)
		f = randomCoeff() * n / d
		if bool(random.getrandbits(1)):
			side = '+'
		else:
			side = '-'
		fTex = latex(f)
		if fTex in solhashs:
			continue
		solhashs[fTex] = True
		s = limit(f, x, r, side)
		sTex = latex(s)
		sTex = sTex.replace("log", "ln")
		numSols += 1
		if prnt:
			print(fTex + ',' + latex(r) + '^' + side + ',' + sTex)
		if write:
			csvfile.write(fTex + ',' + latex(r) + '^' + side + ',' + sTex + '\n')
	if write:
		csvfile.close()
		
def q4(desiredNumSolutions, write, prnt, outputFile="cbe1q4.csv"):
	print("\n\nQuestion 4:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,S\n")
	while numSols < desiredNumSolutions:
		v = randomPolynomial2(random.randint(1, 4), 9, False, True)
		if v == 0:
			continue
		u = randomPolynomial2(random.randint(1, 4), 9, True, True)
		f = u / v
		fTex = latex(f)
		if not "\\frac" in fTex:
			continue
		if fTex in solhashs:
			continue
		solhashs[fTex] = True
		s = limit(f, x, oo) # Limit f to infty. Why reinvent the wheel?
		numSols += 1
		sTex = latex(s)
		sTex = sTex.replace("log", "ln")
		numSols += 1
		if prnt:
			print(fTex + ',' + sTex)
		if write:
			csvfile.write(fTex + ',' + sTex + '\n')
	if write:
		csvfile.close()
		
def q5(desiredNumSolutions, write, prnt, outputFile="cbe1q5.csv"):
	print("\n\nQuestion 5:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,S\n")
	while numSols < desiredNumSolutions:
		a = random.randint(0, 2)
		b = random.randint(1, 5)
		c = random.randint(1, 5)
		d = random.randint(1, 5)
		p = random.randint(1, 2)
		if bool(random.getrandbits(1)):
			tr = sin(x)
		else:
			tr = cos(x)
		f = (a + b * tr) / (c * (x ** p) + d)
		fTex = latex(f)
		if fTex in solhashs:
			continue
		solhashs[fTex] = True
		s = 0 # Save some computation time over limit(f, x, oo) # Limit f to infty. Why reinvent the wheel?
		numSols += 1
		sTex = latex(s)
		sTex = sTex.replace("log", "ln")
		numSols += 1
		if prnt:
			print(fTex + ',' + sTex)
		if write:
			csvfile.write(fTex + ',' + sTex + '\n')
	if write:
		csvfile.close()
'''
This time, f is piecewise
'''
def q6(desiredNumSolutions, write, prnt, outputFile="cbe1q6.csv"):
	print("\n\nQuestion 6:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,r,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,r,S\n")
	while numSols < desiredNumSolutions:
		r = random.randint(-5,5)
		u = randomPolynomial2(random.randint(1, 2))
		v = randomPolynomial2(random.randint(1, 2))
		if bool(random.getrandbits(1)):
			v = abs(v)
		elif u == v:
			continue
		rTex = latex(r)
		fTex = "\\begin{cases}" + latex(u) + " & x < " + rTex + "\\\\"
		fTex += latex(v) + " & x > " + rTex
		if bool(random.getrandbits(1)):
			fTex += "\\\\" + str(random.randint(-5,5)) + " & x = " + rTex
		fTex += "\\end{cases}"
		if fTex in solhashs:
			continue
		solhashs[fTex] = True
		numSols += 1
		# Find s
		l1 = limit(u, x, r, '-')
		l2 = limit(v, x, r, '+')
		if l1 == l2:
			s = l1
			sTex = latex(s).replace("log", "ln")
		else:
			# Limit does not exist
			sTex = "None"
		if prnt:
			print(fTex + ',' + rTex + ',' + sTex)
		if write:
			csvfile.write(fTex + ',' + rTex + ',' + sTex + '\n')
	if write:
		csvfile.close()
		
def q7RandomFunction():
	a = random.randint(-5, 5)
	b = random.randint(-5, 5) * random.randint(0, 1)
	c = random.randint(-5, 5) * random.randint(0, 1)
	#d = random.randint(-5, 5)
	return a + b*cos(x) + c * sin(x)
'''
Just like q6 except the functions we generate are trig functions
'''
def q7(desiredNumSolutions, write, prnt, outputFile="cbe1q6.csv"):
	print("\n\nQuestion 6:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,r,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,r,S\n")
	while numSols < desiredNumSolutions:
		r = random.randint(-5,5) * pi / (2 ** random.randint(0, 2))
		u = q7RandomFunction()
		v = q7RandomFunction()
		if u == v:
			continue
		rTex = latex(r)
		fTex = "\\begin{cases}" + latex(u) + " & x < " + rTex + "\\\\"
		fTex += latex(v) + " & x > " + rTex
		if bool(random.getrandbits(1)):
			fTex += "\\\\" + str(random.randint(-5,5)) + " & x = " + rTex
		fTex += "\\end{cases}"
		if fTex in solhashs:
			continue
		solhashs[fTex] = True
		numSols += 1
		# Find s
		l1 = limit(u, x, r, '-')
		l2 = limit(v, x, r, '+')
		if l1 == l2:
			s = l1
			sTex = latex(s).replace("log", "ln")
		else:
			# Limit does not exist
			sTex = "None"
		if prnt:
			print(fTex + ',' + rTex + ',' + sTex)
		if write:
			csvfile.write(fTex + ',' + rTex + ',' + sTex + '\n')
	if write:
		csvfile.close()
if __name__=='__main__':
	numSols = int(input("How many solutions do you want for each question: "))
	#q1(numSols, False, True)
	#q2(numSols, False, True)
	#q3(numSols, False, True)
	#q4(numSols, False, True)
	#q5(numSols, False, True)
	#q6(numSols, False, True)
	q7(numSols, False, True)
