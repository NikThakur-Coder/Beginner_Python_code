#Here in this Project, i am going to create a dashboad

import pandas as pd

baby = pd.read_csv(r"C:\Users\Neeraj\Desktop\us_baby_names.csv")
list_year = []
for a in baby['Year']:
    if a not in list_year:
        list_year.append(a)
z = 0
while list_year[z]:
    baby_in_year = baby.loc[baby['Year']] == list_year[z]
    baby_in_year_sort = baby_in_year.sort_values(by='Count', ascending=False).head(1)
    csv = baby_in_year_sort.to_csv("Top_one_Name.csv", mode='a', header=False)
    z += 1
    if z == len(list_year):
        break