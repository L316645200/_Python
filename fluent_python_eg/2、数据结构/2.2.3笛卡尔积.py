colors = ['blank', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
tshirts = [(color, size) for size in sizes for color in colors]
print(tshirts)

# 逐个产出元素,不会一次性产出
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
