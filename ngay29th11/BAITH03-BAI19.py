lst = [1, 3, 4, 7, 10, 12]
N = int(input("Nhập số N: "))
lst.sort()
l = 0
r = len(lst) - 1
best_pair = (lst[l], lst[r])
best_diff = abs(lst[l] + lst[r] - N)
while l < r:
    s = lst[l] + lst[r]
    diff = abs(s - N)
    if diff < best_diff:
        best_diff = diff
        best_pair = (lst[l], lst[r])
    if s < N:
        l += 1
    else:
        r -= 1
print("Cặp có tổng gần nhất N là:", best_pair)
