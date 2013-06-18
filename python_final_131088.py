# -*- coding: utf8 -*-

'''
    자판기에 대한 고찰 :
    자판기는 일정 단위로 금액을 받는다
    받은 금액을 기준으로 살 수 있는 목록을 보여준다
    반환 버튼이 존재하여 반환버튼을 누르면 투입된 금액이 반환된다
    투입된 금액이 너무 적어 살 수 있는 품목이 없으면 자동 반환된다

'''


def get_inserted_money (my_money_dict) :

    #1: 돈을 투입합니다.
    inserted_money_sum = 0  #최종 투입된 금액

    while(True):
        
        print '\n내 주머니 상황'
        print '--------------------'
        for key,value in sorted(my_money_dict.items()):
            print "%d원이 %d개 있어요" % (key,value)

        inserted_money = raw_input('\n돈을 넣으세요(입금을 마치려면 엔터) : ')

        #엔터치면 돈 투입 끝으로 간주하고 while loop를 종료한다
        
        if not inserted_money:
            break      
        
        if inserted_money != "100" and inserted_money != "500" and inserted_money != "1000" and inserted_money != "5000" :
            print "유효한 값이 아닙니다"

        else :
            #입력 데이터를 숫자형으로 형변환 (왜냐면 $raw_input()은 숫자입력도 문자열로 입력을 받기때문)
            inserted_money = int(inserted_money)

            #투입한 만큼 지갑에서 돈을 뺀다. (해당 돈의 갯수에서 하나 빼기)
            if my_money_dict[inserted_money] == 0 :
                print "다썼어!!!"
            else :
                my_money_dict[inserted_money] -= 1  

                #누적해서 투입된 돈의 합을 표시한다.
                inserted_money_sum += inserted_money
            
            print '지금까지 %d가 투입되었네요\n' % inserted_money_sum

    #투입된 돈의 총 합이 0이상이 아니면..입금이 안된 것임
    if inserted_money_sum <= 0: 
        print '돈이 입금되지 않았네요. 프로그램 종료 합니다\n'
        return 0

    print '지금까지 %d가 투입되었네요' % inserted_money_sum
    return inserted_money_sum

def show_list(inputMoney) :
    # input된 돈을 기준으로 무엇을 살 수 있는지 출력
    # input된 돈이 남아있는 한, 반환버튼을 누르기 전까지 계속해서 주문할 수 있다

    while (True) :
        if inputMoney >= 900 :
            print "=========================="
            print "     coffee 구매 가능"
            print "     milk 구매 가능"
            print "     vita500 구매 가능"
            print "=========================="

        elif inputMoney >= 700 :
            print "=========================="
            print "     milk 구매 가능"
            print "     vita500 구매 가능"
            print "=========================="

        elif inputMoney >= 500 :
            print "=========================="
            print "     vita500 구매 가능"
            print "=========================="

        else :
            print "잔액이 모자랍니다 : ", inputMoney
            print "다음의 금액이 반환됩니다 : ", inputMoney
            break
            # 모든 코드는 이 부분에서 종결된다
            # 잔액이 없거나 반환버튼을 누르면 코드 전체가 종결된다

        your_choice = raw_input('\n마실 것을 입력하시오 (반환은 Enter) : ')
        # 입력받은 string을 기준으로 뽑을 음료수를 결정

        if not your_choice :
            print "====================================="
            print "다음의 금액이 반환되었습니다 : ", inputMoney
            print "====================================="
            charge_wallet(inputMoney)
            show_wallet(my_money_dict)
            break

        if your_choice == "coffee" :
            inputMoney -= 900
            print "=========================="
            print "남은 금액 : ", inputMoney
            print "coffee 구매하셨습니다"
            print "=========================="

        if your_choice == "milk" :
            inputMoney -= 700
            print "=========================="
            print "남은 금액 : ", inputMoney
            print "milk 구매하셨습니다"
            print "=========================="

        if your_choice == "vita500" :
            inputMoney -= 500
            print "=========================="
            print "남은 금액 : ", inputMoney
            print "vita500 구매하셨습니다"
            print "=========================="

def charge_wallet(inputMoney) :
    # 남은 잔액을 반환할 때, 다음과 같은 금액으로 반환해줌
    while(True) :
        if inputMoney >= 5000 :
            inputMoney -= 5000
            my_money_dict[5000] += 1
    
        elif inputMoney >= 1000 :
            inputMoney -= 1000
            my_money_dict[1000] += 1
    
        elif inputMoney >= 500 :
            inputMoney -= 500
            my_money_dict[500] += 1
    
        elif inputMoney >= 100 :
            inputMoney -= 100
            my_money_dict[100] += 1

        else :
            break

def show_wallet(my_money_dict) :
    # charge_wallet 함수가 잘 동작하는지 확인하기 위한 test함수
    # 동시에 사용자에게 얼마가 남았는지 보여주는 함수
    
    for key in my_money_dict :
        print key
        print my_money_dict[key]


# 메인 로직
if __name__ == '__main__':

    products_dict = {
                    'vita500'   : {'price' : 500, 'number' : 2},
                    'milk'      : {'price' : 700, 'number' : 13},
                    'coffee'    : {'price' : 900, 'number' : 8}
                    }

    #               { 돈의종류 : 돈의갯수 }
    my_money_dict = {5000 : 2 , 1000 : 1, 500 : 2 , 100 : 8}

    #돈 투입하기
    inserted_money = get_inserted_money(my_money_dict)
    show_list(inserted_money)

