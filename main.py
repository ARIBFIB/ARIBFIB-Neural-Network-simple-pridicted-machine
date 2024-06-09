import csv
import pandas as pd
import numpy as np
from colorama import init, Style
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.pyplot import subplots, plot

with open(r"D:\6th Semester\Data Science-Taimoor Riaz\Assignments\Assignment 1\Cities.csv") as newfile:
    CityData = csv.reader(newfile)
    for row in CityData:
        print(row)

# read the file using pandas
print(Style.BRIGHT + "*****Read the file using pandas******" + Style.RESET_ALL)
Cityfile = pd.read_csv(r"D:\6th Semester\Data Science-Taimoor Riaz\Assignments\Assignment 1\Cities.csv")
print(Cityfile)

#read the head
print(Style.BRIGHT+ "HEAD OF CITY DATA" + Style.RESET_ALL)
cityHead = Cityfile.head(5)
print(cityHead)
#read the tail
print(Style.BRIGHT+ "TAIL OF CITY DATA" + Style.RESET_ALL)
cityTail = Cityfile.tail(5)
print(cityTail)

# Deprecated:
# plt.CityData(Cityfile, (0, 5, 6))

# Single subplot¶
Plot = Cityfile.plot("city")
print(Plot)

# Create the graph in python
#create the pieChart