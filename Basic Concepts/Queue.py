## Queue is FIFO ( First In First Out)

import queue
q=queue.Queue()
for i in range(5):
    q.put(i)

while q.empty() is False:
    print(q.get(),end=' ')

print("\n")
## LIFO ( Last in and first out can also be achieved )

import queue
q=queue.LifoQueue()
for i in range(5):
    q.put(i)

while q.empty() is False:
    print(q.get(),end=' ')

#####################
#When we take out the item in q.get() , after that if we use
# the same q.get(), we will not get the element back.. our program
# hang searching the element for g.get() and will not execute next
# code.
print("\n")
import queue
q=queue.Queue()
q.put(7)
print("First item gotten", q.get())
print("q has become empty", q.empty())
q.get()
print("The q is empty now and this statement will nt print")