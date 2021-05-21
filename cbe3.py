import random
import csv
import sympy
#from sympy
from sympy.abc import x # This makes it so x is always defined symbolically
from sympy import latex, exp, diff, pi, sqrt, cbrt
#from math import pi

from sympy import nan, ln

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
			[h, htype] = randomSymbolic(0, 6, 3, True)
			[g, htype] = randomSymbolic(0, 6, 3, True)
			if bool(random.getrandbits(1)):
				h += random.randint(1, 2)
			else:
				h -= random.randint(1, 2)
			if bool(random.getrandbits(1)):
				g += random.randint(1, 2)
			else: 
				g -= random.randint(1, 2)
				
		# Now we have something we can use.
		f = ln(h / g) 
		k = latex(f).replace("log", "ln")
		if not k in solhashs:
			fPrime = diff(f)
			if fPrime.is_infinite:
				continue
			S = latex(fPrime).replace("log", "ln")
			numSols += 1
			if prnt:
				print(k + ',' + S)
			if write:
				csvfile.write(k + ',' + S + '\n')
				
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
			fPrime = diff(f)
			if fPrime.is_infinite:
				continue
			S = latex(fPrime)
			numSols += 1
			if prnt:
				print(k + ',' + S)
			if write:
				csvfile.write(k + ',' + S + '\n')
	
if __name__=='__main__':
	numSols = int(input("How many solutions do you want for each question: "))
	# q1(numSols, False, True)
	# q1Symbolic(numSols, False, True)
	# q2Symbolic(numSols, False, True)
	q3Symbolic(numSols, False, True)
