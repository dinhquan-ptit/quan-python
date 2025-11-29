data = [
    {"name": "A", "score": 7},
    {"name": "B", "score": 9},
    {"name": "A", "score": 8},
]
tong = {}
for hs in data:
    name = hs["name"]
    score = hs["score"]
    if name in tong:
        tong[name] += score
    else:
        tong[name] = score
print(tong)
