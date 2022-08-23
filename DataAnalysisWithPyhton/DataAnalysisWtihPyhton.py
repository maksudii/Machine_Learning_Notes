##############################
# Numpy
##############################

# Verimli veri saklama ve Vektörel işlemler yapar
# Sabit veri tutar.Fixpy ile hızlı işlem yapmayı sağlar
# Array seviyesinde işlemlerle kısa ve öz işlemeler yapar


import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range (0, len(a)): # Normal Pyhton ile yapılabilcek işlemler
    ab.append(a[i] * b[i])

a = np.array([1, 2, 3, 4]) # Numpy ile işlemin sadeleşmiş hali
b = np.array([2, 3, 4, 5])

a * b

np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

np.zeros(10, dtype=int)  # sıfırlardan oluşan int'lar oluşturdu zeros

np.random.random_integers(0 , 10 , size= 10) # Belirlenen sayılar arasında rastegele sayı seçim fonksiyonu

np.random.normal(10 , 4 , (3,4)) #ortalaması 10 St.Sapması 4 olan 4'e 3 oranında tablo oluşurdu






