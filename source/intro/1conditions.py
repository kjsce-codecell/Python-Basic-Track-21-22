'''
take two integers from the user and tell which one greater than the other
'''

# Prompt user for x
x = input('x: ')
# prompt user for y
y = input('y: ')

# Compare x and y
if (x < y):
    print("x is less than y")
elif (x > y):
    print("x is greater than y")
else:
    print("x is equal to y")
