# 게임 캐릭터 생성 클래스는 아이디, 성별, 직업 정보를 갖으며, 기본 공격 함수를 갖는다.
# 기본 공격 함수는 사용시 '공격!' 문자열을 화면에 출력한다.
class char :
    def __init__(self,id,sex,wi):
        self.id = id
        self.sex = sex
        self.wi = wi



    def attack(self, 정준하):
        print(self.id, ": 죽어!",정준하,":♨")




c = char("박명수","남","쩜오")
c.attack()
