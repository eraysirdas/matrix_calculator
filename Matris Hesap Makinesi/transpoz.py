#Boyut bilgisinin alınması
import sys

print("Matrislerin satir sayisini giriniz (m)=")
try:
    m = int(input())
except:
    print("lütfen sadece sayı giriniz...")
    sys.exit()
print("Matrislerin sutun sayisini giriniz (n)=")
try:
    n = int(input())
except:
    print("lütfen sadece sayı giriniz...")
    sys.exit()

#Girilen boyutlarda matrisler oluşturulması
M = [[0 for i in range(n)] for i in range(m)]
C = [[0 for i in range(m)] for i in range(n)]

#Matrisinin elemanlarının alınması
print("Matrisi giriniz:")
try:
    for i in range(m):
        for j in range(n):
            print('M[{}][{}]'.format(i+1, j+1))
            M[i][j] = int(input())
except:
    print("hatalı giris")
    sys.exit()

# "M" matrisin transpozunun alınması
for i in range(m):
    for j in range(n):
        C[j][i] = M[i][j]

#Matrislerin yazdırılması
print("Girdiğiniz Matris:\n")
for i in range(m):
    for j in range(n):
        print(M[i][j],end=" ")
    print(" ")

print("\nTranspozu Alınan Matris:\n")
for i in range(n):
    for j in range(m):
        print(C[i][j],end=" ")
    print(" ")



