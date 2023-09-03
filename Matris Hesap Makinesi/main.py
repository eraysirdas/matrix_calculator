
print("""

Yapmak İstediğiniz İşlemi Seçiniz : 

1 ==> Toplama
2 ==> Çıkarma
3 ==> Çarpma 
4 ==> Tranpoz
5 ==> Sayıyla Toplama
6 ==> Sayıyla Çıkarma 
7 ==> Sayıyla Bölme 
8 ==> Sayıyla Çarpma 
9 ==> Üs alma 
10 ==> Determinant
11 ==> Ters Alma
""")
islem =(input())

if(islem=='1'):
    import toplama
    toplama
elif(islem=='2'):
    import cıkarma
    cıkarma
elif (islem == '3'):
    import carpma
    carpma
elif (islem == '4'):
    import transpoz
    transpoz
elif (islem == '5'):
    import sayı_toplam
    sayı_toplam
elif (islem == '6'):
    import sayı_cıkarma
    sayı_cıkarma
elif (islem == '7'):
    import sayı_bolme
    sayı_bolme
elif (islem == '8'):
    import sayı_carpma
    sayı_carpma
elif(islem=='9'):
    import us_alma
    us_alma
elif (islem == '10'):
    import determinant
    determinant
elif (islem == '11'):
    import ters
    import numpy
    ters
else:
    print("hatalı islem")














