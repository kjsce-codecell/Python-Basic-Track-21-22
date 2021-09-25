import csv

file = open("users.csv", "a")

name = input("Name: ")
password = input("Password: ")

writer = csv.writer(file)
writer.writerow([name, password])

file.close()

