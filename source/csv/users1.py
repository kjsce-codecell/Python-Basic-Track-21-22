import csv

with open('users.csv', 'a') as file:
    name = input('Name: ')
    password = input('Password: ')

    writer = csv.writer(file)
    writer.writerow([name, password])

