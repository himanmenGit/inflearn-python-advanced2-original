"""
Chapter 3-5
Python Advanced(2) - Descriptor(2)
Keyword - descriptor vs property, low level(descriptor) vs high level(property)

"""
"""
디스크립터
1. 상황에 맞는 메소드 구현을 통한 객체 지향 프로그래밍 구현
2. Property와 달리 reuse(재사용) 가능
3. ORM Framework 사용

"""

# Ex1
# Descriptor 예제(1)

import os


class DirectoryFileCount:
    def __get__(self, obj, objtype=None):
        print(os.listdir(obj.dirname))
        return len(os.listdir(obj.dirname))


class DirectoryPath:
    """
    Descriptor instance
    """
    size = DirectoryFileCount()

    def __init__(self, dirname):
        self.dirname = dirname


# 현재 경로에 있는 파일 개수
s = DirectoryPath("./")
print(s.size)
# 이전 경로
g = DirectoryPath("../")
print(g.size)

# 헷갈릴 때 출력 용도
print(f"Ex1 > {dir(DirectoryPath)}")
print(f"Ex1 > {DirectoryPath.__dict__}")
print(f"Ex1 > {dir(s)}")
print(f"Ex1 > {s.__dict__}")

# Descriptor 예제(2)

import logging

logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S"
)


class LoggedScoreAccess:
    def __init__(self):
        self.value = None

    def __get__(self, obj, objtype=None):
        logging.info(f"Accessing {'score'} gibing {self.value}")
        return self.value

    def __set__(self, obj, value):
        logging.info(f"Updating {'score'} gibing {value}")
        self.value = value


class Student:
    # Descriptor instance
    score = LoggedScoreAccess()

    def __init__(self, name, score):
        self.score = score
        # Regular instance attribute
        self.name = name


s1 = Student("Kim", 50)
s2 = Student("Lee", 30)

# 점수 확인 (s1)
print(f"Ex2 s1 > {s1.score}")
s1.score += 20
print(f"Ex2 s1 > {s1.score}")

# 점수 확인 (s2)
print(f"Ex2 s2 > {s2.score}")
s2.score += 30
print(f"Ex2 s2 > {s2.score}")

# __dict__ 확인
print(f"Ex2 > {vars(s1)}")
print(f"Ex2 > {vars(s2)}")
print(f"Ex2 > {s1.__dict__}")
print(f"Ex2 > {s2.__dict__}")
