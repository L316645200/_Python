# 一例胜千言，我们来看看示例 10-4。
# 示例 10-4 了解 __getitem__ 和切片的行为
class MySeq:
    def __getitem__(self, index):
        return index

s = MySeq()
print(s[1])
print(s[1:4])
print(s[1:4:2])

print(s[1:4:2, 9])
print(s[1:4:2, 7:9])



print(slice(None, 10, 2).indices(5))
print(slice(-3, None, None).indices(5))