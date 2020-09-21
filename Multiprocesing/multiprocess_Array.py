## By using Queue Method, we can change the global value
## inside the function and access it in the main program,as
## shown below

import multiprocessing

def calc_square(numbers,result):
    for idx,n in enumerate(numbers):
        result[idx] = n*n

if __name__ == '__main__' :
    arr = [5,8,7]
    result = multiprocessing.Array('i',3)
    p=multiprocessing.Process(target=calc_square,args=(arr,result))
    p.start()
    p.join()
    print(result[:])