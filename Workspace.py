import numpy 
import math
from sympy import *

def nCr(n, r): 
    return math.factorial(n)//(math.factorial(r) * math.factorial(n - r))

#Returns coefficient of x^0, x^1, x^2, x^4, ... as an matrix
def binomialequation(constant,power): 
    coeffs = []
    for i in range(0, power + 1):
        coeff = nCr(power, power - i) * math.pow(constant, power - i)  
        coeffs.append(coeff)
    return coeffs 

def expression_solver(expression, debugging = False): 
    x = Symbol('x')
    converted = sympify(expression)
    if debugging:
        print("Converted is " + str(converted))
    solutions = solve(converted)
    count = 1
    for value in solutions: 
        try:
            print("Solution " + str(count) + ": " + str(round(float(value),3)))
            count += 1
        except:
            continue
    if(count == 1): 
        print("No real solutions")

def equation_creater(coeffs): 
    result = str(int(coeffs[0])) + " + "
    for index in range(1, len(coeffs)): 
        result += str(int(coeffs[index])) + "*x^" + str(index) + " + "
    result = result[:-3]
    print(result)
    return result

def subtract(leftarr, rightarr): 
    updated = [0.0] * max(len(leftarr), len(rightarr))
    for index in range(len(updated)): 
        if(index < len(leftarr)): 
            updated[index] += leftarr[index]
        if(index < len(rightarr)): 
            updated[index] -= rightarr[index]
    return updated

if __name__ == '__main__': 
    leftarr = [0.0, 1.0]
    rightarr = [1.0, 0.0, -4.0]
    #print(subtract(leftarr, rightarr))
    #expression_solver(equation_creater(rightarr))
    expression_solver('2*x - ((-1 + x) + 4)')