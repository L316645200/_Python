
l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)
print(l2)
print(l2 == l1)
print(l2 is l1)

l1[1].append(3)
print(l1)
print(l2)


l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)
l1.append(100)
l1[1].remove(55) # 就地修改
print('l1:', l1)
print('l2:', l2)
l2[1] += [33, 22]  # 就地修改
l2[2] += (10, 11)  # 创建新对象
print('l1:', l1)
print('l2:', l2)

print()
