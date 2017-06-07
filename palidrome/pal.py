def pal(text):
	#[::-1] is called extended slices. will return the number of values throught the list. for -1, it will return the string backwards
	if text == text[::-1]:
		return 'isPal'
	else:
		return 'isnotPal'

print pal('racecar')
print pal('herro')