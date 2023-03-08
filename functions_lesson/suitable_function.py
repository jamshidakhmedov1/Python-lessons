# MOSLASHUVCHAN FUNKSIYALAR

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#              'model':model,
#              'rangi':rangi,
#              'korobka':korobka,
#              'yil':yili,
#              'narh':narhi}
#     return avto

# avto1 = avto_info('GM', 'Malibu', 'Qora','Avtomat', 2018)
# avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanika',2016,15000)
# avtolar = (avto1, avto2)
# print("Onlayn bozordagi avto mashinalar:")

# def oraliq(min,max):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar

# print(oraliq(0,11))
# print(oraliq(10,21)) 

# def summa(x,y,*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return x+y+sum(sonlar)
# print(summa(1,2))
# print(summa(1,2,3,4,5,))
# print(summa(4,5,6,7))


# def avto_info(kompaniya, model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at korinishida qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar

# avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
# avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000, yil=2020)
# print(avto1)
# print(avto2)


