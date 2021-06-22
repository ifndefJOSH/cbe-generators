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

from sympy.geometry.util import idiff # implicit differentiation

from sympy import nan, ln
from sympy import atan, acos, asin

from cbefunctions import *



def q1RandomFunction():
	fType = random.randint(1, 5)
	c = randomCoeff()
	if fType == 1:
		return c * sin(x)
	elif fType == 2:
		return c * cos(x)
	elif fType == 3:
		return c * tan(x)
	elif fType == 4:
		return c * sec(x)
	elif fType == 5:
		return c * csc(x)
	elif fType == 6:
		return c * asin(x)
	elif fType == 7:
		return c * acos(x)
	elif fType == 8:
		return c * atan(x)
'''
Question 1
f: function
l: lower limit
u: upper limit
s = integrate(f, x) from l to u
'''
def q1(desiredNumSolutions, write, prnt, outputFile="cbe6q1.csv"):
	x = sympy.Symbol('x', real=True)
	print("\n\nQuestion 1:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,u,l,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,u,l,S\n")
	while numSols < desiredNumSolutions:
		l = randomCoeff(9, False, True)
		u = randomCoeff(9, False, True) * x
		f = q1RandomFunction()
		fTex = latex(f)
		uTex = latex(u)
		lTex = latex(l)
		k = fTex + uTex + lTex
		if k in solhashs:
			continue
		solhashs[k] = True
		F = integrate(f, x)
		s = F.subs(x, u) - F.subs(x, l)
		#if not s.is_real:
			#print("Solution is not real. Skipping")
			#continue
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
Determine the average value of a simple function over an interval
'''
def q3(desiredNumSolutions, write, prnt, outputFile="cbe6q3.csv"):
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
		l = randomCoeff(9, False, True)
		u = randomCoeff(9, False, True)
		if l > u:
			l, u = u, l # I love Python syntax
		elif l == u:
			continue
		f = randomSymbolic(0, 6) # Everything but ln()
		fTex = latex(f)
		uTex = latex(u)
		lTex = latex(l)
		k = fTex + uTex + lTex
		if k in solhashs:
			continue
		solhashs[k] = True
		# Average value = (F(u) - F(l)) / (u - l)
		F = integrate(f, x)
		s = F.subs(x, u) - F.subs(x, l)
		#print("Got s = " + str(s) + " with " + str(F.subs(x, u)) + " and " + str(F.subs(x, l)))
		#print("Additionally: F = " + str(F))
		s /= (u - l)
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
Determine the enclosed area of a simple function over an interval
'''
def q4(desiredNumSolutions, write, prnt, outputFile="cbe6q4.csv"):
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
		l = randomCoeff(9, False, True)
		u = randomCoeff(9, False, True)
		if l > u:
			l, u = u, l # I love Python syntax
		elif l == u:
			continue
		f = randomPolynomial2(1) # Just linears
		fTex = latex(f)
		uTex = latex(u)
		lTex = latex(l)
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
	
def q5(desiredNumSolutions, write, prnt, outputFile="cbe6q5.csv"):
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
		l = randomCoeff(5, False, True)
		u = randomCoeff(5, False, True)
		if l > u:
			l, u = u, l # I love Python syntax
		elif l == u:
			continue
		f = randomPolynomial2(random.randint(2,3), 9, False, True) # Quadratic or cubic
		fTex = latex(f)
		uTex = latex(u)
		lTex = latex(l)
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
		if len(sTex) > 14:
			continue
		numSols += 1
		if prnt:
			print(fTex + ',' + uTex + ',' + lTex + ',' + sTex)
		if write:
			csvfile.write(fTex + ',' + uTex + ',' + lTex + ',' + sTex + '\n')
	if write:
		csvfile.close()
		
def q6RandomFunction():
	a = randomCoeff()
	if bool(random.getrandbits(1)):
		return sin(a * x)
	return cos(a * x)
		
