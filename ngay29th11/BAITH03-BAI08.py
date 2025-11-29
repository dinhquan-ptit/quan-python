pp={}
for x in range(3) :
    t = input('ten')
    ti = int(input('tuoi'))
    pp[t]=ti
print("\nDANH SÁCH VỪA NHẬP:")
print(pp)
for t, ti in pp.items():
    print(t, ":", ti)
