"""
csv: comma separate value
"""
import csv

with open("mycsvfile.csv","w") as file:
    writer = csv.writer(file)

    writer.writerow(["id","name","subject","city"])
    writer.writerow([1,"mittal","python","Ahmedabad"])
