"""
Chapter 1-4
Python Advanced(2) - Context Manager 1
Keyword - Contextlib, __enter__, __exit__, exception

"""
"""
컨텍스트 매니저 : 원하는 타이밍에 정확하게 리소스를 할당 및 제공, 반환하는 역할
가장 대표적인 with 구문 이해
정확한 이해 후 사용 프로그래밍 개발 중요(문제 발생 요소)

"""

# Ex1

file = open("./testfile1.txt", "w")
try:
    file.write("Context Manager Test1\nContextLib Test1.")
finally:
    file.close()

# Ex2
with open("./testfile2.txt", "w") as f:
    f.write("Context Manager Test2\nContextLib Test2.")


# Ex3
# Use Class -> Context Manager with exception handling.
# 클래스에 __enter__, __exit__가 있으면 컨텍스트 매니저로 사용 할 수 있다.

class MyFileWriter:
    def __init__(self, file_name, method):
        print("MyFileWriter started : __init__")
        self.file_obj = open(file_name, method)

    def __enter__(self):
        print("MyFileWriter started : __enter__")
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("MyFileWriter started : __exit__")
        if exc_type:
            print(f"Logging exception {(exc_type, exc_val, exc_tb)}")
        self.file_obj.close()


with MyFileWriter("./testfile3.txt", "w") as f:
    f.write("Context Manager Test3\nContextLib Test3.")
