#치킨판매 관련 예외처리 

chicken = 10
wating = 1

class SoldOutError(Exception) :
    pass

while(True):
    try:
        print('[남은치킨] : {0}]'.format(chicken))
        order = int(input('몇마리 주문하시겠습니까?'))
        if order > chicken : #주문이 치킨남은 수량보다 많을 때
            print('재료가 소진되었습니다')
        elif order <= 0 :
            raise ValueError
        else :
            print('대기번호 {0} : {1} 마리 주문 완료되었습니다.'.format(wating, order))
            wating += 1
            chicken -= order

            if chicken == 0 :
                raise SoldOutError
            
    except ValueError :
        print('잘못된 값을 입력하였습니다.')
    except SoldOutError :
        print('재료가 소진되어 더이상 주문을 받을 수 없습니다')
        break