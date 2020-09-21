import timeit

setup_code = "import time,threading"

statement = """
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
        
values=range(2,50,3)
t1=threading.Thread(target=calculate_sum,args=(values,))
t2=threading.Thread(target=calculate_cube,args=(values,))
t1.start()
time.sleep(1)
t2.start() 
t1.join()
t2.join()       
"""

print(f"Execution time is: {timeit.timeit(setup = setup_code, stmt = statement, number = 1)}")