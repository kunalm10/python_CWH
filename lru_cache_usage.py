from functools import lru_cache

number = input('How many values you want to save in cache?\t')

@lru_cache(maxsize= int(number))
def square_of(a):
    import time
    time.sleep(2)
    return a**2

if __name__ == '__main__':
    print(square_of(2222222))
    print(square_of(2))
    print(square_of(2222222))
    print(square_of(222))
    print(square_of(2222))

