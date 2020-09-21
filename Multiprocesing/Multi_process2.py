import multiprocessing
import time

squares=[]
def calc_square(numbers):
    global squares
    for i in numbers :
        squares.append(i*i)
    print(f"Within a function: {squares}")



if __name__== "__main__" :
    arr=[2,5,6]
    p1=multiprocessing.Process(target=calc_square,args=(arr,))
    p1.start()
    p1.join()
    print(f"Outside a function: {squares}")