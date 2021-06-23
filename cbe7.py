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

from cbefunctions import *


def q1RandomFunction():
	return random.randint(1, 5) * (x ** 2) + random.randint(1, 5)

'''
Question 1
f: function
s = integrate(f, x) from 0 to 1
'''
def q1(desiredNumSolutions, write, prnt, outputFile="cbe7q1.csv"):
	#x = sympy.Symbol('x', real=True)
	print("\n\nQuestion 1:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,S\n")
	while numSols < desiredNumSolutions:
		f = q1RandomFunction()
		f = f ** random.randint(2, 5)
		f *= random.randint(1, 15) * x
		fTex = latex(f)
		#k = fTex 
		if fTex in solhashs:
			continue
		solhashs[fTex] = True
		F = integrate(f, x)
		s = F.subs(x, 1) - F.subs(x, 0)
		#if not s.is_real:
			#print("Solution is not real. Skipping")
			#continue
		sTex = latex(s)
		sTex = sTex.replace("log", "ln")
		numSols += 1
		if prnt:
			print(fTex + ',' + sTex)
		if write:
			csvfile.write(fTex + ',' + sTex + '\n')
	if write:
		csvfile.close()
		
def q2RandomFunction(c=1):
	fType = random.randint(0, 3)
	if fType == 0:
		return [ln(c * x), 1 / (x), fType]
	elif fType == 1:
		return [1 / (c * x), -1 / (c * x ** 2), fType]
	elif fType == 2:
		return [exp(c * x), c * exp(c * x), fType]
	elif fType == 3:
		return [sqrt(c * x), -c / (2 * sqrt(x)), fType]
	else:
		raise ValueError("Something went wrong in q2RandomFunction()")
	
def q2RandomCoeffs(fType):
	#print(fType, "is fType")
	if fType == 0:
		return [1, exp(random.randint(1, 4) / Rational(2 ** random.randint(0, 2)) * pi)] #.sort()
	elif fType == 1:
		return [1 / pi, random.randint(1, 4) / (Rational(2 ** random.randint(0, 2)) * pi)] #.sort()
	elif fType == 2:
		return [ln(random.randint(1, 4) / Rational(2 ** random.randint(0, 2)) * pi), ln(random.randint(1, 4) / Rational(2 ** random.randint(0, 2)) * pi)] #.sort()
	elif fType == 3:
		return [(random.randint(1, 4) / Rational(2 ** random.randint(0, 2)) * pi) ** 2, (random.randint(1, 4) / Rational(2 ** random.randint(0, 2)) * pi) ** 2] #.sort()
	else:
		raise ValueError("fType is " + str(fType))
	
def q2(desiredNumSolutions, write, prnt, outputFile="cbe7q2.csv"):
	#x = sympy.Symbol('x', real=True) 
	print("\n\nQuestion 2: (Warning, this one takes a while...)\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,u,l,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,u,l,S\n")
	while numSols < desiredNumSolutions:
		g, dg, fType = q2RandomFunction()
		l = 0
		u = 0
		while l == u:
			l, u = q2RandomCoeffs(fType)
		if l > u: # Omit this if we want to really test them
			l, u = u, l
		f = randomCoeff() * sin(g) * dg
		fTex = latex(f).replace("log", "ln")
		uTex = latex(u).replace("log", "ln")
		lTex = latex(l).replace("log", "ln")
		k = fTex + uTex + lTex
		if k in solhashs:
			continue
		solhashs[k] = True
		# Average value = (F(u) - F(l)) / (u - l)
		F = integrate(f, x)
		s = F.subs(x, u) - F.subs(x, l)
		#print("Got s = " + str(s) + " with " + str(F.subs(x, u)) + " and " + str(F.subs(x, l)))
		#print("Additionally: F = " + str(F))
		# s /= (u - l)
		if s == sympy.nan or not s.is_real:
			continue
		sTex = latex(s)
		sTex = sTex.replace("log", "ln")
		numSols += 1
		if prnt:
			print(fTex + ',' + uTex + ',' + lTex + ',' + sTex)
		if write:
			csvfile.write(fTex + ',' + uTex + ',' + lTex + ',' + sTex + '\n')
	if write:
		csvfile.close()
		
def q3RandomFunction():
	fType = random.randint(0, 2)
	if fType == 0:
		return [sin(x), cos(x), fType]
	elif fType == 1:
		return [cos(x), sin(x), fType] # Can omit the - in -cos(x) for more difficulty
	elif fType == 2:
		return [exp(x), exp(x), fType]
	else:
		raise ValueError("Error in q3RandomFunction()")
	
def q3RandomCoeffs(fType):
	if fType == 0 or fType == 1:
		return [random.randint(1, 3) * pi / Rational(2 ** random.randint(0, 2)), random.randint(1, 3) * pi / Rational(2 ** random.randint(0, 2))]
	elif fType == 2:
		return [random.randint(1, 3), random.randint(1, 3)]
	else:
		raise ValueError("Error in q3RandomCoeffs()")
		
