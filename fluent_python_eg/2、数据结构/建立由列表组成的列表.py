board = [['_'] * 3 for i in range(3)]  #
print(board)
board[1][2] = 'x'
print(board)

# 以上等同于
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)

board = [['_'] * 3] * 3  # 当[]里面包含引用对象时，使用*3，则三个列表指向同一个对象
print(board)
board[1][2] = 'x'
print(board)

# 以上等同于
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
