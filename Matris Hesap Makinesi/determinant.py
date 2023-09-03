import copy
import sys
#Matrisinin 2x2 boyutunda geri döndürülmesi



def smaller_matrix(original_matrix, row, column):
    new_matrix = copy.deepcopy(original_matrix)
    new_matrix.remove(original_matrix[row])
    for i in range(len(new_matrix)):
        new_matrix[i].remove(new_matrix[i][column])
    return new_matrix

#Matrisinin determinantını hesaplanması(A11*a11+A12*a12+A13*a13 şeklinde kofaktör yardımıyla ile determinant hesabı yapar)
def determinant(matrix):
    num_rows = len(matrix)
    for row in matrix:
        if len(matrix)==2:
            simple_determinant = matrix[0][0] * \
                                 matrix[1][1] - \
                                 matrix[1][0] * \
                                 matrix[0][1]
            return simple_determinant
        else:
            answer = 0
            num_columns = num_rows
            for j in range(num_columns):
                cofactor = (-1) ** (0+j) * matrix[0][j] * determinant(smaller_matrix(matrix, 0, j))
                answer += cofactor
            return answer

#Matrisin boyutlarının alınması
print("A(n,n) Boyutlarini giriniz:")
try:
    n = int(input())
except:
    print("lütfen sadece sayı giriniz...")
    sys.exit()

# "A" matrisinin oluşturulması
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

#Sonucun yazdırılması
print("detA:",determinant(A))


