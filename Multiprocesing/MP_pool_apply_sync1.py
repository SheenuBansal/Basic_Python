#Another method that gets us the result of our processes
# in a pool is the apply_async() method.

from multiprocessing import Pool
import time
def double(n):
    return n*2
if __name__=='__main__':
   pool=Pool(processes=3)
   result=pool.apply_async(double,(7,))
   print(result.get(timeout=1))