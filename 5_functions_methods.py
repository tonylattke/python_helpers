######################## Example 1 - Create a function and using ########################

# Even or not
# @number : Number to decide
# @return : True if the number is even, otherwise Flase
def even(number):
	return number % 2 == 0

# Testing Function
for aux in xrange(0,10):
	if even(aux):
		print "%d - Even" % aux
	else:
		print "%d - Odd" % aux

################################# Example 2 - Recursion #################################

# Factorial of number
# @number : Number
# @return : Factorial value of number
def factorial(value):
	if (value <= 1):
		return 1
	return value * factorial(value -1)

# Fibonacci
# @value : Number
# @return : Fibonacci value
def fibonacci(value):
	if value == 0: return 0
	elif value == 1: return 1
	else: return fibonacci(value-1)+fibonacci(value-2)

# Testing Function
number = 7
print 'Factorial of %d is %d' % (number,factorial(number))
print 'Fibonacci of %d is %d' % (number,fibonacci(number))

#################################### Example of main ####################################
import sys

def main():
	params = sys.argv
	print params
	print 'Here is the main'

if  __name__ =='__main__':
    main()