import time,threading
start = time.time()
def calculate_sum(numbers):
    print("squares is calculated below:")
    for i in numbers :
        time.sleep(2)
        print("square",i*i)

def calculate_cube(numbers):
    print("cubes is calculated below:")
    for i in numbers :
        time.sleep(2)
        print("cube",i*i*i)


values=[2,3,6]
t1=threading.Thread(target=calculate_sum,args=(values,))
t2=threading.Thread(target=calculate_cube,args=(values,))
t1.start()
time.sleep(0.5)
t2.start()
end=time.time()
t1.join()
t2.join()
print(f"the time taken to execute the program is : {end-start}")
