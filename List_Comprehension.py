list_of_strings = input().split(',')

# TODO: Use list comprehension to convert the strings to integers 👇:
result=[]
numbers=[int(num) for num in list_of_strings ]
result = [digit for digit in numbers if digit%2==0]

# TODO: Use list comprehension to filter out the odd numbers

print(result)

# OP
# 10,20,15,61,45,48,98
# [10, 20, 48, 98]