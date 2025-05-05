
user_name = 'Sergey'
password = '123456'
email = 'Sergey_Martinovsky_15_007@yandex.ru'
invalid_password = '6789'

import random


def gen_email():
    login_email = ''
    domain_email = random.choice(['yandex.ru', 'mail.ru'])
    for _ in range (6):
        login_email += random.choice('abcdefghjiklmnopqrstuvwxyz1234567890')
    random_email= f"{login_email}@{domain_email}"
    return random_email

def gen_name(lenght = 8):
    random_name = random.choice('abcdefghjiklmnopqrstuvwxyz')
    return random_name(lenght)

def gen_password(lenght=4):
    random_password = random.choice('abcdefghjiklmnopqrstuvwxyz')
    return random_password(lenght)

def gen_user_data():
    user_data = {'email': gen_email(),
               'password': gen_password(),
               'name': gen_name()
               }
    return user_data
