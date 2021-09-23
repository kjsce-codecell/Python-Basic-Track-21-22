# The most common form is range(n), for integer n, 
# which returns a numeric series starting with 0 and 
# extending up to but not including n, 
# e.g. range(5) returns 0, 1, 2, 3, 4.

# incorrect if we want to print 5 times
for i in range(1, 5):
    print('codecell is the best council.')

# 1st num is included and last one is excluded
# correct if we want to print 5 times
for i in range(0, 5):
    print('codecell is the best council.')

# skipping values
for i in range(0, 10, 2):
    print('codecell is the best council.')

