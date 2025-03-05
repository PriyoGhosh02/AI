str_input = input("Enter tuple elements: ")

if "," in str_input:
    tuple = tuple(str_input.split(","))
else:
    tuple = tuple(str_input.split())

print(tuple)
print(f"First 4th: {tuple[3]} and last 4th: {tuple[-4]}")

print("hello world")
