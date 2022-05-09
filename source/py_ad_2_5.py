"""
Chapter 2-5
Python Advanced(2) - Method Overloading
Keyword - Overloading, OOP, multiple dispatch

"""
"""
메소드 오버로딩 효과
1. 동일 메소드 재정의
2. 네임이 기능 예측
3. 코드 절약, 가독성 향상
4. 메소드 파라미터 기반 호출 방식

"""


# Ex1
# 동일 이름 메소드 사용 예제
# 동적 타입 검사 ->  Managed 언어, 런타임에 실행(타입 에러가 실행시에 발견)

class SampleA:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z

    # 팩킹으로 해결 가능
    # def add(self, *args):
    #     return sum(args)


a = SampleA()

# print(f"Ex1 > {a.add(2, 3)}")

# 모든 속성 개체 확인
print(f"Ex1 > {dir(a)}")


# print(f"Ex1 > {a.add(2, 3)}")


# Ex2
# 동일 이름 메소드 사용 예제
# 자료형에 따른 분기 처리

class SampleB:
    def add(self, datatype, *args):
        if datatype == "int":
            return sum(args)
        if datatype == "str":
            return ''.join(args)


b = SampleB()

# 숫자 연산
print(f"Ex2 > {b.add('int', 5, 6)}")
print(f"Ex2 > {b.add('str', 'Hi ', 'python')}")

# Ex3
# multipledispatch 패키지를 통한 메소드 오버로딩

from multipledispatch import dispatch


class SampleC:
    @dispatch(int, int)
    def product(self, x, y):
        return x * y

    @dispatch(int, int, int)
    def product(self, x, y, z):
        return x * y * z

    @dispatch(float, float, float)
    def product(self, x, y, z):
        return x * y * z


c = SampleC()
print(f"Ex3 > {c.product(2, 5)}")
print(f"Ex3 > {c.product(2, 5, 10)}")
print(f"Ex3 > {c.product(2.5, 5.0, 10.0)}")
