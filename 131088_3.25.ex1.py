'''
def reModelNameAgeData() :
	dict_age ={}

	for name in info:
		nAge = info[name]
		nAgeRange = int(nAge/10)*10
		new_keyname = str(nAgeRange)+'s'
		add_new_data(new_keyname, dict_age,name)
	
	return dict_age
'''

def dict_loop(dict):
	s2=[]
	s3=[]
	for name in dict:
		if dict[name]>=20 and dict[name]<30:
			s2.append(name)
		elif dict[name]>=30 and dict[name]<40:
			s3.append(name)
		
	new_info = {'30s':s3, '20s':s2}
	print new_info

info = {'Old':44, 'minsu':23, 'jisu':33, 'john':21, 'david':33, 'jisu':21, 'hary':36, 'messi':33, 'ronaldo':27}
dict_loop(info)
