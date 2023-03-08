
from googletrans import Translator

tarjimon = Translator()

msg = 'Tarjima uchun so\'z kiriting (chiqib ketish uchun "q" deb yozing): '
while True:
    text = input(msg)
    if text == "q":
        break
    else:
        tarjima = tarjimon.translate(text, src="uz", dest="en")
        print(tarjima.text)
from googletrans import Translator

tarjimon = Translator()  # Translator bu maxsus klass (tarjimon esa obyekt)

matn_uz = "Python - dunyodagi eng mashxur dasturlash tili"

# Istalgan matnni ingliz tiliga tarjima qilish uchun tranlsate metodini chariqamiz
tarjima = tarjimon.translate(matn_uz)
# Original matn
# print(tarjima.origin)
# # Tarjima
# print(tarjima.text)
# # Original matn tili
# print(tarjima.src)

# # Boshqa tilga tarjima qilish uchun dest parametridan foydalanamiz
tarjima_ru = tarjimon.translate(matn_uz, dest="ru")
# print(tarjima_ru.text)

# # Ingliz tilidan tarjima
matn_en = "Tashkent is the capital of Uzbekistan"
tarjima_uz = tarjimon.translate(matn_en, dest="uz")
print(tarjima_uz.text)
