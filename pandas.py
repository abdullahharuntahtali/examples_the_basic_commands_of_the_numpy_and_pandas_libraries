# -*- coding: utf-8 -*-
import pandas as pd

dictionary={"Name" :["ali","veli","ayse","hatice","osman","mehmet"],
            "Age" :[15,40,30,60,19,25],
            "Maas" :[300,800,1000,850,100,250]}

dataframe=pd.DataFrame(dictionary) #DataFrame oluşturduk

#.head() datayı önizlemek için içinde ne olduğunu görmek için kullanılır
head=dataframe.head() #İlk 5 veriyi verir.Diğerlerini vermez

tail=dataframe.tail()#Son 5 veri verir.

head1=dataframe.head(3)#İlk 3 veriyi verir

#%%
#pandas basic method

print(dataframe.columns) #sütun isimlerini verir(columns)
print(dataframe.info())#dataframe hakkında bilgi verir

print(dataframe.dtypes)#dataframe hakkında özet bilgi verir

#count=6 yani 6 satırn var
#mean= sütunların ortalamlarını verir
#std standart sapmayı verir.
#min= sütunların min değerini verir
#max= sütunların max değerini verir
#%25 vs sonra öğrenirim
print(dataframe.describe())#sayısal özellikteki sütunları verir.

#%%
#indexing and slicing

print(dataframe["Name"]) #Name sütununu ve indexlerini  çektik

print(dataframe.Name) #Name sütununu ve indexlerini çektik.Yukarıdaki ile aynı işi yapar

dataframe["yeni_ozellik"]=[-1,-2,-3,-4,-5,-6] #Yeni sütun oluşturduk

print(dataframe.yeni_ozellik)
print(dataframe.loc[:,"Name"])
print(dataframe.loc[1:3,"Name":"Age"])
print(dataframe.loc[::-1,:])
print(dataframe.loc[:,:"Age"])
print(dataframe.iloc[:,:2]) #integer location


#%%

#filtering

filtre1=dataframe.Maas>500 #False ve True değerleri döndürür.Büyük olanlar True alır

filtrelenmis_data=dataframe[filtre1] #Maası 500ün üzerindekileri içeren dataframe oluşturdu

filtre2=dataframe.Age<35
print(dataframe[filtre1 & filtre2])

#%% list comprehension
import numpy as np
ortalama_maas=dataframe.Maas.mean()
print(ortalama_maas)
ortalama_maas_np=np.mean(dataframe.Maas) #numpy ile ortalama maas
print(ortalama_maas_np)

dataframe["maas_seviyesi"]=["Yüksek" if ortalama_maas<each  else "Düşük" for each in dataframe.Maas]


dataframe.columns=[each.lower() for each in dataframe.columns] #Sütun isimlerini küçük harf yaptık

#alttaki işlemde boşluk içeren sütun adlarını birleştirdik maas seviyesi-->maas_seviyesi
dataframe.columns=[each.split()[0]+"_"+each.split()[1] if len(each.split())>1 else each for each in dataframe.columns]

#%% drop and concatenating

#axis=1
#inplace=True yaparsan içeriği axise göre komple değiştirir.
dataframe.drop(["yeni_ozellik"],axis=1,inplace=True)

data1=dataframe.head()
data2=dataframe.tail()
#vertical yukarıdan aşağı birleştir
data_concat=pd.concat([data1,data2],axis=0)
#horizontal
maas=dataframe.maas
age=dataframe.age

data_h_concat=pd.concat([maas,age],axis=1)


#%%

#transforming data

dataframe["list_comp"]=[each*2 for each in dataframe.age]

#apply() yukarıdaki işlemi yapıyor.
def multiply(age):
    return age*2
dataframe["apply_metodu"]=dataframe.age.apply(multiply)




