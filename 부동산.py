# 건물이름 : "힐스테이트"
# 건물연식 : "2008년"

# 부동산 정보 클래스는 위치, 평수, 건물의 종류, 가격, 건물이 지어진 년도 정보를 갖는다.
# 정보 확인 함수를 사용하면 부동산 객체에 포함된 속성 정보를 화면에 출력한다.

class Building
    def __init__(self,l, a, p, y):
        self. location = l
        self. area = a
        self. price = p
        self. year = y

    def print_info(self) :
        print(self.location, self.year, self.price, self.area)

Building = Building("용인", "1995", '100억', "100평")
Building.print_info

