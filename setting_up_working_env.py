####################################
#Virtual Env ve Paket Yöneticisi
####################################

# Sanal ortamların listelenmesi
# conda env list
# conda create -n myenv //Alt Env Oluştururken

# conda upgrade -all


####################################
# Veri Yapıları
####################################

long_str = """Veri Yapıları: Hızlı Özet,
Sayıları: int, float, complex
Karakter Dizileri: str, List, Dic, Tuple, Set
Boolean (TRUE-FALSE): bool """

####################################
# Karakter Dizilerine Erişim
####################################

name = 'John'
long_str[0:10]

"veri" in long_str

####################################
# String Metodları
####################################

dir(str)


####################################
# len
####################################

type(name)
type(len)
len(name)

####################################
# upper() & lower()
####################################

a = "miuul".upper()
b = a.lower()

print(a,b)

####################################
# replace: karakter değiştir
####################################

hi = "Hello AI era"
hi.replace("l", "p")

####################################
# split: böler
####################################

"Hello AI Era".split(" ")
"""['Hello', 'AI', 'Era']"""

" ofofo ".strip()
"ofofo".strip("o")

####################################
# capitlaze: ilk harfi büyütür
####################################
"foo".capitalize()

dir("foo")

####################################
# list
####################################

notes = [99 , 2, 3 ,100]
len(notes)
type(notes)

notes.insert(2 , 99)
notes.insert(4, 100)
notes.insert(3, 100)

####################################
# Sözlük
####################################

dictionary = {"REG":["RMSE",10],
              "LOG":["MSE",20],
              "CART":["SSE",30]}
dictionary = {"REG": 10,
              "LOG":20,
              "CART":30}
####################################
# Key Sorgulama
####################################

"RE" in dictionary

####################################
# Key'e Value Sorgulama
####################################

dictionary["REG"]
dictionary.get("REG")

####################################
# Value Değiştirmek
####################################

dictionary["REG"] = ["YSA", 10]

####################################
# Tüm Key'lere Değiştirmek
####################################

dictionary.values()

####################################
# Tüm Key'leri Tuple'ye Değiştirmek
####################################

dictionary.items()

####################################
#  Key'lerin değerini güncellemek
####################################

dictionary.update({"REG":11})


####################################
#  Key'lerin değerini güncellemek
####################################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.difference(set2) # set1-set2
set2.difference(set1) # set2-set1

set1.symmetric_difference(set2) #Simetrik farklar

set1.intersection(set2) #Kesişim

set1.union(set2) #iki küme birleşimi

set1.isdisjoint(set2) #iki kesişim boş mu

set2.issuperset(set1) #Bir küme diğerini kapsıyor mu?

