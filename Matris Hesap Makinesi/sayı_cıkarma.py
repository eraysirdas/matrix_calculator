import sys
#Matrisin boyutlarının alınması
print("A(m,n) Boyutlarini giriniz:")
try:
    m = int(input())
    n = int(input())
except:
    print("lütfen sadece sayı giriniz...")
    sys.exit()

#İşleme alınacak sayının alınması
print("Çıkarılacak doğal sayıyı giriniz:")

try:
 x = int(input())
except:
    print("lütfen sadece sayıı giriniz...")
    sys.exit()

# Matrislerin oluşturulması
A = [[0 for i in range(n)] for i in range(m)]
C = [[0 for i in range(n)] for i in range(m)]

# “A” matrisinin girilmesi
print("A matrisini giriniz:")
try:
    for i in range(m):
        for j in range(n):
            print('A[{}][{}]'.format(i+1, j+1))
            A[i][j] = int(input())
except:
    print("hatalı giris")
    sys.exit()

# Çıkarmanın hesaplanması
for i in range(m):
    for j in range(n):
        C[i][j] += A[i][j] - x

#Matrislerin yazdırılması
print("Girdiğiniz Matris\n")
for i in range(m):
    for j in range(n):
        print(A[i][j],end=" ")
    print()

print("\n{} ile Çıkarılmış Yeni Matris\n".format(x))
for i in range(m):
    for j in range(n):
        print(C[i][j],end=" ")
    print()