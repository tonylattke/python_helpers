# Commpare Values
aux = 23
equal 			= aux == 42
not_equal 		= aux != 42

less_than 		= aux < 42
more_than 		= aux > 42
less_equal_than = aux <= 42
more_equal_than = aux >= 42

operator_or		= aux < 23 or aux > 42
operator_and	= aux < 23 and aux > 42

# If .. then .. else ..
number = 23
if number == 23:
	print 'Number is 23'
else:
	print 'Number is not 23'

# If .. then .. else if .. then .. else ..
names = ['Tony', 'Enrique']
name  = 'Heinrich'
if name == names[0]:
	print 'It is Tony'
elif name == names[1]:
	print 'It is Enrique'
else:
	print 'It\'s not Tony or Enrique'

# 'In' property on list
numbers = [4,8,15,16,23,42]
aux 	= 69
if aux in numbers:
	print 'It is on the list'