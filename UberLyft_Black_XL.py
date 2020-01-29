# Modules
import os
import csv

Uber_XL = "UberXL"
UberLux = "UberX"
Uber_Black = "Black"
Uber_Black_SUV = "BlackSUV"

# Set path for file
# csvpath = os.path.join("..", "Data_files", "uber.csv")
csvpath = os.path.join("Data_files", "uber.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        if row[7] == Uber_XL or row[7] == UberLux or row[7] == Uber_Black or row[7] == Uber_Black_SUV:
            print(row[0] + "   " + row[7] + "   " + row[8] + "   " + row[9])

