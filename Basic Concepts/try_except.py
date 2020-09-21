# try and except are used when we want something to print neccesarily, whether the other (above function above it) executes or not
# So we use except .. in this way the prgram will not throw error and prints the last line writen in this below example.

print("Enter num1 : ",)
num1=input()
print("Enter num2 : ",)
num2=input()
try:
    print("Sum of numbers:",int(num1)+int(num2))
except Exception as e:
    print(e)

print("This line is very important")