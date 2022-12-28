import csv

# print(dir(csv))

path = "C:/Users/daphn/Downloads/google_stock_data.csv.csv"
lines = [line for line in open(path)]
# Strip() removes whitespace
# Split()  used to split a string into a list of substrings based on a specified delimiter.
print(lines[0].strip().split(','))
print(lines[1].strip().split(','))

dataset = [line.strip().split(',') for line in open(path)] 
print(dataset[0:4])

