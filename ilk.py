vize = input("Vize notunuzu girin:")
final = input("Final notunuzu girin:")
v1 = int(vize) * 0.4
f1 = int(final) * 0.6
ortalama = v1 + f1
if ortalama < 60:
    print("Öğrenci ortalaması 60'tan küçük Büte girecek")
    but = input("Bütünleme notunuzu giriniz:")
    b1 = int(but) * 0.6
    ort1 = v1+b1
    if ort1 < 60:
        print("Öğrenci dersten kaldı!")
        print("Öğrenci Ortalaması= ", ort1)
    else:
        print("Öğrenci Dersten Bütünleme ile Geçti!")
        print("Öğrenci Ortalaması= ", ort1)
else:
    print("Öğrenci Dersten Doğrudan Geçti! ")
    print("Öğrenci ortalaması= ", ortalama)
