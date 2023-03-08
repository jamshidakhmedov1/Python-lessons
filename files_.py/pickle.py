# fayllar 
# file = open('pi.txt')
# PI = file.read()
# print(PI)
# file.close()
# pi = 3.14565878678966856786789
# with open('pi.txt') as file:
#     pi = file.read()

# print(pi)
# pi = pi.rstrip()
# pi = pi.replace('\n','')
# pi = float(pi)
# print(pi)

# filename = 'data/talabalar.txt'
# with open(filename) as file:
#     for line in file:
#         print(line)

# with open(filename) as file:
#     talabalar = file.readlines()

# print(talabalar)


import pickle 

talaba1 = {'ism':'hasan',  'familiya':'husanov', 'tyil':2003, 'kurs': 2}
talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

with open('info.pkl','wb') as file:
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)

import pickle

with open('info','rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)

print(talaba1)
print(talaba2)

     