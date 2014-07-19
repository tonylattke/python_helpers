####################################### Tuples ##########################################

# Tuple
mytuple = ("Bruce","Wayne")
print mytuple

# Triplet
print ("Red", "Green", "Blue")

# N-Tuple
print ("Batman", "Superman", "Wonder Woman", "Green Light", "Flash", "J\'onn")

# Access
print mytuple[0]

# Replacing is not suporting on tuples

######################################## Lists ##########################################

# Empty list
empty_list = []

# Append elements to the list
numbers = empty_list
numbers.append(1)
numbers.append(2)
numbers.append(3)
print numbers

# Delete the last element
numbers.pop()
print numbers

# Delete the first element
numbers.popleft()
print numbers

# List loaded
lost = [4, 8, 15, 16, 23, 42]
print "Lost numbers: %s" % lost

# Length of list
print "Lost numbers are only %d numbers" % len(lost)

# Concat lists
numbers_2 = range(3,10)
print [0,1] + numbers + numbers_2

# Access to diferents elements
squares = [1, 4, 9, 16, 36] 
print "The element number 2 on the list is " + str(squares[3])
print "The last element on the list is " + str(squares[-1])

# Change value of element on list
squares[4] = 25
print squares

# List inside lists
print [[1,2,3,4], [5,6,7,8], [9,10,11,12]]

# List with diferents types
info = ['Tony', 24, (True, False), ['movies','programming','games']]
print info

# Delete element by index
del info[1]
print info

# Sort list
numbers = [5, 13, 2, 1 , 21, 1, 8, 3]
numbers.sort()
print numbers

##################################### Dictionary ########################################

# Empty dictionary
dictionary = {}

# Append elements
dictionary["a"] = "Alice"
dictionary["e"] = "Erick"
dictionary["i"] = "Isaac"
dictionary["o"] = "Oscar"
dictionary["u"] = "Ursula"
print dictionary

# Access
print dictionary["i"]

# Change Value
dictionary["o"] = "Oriana"
print dictionary["o"]

# Keys from dictionary
print dictionary.keys()

# Values from dictionary
print dictionary.values()

# Dictionary loaded
months = {
	'January' 	: 'Capricorn',
	'February' 	: 'Aquarius',
	'March'		: 'Pisces',
	'April'		: 'Aries',
	'May'		: 'Taurus',
	'June'		: 'Gemini',
	'July'		: 'Cancer',
	'August'	: 'Leo',
	'September' : 'Virgo',
	'October'	: 'Libra',
	'November'	: 'Scorpio',
	'December'	: 'Sagittarius'
}
print months

# Number of months
print len(months)

# Delete element
del months["December"]