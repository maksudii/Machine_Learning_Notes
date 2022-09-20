#################################
# Pandas Kütüphanesi
#################################
# Pandas Serileri
#################################

import pandas as pd
import seaborn as sns
import numpy as np

s = pd.Series([10, 77, 12, 4, 5])
print(s)            # Hücreleri numarandırılır
print(type(s))      # Serilerin türleri sogular
print(s.index)      # İndexi oluşturulur.
print(s.dtype)      # Serilerin tipini verir.
print(s.size)       # Boyutunu türünü verir.
print(s.ndim)       # Liste sayısını verir.
print(s.values)     # Değerlerin yazdırır.
print(type(s.values))
print(s.head(3))    # Başındaki 3 değerini verir.
print(s.tail(3))    # Sonundaki 3 değerini verir.

# Veri Okuma (Reading Data)
df = pd.read_csv("datasets/advertising.csv")
# .read_csv() ile csv dosyasını pandas serisi olarak okur.
print(df.head())
a = sns.load_dataset("titanic")  # .load_dataset() ile titanic verisetini pandas serisi olarak okur.
print(a.head())
print(a.tail())
print(a.shape)                      # csv dosyasının boyutlarını verir.
print(a.info())                     # Veri setinin bilgilerini verir( Kolon, Dosya tipleri, Boşlukları, değişken tipleri, boyut büyüklüğü.)
print(a.columns)                    # Veri setinin sütun sayılarını verir.
print(a.index)                      # Veri setinin indexlerini verir.
print(a.describe().T)               # Veri setinin özet bilgilerini verir. T ile transpose edilir.
print(a.isnull().values.any())      # .isnull() ile veri setinin boş değerlerinin varlığını yazdırır. isnull().values.any() ile boş değerlerin varlığını yazdırır
print(a.isnull().sum())             # isnull().sum() ile veri setinin boş değerlerin toplam sayısını verir.
print(a["sex"].head())              # Seçilen cinsiyetin head'ini yazdırır
print(a["sex"].value_counts())      # Seçilen kolondaki özeti verir

################################################
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
################################################
print(a.index)          # İndex Özeti
print(a[0: 13])         # Listeden satır seçim,

# .drop() ile silme işlemi yapılır. Inplace = true yaparsak kalıcı silme işlemi gerçekleştirir.
# axis = 0 yaparsak satırları siler.
# axis = 1 yaparsak sütunları siler.
print(a.drop(0, axis=0).head) # Yani sıfırıncı satır silinir.

delete_indexes = [1, 3, 5, 7]
print(a.drop(delete_indexes, axis=0).head(10))

# a = a.drop(delete_indexes, axis=0)
# a.drop(delete_indexes, axis=0, inplace=True)

# Değişkeni Indexe Çevirmek
print(a["age"].head())
print(a.age.head())

a.index = a["age"]  # Indexi değişkene çevirme
a["age"] = a.index  # Değişkeni Indexe çevirme

# reset_index() ile indexleri sıfırlar.
print(a.drop("age", axis=1, inplace=True))
print(a.reset_index().head())
a = a.reset_index()
print(a.head())

# Değişkenler Üzerinde İşlemler
pd.set_option('display.max_columns', None)  # .set_option() ile pandas'ın görüntülenmesini kısıtlar.

print("age" in a)  # in ile değişkenin varlığını kontrol eder.
print(a["age"].head())
print(a.age.head())
print(type(a["age"].head()))
print(a[["age"]].head())
print(type(a[["age"]].head()))

print(a[["age", "alive"]])
# Data frame kalması için iki köşeli parantez kullanılır.

col_names = ["age", "adult_male", "alive"]
print(a[col_names])                     #Titanic Veri setinden seçilen sütunları yazdırır

a["age2"] = a["age"] ** 2               # Yaşların karesini alarak yeni sütun oluşturur
print(a)

a["age3"] = a["age"] / a["age2"]        # Oluşturulan yaşlar karesini yaşlara böler
print(a)

print(a.drop("age3", axis=1).head())    # Karesini alip böldüğümüz Age3 Sütununu droplar

print(a.drop(col_names, axis=1).head())
print(a.loc[:, ~a.columns.str.contains("age")].head())  # ~ a.columns.str.contains("age") ile age sütunu  yok eder.

# iloc: integer based selection. iloc ile sütun ve satır seçimi yapılır.
print(a.iloc[0: 3])
print(a.iloc[0, 0])  # iloc [   satir, sutun]

# loc: label based selection. Dizinden belirli bir sütun veya satır seçimi yapılır.
print(a.loc[0: 3])      # Satırdan ve Sütundan 3'er değişken seç

print(a.iloc[0:3, 0:3])     # Satır Sütun Seçimi
print(a.loc[0:3, "age"])    # Sütun sayısını

