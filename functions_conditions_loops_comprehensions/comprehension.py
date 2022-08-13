#############################################
# Comprehensions
#############################################

#############################################
# List Comprehensions
#############################################
from functions_conditions_loops_comprehensions.If_statement import students

salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(x):
    return x * 20 / 100 + x


for salary in salaries:
    print(new_salary(salary))

null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))  # Gelir listesindeski hepsini listeye ekleyin

for salary in salaries:
    if salary > 3000:  # Gelir seviyesi 3000 üzerinde ise boş listeye ekle
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))  # Değil ise iki ile çarpıp öyle ekle

[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

[salary * 2 for salary in salaries]  # Compreshension list şeklinde yazım şekilleri

[salary * 2 for salary in salaries if
 salary < 3000]  # Comprehension yazım şekli ile 3000 for döngüsünün sol kısmına yerleştirilir

[salary * 2 if salary < 3000 else salary * 0 for salary in
 salary]  # Comprehension else geldiğinde if'in else sol kısma yazılır

[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in
 salaries]  # List if ve for döngüsünün aynı anda kullanımı

students = ["John", "Mark"]

student_no = ["John", "Vennessa"]

[student.lower() if student in student_no else student.upper() for student in
 students]  # Öğrenci listesindeki kişilerin küçük harflere dönüştür ['john', 'MARK']

[student.lower() if student not in student_no else student.upper() for student in
 students]  # Öğrenci listesinde olmayanları küçük harfe Dönüştürür. ['JOHN', 'mark']

#############################################
# Dic Comprehensions
#############################################

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}
dictionary.keys()  # Kelimeler
dictionary.values()  # Değerler
dictionary.items()  # Dic'te elemanları

{k: v ** 2 for (k, v) in dictionary.items()}  # Keyleri ve değerlerin karesi alınır

{k.upper(): v for (k, v) in dictionary.items()}  # Key ve değerleri Büyük harf çevrilmesi

{k.upper(): v * 2 for (k, v) in dictionary.items()}  # Key ve değeleri iki katı ile çarpılır

#############################################
# Comprehensions - Mülakat soruları
#############################################

# Amaç: çift sayıların karesi alınarak bir sözlüğe eklenmek istemektedir.

# Listedeki Çift sayıları yakala karesini al ve dic'e ekle

c = range(50)
a = 0
b = []
new_dic = {}

while a < 50:  # 50'ye kadar liste oluştur
    a += 1
    b.append(a)

for n in b:  # Oluşturduğun listedeki b sayılarında n ile gezin
    if n % 2 == 0:  # n sayısı 2'ye bölündükten sonra sıfır'a eşit ise
        new_dic[n] = n ** 2  # n sayısının karesini al ve sözlüğe ekle

{n: n ** 2 for n in b if n % 2 == 0}  # Yukardaki yöntemin comprehension şeklinde yazımı

import seaborn as sns

df = sns.load_dataset ("car_crashes")
df.columns

df
num_cols = [col for col in df.columns if df[col].dtype != 0]
soz = {}
agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list

new_dic = {col : agg_list for col in num_cols}

df[num_cols].head()

df[num_cols].agg(new_dic)

