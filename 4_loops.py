# While .. then ..
print 'While'
i = 1
while i < 5:
	print i
	i += 1

# While with function break
print 'While with break'
i = 5
result = 1
while True:
	result *= i
	if i <= 1:
		print result
		break
	# else:
	# 	pass
	i -= 1

# For .. in .. then ..
print 'For each'
for aux in xrange(1,10):
	print aux