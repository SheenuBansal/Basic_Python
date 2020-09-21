f1= open("Timeit.py")
try:
    open("my_file.txt")
except Exception as e:
    print(e)
else:
    print("this will run only if except is not running")
finally:
    print("Run this anyway")
    f1.close()