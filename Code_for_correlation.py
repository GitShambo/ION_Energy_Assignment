###Correlation between
#1. Grid Status, SOC
#2. Equivalent cycle, SOH
#3. SOC, temparature

#Importing the required libraries
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

import os
os.getcwd()
#Changing the directory
os.chdir('Desktop\ION_Energy_Assignment')
os.getcwd()

data = pd.read_csv("Assignment file for Data Analyst - assignment file.csv")
data.head()
#Checking the dimension of the dataset
data.size
data.shape
data.ndim
#checking the data types
data.dtypes
#Among the variables we require all are continuous except Grid status
#Grid status is categorical, it takes the values only 0 and 1

#Data sanity check
#To check if there is any missing values in Grid status
data['Grid status'].isnull().values.any()
#If there is no missing values the sum should be zero
data['Grid status'].isnull().sum()

#To check if there is any missing values in SOC
data['SOC'].isnull().values.any()
#If there is no missing values the sum should be zero
data['SOC'].isnull().sum()

#To check if there is any missing values in Equivalent cycle
data['Equivalent cycle'].isnull().values.any()
#If there is no missing values the sum should be zero
data['Equivalent cycle'].isnull().sum()

#To check if there is any missing values in SOH
data['SOH'].isnull().values.any()
#If there is no missing values the sum should be zero
data['SOH'].isnull().sum()

#To check if there is any missing values in Temperature
data['Temperature'].isnull().values.any()
#If there is no missing values the sum should be zero
data['Temperature'].isnull().sum()


#Correlation coefficient between Grid status and SOC
#Grid status is dichotomous and SOC is continuous varibale. So point biserial correlation
#is mathematically equivalent to Pearson's correlation coefficient. So we are calculating
#Pearson's correlation coefficient here
np.corrcoef(data['Grid status'], data['SOC'])
#0.22794666

#Sctterplot of Grid status and SOC
#It would be just two columns as the one of the variable is of binary type
matplotlib.style.use('ggplot')
plt.scatter(data['Grid status'], data['SOC'])
plt.xlabel('Grid status')
plt.ylabel('SOC')
plt.title('Grid status vs SOC')
plt.savefig('Grid status vs SOC.png')
#Let's see the distribution of SOC when Grid status is 0 and when Grid status is 1    
#Spliiting the dataset in two dataset where Grid status is 0 and 1
k0 = data[data['Grid status'] == 0]
k1 = data[data['Grid status'] == 1]
#Having a look and checking the dimension of the two dataset
k0.head()
k0.shape

k1.head()
k1.shape

#Histogram of SOC when Grid status is 0, taking 10 bins
plt.hist(k0.SOC, bins = 10, color = 'skyblue')
plt.title('Histogram of SOC when Grid status is 0')
plt.savefig('Histogram of SOC when Grid status is 0.png')
#Histogram of SOC when Grid status is 1, taking 10 bins
plt.hist(k1.SOC, bins = 10, color = 'seagreen')
plt.title('Histogram of SOC when Grid status is 1')
plt.savefig('Histogram of SOC when Grid status is 1.png')

#For histogram and density plot in same curve
import seaborn as sb
sb.distplot(k0.SOC, bins = 10, color = 'blue')
plt.title('Histogram with density plot of SOC when Grid status is 0')
plt.savefig('Histogram with density plot of SOC when Grid status is 0.png')

sb.distplot(k1.SOC, bins = 10, color = 'green')
plt.title('Histogram with density plot of SOC when Grid status is 1')
plt.savefig('Histogram with density plot of SOC when Grid status is 1.png')

#Correlation coefficient between Equivalent cycle and SOH
np.corrcoef(data['Equivalent cycle'], data['SOH'])
#-0.98426245

#Sctterplot of Equivalent cycle and SOH
plt.scatter(data['Equivalent cycle'], data['SOH'])
plt.xlabel('Equivalent cycle')
plt.ylabel('SOH')
plt.title('Equivalent cycle vs SOH')
plt.savefig('Equivalent cycle vs SOH.png')

#Correlation coefficient between SOC and Temperature
np.corrcoef(data['SOC'], data['Temperature'])
#-0.36904035

#Sctterplot of SOC and Temperature
plt.scatter(data['SOC'], data['Temperature'])
plt.xlabel('SOC')
plt.ylabel('Temperature')
plt.title('SOC vs Temperature')
plt.savefig('SOC vs Temperature.png')