def q3(desiredNumSolutions, write, prnt, outputFile="cbe7q3.csv"):
	#x = sympy.Symbol('x', real=True) 
	print("\n\nQuestion 3:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,u,l,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,u,l,S\n")
	while numSols < desiredNumSolutions:
		g, dg, fType = q3RandomFunction()
		l = 0
		u = 0
		while l == u:
			l, u = q3RandomCoeffs(fType)
		if l > u: # Omit this if we want to really test them
			l, u = u, l
		f = randomCoeff() * dg / ((g + randomCoeff(9, False, True)) ** random.randint(1, 2))
		fTex = latex(f).replace("log", "ln")
		uTex = latex(u).replace("log", "ln")
		lTex = latex(l).replace("log", "ln")
		k = fTex + uTex + lTex
		if k in solhashs:
			continue
		solhashs[k] = True
		# Average value = (F(u) - F(l)) / (u - l)
		F = integrate(f, x)
		s = F.subs(x, u) - F.subs(x, l)
		#print("Got s = " + str(s) + " with " + str(F.subs(x, u)) + " and " + str(F.subs(x, l)))
		#print("Additionally: F = " + str(F))
		# s /= (u - l)
		if s == sympy.nan or not s.is_real:
			continue
		sTex = latex(s)
		sTex = sTex.replace("log", "ln")
		numSols += 1
		if prnt:
			print(fTex + ',' + uTex + ',' + lTex + ',' + sTex)
		if write:
			csvfile.write(fTex + ',' + uTex + ',' + lTex + ',' + sTex + '\n')
	if write:
		csvfile.close()

'''
Q4 has the same base function set as q3

LaTeX issue on this question...works, just isn't pretty
'''
def q4(desiredNumSolutions, write, prnt, outputFile="cbe7q4.csv"):
	#x = sympy.Symbol('x', real=True) 
	print("\n\nQuestion 4:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,u,l,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,u,l,S\n")
	while numSols < desiredNumSolutions:
		g, dg, fType = q3RandomFunction()
		l = 0
		u = 0
		g += randomCoeff(5, False, True)
		while l == u:
			l, u = q3RandomCoeffs(fType)
		if l > u: # Omit this if we want to really test them
			l, u = u, l
		f = randomCoeff() * dg 
		if bool(random.getrandbits(1)):
			f = f * sqrt(g)
		else:
			f /= sqrt(g)
		fTex = latex(f).replace("log", "ln")
		uTex = latex(u).replace("log", "ln")
		lTex = latex(l).replace("log", "ln")
		k = fTex + uTex + lTex
		if k in solhashs:
			continue
		solhashs[k] = True
		# Average value = (F(u) - F(l)) / (u - l)
		F = integrate(f, x)
		s = F.subs(x, u) - F.subs(x, l)
		#print("Got s = " + str(s) + " with " + str(F.subs(x, u)) + " and " + str(F.subs(x, l)))
		#print("Additionally: F = " + str(F))
		# s /= (u - l)
		if s == sympy.nan or not s.is_real:
			continue
		sTex = latex(s)
		sTex = sTex.replace("log", "ln")
		numSols += 1
		if prnt:
			print(fTex + ',' + uTex + ',' + lTex + ',' + sTex)
		if write:
			csvfile.write(fTex + ',' + uTex + ',' + lTex + ',' + sTex + '\n')
	if write:
		csvfile.close()

'''
Q5 also uses the same format as q3/q4, except it's IBP
'''
def q5(desiredNumSolutions, write, prnt, outputFile="cbe7q5.csv"):
	#x = sympy.Symbol('x', real=True) 
	print("\n\nQuestion 5:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,u,l,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,u,l,S\n")
	while numSols < desiredNumSolutions:
		g, dg, fType = q3RandomFunction()
		l = 0
		u = 0
		g # += randomCoeff(5, False, True)
		while l == u:
			l, u = q3RandomCoeffs(fType)
		if l > u: # Omit this if we want to really test them
			l, u = u, l
		f = randomCoeff() * x * g

		fTex = latex(f).replace("log", "ln")
		uTex = latex(u).replace("log", "ln")
		lTex = latex(l).replace("log", "ln")
		k = fTex + uTex + lTex
		if k in solhashs:
			continue
		solhashs[k] = True
		# Average value = (F(u) - F(l)) / (u - l)
		F = integrate(f, x)
		s = F.subs(x, u) - F.subs(x, l)
		#print("Got s = " + str(s) + " with " + str(F.subs(x, u)) + " and " + str(F.subs(x, l)))
		#print("Additionally: F = " + str(F))
		# s /= (u - l)
		if s == sympy.nan or not s.is_real:
			continue
		sTex = latex(s)
		sTex = sTex.replace("log", "ln")
		numSols += 1
		if prnt:
			print(fTex + ',' + uTex + ',' + lTex + ',' + sTex)
		if write:
			csvfile.write(fTex + ',' + uTex + ',' + lTex + ',' + sTex + '\n')
	if write:
		csvfile.close()
