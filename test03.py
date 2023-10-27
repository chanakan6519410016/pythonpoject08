# OOP Object/lnstance

class IotSAU :
    # data/property/field/atribute
    major = "SAU"
    name = ""

    # method (มันคือ Funciton แต่เราไม่เรียกฟังก์ชัน)
    def showHi(self) :
        print('Hi.....')

    def introduceMySelf(self) :
        print(f'My name is {self.name}')
        print(f'My major is {self.major}')

#----------------
# สร้าง object ขึ้นต้นด้วยตัวเล็ก 
obA = IotSAU( ) # จะเป็นการเรียกใช้ constructor ของคลาสให้ทำงาน (ถ้ามี)
obB = IotSAU( ) 

# การใช้งาาน data ของ object คือ เอาค่ามันมาใช้ หรือเปลี่ยนค่าให้มันใหม่
print( obA.major)
obA.major = "Wow"
obA.name = "ฟ้าร้องดัง"
obB.name = "ฝนตกอีกแล้ว"

# การใช้งาาน method ของ data ของ object คือ สั่งให้เมธอด object นั้น ๆ ทำงาน
obA.introduceMySelf()
obB.introduceMySelf()

