#Name : Sarang Barshikar
#Title : K-nearest Neigbour for iris dataset

import pandas as pd
import math
df=pd.read_csv("iris2.csv")

# If want a program with dynamic inputs just remove the comments of line 8,9,10 & comment lines 19,20,21,22



# sepallength = input("Enter the sepal length : ")
# sepalwidth  = input("Enter the sepal width : ")
# petallength = input("Enter the petal length : ")
# petalwidth  = input("Enter the petal width : ")


# 5.1,3.5,1.4,0.2,0

# 6.4,3.2,4.5,1.5,1
# 7.7,2.8,6.7,2
sepallength = 15.1
sepalwidth = 10.5 
petallength = 5.7
petalwidth = 1.2


euclideans =0
edistance = []
i=0
train_sepallen = df['sepal_length']
train_sepalwid = df['sepal_width']
train_petallen = df['petal_length']
train_petalwid = df['petal_width']
# print(len(df))

#Calculating the euclidean distance between query points & actual data points
for i in range(len(df)):
    euclideans= math.sqrt(((sepallength - df['sepal_length'][i])**2)+((sepalwidth - df['sepal_width'][i])**2)+((petallength - df['petal_length'][i])**2)+((petalwidth - df['petal_width'][i])**2))
    edistance.append((euclideans,df['species'][i]))


#getting smallest k neighbours from the set . Here we have k =3
k=3
res = [list(ele) for ele in edistance] 
distance = sorted(res,key=lambda x:x[0])[:k]

zero = 0
one = 0
two = 0
for i in distance: 
    if i[1] == 0:
        zero+=1
    if i[1] == 1:
        one+=1
    if i[1] == 2:
        two+=1
print(distance)

if zero>one and zero>two:
    print("Flower is Setosa")
if one>zero and one>two:
    print("Flower is Versicolor")
if two>zero and two >one:
    print("Flower is Verginica")
