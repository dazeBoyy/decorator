import math
from math import *
import time

def print_func(func):
        def wraper1(*args):
            print(f"Была вызвана функци {func.__name__}")
            return func(*args)
        return wraper1



@print_func
def find_area(s: int,n: int):
    timeStart = time.time()
    area = (n * (s ** 2))/(4 * math.tan(math.pi/n))
    print(time.time() - timeStart)
    print(area)
    return area

@print_func
def sum_numbers(n: int):
    timeStart = time.time()
    sum = (n + (n+1))/2
    print(time.time() - timeStart)
    print(sum)
    return sum



def main():
     s = int(input("Введите длинну стороны: "))
     n = int(input("Введите кол-во сторон: "))

     area = find_area(s,n)
     sum = sum_numbers(n)



if __name__ == '__main__':
    main()
