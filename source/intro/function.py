# implement 'bad' design
print('codecell is the best council')
print('codecell is the best council')
print('codecell is the best council')

# make function for the same
def codecell():
    for i in range(0, 3):
        print('codecell is the best council')

codecell()

# make it even better by giving it arguments
def codecell(n):
    for i in range(0, n):
        print('codecell is the best council')

codecell(5)