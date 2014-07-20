##################################### Creating Class ####################################
class Color:
	r = 0
	g = 0
	b = 0

	# To string
	def __str__(self):
		return "R: %d G: %d B: %d" % (self.r,self.g,self.b)

	# To String unicode
	def __unicode__(self):
		return u"R: %d G: %d B: %d" % (self.r,self.g,self.b)

aux = Color()
print aux

# Creating a class with Initialize method
class Person:

	def __init__(self,name,age):
		self.name = name
		self.age  = age

	def hello(self):
		print "Hello " + self.name

# Create an Instance
aux = Person("Bruce", 28)
aux.hello()

# Change value inside class
aux.name = "Tony"
aux.hello()

###################################### Inheritance ######################################
class Civil(Person):

	def __init__(self,name,age,profesion_name):
		self.name 			= name
		self.age  			= age
		self.profesion_name = profesion_name

aux = Civil('Tony',24,'Programmer')