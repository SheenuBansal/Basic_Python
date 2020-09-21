ls=[]
for i in range(100):
    if i%3==0 :
        ls.append(i)
print(ls)

# List Comprehension : We can write the above code in just  line, that's what we called list comprehsnion.

ls=[i for i in range(100) if i%3==0]
print(ls)

# Dict Comprehensions : It is not only for shortening the code to 1 line but we can reverse the dictionary also by this method.

dict1 = {i:f"Item {i}" for i in range(50) if i%5 == 0}
dict2 = {value:key for key,value in dict1.items() }
print(dict1,"\n",dict2)

# Set comprehension:

set1={dress for dress in ["apple","apple","mango","grapes","mango"]}
print(set1)

# generator comprehension: We write it in parenthesis

evens =(i for i in range(20) if i%2==0)
print(type(evens))
print(evens)
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())