col_names = ["age", "embarked", "alive"]
print(a.loc[0:3, col_names])

# loc ile sütun ismine göre sutun seçimi yapılır. Ama iloc ile sutun ismine göre sutun seçimi yapılamaz.

# Koşullu Seçim (Conditional Selection)
print(a[a["age"] > 50].head())                              # age sütunu 50 den büyük olanları seçer.
print(a[a["age"] > 50].count())                             # age sütunu 50 den büyük olanların sayısını verir.
print(a.loc[a["age"] > 50, ["age", "class"]].head())        # age sütunu 50 den büyük olanların age ve class sütunlarını seçer.
print(a.loc[(a["age"] > 50) & (a["sex"] == "male"), ["age", "class"]].head())  # Yaşı 50'den büyük ve cinsiyeti erkek olan age ve class koşullarını seç.
df_new = a.loc[(a["age"] > 50) & (a["sex"] == "male") & (
        (a["embark_town"] == "Cherbourg") | (a["embark_town"] == "Southampton")), ["age", "class", "embark_town"]]
# Yaşı 50'den büyük ve cinsiyeti erkek olanları ve Cherbourg ve Southampton'da olanları seç. age, class, embark_town sütunlarını yaz.

print(df_new["embark_town"].value_counts()) # Atanan değerleri saydırır

df = pd.DataFrame(a)
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
print(df.count())        # - count()     Say
print(df.first())        # - first()     İlk Değer
print(df.last())         # - last()      Son Değer
print(df.mean())         # - mean()      Ortalaması
print(df.median())       # - median()    Medyanı
print(df.min())          # - min()       Minimum Değeri
print(df.max())          # - max()       Max Değeri
print(df.std())          # - std()       Standart Sapma
print(df.var())          # - var()
print(df.sum())          # - sum()       Toplam
                        # - pivot table

print(a["age"].mean())

# groupby() ile gruplama yapılır.
# Cinsiyete göre yaş ortalamasını ekrana yazdırır.
print(a.groupby("sex")["age"].mean())

print(a.groupby("sex").agg({"age": "mean"}))
print(a.groupby("sex").agg({"age": ["mean", "sum"]}))  # Cinsiyete göre yaş ortalamasını ve yaş toplamını alır.

print(a.groupby("sex").agg({"age": ["mean", "sum"],
                            "survived": "mean"}))

print(a.groupby(["sex", "embark_town"]).agg({"age": ["mean"], "survived": "mean"}))

print(a.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"], "survived": "mean"}))

print(a.groupby(["sex", "embark_town", "class"]).agg(
    {"age": ["mean"],
     "survived": "mean",
     "sex": "count"}))

# Pivot table
print(a.pivot_table("survived", "sex", "embarked"))
print(a.pivot_table("survived", "sex", ["embarked", "class"]))
a["new_age"] = pd.cut(a["age"],
                      [0, 10, 18, 25, 40, 90])  # pd.cut() fonksiyonuyla birlikte aralıklar belirlenerek sınıflar
print(a.pivot_table("survived", "sex", ["new_age", "class"]))
pd.set_option('display.width', 500)

# Apply ve Lambda
# apply() fonksiyonu içerisinde lambda kullanarak var olan değişken içerisinde değişiklik yapılır veya DataFrame içerisinde yer alan değişkenlerden yeni değişkenler türetilebilir.

a["age2"] = a["age"] * 2
a["age3"] = a["age"] * 5
print(a)

print((a["age"] / 10).head())
print((a["age2"] / 10).head())
print((a["age3"] / 10).head())

for col in a.columns:
    if "age" in col:
        print(col)

for col in a.columns:
    if "age" in col:
        print((a[col] / 10).head())

for col in a.columns:
    if "age" in col:
        a[col] = a[col] // 10

print(a.head)               # Başlangıcını Göster

print(a[["age", "age2", "age3"]].apply(lambda x: x / 10).head())



print(a.loc[:, a.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head())

def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

print(a.loc[:, a.columns.str.contains("age")].apply(standart_scaler).head())

a.loc[:, a.columns.str.contains("age")] = a.loc[:, a.columns.str.contains("age")].apply(standart_scaler)


print(a.head())

# Birleştirme (Join) İşlemleri
m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

print(pd.concat([df1, df2]))

print(pd.concat([df1, df2], ignore_index=True))
# Merge ile Birleştirme İşlemleri


df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

print(pd.merge(df1, df2))
print(pd.merge(df1, df2, on="employees"))

# Amaç: Her çalışanın müdürünün bilgisine erişmek istiyoruz.
df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})

print(pd.merge(df3, df4))

# concat() fonksiyonu ile birleştirme işlemleri yapılır.
# merge() fonksiyonu ile birleştirme işlemleri yapılır.

import pandas as pd
series = pd.Series ( [ 1,2,3 ] )
series ** 2