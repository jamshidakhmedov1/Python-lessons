# functions_

# def toliq_ism_yasa(ism, familiya):
#     """Toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     print(toliq_ism)
#     return toliq_ism

# toliq_ism_yasa("olim", "olimov")

# talaba1 = toliq_ism_yasa('olim', 'hakimov')
# talaba2 = toliq_ism_yasa('hakim', 'olimov')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# print(f"{talaba1} dasrga kechikib keldi")

def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yili':yili,
            'narhi':narhi}
    return avto
# avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
# avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanika', 2016,15000)
# avtolar = [avto1, avto2]


# print('Onlayn bozordagi mavjud mashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

# def oraliq(min, max):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# print(oraliq(0,10))
# print(oraliq(10,21))


print("Saytimizda avtolar ro'yxatini shakllantiramiz.")
avtolar=[]
while True:
    print("\nQuyidagi ma'lumotlarni kiriting",end='')
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rangi=input("Rangi")
    korobka=input("Korobka")
    yili=("Ishlab chiqargan yili: ")
    narhi=input("Narhi: ")
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break
print("\nSalonimizdagi avtolar:")
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narhi: {narh}")
    