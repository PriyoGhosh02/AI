numbers= list(map(int, input("Enter elements: ").split()))

c_odd=0
c_even=0
list_odd= []
list_even= []

for num in numbers:
    if num%2==0:
        c_even+=1
        list_even.append(num)
    else:
        c_odd+=1
        list_odd.append(num)
        
print(f"Even Numbers: {list_even} and Odd Numbers: {list_odd}")
print(f"Total Even Numbers: {c_even} and Total Odd Numbers: {c_odd}")