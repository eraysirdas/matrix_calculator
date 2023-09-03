import sys
#Matrisin boyutlarının alınması
print("Matrislerin satir sayisini giriniz (m)=")
try:
    m = int(input())
except:
    print("lütfen sadece sayı girin...")
    sys.exit()
print("Matrislerin sutun sayisini giriniz (n)=")
try:
    n = int(input())
except:
    print("lütfen sadece sayı girin")
    sys.exit()

# Matrislerin oluşturulması
A = [[0 for i in range(n)] for i in range(m)]
B = [[0 for i in range(n)] for i in range(m)]
C = [[0 for i in range(n)] for i in range(m)]

#Matrislerin elemanlarının girilmesi
print("A matrisini giriniz:")
try:
    for i in range(m):
        for j in range(n):
            print('A[{}][{}]'.format(i+1, j+1))
            A[i][j] = int(input())
except:
    print("hatalı giris")
    sys.exit()

print("B matrisini giriniz:")
try:
    for i in range(m):
        for j in range(n):
            print('B[{}][{}]'.format(i+1, j+1))
            B[i][j] = int(input())
except:
    print("hatalı giris")
    sys.exit()

# A+B matrisinin C matrisine atılması
for i in range(m):
    for j in range(n):
        C[i][j] = A[i][j] + B[i][j]

#Matrislerin yazdırılması
print("Girdiğiniz A Matrisi\n")
for i in range(m):
    for j in range(n):
        print(A[i][j],end=" ")
    print()

print("\nGirdiğiniz B Matrisi\n")
for i in range(m):
    for j in range(n):
        print(B[i][j], end=" ")
    print()

print("\nA+B Matrisi\n")
for i in range(m):
    for j in range(n):
        print(C[i][j],end=" ")
    print()
