# FUNKSIYALARNI TEKSHIRISH

def get_full_name(ism, familiya, otasi=''):
    if otasi:
        return f"{ism} {otasi} {familiya}".title()
    else:
        f"{ism} {otasi} {familiya}".title()

print(get_full_name('alijon', 'olimovich', 'valiyev'))

