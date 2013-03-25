def reverse_check(string):
    if string==string[::-1]:
        print "same"
    else:
        print "different"

string = raw_input ("input string : ")
reverse_check(string)


