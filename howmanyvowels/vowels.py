def howManyVowels(text):
	j=0
	t=''
	list = [0,0,0,0,0]
	for i in text.lower():
		if i == 'a':
			j+=1
			list[0]+=1
		if i=='e':
			j+=1
			list[1]+=1
		if i=='i':
			j+=1
			list[2]+=1
		if i=='o':
			j+=1
			list[3]+=1
		if i=='u':
			j+=1
			list[4]+=1	
	print 'in the word "'+text+'"'	
	print 'total vowels ' +str(j)
	print 'total a'+str(list[0])
	print 'total e'+str(list[1])
	print 'total i'+str(list[2])
	print 'total o'+str(list[3])
	print 'total u'+str(list[4])

howManyVowels('aslkdjqwejiojovxasjkldipqwoi')

