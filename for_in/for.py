# FOR LOOP


mehmonlar = ['Ali"', 'Vali', 'Husan', 'Xasan', 'Olim']
for mehmon in mehmonlar:
    print("Salom", mehmon)
    print("hayr,", mehmon)

    sonlar = list(range(1,11))
    for son in sonlar:
        print(f"{son} ning kvadrati {son**2} ga teng")


sonlar = list(range(11))
sonlar_kvadrati =[]
for son in sonlar:
    sonlar_kvadrati.append(son**2)
print(sonlar)
print(sonlar_kvadrati)


dostlar = []
print("5ta eng yaqin do'stingiz kim?")
for n in range(5):
    print(dostlar)


