"""
Chapter 2-3
Python Advanced(2) - Property(2) - Getter, Setter
Keyword - @property

"""
"""
프로퍼티(Property) 사용 장점
1. 파이써닉한 코드
2. 변수 제약 설정
3. Getter, Setter 효과 동등(코드 일관성)
    - 캡슐화, 유효성 검사 기능 추가 용이
    - 대체 표현(속성 노출, 내부의 표헌 숨기기 가능)
    - 속성의 수명 및 메모리 관리 용이
    - 디버깅 용이
    - Getter, Setter 작동에 대해 설계된 여러 라이브러리(오픈소스) 상호 운용성 증가
    
"""


# Ex1
# Propetry 활용 Getter, Setter 작성

class SampleA:
    def __init__(self):
        self.x = 0
        self.__y = 0  # private

    @property
    def y(self):
        print("Called get method.")
        return self.__y

    @y.setter
    def y(self, value):
        print("Called set method.")
        self.__y = value

    @y.deleter
    def y(self):
        print("Called deleter method.")
        del self.__y


a = SampleA()

a.x = 1
a.y = 2

print(f"Ex1 > x: {a.x}")
print(f"Ex1 > y: {a.y}")

# deleter
del a.y
print(f"Ex1 > {dir(a)}")


# Ex2
# Property 활용 제약 조건 추가
class SampleB:
    def __init__(self):
        self.x = 0
        self.__y = 0  # private

    @property
    def y(self):
        # print("Called get method.")
        return self.__y

    @y.setter
    def y(self, value):
        # print("Called set method.")
        if value < 0:
            raise ValueError("0 보다 큰 값을 입력하세요.")
        self.__y = value

    @y.deleter
    def y(self):
        # print("Called deleter method.")
        del self.__y


b = SampleB()

b.x = 1
b.y = 10
# b.y = -5 # raise error

print(f"Ex2 > x: {b.x}")
print(f"Ex2 > y: {b.y}")
