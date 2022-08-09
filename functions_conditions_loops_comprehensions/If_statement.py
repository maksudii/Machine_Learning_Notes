#############################################
# IF & ELSE DÖNGÜLERİ
#############################################

def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")


number_check(15)


#############################################
# ELIF DÖNGÜLERİ
#############################################
def doub_number_check(number):
    if number == 10:
        print("number is 10")
    elif number >= 10:
        print("number could be higher than 10")
    elif number <= 10:
        print("number could lower than 10")


number_check(15)

#############################################
# FOR DÖNGÜLERİ
#############################################

students = ["Yusuf", "Mehmet", "Melisa", "Fatih"]

for student in students:  # students listesinde gezin.
    print(student)

salaries = [1000, 2000, 3000, 4000]

for salary in salaries:
    print(1, 5 * salary + salary)  # maaşlara %50 zam yapıldı

#############################################
# break & continue & while
#############################################


salaries = [1000, 2000, 3000, 4000]

for salary in salaries:
    if salary <= 1500:  # Gelir 1500'den altında kalır ise işlemi durdur
        break

for salary in salaries:
    if salary <= 1500:  # Gelir 1500'den altında kalır ise işleme devam et
        continue

number = 5
while number < 25:  # number ifadesi 5 olana kadar devam et
    print(number)
    number += 1

#############################################
# Enumerate: Otomatik counter İndexer for Loop
#############################################
students = ["Yusuf", "Mehmet", "Melisa", "Fatih"]

A = []
B = []

for index, student in enumerate(students):
    print(index, student)
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

#############################################
# Uygulama - Mülakat Sorusu, Enumerate
#############################################
# divide_students fonksiyonunu yazınız.
# Çift indexte yer alan öğrencileri bir listelemeye alınız.
# Tek indexte yer alan öğrencileri başka bir listeye alınız.
# Fakat bu iki liste tek bir liste olarak olsun.

students = ["Yusuf", "Mehmet", "Melisa", "Fatih"]


def divide_student(students):  # Listedeki elemenalrı index numaralarına göre gruplara ayrılması
    group = ([], [])
    for index, student in enumerate(students):
        if index % 2 == 0:
            group[0].append(student)
        else:
            group[1].append(student)
    print(group)
    return group


divide_student(students)

st = divide_student(students)
st[0]
st[1]


#############################################
# Lambda, Map , Apply Fonksiyonu
#############################################

def summer(x, y):
    return x + y


summer(1, 3) * 9

new_sum = lambda a, b: a + b  # lambda Kullan at fonksiyonlardır

##########################################################################################
##########################################################################################

salaries = [1000, 2000, 3000, 4000, 5000]


def new_salaries(x):
    return x + 20 / 100 * x


new_salaries(5000)

for salary in salaries:
    print(new_salaries(salary))

list(map(new_salaries, salaries))

list(
    map(lambda x: x * 20 / 100 * x, salaries))  # Yukardaki döngü işlemini tek satır ve tek seferlik bir şekilde yazıldı

# FILTER
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store))

# REDUCE
from functools import reduce

list_store = [1, 2, 3, 4]
reduce(lambda a, b,: a + b, list_store)
