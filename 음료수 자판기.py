# -*- coding: utf-8 -*-

myMoney = 10000
givenMoney = 0
countT = 0
drinkList 		#딕셔너리
remainList  	#딕셔너리

def insertMoney(money) :
	if money == 1000 :
		if countT == 0 :
			countT++
			givenMoney += 1000
		else :
			print "천원은 한장만!!!"

	if money == 500 :
		givenMoney += 500

	if money == 100 :
		givenMoney += 100

	if money == 50 :
		givenMoney += 50				
	
	return givenMoney

def showGivenMoney() :
	print givenMoney

def showRemainMoney() :
	print myMoney - givenMoney

def returnMoney() :
	# 큰 단위부터 차례차례 반환
	while givenMoney >= 1000 :
		givenMoney - 1000
		print "1000원 반환"
	
	while givenMoney >= 500 :
		givenMoney - 500
		print "500원 반환"
	
	while givenMoney >= 100 :
		givenMoney - 100
		print "100원 반환"
	
	while givenMoney >= 50 :
		givenMoney - 50
		print "50원 반환"

def showDrink(drinkList) :
	# 딕셔너리 drinkList로 받은 음료수 이름과 가격을 표시
	# 재고관리 remainList와 비교, 재고가 없다면 불가 표시

def selectDrink(drinkName) :
	# 선택된 음료수 remainList에서 --, givenMoney에서 가격만큼 감소
	# 만약 remainList가 0이라면 재선택 알림!!!
	# print drinkName 나온다

	# if 남은 돈이 < 100 :
	#	자동 반환
