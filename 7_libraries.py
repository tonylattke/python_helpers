from datetime import datetime, timedelta

import math
import random

###################################### Datetime #########################################
# Now
print datetime.now()

# Now - 2 Hours
print datetime.now() - timedelta(hours = 2)

####################################### Math ############################################

# Elemental numbers
pi 	= math.pi
e 	= math.e

def phi():
	return (1 + math.sqrt(5))/2

x = 10

math.isnan(x)		# Is not a number

math.trunc(x)		# Truncate x

math.exp(x) 		# e to the power of x

math.log(x) 		# Default base e (math.log(x,base))

math.log10(x)

math.sqrt(x)

math.sin(x)
math.cos(x)
math.tan(x)

######################################## Random #########################################

# Random number betwen 0 and 1
print random.random()

mylist = [4, 8, 15, 16, 23, 42]

# Random sort of list
random.shuffle(mylist)

# Random member of list
print random.choice(mylist)

# Random int on range
print random.randint(0,9)