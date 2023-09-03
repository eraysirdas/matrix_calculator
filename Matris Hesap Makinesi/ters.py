import sys
import numpy as np

# "A" matrisinin boyutlarının girilmesi
print("A(n,n) Boyutlarini giriniz:")
try:
    n = int(input())
except:
    print("lütfen sadece sayı giriniz...")
    sys.exit()

# Girilen boyutlarda "A" matrisi oluşturulması
A = [[0 for i in range(n)] for i in range(n)]

# “A” matrisinin girilmesi
print("A matrisini giriniz:")
try:
    for i in range(n):
        for j in range(n):
            print('A[{}][{}]'.format(i + 1, j + 1))
            A[i][j] = int(input())
except:
    print("hatalı giris")
    sys.exit()

#numpy kütüphanesi ile matrisin tersinin alınması
D=np.linalg.inv(A)

#Matrisin ve sonucun yazdırılması
print("\nGirdiğiniz Matris\n")
for i in range(n):
    for j in range(n):
        print(A[i][j],end=" ")
    print()

print("\nTersi Alınmış Matris\n")
print(D,end=" ")

