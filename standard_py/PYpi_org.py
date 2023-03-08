# TASHQI KUTUBXONA

# pip install googletrans
# translator.py
# from .googletrans import Googletrans

# class Translator:
#      def __init__(self):
#          self.googletrans = Googletrans()
# tarjimon = Translator() # Translator bu maxsus klass (tarjimon esa obyekt)
# matn_uz = "Python - dunyodagi eng mashxur dasturlash tili"
# # tarjima = tarjimon.translate(matn_uz)
# # print(tarjima.origin)
# # print(tarjima.text)
# # print(tarjima.src)

# tarjima_ru = tarjimon.translate(matn_uz, dest='ru')
# print(tarjima_ru.text)
# import requests
# from pprint import pprint

# manzil= "https://kun.uz/news/main"
# r = requests.get(manzil)
# pprint(r.text)
# import requests
# from bs4 import BeautifulSoup

# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)


# soup = BeautifulSoup(r.text, 'html.parser')
# news = soup.find_all(class_="news-title") # yangiliklarning mavzusini ajratib olamiz
# print(news[0].text) # eng birinchi yangilikni konsolga chiqaramiz