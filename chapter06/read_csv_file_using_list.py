import csv

data = []
sum_data = 0

with open("numbers.csv", "r") as f:
  data.extend(list(csv.reader(f)))

for row in data[1:]:
  sum_data += sum(map(int, row))

print(sum_data)
