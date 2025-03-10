import csv

with open(r"./test.csv", "r") as f:
    a_csv = csv.reader(f)
    header = next(a_csv)
    print(header)
    for row in a_csv:
        print(row)