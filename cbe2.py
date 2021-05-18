import random
import csv
import sympy
#from sympy
from sympy.abc import x # This makes it so x is always defined symbolically
from sympy import latex, exp, diff


def randomPolynomial(order, mn, mx):
	f = 0
	for i in range(0, order + 1):
		f += random.randint(mn, mx) * (x ** i)
	return f
		
def randomSimpleFract(mn, mx):
	f = 0
	while f == 0 or f == 1:
		f = randomPolynomial(1, mn, mx) / randomPolynomial(1, mn, mx)
	return f

def randomExponential(order, mn, mx):
	f = 0
	for i in range(0, order + 1):
		f += random.randint(mn, mx) * exp(x * i)
	return f

def isNum(blah):
	return isinstance(blah, int) or isinstance(blah, float)
'''
CBE 2 Problem auto-generator

Author: Josh Jeppson

For: Dr. Greg Wheeler

'''

def strPretty(num, showOnes=False):
	if isinstance(num, int) or isinstance(num, float):
		base = str(abs(num))
		if base == "1" and not showOnes:
			base = ""
		if num < 0:
			return "-" + base
		else:
			return "+" + base
	# Default to sympy latex printing
	else:
		return sympy.latex(num)

'''
Simple function to create a hash key so we don't duplicate answers
'''
def key(params):
	k = ""
	for param in params:
		k += str(param)
	return k
'''
Simple function to print our line of parameters
'''
def printLine(params):
	for i in range(len(params)):
		param = params[i]
		if i == 0 and abs(param) != 1:
			print(str(param) + ",", end="")
		elif i == 0 and param < 0:
			print("-,", end="")
		elif i == 0 and param > 0:
			print(",", end="")
		elif i < len(params) - 1:
			print(strPretty(param) + ",", end="")
		else:
			print(strPretty(param, True))
			
def printSymbolicLine(params):
	for i in range(len(params) - 1):
		param = params[i]
		print(sympy.latex(param) + ",", end="")
	print(sympy.latex(params[len(params) - 1]))
'''
Generates a random short symbolic function for CBE 2 question 2
'''
def randomSymbolic():
	ftype = random.randint(0, 4)
	# Coefficient multiplied by x to a power, ax^b
	if ftype == 0:
		a = random.randint(1, 10)
		b = random.randint(1, 4) # Max wil be cubed 
		f = a * (x ** b)
	# Square root
	elif ftype == 1:
		f = sympy.sqrt(x)
	# Cubed root
	elif ftype == 2:
		f = x ** (1 / 3)
	else:
		f = sympy.exp(x)
		
	return sympy.nsimplify(f) # sympy.Rational(f)

'''
Simple function to write line to csv file
'''
def writeLine(params, csvfile):
	strToWrite = ""
	for param in params:
		strToWrite += strPretty(param) + ","
	if params[0] < 0:
		csvfile.write(strToWrite[0:len(strToWrite) - 1] + "\n")
	else: # If positive, ignore the first +
		csvfile.write(strToWrite[1:len(strToWrite) - 1] + "\n")

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
		while A == 0 or B == 0 or A == B:
			A = randomSymbolic()
			B = randomSymbolic()
		C = random.randint(0, 5) # the x values we evaluate at
		k = key([A, B, C])
		if not k in solhashs:
			solhashs[k] = True
			f = A * B
			fprime = sympy.diff(f, x)
			S = fprime.subs(x, C)
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
		while num == 0:
			a = random.randint(1, 6) * random.randint(0, 1)
			b = random.randint(1, 6) * random.randint(0, 1)
			c = random.randint(1, 6) * random.randint(0, 1)
			d = random.randint(1, 6) * random.randint(0, 1)
			num = a*(x**3) + b*(x**2) + c*x + d
		den = 0
		while den == 0 or den == num: # Do not allow denominator to be zero or equal to numerator
			# Regenerate random coefficients. Second term for randomizing inclusion
			a = random.randint(1, 6) * random.randint(0, 1)
			b = random.randint(1, 6) * random.randint(0, 1)
			c = random.randint(1, 6) * random.randint(0, 1)
			d = random.randint(1, 6) * random.randint(0, 1)
			den = a*(x**3) + b*(x**2) + c*x + d
		h = num / den
		k = sympy.latex(h)
		if not k in solhashs:
			solhashs[k] = True
			#hstr = sympy.latex(sympy.nsimplify(h))
			# Generate solution
			hPrime = sympy.diff(h)
			S = hPrime.subs(x, 1)
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
			solhashs[k] = True
			sPrime = sympy.diff(s)
			S = sPrime.subs(t, 0)
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
			numSols += 1
			solhashs[k] = True
			vPrime = diff(v)
			S = vPrime.subs(x, 0)
			if prnt:
				print(k + ',' + latex(S))
			if write:
				csvfile.write(k + ',' + latex(S) + "\n")
			
if __name__=='__main__':
	numSols = int(input("How many solutions do you want for each question: "))
	# q1Cubic(numSols, False, True)
	# q1Quadratic(numSols, False, True)
	q2(numSols, False, True)
	# q3(numSols, False, True)
	# q4(numSols, False, True)
	#q5(numSols, False, True)
