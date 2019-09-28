import numpy as np
array=np.array([1,2,3,4,5,6,7,8,9,10,11,12]) #1*12 vector
print(array.shape)
a=array.reshape(2,6)
print("shape : ",a)
print("dimension : ",a.ndim)
print("data type : ",a.dtype.name)
print("size : ",a.size)
print("array : ",type(a))

array1=np.array([[1,2,3],[4,5,6],[7,8,9]])

zeros=np.zeros((3,4))
print(zeros)
zeros[0,0]=1
print(zeros)

#one= np.ones((3,4))
#empty=np.empty((3,4))
a=np.arange(10,50,5)
print(a)
a=np.arange(1,15,1.5)
print(a)
a=np.linspace(10,50,6) #10-50 arası 6 boyutlu dizi üretti
print(a)


#%%

a=np.array([1,2,3])
b=np.array([4,5,6])
print("Toplamı : ",a+b)
print("Çıkarma :",a-b)
print("karesi : ",a**2)

print("sinüsü : ",np.sin(a))
print("2den küçük olanlar : ",a<2) #Küçükse true

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2,3],[4,5,6]])

print("satır ve sütunları aynı olanlarınçarpımları : ",a*b)

#matris çarpımı (birinci matrisin sütunu ile ikinci matrisin satırı aynı uzunlukta olmalı)
print(a.dot(b.T)) #bnin transpozuunu alarak hatayı ortadan kaldırdık.a.dot(b) hata verir deneyin

print(np.exp(a))

a=np.random.random((5,5))
print(a.max())
print(a.min())
print(a.sum())
print(a.sum(axis=0))# sütunları toplar
print(a.sum(axis=1))# satırları toplar

print(np.sqrt(a))#karekökünü alır
print(np.square(a))# karesini alır

np.add(a,a) #a+a işlemini yapar

#%%
#numpy tekrardan import et yeniden başlattığında
array=np.array([1,2,3,4,5,6,7])# vector dimension=1 yani tek boyutlu

print(array[0:4])
reverse_array=array[::-1]
print(reverse_array)

array1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array1[1,1])

print("1. sütunu verir komple",array1[:,1])
print("1. satırı verir komple",array1[1,:])

print("1. satırın 1.,2.,3. elemanı",array1[1,1:4])

print("son satırı verir",array1[-1:])
print("son sütunu verir",array1[:-1])


#%%

#shape manipulation
array=np.array([[1,2,3],[4,5,6],[7,8,9]])


#flatten
a=array.ravel() # matrisi vector haline getirir.Tek satıra indirger

array2=a.reshape(3,3) #Tek satıra indirgediğimizi tekrardan 3e 3 matris yapar

arrayT=array2.T #transpozesini aldı

print("boyutunu verir(shape) ",arrayT.shape)

array3=np.array([[1,2],[3,4],[4,5]])
print("matrisi 2ye 3 yaptık",array3.reshape(2,3))


#%%
array1=np.array([[1,2],[3,4]])
array2=np.array([[-1,-2],[-3,-4]])

#vertical dikey birleştirir
array3=np.vstack((array1,array2))
#horizontal yatay birleştirme
array4=np.hstack((array1,array2))


#%%

#convert and copy

liste=[1,2,3,4] #liste
array=np.array([5,6,7,8]) #dizi
array=np.array(liste) # listeden diziye böyle geçilir

liste2=list(array)# diziyi listeye çevirme
print(type(liste2))


a=np.array([1,2,3])
b=a
c=b
b[0]=5
print(a) #byi değiştirisen b değişir.Çünkü bir hafıza alanını kullanıyor 3 değişken.
print(c) #byi değiştirirsen c değişir

#değişmesini istemiyorsan her değişken için hafıza aç
d=np.array([1,2,3])

e=d.copy()
e[0]=5
print(d)
print(e)