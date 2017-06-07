def pig(text):
	if len(text)<2:
		return 'unable to print pig latin since one char'
	else:
		return text[1:]+'-'+text[0]+'ay'

print pig('hello')
print pig('a')