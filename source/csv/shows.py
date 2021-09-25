import csv

shows = {
    "Sex Education": 0,
    "Money Heist": 0,
    "Kota Factory": 0,
    "Codecell Python Workshop": 0
}

with open("shows.csv", "r") as file:

    reader = csv.reader(file)

    # ignore the very first line in the csv file
    next(reader)

    # loop over the remaining rows in the file
    for row in reader:
        # get the name of show currently being looped over
        name_of_show = row[1]
        # index into the dictionary and increment its value by 1
        shows[name_of_show] += 1
 
# loop over our local dictionary
for show in shows:
    # using format string pretty print the key and value
    print(f"{show}: {shows[show]}")

