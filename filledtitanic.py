# Write a program of the read to file and using some methods
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# read to file as
df = pd.read_csv("Titanic_filled.csv")
print(df)


# finding to be null 
NUll2 = df['age'].isnull().sum()
print(f"check to be null in file : {NUll2} ")


# here count to be sex ;
single_line = df["sex"]
print(single_line)

# here finding to be null in sex
Null2 = df['age'].isnull().sum()
print(f"checking here null in sex line : {Null2}")

# here print only female ;
count1 = df["sex"].value_counts()
print(count1)

sns.lineplot(x ="age",y ="fare",hue="sex",data = df,dashes=False,size= 70,markers="o")
plt.title("Age vs Fare in sex ")
plt.legend()
plt.grid(True)
plt.show()


average = df["age"].mean()
print(f"Average per person : {round(average)}")