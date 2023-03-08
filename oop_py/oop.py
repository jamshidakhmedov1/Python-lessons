# darsliklar

# x=10
# print(type(x))
# matn = 'salom'
# print(type(matn))
# print(matn.upper())
def salom():
    print("Assalomu alaykum")

print(type(salom))

class Talaba:
    def  __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def get_name(self):
        return self.ism

    def get_age(self,yil):
        return yil -self.tyil

    def tanishtir(self):
        return f"Ismim {self.ism} {self.familiya} tug'ilgan yilim {self.tyil}"

talaba1 = Talaba("Olim","Olimov",2000)
