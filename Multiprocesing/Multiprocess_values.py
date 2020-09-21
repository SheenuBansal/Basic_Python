import multiprocessing

def calc_square(numbers,result,v):
    v.value=5.57
    for idx,n in enumerate(numbers):
        result[idx] = n*n

if __name__ == '__main__' :
    arr = [5,8,7]
    result = multiprocessing.Array('i',3)
    v=multiprocessing.Value('d',0.0)
    p=multiprocessing.Process(target=calc_square,args=(arr,result,v))
    p.start()
    p.join()

    print(v.value)