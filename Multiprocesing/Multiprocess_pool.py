from multiprocessing import Pool
import time

def f(n):
    sum=0
    for i in range(10000):
        sum += i*i
    return sum
if __name__ == "__main__" :
    t1=time.time()
    p=Pool()
    result=p.map(f,range(1))
    p.close()

    print(result)
    print("Pool took:",time.time()-t1)

    t2=time.time()
    result=[]
    for x in range(10000):
        result.append(f(x))

    print("Serial processing took:" , time.time()-t2)