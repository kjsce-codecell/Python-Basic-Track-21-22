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

my_name("Manasi","Varaiya") #function calling 

#This Code will give an error
def my_name(fname,lname):
  print(fname +" "+ lname)

my_name("Manasi") #function calling 