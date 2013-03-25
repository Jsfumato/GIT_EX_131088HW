def Ab_value(num):
	if num>0:
		print 'absolute value \n', num
	elif num<0:
		print 'absolute value \n', -num
	else:
		print 'absolute value \n', 0

num = raw_input ("input your number: ")
num = int(num)
Ab_value(num)