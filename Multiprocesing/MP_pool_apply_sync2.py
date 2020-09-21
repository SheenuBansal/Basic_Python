# Meaning of providing optional argument timeout
# is that it will throw timeout error if our process
# is taking more time than described in timeout = x

from multiprocessing import Pool
import time
def double(n):
    time.sleep(5)
    return n*2
if __name__=='__main__':
   pool=Pool(processes=3)
   result=pool.apply_async(double,(7,))
   print(result.get(timeout=0.8))