import random
import csv
import sympy
import numpy
#from sympy
from sympy.abc import x, y # This makes it so x is always defined symbolically
from sympy import latex, exp, diff, ln, integrate

t = sympy.Symbol('t')

def randomPolynomial(order, mn, mx):
	f = 0
	for i in range(0, order + 1):
		f += random.randint(mn, mx) * (x ** i)
	return f
		
def randomPolynomial2(order, key=9, randomizeInclusion=False):
	f = 0
	for i in range(0, order + 1):
		if randomizeInclusion and bool(random.getrandbits(1)):
			term = 0
		else:
			term = randomCoeff(key) * (x ** i)
		f += term
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
def randomCoeff(key=9, allowFracs=True, allowNegs=True):
	a = random.randint(1, key)
	if allowFracs and bool(random.getrandbits(1)):
		a = sympy.Rational(1, a)
	if allowNegs and bool(random.getrandbits(1)):
		a = -a
		
	return a

def randomCoeffOrZero(key=9):
	if bool(random.getrandbits(1)):
		return 0
	else:
		return randomCoeff(key)
	
'''
Integrates an array-like numpy object and adds a random coefficient at the end.
'''
def numpIntCoeff(a):
	r = list(a).copy()
	r.append(randomCoeff())
	for i in range(len(a) - 1):
		r[i] /= len(a) - i
	return r
'''
Creates latex for an array-like numpy thing

Uses sympy since we are already.
'''
def numTex(a):
	l = len(a)
	tex = ""
	if a[0] < 0:
		tex += '-'
	for i in range(l):
		if a[i] == 0:
			continue
		if (not abs(a[i]) == 1) and i < len(a) - 1:
			tex += latex(sympy.Rational(abs(a[i]))) 
		if i != len(a) - 1 and l - i - 1 > 1:
			tex += "x^{" + str(l - i - 1) + "}"
		elif l - i - 1 == 1:
			tex += 'x'
		if i < l - 1 and a[i + 1] > 0:
			tex += ' + '
		elif i < l - 1 and a[i + 1] < 0:
			tex += ' - '
	tex += latex(abs(a[len(a) - 1]))
	return tex

def numEval(a, xVal):
	result = 0
	for i in range(len(a)):
		result += a[i] * (xVal ** (len(a) - i - 1))
	return sympy.Rational(result)
	
def isNiceRational(r, howNotNice=20):
	rat = sympy.Rational(r)
	return len(latex(rat)) < howNotNice
		
		
'''
Generates a function with exactly ONE inflection point.

returns both the function, and the x coordinate of the inflection 

Core is a 2nd derivative based on a linear term and constant.
Optionally, e^x are multiplied
'''
def oneInflection():
	a = randomCoeff(9, False)
	b = randomCoeff(9, False)
	fDoublePrime = a*x + b
	inflectionPoint = -sympy.Rational(b, a)
	if bool(random.getrandbits(1)):
		fDoublePrime *= exp(x)
	fPrime = integrate(fDoublePrime) + randomCoeffOrZero()
	f = integrate(fPrime) + randomCoeffOrZero()
	return [f, inflectionPoint]
