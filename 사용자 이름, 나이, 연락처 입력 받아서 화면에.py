# 사용자의 이름, 나이, 연락처를 입력받아서 화면에
# '입력하신 이름은 ㅇㅇㅇ이며, 나이는 ㅇㅇ, 그리고 연락처는 ㅇㅇㅇ-ㅇㅇㅇㅇ-ㅇㅇㅇㅇ입니다.'를
# 출력하는 클래스를 작성하시오.
class user :
    def __init__(self, name, old, phone):
        self.user_name = name
        self.user_old = old
        self.user_phone = phone

    def user(self):
        print(self.user_name,self.user_old,self.user_phone)

data_1 = input("이름이 뭐야")
data_2 = input("몇살이야")
data_3 = input("전화번호 뭐야")

my_person = Person