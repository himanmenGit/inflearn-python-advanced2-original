"""
Chapter 3-4
Python Advanced(2) - Descriptor(1)
Keyword - descriptor, set, get, del, property

"""
"""
디스크립터

1. 객체에서 서로다른 객체를 속성값으로 가지는 것.
2. Read, Write, Delete 등을 미리 정의 가능
3. data secriptior(set, del), non-data descriptor(get)
4. 읽기 전용 객체 생성 장점, 클래스를 의도하는 방향으로 생성 가능
 
"""


# Ex1
# 기본 적인 Descriptor 예제

class DescriptorEx1:
    def __init__(self, name="Default"):
        self.name = name

    def __get__(self, obj, objtype):
        return f"Get method called. -> self: {self}, obj : {obj}, objtype: {objtype}, name : {self.name}"

    def __set__(self, obj, name):
        print("Set method called.")
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name should be string.")

    def __delete__(self, obj):
        print("Delete method called.")
        self.name = None


class Sample1:
    name = DescriptorEx1()


s1 = Sample1()

# __set__ 호출
s1.name = "Descriptor Test1"

# 예외 발생
# s1.name = 10

# attr 확인
# __get__
print(f"Ex1 > {s1.name}")

# __delete__ 호출
del s1.name

# 재확인
# __get__ 호출
print(f"Ex1 > {s1.name}")


# Ex2
# property 클래스 사용 Descriptor 직접 구현
# class property(fget=None, fset=None, fdel=None, doc=None)

class DescriptorEx2:
    def __init__(self, value):
        self._name = value

    def getVal(self):
        return f"Get method called. -> self : {self}, name: {self._name}"

    def setVal(self, value):
        print("Set method called.")
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError("name should be string.")

    def delVal(self):
        print("Delete method called.")
        self._name = None

    name = property(getVal, setVal, delVal, "Property Method Example.")


s2 = DescriptorEx2("Descriptor Test2")

# 최초 값 확인
print(f"Ex2 > {s2.name}")

# setVal 호출
s2.name = "Descriptor Test2 Method."

# 예외 발생
# s2.name = 10

# getVal 호출
print(f"Ex2 > {s2.name}")

# delVal 호출
del s2.name

# 재확인
# getVal 호출
print(f"Ex2 > {s2.name}")

# Doc 확인
print(f"Ex2 > {DescriptorEx2.name.__doc__}")