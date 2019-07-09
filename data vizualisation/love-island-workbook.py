# Love Island Data Visualisation Workbook

# First load in the packages needed to run this code

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Read CSV file from local directory
data = pd.read_csv('love-island-historical-dataset.csv')
#data.tail()
data.head()

# The describe() function shows you counts, max, min etc values of what is in your dataset 
data.describe()

# Look at the shape/size of the data, as well as the columns used in the Pandas DataFrame structure
shape = data.shape
columns = data.columns.tolist()
print("Shape of the data: ", shape)
print("Columns within the dataset: ", columns)

# Select and filter your data frame to view different values. Below we are filtering the dataframe where the OUTCOME field is equal to 'WINNER'
winners = data[data['OUTCOME'].values == 'WINNER']
#if running in notebooks:
# winners.style
#if running in IDE terminal:
print(winners)

# Can you filter the dataframe where the OUTCOME field is equal to 'RUNNER UP'
# <<Add your code here>>


# Can you filter the dataframe where the OUTCOME field is equal to 'THIRD PLACE'
# <<Add your code here>>


# Graphs

#Simple Box Plot showing the spread of ages of contestants in the villa
ages = data['Age']
plt.boxplot(ages)
plt.show()
#if running in interactive IDE (such as notebooks) you do not need plt.show()

# Split data by love island series
year2018 = data[data['love-island-series'].values == 2018]
year2017 = data[data['love-island-series'].values == 2017]
year2016 = data[data['love-island-series'].values == 2016]

ages_2018 = np.array(year2018[['Age']])
ages_2017 = np.array(year2017[['Age']])
ages_2016 = np.array(year2016[['Age']])

fig = plt.figure(figsize =(10,10))

ax1 = fig.add_subplot(221)
ax1.violinplot(ages_2018, showmedians = True)
plt.xticks([1], ['2018'])
plt.title('Distribution of Ages for Love Island 2018')

ax2 = fig.add_subplot(222)
ax2.violinplot(ages_2017, showmedians = True)
plt.xticks([1], ['2017'])
plt.title('Distribution of Ages for Love Island 2017')

plt.show()

# Lets work through this together ...
# Can we add a 3rd Violin plot for age distribution of Love Island 2016 contestants

# main dataset
daysinvilla = data[['Contestant Name','NUMBER OF DAYS IN VILLA', 'love-island-series', 'First Group to enter villa']]

# Split data by love island series
year2018 = daysinvilla[daysinvilla['love-island-series'].values == 2018].sort_values('NUMBER OF DAYS IN VILLA')
year2017 = daysinvilla[daysinvilla['love-island-series'].values == 2017].sort_values('NUMBER OF DAYS IN VILLA')
year2016 = daysinvilla[daysinvilla['love-island-series'].values == 2016].sort_values('NUMBER OF DAYS IN VILLA')


fig = plt.figure(figsize =(20,20))

ax1 = fig.add_subplot(221)
ax1.barh(year2018['Contestant Name'], year2018['NUMBER OF DAYS IN VILLA'],height= 0.8, color = 'magenta', label = '2018')
plt.title('Love Island 2018 - Contestants by number of days in the villa')
plt.legend()

ax2 = fig.add_subplot(222)
ax2.barh(year2017['Contestant Name'], year2017['NUMBER OF DAYS IN VILLA'],height= 0.8, color = 'blue', label = '2017')
plt.title('Love Island 2017 - Contestants by number of days in the villa')
plt.legend()

ax3 = fig.add_subplot(223)
ax3.barh(year2016['Contestant Name'], year2016['NUMBER OF DAYS IN VILLA'],height= 0.8, color = 'lawngreen', label = '2016')
plt.title('Love Island 2016 - Contestants by number of days in the villa')
plt.legend()

plt.show()

# simple pie charts
areaofuk = data['Area of UK'].value_counts()

# print the value counts of where the love island contestants live in the UK

#Change the colours of the pie chart - what colours are available: https://matplotlib.org/1.2.1/api/colors_api.html
colours = ['deeppink', 'aqua', 'magenta', 'silver', 'lime', 'yellow']

# Change the exploded value of the pie chart to 'North'
explode = (0.2,0,0, 0,0, 0)

