##############################
# Fonksiyonlar
##############################

def calculate(x):
    print(x * 2)  # Girdiyi 2 ile çarpma fonksiyonu


calculate(3)


##############################
#  Docstring açıklama ekleme
##############################
def summer(arg1, arg2):
    """

    Parameters
    ----------
    arg1
    arg2

    Returns
    -------

    """
    print(arg1 + arg2)


summer(2, 5)

##############################
# Listeye ekleme fonksiyonu
##############################
list_store = []


def add_element(a, b):
    c = a + b
    list_store.append(c)
    print(list_store)


add_element(3, 4)

add_element(5, 5)


##############################
# Ön tanımlı fonksiyonlar
##############################

def divide(a, b):
    print(a / b)


divide(5, 7)


def divide(a, b=2):  # Ön tanımlı değer oluştururken kullanılır
    print(a / b)


divide(10)


##############################
# Return değeri oluşturmak
##############################

def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge

    print(varm, moisture, charge, output)


calculate(4, 5, 6)


def standardization(a, p):
    return a * 10 / 100 * p * p


standardization(45, 1)


##############################
# Dışardan fonksiyon çağırma uygulaması
##############################

def all_calculate(varm, miosture, charge, a, p):
    print(calculate(varm, miosture, charge))
    b = standardization(a, p)
    print(b * 10)


all_calculate(3, 4, 5, 10, 9)
