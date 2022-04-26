"""
Chapter 1-5
Python Advanced(2) - Context Manager 2
Keyword - Contextlib, __enter__, __exit__, exception

"""
"""
ContextLib - Measure execution(타이머) 제작

"""

# Ex1
# Use Class

import time


class ExcuteTimer:
    def __init__(self, msg):
        self._msg = msg

    def __enter__(self):
        self._start = time.monotonic()
        return self._start

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Logging exception {(exc_type, exc_val, exc_tb)}")
        else:
            print(f"{self._msg} : {time.monotonic() - self._start} s")
        # return True


with ExcuteTimer("Start! Job") as v:
    print(f"Received start monotonic1 : {v}")
    # Excute Job
    for i in range(30000000):
        pass
    raise Exception("Raise! Excpetion !!")
