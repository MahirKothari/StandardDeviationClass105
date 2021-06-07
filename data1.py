import csv
import math
with open('data1.csv',newline = '')as f:
    reader = csv.reader(f)
    filedata = list(reader)
data = filedata[0]
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total = total+int(x)
    mean = total/n
    return mean
squaredList = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    squaredList.append(a)
sum = 0
for i in squaredList:
    sum = sum+1
result = sum/len(data)
standardDeviation = math.sqrt(result)
print(standardDeviation)