string = "next people"

n=len(string)
num = 0
for i in range(0, n):
	if string[i] == 'e':
		num = num+1

print num

