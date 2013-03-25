def return_v(a):
	if a>0 and a<10 :
		print num + 10

	elif a>=10 and a <100 :
		print num *0.1

	else :
		print bool(0)

num = raw_input ("input your number: ")
num = int(num)
return_v(num)