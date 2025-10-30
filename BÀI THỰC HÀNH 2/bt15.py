a = input('hãy nập một đoạn văn :')
for i in '.,!?':
    a = a.replace(i,'')
print(a)
c = a.lower().split()
dem = {} 
for tu in c:
    if tu in dem:
        dem[tu] += 1
    else:
        dem[tu] = 1
print(dem)
ket_qua = sorted(dem.items(), key=lambda x: x[1], reverse=True)
print(ket_qua)


