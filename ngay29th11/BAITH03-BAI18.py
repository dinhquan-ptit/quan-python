data = [
    ("A01", 5),
    ("B02", 3),
    ("A01", 7),
    ("C03", 2),
    ("B02", 4)
]
gop = {}
for sku, qty in data:
    if sku in gop:
        gop[sku] += qty
    else:
        gop[sku] = qty
result = [(sku, qty) for sku, qty in gop.items()]

print(result)
