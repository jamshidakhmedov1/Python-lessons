# FUNCTIONS

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")

# salom_ber()
# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib,
#     unga salom beruvchi beruvchi fuksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
     
# salom_ber('hasan')
# salom_ber('olim')

# def toliq_ism(ism, familiya):
#     """Foydalanuvchi  ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")

# # toliq_ism('olim', 'hakimov')
# # toliq_ism('hakimov', 'olim')

# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchini yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2020-tugilgan_yil} yoshda")

# # yosh_hisobla('olim', 1997)
# yosh_hisobla(tugilgan_yil=1997, ism='olim')
# toliq_ism(familiya='hakimov', ism='olim')


def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# yosh_hisobla(1995, 2020)
yosh_hisobla(1993)
