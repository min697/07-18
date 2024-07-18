class Dog :
    def __init__(self,name,breed):
        self.dog_name = name
        self.dog_breed = breed
        self.dog_sex = "중성마녀"
    def bark(self):
        print(self.dog_name, "(이)가 짖습니다.")

my_dog = Dog("꽁식","푸들")
my_dog.bark



Dog("꽁식","푸들").bark()
Dog("꽁식","푸들").bark()
Dog("꽁식","푸들").bark()
Dog("꽁식","푸들").bark()
Dog("꽁식","푸들").bark()