plt.pie(areaofuk, labels = areaofuk.index, colors = colours, explode=explode, autopct='%.0f', startangle=90)
plt.show()

# % chance given historical data
first_to_enter_villa = len(data['First Group to enter villa'])
first_to_enter_villa_yes = len(data[data['First Group to enter villa'].values == 'YES'])
first_to_enter_villa_no = len(data[data['First Group to enter villa'].values == 'NO'])

first_villa = data[(data['First Group to enter villa'].values == 'YES')]
winner = data[data['OUTCOME'].values == 'WINNER']
runnerup = data[data['OUTCOME'].values == 'RUNNER UP']
thirdplace = data[data['OUTCOME'].values == 'THIRD PLACE']
first_villa_and_winner = data[(data['First Group to enter villa'].values == 'YES')&(data['OUTCOME'].values == 'WINNER')]
first_villa_and_runnerup = data[(data['First Group to enter villa'].values == 'YES')&(data['OUTCOME'].values == 'RUNNER UP')]
first_villa_and_thirdplace = data[(data['First Group to enter villa'].values == 'YES')&(data['OUTCOME'].values == 'THIRD PLACE')]



percent_first_villa_and_winner = (len(first_villa_and_winner)/len(winner))*100
print('Percentage of poeple who won and were part of the first group to enter the villa: '+ str(percent_first_villa_and_winner) + '%')

percent_first_villa_inc_runnerup = ((len(first_villa_and_winner)+(len(first_villa_and_runnerup)))/(len(winner)+len(runnerup)))*100
print('Percentage of poeple who won/runner up and were part of the first group to enter the villa: ' + str(percent_first_villa_inc_runnerup) + '%')

percent_first_villa_inc_thirdplace = ((len(first_villa_and_winner)+len(first_villa_and_runnerup)+len(first_villa_and_thirdplace))/(len(winner)+len(runnerup)+len(thirdplace)))*100
print('Percentage of poeple who won/runner up/third place and were part of the first group to enter the villa: ' + str(percent_first_villa_inc_thirdplace) + '%')

#Creating variables from the dataframe to create scatter plots to see correlations between variables
x1 = data['Day Joined Villa']
y1 = data['Number of Couples']
x2 = data['Age']
y2 = data['Longest couple length']
y3 = data['NUMBER OF DAYS IN VILLA']
y4 = data['Day left Villa']

data_2018 = data[data['love-island-series'] >= 2018]
x5 = data_2018['NUMBER OF DAYS IN VILLA']
y5 = data_2018['Times got Pied']
y6 = data_2018['Number of dates']
y7 = data_2018['Number of Bust Ups']

data_2017 = data[data['love-island-series'] >= 2017]
x6 = data_2017['NUMBER OF DAYS IN VILLA']
y8 = data_2017['Times got Pied']
y9 = data_2017['Number of dates']
y10 = data_2017['Number of Bust Ups']


#Example Scatter plot of:
# x axis: Day contestant entered the villa
# y-axis: Number of couples they were in

plt.figure(figsize=(10,10))
plt.scatter(x1,y1, color='magenta', marker='d', linewidths = '3')
plt.xlabel("Day entered the Villa")
plt.ylabel("Number of couples")
plt.title('Day Contestant Joined the Villa by Number of Couples they had - trending down')
plt.show()


# Create your own scatter plots using the variables above to find correlations between variables
plt.figure(figsize=(10,10))
plt.scatter(<ENTER X AXIS HERE>,<ENTER Y AXIS HERE>, color='cyan', marker='d', linewidths = '3')
plt.xlabel("Enter X axis label here")
plt.ylabel("Enter Y axis label here")
plt.title('Enter graph title here')
plt.show()


# Here is an example of adding all the graphs onto one figure/chart space
fig = plt.figure(figsize =(20,20))

ax1 = fig.add_subplot(221)
ax1.scatter(x1,y1, color='magenta', marker='d', linewidths = '3')
plt.xlabel("Day entered the Villa")
plt.ylabel("Number of couples")
plt.title('Day Contestant Joined the Villa by Number of Couples they had - trending down')

ax2 = fig.add_subplot(222)
ax2.scatter(x2,y1, color='cyan', marker='d', linewidths = '3')
plt.xlabel("Age")
plt.ylabel("Number of couples")
plt.title('A graph to show how age relates to Number of couples across the show')

