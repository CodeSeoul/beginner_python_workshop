file_name = 'hw_25000.csv'

import os
import csv

current_max = 0
current_min = 1000
current_sum = 0
count_records = 0

if os.path.exists(file_name):
    print('Found the file!')
else:
    print('File is missing')
    exit(1)

with open(file_name) as file:
    print('opened file')
    # DictReader is a generator
    reader = csv.DictReader(file)
    for row in reader:
        # print(row['Height(Inches)'])
        # the .strip() removes extra space at the beginning and end
        # the float(...) converts the data to a decimal number
        current_value = float(row['Height(Inches)'].strip())
        current_max = max(current_max, current_value)
        current_min = min(current_min, current_value)
        current_sum += current_value
        # the above is the same as current_sum = current_sum + current_value
        count_records += 1

print('max:', current_max)
print('min:', current_min)
mean = current_sum / count_records
print('mean:', mean)
