import ast

################################### Value to String #####################################

# Integer
value  = 42
string = str(value)

# Float
value  = 42.0
string = str(value)

# Boolean
value  = True
string = str(value)

################################### String to Value #####################################

# Integer
string = "42"
value  = int(string)

# Float
string = "42.0"
value  = float(string)

# Boolean

# Option 1
def strToBool(v):
	return v.lower() in ["yes", "true", "t", "1"]

string = "True"
value  = strToBool(string)

# Option 2
string = "True"
value  = ast.literal_eval(string)