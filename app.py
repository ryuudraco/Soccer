import csv
filename = 'data.txt'

# closing file automatically after reading
with open(filename) as f:
    data = f.readlines()

# old version
# f = open(filename)
# data = f.readlines()
# f.close()

for line in data:
    fields = line.strip().split(',')
    print(fields[0], fields[1])