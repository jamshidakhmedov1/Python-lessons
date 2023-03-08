ism = "Anvar"


shahar = "Qo'qon"
viloyat = "Fargona"
matn = "Men yangi 📱 oldim"
smayl = "😆"
print(matn)

# STRING USTIDA AMALLAR


ism = 'Ahmad'
print("Mening ismim " + ism)
ism = 'Ahad'
familiya = 'Qayum'
print(ism +familiya)
print(ism + ' ' + familiya)


# f-string

ism = "Ahad"
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)


ism = "James"
familiya = 'Bond'
print( f"Salom, Mening ismim {familiya}.{ism} {familiya}!")


# MAHSUS BELGILAR


print('Hello World!')
print('Hello \tWorld!')
print('Hello \nWorld')

# STRING METODLAR

ism = 'james'
familiya = 'bond'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper())
print(ism_sharif.lower())
print(ism_sharif.title())
print(ism_sharif.capitalize())
meva = "   olma  "
print("Men " + meva.lstrip() + " yaxshi ko'raman")
print("Men " + meva.rstrip() + " yaxshi ko'raman")
print("Men " + meva.strip() +" yaxshi ko'raman")
print("Men " + meva + " yaxshi ko'raman")



# INPUT

ism = input("ismingiz nima?")
print("Assalomu alaykum, " + ism)

ism = input("Ismingiz nima?\n>>>")
print("Assalomu alaykum, " + ism.title())



