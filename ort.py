def dizi_ort(dizi):
    toplam=0
    ortalama=0
    for i in range(0,len(dizi)):
        toplam+=dizi[i]
        ortalama=toplam/len(dizi)

    print(toplam)
    print(ortalama)



dizi=[10,23,45,89,52]
dizi_ort(dizi)