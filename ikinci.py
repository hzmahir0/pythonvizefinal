vize = input("Vize notunuzu girin:")
v1 = int(vize) * 0.4
gerekAA = 90
gerekBA = 80
gerekBB = 75
gerekCB = 65
gerek = 60
gerekli = gerek - v1
gerekliA = gerekAA - v1
gerekliBA = gerekBA - v1
gerekliB = gerekBB - v1
gerekliCB = gerekCB - v1
if int(vize)>100:
    print("Düzgün bir değer girmelisin.")
else:
    if v1<60:
        print("AA ile Geçmesi için gerekli not= ", gerekliA / 0.6)
        print("BA ile Geçmesi için gerekli not= ", gerekliBA / 0.6)
        print("BB ile Geçmesi için gerekli not= ", gerekliB / 0.6)
        print("CB ile Geçmesi için gerekli not= ", gerekliCB / 0.6)
        print("Geçmesi için gerekli not= ", gerekli / 0.6)
        final = input("Final Notunuzu Girin:")
        f1 = int(final) * 0.6
        ortalama = v1 + f1
        if ortalama>=90:
            print("Öğrenci AA ile Geçti")
        elif ortalama>=80:
            print("Öğrenci BA ile Geçti")
        elif ortalama>=75:
            print("Öğrenci BB ile Geçti")
        elif ortalama>=65:
            print("Öğrenci CB ile Geçti")
        elif ortalama>=60:
            print("Öğrenci CC ile Geçti")
        else:
            print("Öğrenci Dersten Kaldı.")
    else:
        print("Düzgün bir değer gir sadece vize ile geçemezsin!!!")