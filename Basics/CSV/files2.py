import csv
import datetime

path = "C:/Users/daphn/Downloads/google_stock_data.csv.csv"
# the newline variable is a special variable that is used to specify the newline character used in text files
file = open(path, newline='')
# The csv.reader() function returns a list of values for each row in the CSV file.
reader = csv.reader(file)

header = next(reader) #First line is the Header 
data = []
for row in reader:
    date = datetime.datetime(row[0], '%m/%d/%Y')
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])
    data.append([date, open_price, high, low, close, volume, adj_close])

    # will read the remaining data in the file 
    
print(data[0])

