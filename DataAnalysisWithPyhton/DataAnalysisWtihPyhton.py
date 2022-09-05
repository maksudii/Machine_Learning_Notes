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

##############################
# Numpy Array Özellikleri
##############################

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

RandomVeri = np.random.randint(10, size=5)

RandomVeri.ndim #boyut sayısı
RandomVeri.shape #boyut bilgisi
RandomVeri.size #toplam eleman sayısı
RandomVeri.dtype #array veri tipi



##############################
# ReShaping
##############################

RandomVeriSet = np.random.randint(10, size=(3, 5))
RandomVeriSet.reshape(3, 3) #Üretilen Sayılardan şekillendirdi

##############################
# Index
##############################

RandomVeriSet[0]
RandomVeriSet[0:5]
RandomVeriSet[0] = 14 # Sıfırıncı indexteki sayıyı değişitirir

RandomVeriSet[1, 1] # Satır sütün index konumları

RandomVeriSet[:, 1] # Sütun Seçimi

RandomVeriSet[0:2, 0:3] # Satırdan seçimler

##############################
# Fancy Index
##############################
import numpy as np
R = np.arange(0, 30, 3)

catch = [1, 2, 3]
R[catch]  # istenilen indexleri görüntüler  # arange(start, stop, step)


##############################
# Numpy Koşullu İşlemler
##############################

n = np.array([1, 2, 3, 4, 5])

# 3'ten küçük sayıları yazdır

print("Numpy")
ab = n[n < 3]
print(ab)

print(n[n > 3])  # 3  küçükleri al
print(n[n != 3]) # 3 Harici sayıları al
print(n[n == 3]) # 3'e eşit sayıları al
print(n[n >= 3]) # 3'e büyük eşit sayıları al

# Numpy array içerisinde işlem yapılırken parantez içine yazılan işlem bütün array'e uygulanır.
#
print(n / 5)        # Her bölümü 5'e böler
print(n * 5 / 10)   # Her bölümü 5 ile çarpıp 10'a böler
print(n ** 2)       # Üslü Sayıları ifade eder
print(n - 1)        # Her sayıdan 1 çıkartır

# Numpy da matematiksel işlemleri yaparken numpy özel fonksiyonlarını da  kullanabiliriz.

print(np.subtract(n, 100))    # subtract()    Girilen değerlerden  eksiltir.
print(np.add(n, 0))         # add()         Girilen değerden sonrasında array eleman sayısınca ekler.
print(np.mean(n))           # mean()        Ortalamasını alır.
print(np.min(n))            # min()         Küçüğünü alır.
print(np.max(n))            # max()         En büyüğünü alır.
print(np.sum(n))            # sum()         Toplamını alır.
print(np.var(n))            # var()         Varyans alır



#######################
# NumPy ile İki Bilinmeyenli Denklem Çözümü
#######################

# 5x + y = 12
# x + 3y = 10

a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])
print(np.linalg.solve(a, b)) # linalg.solve() fonksiyonu ile denklemi çözümler.