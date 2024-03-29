import time

import multiprocessing

def calc_square(numbers):
    for n in numbers:
        time.sleep(2)
        print('square ' + str(n*n))

def calc_cube(numbers):
    for n in numbers:
        time.sleep(2)
        print('cube ' + str(n*n*n))

if __name__ == "__main__" :
    start = time.time()
    arr=[2,3,6]
    p1 = multiprocessing.Process(target=calc_square,args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))
    p1.start()
    time.sleep(0.5)
    p2.start()
    p1.join()
    p2.join()
    end=time.time()

    print("Total execution time:",end-start)