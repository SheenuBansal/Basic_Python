# print("Hello World")
# import bisect
#
# a=[1,2,5,8,56,87,781]
# number=6
# print(bisect.bisect(a,number))
# bisect.insort(a,number)
# print(a)
# b=[56,54,57,98,123]
# number1=55
# bisect.insort(b,number1)
# print(b)
# #
# names=["jack","Sherry","Nancy","Tom"]
# age=[22,25,25]
# dict=dict(zip(names,age))
# print(dict)
#
# students1={1:"Jack",2:"Ashok",3:"Jerry"}
# students2={1:"Nancy",2:"Tom"}
# print({**students1,**students2})

# HexNumber="0xfdf"
# print(int(HexNumber,0))
# print(hex(16))

# import time
# from threading import Thread
#
# class worker(Thread):
#     def run(self):
#         for x in xrange(0,11):
#             print(x)
#             time.sleep(1)
#
# class waiter(Thread):
#     def run(self):
#         for x in xrange(100,103):
#             print(x)
#             time.sleep(5)
#
# def run():
#     worker().start()
#     waiter().start()
# run()

# import threading
# import time
# start=time.time()
#
# def print_hello():
#     for i in range(4):
#         time.sleep(0.5)
#         print("Hello")
#
#
# def print_hi():
#     for i in range(4):
#         time.sleep(0.7)
#         print("Hi")
#
#
# t1 = threading.Thread(target=print_hello)
# t2 = threading.Thread(target=print_hi)
# t1.start()
# t2.start()
# end=time.time()
#
# print(f'Execution time of program is {end-start}')
#
# def test():
#     for i in range(6):
#         print(i)
#         return("hi")
#
#
# print(test())
# print("======================")
#
# import re
# string= "at what time?"
# match= re.split('a',string)
# print(match)

try:
    total= 5+5
except:
    print("error")
else:
    print(total)
#
import keyword
print(keyword.iskeyword("in"))

import builtins
print(dir(builtins))
# import random
# letters=[chr(i) for i in range(97,122)]
# print(letters[random.randint(0,25)])
help = "ji"
print(help)