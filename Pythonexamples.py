
#Bazı şehir isimleri içeren bir liste oluşturulur.
sehirler = ["Ankara","Amasya","İstanbul","Adana","Bursa","Kars","Rize"]

#Listeye iki şehir ismi daha eklenir. Extend() metodu kullanılarak.
sehirler.extend(["Edirne","Aydın"])

print(sehirler)

#İstanbul şehirinin indeks değeri index() metodu ile bulunur.
istanbul_index = sehirler.index("İstanbul",0)

print(istanbul_index)

#Pop ile listeden eleman silme işlemi yapılır.
remove_city = sehirler.pop(istanbul_index)

#Listenşn yeni hali:
print(sehirler)


#Listeyi alfabetik sıraya göre sıralamak için sorted() metodu kullanılır.
alfabetik_sıra = sorted(sehirler)
print(alfabetik_sıra)





