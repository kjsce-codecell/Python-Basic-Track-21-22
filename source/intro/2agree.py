'''
We need to check if the user accepted the terms and condition or not
'''


print('Do you agree?')
c = input()

# check whether ageed
if c == 'Y' or c == 'y':
    print('Agreed')
elif c == 'N' or c == 'n':
    print('Disagreed')

# Better implementation
if c.lower() == 'y':
    print('Agreed')
elif c.lower() == 'n':
    print('Disagreed')
