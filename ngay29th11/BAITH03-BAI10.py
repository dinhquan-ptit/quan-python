lst = [1, 2, 2, 3, 3, 3, 4]
count = {}
for x in lst:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1
max_num = None
max_count = 0
for k, v in count.items():
    if v > max_count:
        max_count = v
        max_num = k
print("Phần tử xuất hiện nhiều nhất là:", max_num)
print("Số lần xuất hiện:", max_count)
