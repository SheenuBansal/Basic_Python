import time
from functools import  lru_cache        #lru_cache is a decorator in the builtin module functools, which helps in caching of the function and
                                        # saves our time when we need to cll that function same again
@lru_cache(maxsize=3)
def some_work(n):
    time.sleep(n)
    return n

if __name__ == '__main__' :
    print("Now running some_work")
    some_work(3)
    print("Done work.. calling again")
    some_work(3)
    print("Done calling again")

## max Size = 3 means it will save the 3 recent values only. In the example below, it will print ("Done calling again)
## after 3 econds again, it did not store the 4th one..

@lru_cache(maxsize=3)
def some_work(n):
    time.sleep(n)
    return n

if __name__ == '__main__' :
    print("Now running some_work")
    some_work(3)
    some_work(1)
    some_work(5)
    some_work(2)
    print("Done work.. calling again")
    some_work(3)
    print("Done calling again")