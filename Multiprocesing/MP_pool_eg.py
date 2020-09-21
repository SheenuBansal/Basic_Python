# We create an instance of Pool and
# have it create a 3-worker process.
# map() maps the function double and
# an iterable to each process.
# The result gives us [4,6,12].

from multiprocessing import Pool
def double(n):
   return n*2
if __name__=='__main__':
   nums=[2,3,6]
   pool=Pool(processes=3)
   print(pool.map(double,nums))



