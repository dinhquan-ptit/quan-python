lst = [(1,2),(2,3),(4,5),(6,7)]
sum_x = 0
sum_y = 0
for x, y in lst:
    sum_x += x
    sum_y += y
avg_x = sum_x / len(lst)
avg_y = sum_y / len(lst)
print("Trung bình x =", avg_x)
print("Trung bình y =", avg_y)