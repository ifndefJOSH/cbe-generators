import random
import csv
import sympy
#from sympy
from sympy.abc import x, y # This makes it so x is always defined symbolically
from sympy import latex, exp, diff

t = sympy.Symbol('t')

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

Type 0: random polynomial
Type 1: f(x) = sqrt(x)
Type 2: f(x) = cubedroot(x)
Type 3: f(x) = e^x
Type 4: f(x) = e^ax
Type 5: f(x) = acos(bx)
Type 6: f(x) = asin(bx)
Type 7: f(x) = ln(ax)
'''
def randomSymbolic(type1=0, type2=3, polyMaxOrder=3, retType=False):
	ftype = random.randint(type1, type2)
	# Coefficient multiplied by x to a power, ax^b
	if ftype == 0:
		a = random.randint(1, 10)
		b = random.randint(1, polyMaxOrder) # Max wil be cubed for default polyMaxOrder of 3
		f = a * (x ** b)
	# Square root
	elif ftype == 1:
		f = sympy.sqrt(x)
	# Cubed root
	elif ftype == 2:
		f = x ** (1 / 3)
	elif ftype == 3:
		f = sympy.exp(x)
	elif ftype == 4:
		a = random.randint(1, 10)
		f = sympy.exp(a * x)
	elif ftype == 5:
		a = random.randint(1, 10)
		b = random.randint(1, 10)
		f = a * sympy.cos(x * b)
	elif ftype == 6:
		a = random.randint(1, 10)
		b = random.randint(1, 10)
		f = a * sympy.sin(x * b)
	elif ftype == 7:
		a = random.randint(1, 10)
		f = sympy.ln(a * x)
		
	if retType:
		return [sympy.nsimplify(f), ftype] 
	else:
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
Finds a random coefficient, which may be positive, negative, or fractional
'''
def randomCoeff(key=9):
	a = random.randint(1, key)
	if bool(random.getrandbits(1)):
		a = sympy.Rational(1, a)
	if bool(random.getrandbits(1)):
		a = -a
		
	return a

def randomCoeffOrZero(key=9):
	if bool(random.getrandbits(1)):
		return 0
	else:
		return randomCoeff(key)
