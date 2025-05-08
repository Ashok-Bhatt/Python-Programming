import sys
import csv

print(f"The maximum field size limit of a csv file is {csv.field_size_limit(sys.maxsize//10000000000000)}.")
print(f"The list of dialects: {csv.list_dialects()}")
print(csv.get_dialect("excel-tab"))