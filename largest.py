def largest(a,b):
    if a>b:
        return a
    else:
        return b

a=int(input("Enter a number: "))
b=int(input("Enter another number: "))

print("The largest number is:", largest(a,b))