'''
Question 6 is symbolic integration
'''
def q6(desiredNumSolutions, write, prnt, outputFile="cbe7q6.csv"):
	x = sympy.Symbol('x', real=True) 
	print("\n\nQuestion 6:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,S\n")
	while numSols < desiredNumSolutions:
		#print("Loop iteration")
		f = randomCoeff(9) * (x ** random.randint(2, 6)) * ln(x)
		fTex = latex(f).replace("log", "ln")
		k = fTex
		if k in solhashs:
			continue
		solhashs[k] = True
		# Average value = (F(u) - F(l)) / (u - l)
		s = integrate(f, x)
		#s = F.subs(x, u) - F.subs(x, l)
		#print("Got s = " + str(s) + " with " + str(F.subs(x, u)) + " and " + str(F.subs(x, l)))
		#print("Additionally: F = " + str(F))
		# s /= (u - l)
		#print("Got a solution")
		#if s == sympy.nan or not s.is_real:
			#print("Solution is either NaN or imaginary", str(s))
			#continue
		sTex = latex(s) + " + C"
		sTex = sTex.replace("log", "ln")
		numSols += 1
		if prnt:
			print(fTex + ',' + sTex)
		if write:
			csvfile.write(fTex + ',' + sTex + '\n')
	if write:
		csvfile.close()
		
'''
Questions 7 and 8 are arc length

Arc length formula (differentials and pythagoras' theorem):

\int_S sqrt{(dy/dx) ^2 + (dx / dx)^2} dS

OR (in calc 1 terminology):

\int_xmin^xmax \sqrt{ f'(x) ^2 + 1} dx
'''

'''
Q7: Arc length of a line
'''
def q7(desiredNumSolutions, write, prnt, outputFile="cbe7q7.csv"):
	#x = sympy.Symbol('x', real=True) 
	print("\n\nQuestion 7:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,ux,uy,lx,ly,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,ux,uy,lx,ly,S\n")
	while numSols < desiredNumSolutions:
		#g, dg, fType = q3RandomFunction()
		l = 0
		u = 0
		while l == u:
			l = random.randint(-5, 5)
			u = random.randint(-4, 9)
		if l > u: # Omit this if we want to really test them
			l, u = u, l
		f = randomPolynomial2(1)

		fTex = latex(f)
		uTex = latex(u) + "," + latex(f.subs(x, u))
		lTex = latex(l) + "," + latex(f.subs(x, l))
		k = fTex + uTex + lTex
		if k in solhashs:
			continue
		solhashs[k] = True
		dF = diff(f, x)
		dS = sqrt(dF ** 2 + 1)
		# Average value = (F(u) - F(l)) / (u - l)
		F = integrate(dS, x)
		s = F.subs(x, u) - F.subs(x, l)
		#print("Got s = " + str(s) + " with " + str(F.subs(x, u)) + " and " + str(F.subs(x, l)))
		#print("Additionally: F = " + str(F))
		# s /= (u - l)
		if s == sympy.nan or not s.is_real:
			continue
		sTex = latex(s)
		sTex = sTex.replace("log", "ln")
		numSols += 1
		if prnt:
			print(fTex + ',' + uTex + ',' + lTex + ',' + sTex)
		if write:
			csvfile.write(fTex + ',' + uTex + ',' + lTex + ',' + sTex + '\n')
	if write:
		csvfile.close()
'''
Q8 Asks for symbolic equivalence
'''
def q8(desiredNumSolutions, write, prnt, outputFile="cbe7q8.csv"):
	#x = sympy.Symbol('x', real=True) 
	print("\n\nQuestion 8:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,ux,uy,lx,ly,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,ux,uy,lx,ly,S\n")
	while numSols < desiredNumSolutions:
		#g, dg, fType = q3RandomFunction()
		l = 0
		u = 0
		while l == u:
			l = random.randint(-5, 5)
			u = random.randint(-4, 9)
		if l > u: # Omit this if we want to really test them
			l, u = u, l
		f = q2RandomFunction(random.randint(1, 5))[0]

		fTex = latex(f)
		uTex = latex(u) + "," + latex(f.subs(x, u))
		lTex = latex(l) + "," + latex(f.subs(x, l))
		k = fTex + uTex + lTex
		if k in solhashs:
			continue
		solhashs[k] = True
		dF = diff(f, x)
		dS = sqrt(dF ** 2 + 1)

		sTex = "\\int_{" + latex(l) + "}^{" + latex(u) + "} " + latex(dS) + "dx"
		sTex = sTex.replace("log", "ln")
		numSols += 1
		if prnt:
			print(fTex + ',' + uTex + ',' + lTex + ',' + sTex)
		if write:
			csvfile.write(fTex + ',' + uTex + ',' + lTex + ',' + sTex + '\n')
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
	#q7(numSols, False, True)
	q8(numSols, False, True)
