## Iterable = __iter__ or __getitem()__ These both defined in iterable. if we will run this object on iterable, it will give iterable
## Iterator = __next__
## Iteration=       This method is called iteration.

# Generators : these can be traversed one.
#Yield is a generator. it will give generator oject when we print it.n the fly values are generated by using yield to save memory.
#We create a generator, which is capable of genrating numbers when we need .

def gen(n):
    for i in range(n):
        yield i

g=gen(1511616)
print(g)

print(" ---------------------------------------- ")
def gent(n):
    for i in range(n):
        yield i%2

g=gent(8)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
