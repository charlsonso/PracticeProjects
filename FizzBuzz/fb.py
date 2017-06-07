#used git/jaysonrowe

def fb(n):
	if n%3==0 and n%5 ==0:
		return 'FizzBuzz'
	elif n%3==0:
		return 'Fizz'
	elif n%5 == 0:
		return 'Buzz'
	else:
		return str(n)

print "\n".join(fb(n) for n in xrange(1,100))
#xrange is usefull because of special technique callled yielding. this technique used with a type of object known as generators.
#use to generate a long list

#another program
for num in xrange(1,101):
	msg=''
	if num%3==0:
		msg+='Fizz'
	if num%5==0:
		msg+='Buzz'
	print msg or num