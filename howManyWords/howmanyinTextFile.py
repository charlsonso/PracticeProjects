def howmanyinText(text):
	string = open(text).read()
	string = string.split()
	print string
	return len(string)

print howmanyinText('text.txt')