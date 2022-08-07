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




