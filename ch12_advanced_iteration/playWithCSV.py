import csv

# 1 separated line
with open('buzzers.csv') as raw_data:
    print(raw_data.read())

# 2 each line like list
with open('buzzers.csv') as data:
    for line in csv.reader(data):
        print(line)

# 3 each line like dict
with open('buzzers.csv') as data:
    for line in csv.DictReader(data):
        print(line)

