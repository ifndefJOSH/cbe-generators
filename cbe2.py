import random
import csv
import sympy
#from sympy
from sympy.abc import x # This makes it so x is always defined symbolically

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
		if not key in solhashs:
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
		if not key in solhashs:
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
		A = randomSymbolic()
		B = randomSymbolic()
		C = random.randint(0, 5) # the x values we evaluate at
		k = key([A, B, C])
		if not key in solhashs:
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
		
if __name__=='__main__':
	numSols = int(input("How many solutions do you want for each question: "))
	q1Cubic(numSols, False, True)
	q1Quadratic(numSols, False, True)
	q2(numSols, False, True)
