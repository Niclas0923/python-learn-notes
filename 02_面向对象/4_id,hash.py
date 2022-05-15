# 可哈希的概念
# hash(x)有定义则称其可哈希
# 可哈希的类才能作为集合的元素和字典的键
# 列表，集合，字典这三类的__hash__均被设置为None，不可哈希
# 整形变量，小数，元祖，字符串均可哈希

# 可哈希的类（自带）都是与内容有关的

x = 21.1
print(hash(x))
print(hash(21.1))  # 230584300921372693 两者结果完全相同

# 整形的哈希值为本身
print(hash(10))  # 10


# 自己设置的类默认有__hash__，但与其中的值无关，与其存储的地点有关
class A:
    def __init__(self, a) -> None:
        self.a = a


a = A(1)
b = A(1)

print(hash(a))  # 8773427146587
print(hash(b))  # 8773427146599 由储存位置id决定所以每次都不同


# 自己设置类时可以直接修改__hash__来使其的哈希值与内容有关

class B(A):
    def __init__(self, a) -> None:
        super().__init__(a)

    def __hash__(self):
        return hash(self.a)


a = B(1)
b = B(1)

print(hash(a))  # 1
print(hash(b))  # 1

# 但是此时他们的储存位置，也就是id是不同的，所以

print(a == b)  # False


# 如有需要也可以同时修改__eq__
class C(B):
    def __init__(self, a):
        super().__init__(a)

    def __eq__(self, other):
        if isinstance(other, C):
            return self.a == other.a
        elif isinstance(other, int):
            return self.a == other
        else:
            return False


a = C(1)
b = C(1)

print(a == b)  # True


# 但是只修改__eq__则__hash__会被直接设置为None，所以同时修改

class D(A):
    def __init__(self, a) -> None:
        super().__init__(a)

    def __eq__(self, other):
        if isinstance(other, D):
            return self.a == other.a
        elif isinstance(other, int):
            return self.a == other
        else:
            return False


a = D(1)
try:
    print(hash(a))
except:
    print('False')  # False