ax3 = fig.add_subplot(223)
ax3.scatter(x2,y4, color='lime', marker='d', linewidths = '3')
plt.xlabel("Age")
plt.ylabel("Day left the Villa")
plt.title('No correlation shown between leaving the villa and age')

ax4 = fig.add_subplot(224)
ax4.scatter(x5,y6, color='magenta', marker='d', linewidths = '3')
plt.xlabel("Number of days in Villa")
plt.ylabel("Number of times pied")
plt.title('Number of days in villa by number of dates')
plt.show()


#CASA AMOR EXPLORATORY ANALYSIS

casa_amor = data[data['Casa Amor addition'].values == 'YES']
#print(casa_amor)

casaamor_sort= casa_amor.groupby(['OUTCOME'])
counts = casaamor_sort.size()

total = sum(counts)

dumped = (counts[0] / total) * 100
other = (counts[1] / total) * 100


print('Percentage of contestants who were dumped from the island: '+ str(round(dumped,2)) + '%')
print('Percentage of contestants who placed well on Love Island: '+ str(round(other,2)) + '%')


print(casa_amor)

# main dataset
daysinvilla = casa_amor[['Contestant Name','NUMBER OF DAYS IN VILLA', 'love-island-series']]
#print(daysinvilla.sort_values('NUMBER OF DAYS IN VILLA'))

# Split data by love island series
year2018 = daysinvilla[daysinvilla['love-island-series'].values == 2018].sort_values('NUMBER OF DAYS IN VILLA')
year2017 = daysinvilla[daysinvilla['love-island-series'].values == 2017].sort_values('NUMBER OF DAYS IN VILLA')


fig = plt.figure(figsize =(20,20))

ax1 = fig.add_subplot(221)
ax1.barh(year2018['Contestant Name'], year2018['NUMBER OF DAYS IN VILLA'],height= 0.8, facecolor = 'magenta')
plt.xlabel("No. of days in the villa")
plt.ylabel("Contestant Name")
plt.title('No. of days Casa Amor contestant additions were in the villa - 2018')

ax2 = fig.add_subplot(222)
ax2.barh(year2017['Contestant Name'], year2017['NUMBER OF DAYS IN VILLA'],height= 0.8, facecolor = 'lime')
plt.xlabel("No. of days in the villa")
plt.ylabel("Contestant Name")
plt.title('No. of days Casa Amor contestant additions were in the villa - 2017')
plt.show()


#Histogram of Casa Amor additions and how long they stay in the villa
days = daysinvilla['NUMBER OF DAYS IN VILLA']
casa_amor_2017 = year2017['NUMBER OF DAYS IN VILLA']
casa_amor_2018 = year2018['NUMBER OF DAYS IN VILLA']

fig = plt.figure(figsize=(25,15))
ax1 = plt.subplot2grid((2,3),(0,0), colspan = 2)
ax1.hist(days, facecolor='magenta', edgecolor='black', bins=7)
ax1.set_label('All Casa Amor Contestants')
plt.xlabel('Buckets of Number of days Casa Amor additions stayed in the villa')
plt.ylabel('Number of contestants that lasted that many days')
plt.title('The number of days ALL Casa Amor contestants have stayed in the Villa')

ax2 = plt.subplot2grid((2,3), (1,0))
ax2.hist(casa_amor_2017, facecolor='cyan', edgecolor='black', bins=10)
ax2.set_label('Casa Amor Contestants from 2017')
plt.xlabel('Buckets of Number of days Casa Amor additions stayed in the villa')
plt.ylabel('Number of contestants that lasted that many days')
plt.title('The number of days 2017 Casa Amor contestants have stayed in the Villa')

ax3 = plt.subplot2grid((2,3), (1,1))
ax3.hist(casa_amor_2018, facecolor='lime', edgecolor='black', bins=10)
ax3.set_label('Casa Amor Contestants from 2018')
plt.xlabel('Buckets of Number of days Casa Amor additions stayed in the villa')
plt.ylabel('Number of contestants that lasted that many days')
plt.title('The number of days 2018 Casa Amor contestants have stayed in the Villa')
ax3.yaxis.tick_right()

plt.show()

