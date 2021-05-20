import random
import csv
import sympy
#from sympy
from sympy.abc import x # This makes it so x is always defined symbolically
from sympy import latex, exp, diff

from sympy import nan

from cbefunctions import *

'''
Function: q1Cubic

Parameters: A, B, C, D, S (solution)

Description: for a cubic polynomial of the form Ax^3 + Bx^2 + Cx + D, evaluate the derivative at 1

Solution:
3A + 2B + C

WARNING: This does NOT check to make sure there are that many available solutions. There are 18^4 possible solutions.
This does NOT iterate through them, either, so it's not the most efficient, because it gets random solutions each time.
'''
def q1Cubic(desiredNumSolutions, write, prnt, outputFile="q1Cubic.csv"):
	print("Question 1A:\n")
	output = [['A', 'B', 'C', 'D', 'S']]
	# Create a blank dict to keep track of the used answers so we don't duplicate
	solhashs = {}
	numSolutions = 0
	if prnt:
		print("A,B,C,D,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("A,B,C,D,S\n")
	while numSolutions < desiredNumSolutions:
		A = random.randint(1, 10) # A is bounded to 1-9
		B = random.randint(1, 10) # B is bounded to 1-9
		C = random.randint(1, 10) # C is bounded to 1-9
		D = random.randint(1, 10) # D is bounded to 1-9
		# Randomize whether or not each parameter is positive or negative
		if bool(random.getrandbits(1)):
			A = -A
		if bool(random.getrandbits(1)):
			B = -B
		if bool(random.getrandbits(1)):
			C = -C
		if bool(random.getrandbits(1)):
			D = -D
		k = key([A, B, C, D])
		if not k in solhashs:
			# Mark we have created this solution already
			solhashs[k] = True
			S = 3*A + 2*B + C
			output.append([A, B, C, D, S])
			numSolutions += 1
			if prnt:
				printLine([A, B, C, D, S])
			if write:
				writeLine([A, B, C, D, S], csvfile)
				
	if write:
		csvfile.close()
	
	return output
			
'''
Function: q1Quadratic

Parameters: A, B, C, D, E, S (solution)

Description: for a quadratic polynomial of the form Ax^4 + Bx^3 + Cx^2 + Dx + E, evaluate the derivative at 1

Solution:
4A + 3B + 2C + D
'''

def q1Quadratic(desiredNumSolutions, write, prnt, outputFile="q1Quadratic.csv"):
	print("\n\nQuestion 1B:\n")
	output = [['A', 'B', 'C', 'D', 'E', 'S']]
	# Create a blank dict to keep track of the used answers so we don't duplicate
	solhashs = {}
	numSolutions = 0
	if prnt:
		print("A,B,C,D,E,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("A,B,C,D,E,S\n")
	while numSolutions < desiredNumSolutions:
		A = random.randint(1, 10) # A is bounded to 1-9
		B = random.randint(1, 10) # B is bounded to 1-9
		C = random.randint(1, 10) # C is bounded to 1-9
		D = random.randint(1, 10) # D is bounded to 1-9
		E = random.randint(1, 10) # D is bounded to 1-9
		# Randomize whether or not each parameter is positive or negative
		if bool(random.getrandbits(1)):
			A = -A
		if bool(random.getrandbits(1)):
			B = -B
		if bool(random.getrandbits(1)):
			C = -C
		if bool(random.getrandbits(1)):
			D = -D
		if bool(random.getrandbits(1)):
			E = -E
		k = key([A, B, C, D, E])
		if not k in solhashs:
			# Mark we have created this solution already
			solhashs[k] = True
			S = 4*A + 3*B + 2*C + D
			output.append([A, B, C, D, E, S])
			numSolutions += 1
			if prnt:
				printLine([A, B, C, D, E, S])
			if write:
				writeLine([A, B, C, D, E, S], csvfile)
				
	if write:
		csvfile.close()
		
	return output

def q1General(desiredNumSolutions, write, prnt, outputFile="q1.csv"):
	solhashs = {}
	numSolutions = 0
	print("A,S")
	while numSolutions < desiredNumSolutions:
		# t = Symbol('t')
		A = random.randint(1, 2) * random.randint(0, 2) # A is bounded to 1-9
		B = random.randint(1, 3) # B is bounded to 1-9
		C = random.randint(1, 4) # C is bounded to 1-9
		D = random.randint(1, 5) # D is bounded to 1-9
		E = random.randint(1, 10) # D is bounded to 1-9
		f = A * (x ** 4) + B * (x ** 3) + C * (x ** 2) + D * x + E
		k = latex(f)
		if not k in solhashs:
			solhashs[k] = True
			fPrime = diff(f)
			# c = random.randint(-10, 11)
			S = fPrime
			if S.is_infinite or S == nan:
				# print("Skipping infinite solution")
				continue
			print(k + ',' + latex(S))
			numSolutions += 1
'''
Description: Generates product rule CSVs

Parameters: A, B, C, S

f(x) = A(x) * B(x)
S = f'(C) = A(C) * B'(C) + A'(C) * B(C) (But that's handled via SymPy)

'''
def q2(desiredNumSolutions, write, prnt, outputFile="q2.csv"):
	print("\n\nQuestion 2:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("A,B,C,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("A,B,C,S\n")
	while numSols < desiredNumSolutions:
		# Come up with two random functions:
		A = 0
		B = 0
		atype = 0
		btype = 0
		while A == 0 or B == 0 or atype == btype: # Don't use the same type. "or A == B" was not needed as equivalence is covered in type
			[A, atype] = randomSymbolic(0, 3, 3, True)
			[B, btype] = randomSymbolic(0, 3, 3, True)
		# Swap order so they show in the defined order.
		if btype < atype:
			B, A = A, B
		C = random.randint(0, 5) # the x values we evaluate at
		k = key([A, B, C])
		if not k in solhashs:
			f = A * B
			fprime = sympy.diff(f, x)
			S = fprime.subs(x, C)
			if S.is_infinite:
				#print("Skipping infinite solution")
				continue
			solhashs[k] = True
			numSols += 1
			if prnt:
				printSymbolicLine([A, B, C, S])
			if write:
				writeLine([A, B, C, S], csvfile)
	
	if write:
		csvfile.close()
'''
Description: Basic Quotient rule

Parameters: A, S
A = latex() of h(x)
S = h'(1)

h(x) is a quotient of two polynomials, with a max order on both the numerator and denominator of 3
'''
def q3(desiredNumSolutions, write, prnt, outputFile="q3.csv"):
	print("\n\nQuestion 3:\n")
	solhashs = {}
	numSols = 0
	if prnt:
		print("A,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("A,S\n")
	while numSols < desiredNumSolutions:
		# Generate random coefficients. Second term for randomizing inclusion
		num = 0 
		while num == 0 or not num.is_algebraic_expr() or num.is_constant():
			a = random.randint(1, 6) * random.randint(0, 1)
			b = random.randint(1, 6) * random.randint(0, 1)
			c = random.randint(1, 6) * random.randint(0, 1)
			d = random.randint(1, 6) # Numerator always has constant
			num = a*(x**3) + b*(x**2) + c*x + d
		den = 0
		# This is not the most efficient way to do this...too bad! It gets the job done.
		while den == 0 or not latex(num / den).startswith("\\frac") or not (num / den).is_algebraic_expr(): # den == num or not den.is_algebraic_expr(): # or (num / den).is_constant(): # Do not allow denominator to be zero or equal to numerator
			# Regenerate random coefficients. Second term for randomizing inclusion
			a = random.randint(1, 6) * random.randint(0, 1)
			b = random.randint(1, 6) * random.randint(0, 1)
			c = random.randint(1, 6) * random.randint(0, 1)
			d = random.randint(1, 6) # Denominator always has constant
			den = a*(x**3) + b*(x**2) + c*x + d
		h = num / den
		# Sympy was automatically simplifying with latex(h)
		k = "\\frac{" + latex(num) + "}{" + latex(den) + "}"
		if not k in solhashs:
			solhashs[k] = True
			#hstr = sympy.latex(sympy.nsimplify(h))
			# Generate solution
			hPrime = sympy.diff(h)
			S = hPrime.subs(x, 1)
			if S.is_infinite:
				# print("Skipping infinite solution")
				continue
			numSols += 1
			if prnt:
				print(k + "," + sympy.latex(S))
			if write:
				csvfile.write(k + "," + sympy.latex(S) + "\n")
'''
Question 4: More product rule. Params A, B, S

s(t) = (f(t))(g(t))

A = f(t)
B = g(t)
S = s'(0)

A, B, may either be a random polynomial of order 2 or 3, or may be a simple random fraction of the form (at + b) / (ct + d)
'''
def q4(desiredNumSolutions, write, prnt, outputFile="q4.csv"):
	print("\n\nQuestion 4:\n")
	t = sympy.Symbol('t')
	solhashs = {}
	numSols = 0
	if prnt:
		print("A,B,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("A,B,S\n")
	while numSols < desiredNumSolutions:
		# Get a single solution
		f = 0
		g = 0
		while f == 0 or g == 0 or f == g:
			if bool(random.getrandbits(1)):
				f = randomPolynomial(random.randint(2, 3), -9, 9)
			else:
				f = randomSimpleFract(-9, 9)
			if bool(random.getrandbits(1)):
				g = randomPolynomial(random.randint(2, 3), -9, 9)
			else:
				g = randomSimpleFract(-9, 9)
		# Swap the variables to t rather than x
		f = f.subs(x, t)
		g = g.subs(x, t)
		s = f * g
		k = sympy.latex(s)
		if not k in solhashs:
			sPrime = sympy.diff(s)
			S = sPrime.subs(t, 0)
			if S.is_infinite or S == nan:
				#print("Skipping infinite solution")
				continue
			solhashs[k] = True
			numSols += 1
			if prnt:
				print(sympy.latex(f) + ',' + sympy.latex(g) + ',' + sympy.latex(S))
			if write:
				csvfile.write(sympy.latex(f) + ',' + sympy.latex(g) + ',' + sympy.latex(S) + "\n")
'''
Question 5. 

v(t) is either equal to f(t) / g(t) or f(t) * g(t)

f(t) is either a random polynomial of order 1 or 2 or a random exponential of order 1
g(t) is determined similarly to f(t)

S = v'(0)
'''
def q5(desiredNumSolutions, write, prnt, outputFile="q5.csv"):
	print("\n\nQuestion 5:\n")
	t = sympy.Symbol('t')
	solhashs = {}
	numSols = 0
	if prnt:
		print("A,S")
	if write:
		csvfile = open(outputFile, 'w')
		csvfile.write("A,S\n")
	while numSols < desiredNumSolutions:
		# Get a single solution
		f = 0
		g = 0
		while f == 0 or g == 0 or f == g:
			if bool(random.getrandbits(1)):
				f = randomPolynomial(random.randint(1, 2), -9, 9)
			else:
				f = randomExponential(1, -9, 9)
			
			if bool(random.getrandbits(1)):
				g = randomPolynomial(random.randint(1, 2), -9, 9)
			else:
				g = randomExponential(1, -9, 9)
		# Now that f and g are chosen:
		if bool(random.getrandbits(1)):
			v = f * g
		else:
			v = f / g
		k = latex(v.subs(x, t))
		if not k in solhashs:
			vPrime = diff(v)
			S = vPrime.subs(x, 0)
			if S.is_infinite or S == nan:
				#print("Skipping infinite solution")
				continue
			numSols += 1
			solhashs[k] = True
			if prnt:
				print(k + ',' + latex(S))
			if write:
				csvfile.write(k + ',' + latex(S) + "\n")
			
if __name__=='__main__':
	numSols = int(input("How many solutions do you want for each question: "))
	# q1Cubic(numSols, False, True)
	# q1Quadratic(numSols, False, True)
	# q1General(numSols, False, True)
	# q2(numSols, False, True)
	q3(numSols, False, True)
	# q4(numSols, False, True)
	# q5(numSols, False, True)
