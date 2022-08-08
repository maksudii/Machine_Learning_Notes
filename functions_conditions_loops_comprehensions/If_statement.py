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

students = ["Yusuf", "Mehmet", "Melisa" , "Fatih" ]

for student in students:  # students listesinde gezin.
    print(student)

salaries = [1000, 2000, 3000, 4000]

for salary in salaries:
    print(1,5*salary + salary)  # maaşlara %50 zam yapıldı


#############################################
# break & continue & while
#############################################


salaries = [1000, 2000, 3000, 4000]

for salary in salaries:
    if  salary <= 1500   #Gelir 1500'den altında kalır ise işlemi durdur
        break

for salary in salaries:
    if  salary <= 1500   #Gelir 1500'den altında kalır ise işleme devam et
        continue

number = 5
while  number < 25: # number ifadesi 5 olana kadar devam et
    print(number)
    number += 1

#############################################
# Enumerate: Otomatik counter İndexer for Loop
#############################################
students = ["Yusuf", "Mehmet", "Melisa" , "Fatih" ]

A = []
B = []

for index, student in enumerate(students):
    print(index, student)
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)
