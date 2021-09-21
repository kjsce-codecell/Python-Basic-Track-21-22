#creating function
def my_name():
  print("Hello! My name is Manasi")

#calling function
my_name()

#with one argument/data
def my_name(fname):
  print(fname + " Varaiya")

my_name("Manasi")  #function calling 

#with two arguments/data
def my_name(fname,lname):
  print(fname +" "+ lname)

my_name("Manasi","Varaiya")        #function calling 

#This Code will give an error
def my_name(fname,lname):
  print(fname +" "+ lname)

my_name("Manasi")       #function calling 

# function to show multiplication
def multi(x):         #creating the function
  return 2 * x

print(multi(2))         #function calling 
print(multi(9))         #function calling 

#usage of pass keyword
def myfunction():
  pass

# having an empty function definition like this, would raise an error without the pass statement

def myfunction():


#Lambda Function
#with 1 argument
x = lambda a : a - 5
print(x(20))

#with 2 arguments
x = lambda a, b : a / b
print(x(24, 6))
