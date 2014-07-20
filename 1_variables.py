################################## Printing Variables ###################################

# Using Strings
foo = "World"
print "Hello, %s!" % foo

# Using numbers
minutes = 60
print "1 Hour have %d minutes." % minutes

# Using Floating point numbers
celcius   = 0
farenheit = 32 + celcius*(9.0/5)
print "%f Celcius are %f Farenheit grades" % (celcius,farenheit)

# Using Floating point numbers with fixed amount digits of the right
# Only the first 5 first digits of phi will be showed with %.5f
phi   = 1.618033988749894848
print "The golden ratio %.5f" % phi

# Representation Hexadecimal of numbers on lowercase (uppercase use %X)
red, green, blue = 0xFF0000, 0x00FF00, 0x0000FF
print "Hexadecimal code of:\nRed is: %x \nGreen is: %x \nBlue is: %x" % (red,green,blue)

# Print text with multiline string
print """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Phasellus mattis ac tortor sed fringilla. Etiam aliquam
turpis sit amet nisi molestie, nec accumsan massa tempus."""

################################## Operating Variables ##################################

# Numbers
foo = 23
bar = 19
baz = foo + bar	# Plus
print ("%d + %d is: " % (foo,bar)) + str(baz)

foo = 69
bar = 27
baz = foo - bar	# Minus
print ("%d - %d is: " % (foo,bar)) + str(baz)

foo = 7
bar = 6
baz = foo * bar # Multiply
print ("%d * %d is: " % (foo,bar)) + str(baz)

foo = 420
bar = 10
baz = foo / bar # Divide
print ("%d / %d is: " % (foo,bar)) + str(baz)

foo = 429
bar = 43
baz = foo % bar # Module
print ("%d mod %d is: " % (foo,bar)) + str(baz)

foo = 6.48074069840786
bar = 2
baz = foo ** bar # Pow
print ("%d to the power of %d is: " % (foo,bar)) + str(baz)

# Strings
foo = "Python"
bar = "Works"
print foo + " " + bar

foo = '"It Wokrs"' # Single quotes print literally text
print foo

foo = "Lorem ipsum dolor sit amet"
foo = foo.replace(" ", "_") # Replacing spaces by _
print foo

foo = "Lorem ipsum dolor sit amet"
print foo[0] 	# First char on string "Lorem ipsum dolor sit amet"
print foo[6:12] # 6 till 12 chars on string "Lorem ipsum dolor sit amet"
print foo[:5] 	# First 5 chars on string "Lorem ipsum dolor sit amet"
print foo[6:] 	# 6 till the end chars on string "Lorem ipsum dolor sit amet"