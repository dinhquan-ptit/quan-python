matrix = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
]
tong_chinh = 0
for i in range(len(matrix)):
    tong_chinh += matrix[i][i]
print("Tổng đường chéo chính:", tong_chinh)
tong_phu = 0
n = len(matrix)
for i in range(n):
    tong_phu += matrix[i][n - i - 1]
print("Tổng đường chéo phụ:", tong_phu)
matrix_tuple = tuple(tuple(row) for row in matrix)
print(matrix_tuple)
