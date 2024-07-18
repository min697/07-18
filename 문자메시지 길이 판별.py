# 문자메시지 길이에 따라 요금이 결정되는 프로그램
# 문자메시지의 길이에 따라 부과되는 요금은, 클래스를 생성할 때 속성 정보로 갖게 된다.
# 요금이 부과될 문자 메시지의 길이를 정할 수 있도록 설정하시오.(속성정보)
# 사용자로부터 문자메시지를 입력 받아서 문자 요금을 반환하는 코드를 작성하시오.
class 문자 :
    def __init__(self,len,p,p2):
        self.len = len
        self.p1 = p
        self.p2 = p2
    def message (self,data):
        if len(data) <= self.len :
            print(self.p1)
        else :
            print(self.p2)

dat = input("사용자 입력값")
x = 문자(200,500,1000)
x.message(dat)


