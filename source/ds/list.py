'''
primes = [2, 3, 5, 7, 11]
print(primes)

list1 = []

items = ['a','b','c']
total_items = items + ['d','e']
print(total_items)
# Result: ['a','b','c','d','e']
'''


'''
numbers = [1, 2, 3, 4, 10]
names = ['Jen', 'Sam', 'Alex']
mixed = ['Jen', 1, 2]
list_of_lists = [['a', 1], ['b', 2]]
'''


'''
tools = ['pen','hammer','lever']
tools_slice = tools[1:3]
# ['hammer', 'lever']
tools_slice[0] = 'nail'

# Original list is unaltered:
print(tools) 
# ['pen', 'hammer', 'lever']
'''

'''
heist = ['prof', 'rio', 'tokyo', 'nairobi']
heist[-1]   
# 'nairobi'
heist[-3:]  
# 'rio', 'tokyo', 'nairobi'
heist[:-2]  
# 'prof', 'rio'
'''

'''
# A 2D list of names and hobbies
class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]

# The sublist of Jenny is at index 0. The hobby is at index 1 of the sublist.
class_name_hobbies[0][1] = "Meditation"  #modifying the list
print(class_name_hobbies)

# Output
# [["Jenny", "Meditation"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
'''


'''
orders = ['daisies', 'roses']
orders.append('tulips')
print(orders)
# Result: ['daisies', 'roses', 'tulips']

'''

'''
# Create a list
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]
 
# Removes the first occurance of "Chris"
shopping_line.remove("Chris")
print(shopping_line)
 
# Output
# ["Cole", "Kip", "Sylvana", "Chris"]
'''


'''
backpack = ['pencil', 'pen', 'notebook', 'textbook', 'pen', 'highlighter', 'pen']
numPen = backpack.count('pen')
 
print(numPen)
# Output: 3
'''

'''
knapsack = [2, 4, 3, 7, 10]
size = len(knapsack)
print(size) 
# Output: 
'''

'''
exampleList = [4, 2, 1, 3]
exampleList.sort()
print(exampleList)
exampleList.sort(reverse=True)
# Output: [1, 2, 3, 4]
# Output: [4, 3, 2, 1]
'''

'''
unsortedList = [4, 2, 1, 3]
sortedList = sorted(unsortedList) # ,reverse=True
print(sortedList)
# Output: [1, 2, 3, 4]
'''

'''
# Here is a list representing a line of people at a store
store_line = ["Karla", "Maxium", "Martim", "Isabella"]
 
# Here is how to insert "Vikor" after "Maxium" and before "Martim"
store_line.insert(2, "Vikor")
 
print(store_line) 
# Output: ['Karla', 'Maxium', 'Vikor', 'Martim', 'Isabella']
'''


'''
cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]
 
# Pop the last element
removed_element = cs_topics.pop()
 
print(cs_topics)
print(removed_element)
 
# Output:
# ['Python', 'Data Structures', 'Balloon Making', 'Algorithms']
# 'Clowns 101'
 
# Pop the element "Baloon Making"
cs_topics.pop(2)
print(cs_topics)
 
# Output:
# ['Python', 'Data Structures', 'Algorithms']
'''


'''
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
del List[0]
print(List)
'''