def q6(desiredNumSolutions, write, prnt, outputFile="cbe6q6.csv"):
	#x = sympy.Symbol('x', real=True) 
	print("\n\nQuestion 6:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,u,l,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,u,l,S\n")
	while numSols < desiredNumSolutions:
		l = randomCoeff(5, False, True) * pi / (2 ** random.randint(0, 2))
		u = randomCoeff(5, False, True) * pi / (2 ** random.randint(0, 2))
		if l > u:
			l, u = u, l # I love Python syntax
		elif l == u:
			continue
		f = q6RandomFunction()
		fTex = latex(f)
		uTex = latex(u)
		lTex = latex(l)
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
		#sTex = sTex.replace("log", "ln")
		if len(sTex) > 14:
			continue
		numSols += 1
		if prnt:
			print(fTex + ',' + uTex + ',' + lTex + ',' + sTex)
		if write:
			csvfile.write(fTex + ',' + uTex + ',' + lTex + ',' + sTex + '\n')
	if write:
		csvfile.close()
		
def q7RandomFunction():
	if bool(random.getrandbits(1)):
		fpart = sqrt(x)
		v = 2
	else:
		fpart = cbrt(x)
		v = 3
	# Determine if in numerator or denominator
	if bool(random.getrandbits(1)):
		return randomCoeff() * fpart, v
	else:
		return randomCoeff() / fpart, v
def q7RandomCoeff(v):
	return (-1) ** random.randint(0, 1) * (random.randint(1, 5) ** v)
		
def q7(desiredNumSolutions, write, prnt, outputFile="cbe6q7.csv"):
	#x = sympy.Symbol('x', real=True) 
	print("\n\nQuestion 7:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,u,l,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,u,l,S\n")
	while numSols < desiredNumSolutions:
		f, v = q7RandomFunction()
		l = q7RandomCoeff(v)
		u = q7RandomCoeff(v)
		if l > u:
			l, u = u, l # I love Python syntax
		elif l == u:
			continue
		fTex = latex(f)
		uTex = latex(u)
		lTex = latex(l)
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
		#sTex = sTex.replace("log", "ln")
		if len(sTex) > 14:
			continue
		numSols += 1
		if prnt:
			print(fTex + ',' + uTex + ',' + lTex + ',' + sTex)
		if write:
			csvfile.write(fTex + ',' + uTex + ',' + lTex + ',' + sTex + '\n')
	if write:
		csvfile.close()
		
def q8(desiredNumSolutions, write, prnt, outputFile="cbe6q8.csv"):
	#x = sympy.Symbol('x', real=True) 
	print("\n\nQuestion 8:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,u,l,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,u,l,S\n")
	while numSols < desiredNumSolutions:
		l = randomCoeff(9, False, True)
		u = randomCoeff(9, False, True)
		if l > u:
			l, u = u, l # I love Python syntax
		elif l == u:
			continue
		f = randomPolynomial2(1) / x # Just linears
		fTex = latex(f)
		uTex = latex(u)
		lTex = latex(l)
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
		
def q9RandomFunction():
	fType = random.randint(0, 3)
	if fType == 0:
		return sin(x)
	elif fType == 1:
		return cos(x)
	elif fType == 2:
		return ln(x)
	elif fType == 3:
		return 1 / x
		
def q9(desiredNumSolutions, write, prnt, outputFile="cbe6q9.csv"):
	#x = sympy.Symbol('x', real=True) 
	print("\n\nQuestion 9:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("f,u,l,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("f,u,l,S\n")
	while numSols < desiredNumSolutions:
		l = randomCoeff(9, False, True)
		u = randomCoeff(9, False, True)
		if l > u:
			l, u = u, l # I love Python syntax
		elif l == u:
			continue
		f = q9RandomFunction() # Just linears
		fTex = latex(f)
		uTex = latex(u)
		lTex = latex(l)
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
		
if __name__=='__main__':
	numSols = int(input("How many solutions do you want for each question: "))
	#q1(numSols, False, True)
	# q2(numSols, False, True)
	# q3(numSols, False, True)
	#q4(numSols, False, True)
	#q5(numSols, False, True)
	#q6(numSols, False, True)
	#q7(numSols, False, True)
	#q8(numSols, False, True)
	q9(numSols, False, True)
	#q10(numSols, False, True)
	
