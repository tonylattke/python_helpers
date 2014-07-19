import os

################################### Input reading #######################################
name = raw_input("Introduce the file name: ")


#################################### Create file ########################################
file = open(name + '.txt', 'w')

# Write the text
file.write('test on file\n')

# Write every line from the list
lines_of_text = ["second text\n", "third text\n", "fourth line"]
file.writelines(lines_of_text)

# Close the file
file.close()

##################################### Read file ########################################$
file = open(name + '.txt', 'r')

## Option 1 - Read with for
for line in file:
	print line,
print ''

# Reset the seek (position 0 on file)
file.seek(0)

## Option 2 - Read all with read
# Read the file complete
aux = file.read()
print aux.split('\n')

## Option 3 - Read and save on a list
file.seek(0)
print file.readlines()

# Close the file
file.close()