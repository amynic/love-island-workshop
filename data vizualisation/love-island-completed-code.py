#Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Read CSV file
data = pd.read_csv('love-island-historical-dataset.csv')
data.tail()

data.describe()


shape = data.shape
columns = data.columns.tolist()
print("Shape of the data: ", shape)
print("Columns within the dataset: ", columns)



winners = data[data['OUTCOME'].values == 'WINNER']
winners.style

winners = data[data['OUTCOME'].values == 'RUNNER UP']
winners.style


winners = data[data['OUTCOME'].values == 'THIRD PLACE']
winners.style


# Graphs

#simple histogram
ages = data['Age']
plt.boxplot(ages)


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

ax3 = fig.add_subplot(223)
ax3.violinplot(ages_2016, showmedians = True)
plt.xticks([1], ['2016'])
plt.title('Distribution of Ages for Love Island 2016')


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

# simple pie charts
areaofuk = data['Area of UK'].value_counts()
destination = data['From'].value_counts()

colours = ['deeppink', 'aqua', 'magenta', 'silver', 'lime', 'yellow']
explode = (0.2,0,0, 0,0, 0)

fig = plt.figure(figsize =(10,10))

ax1 = fig.add_subplot(221)
ax1.pie(areaofuk, labels = areaofuk.index, colors = colours, explode=explode, autopct='%.2f', startangle=90)
#plt.axis('equal')

ax2 = fig.add_subplot(222)
ax2.pie(destination, labels = destination.index, colors = colours, autopct='%.2f', startangle=90)
#plt.axis('equal')


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

#Scatter Plot - day joined villa / no of couple
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


plt.figure(figsize=(10,10))
plt.scatter(x1,y1, color='magenta', marker='d', linewidths = '3')
plt.xlabel("Day entered the Villa")
plt.ylabel("Number of couples")
plt.title('Day Contestant Joined the Villa by Number of Couples they had - trending down')
plt.show()

plt.figure(figsize=(10,10))
plt.scatter(x2,y1, color='cyan', marker='d', linewidths = '3')
plt.xlabel("Age")
plt.ylabel("Number of couples")
plt.title('A graph to show how age relates to Number of couples across the show')#
plt.show()


plt.figure(figsize=(10,10))
plt.scatter(x2,y4, color='lime', marker='d', linewidths = '3')
plt.xlabel("Age")
plt.ylabel("Day left the Villa")
plt.title('No correlation shown between leaving the villa and age')
plt.show()


plt.figure(figsize=(10,10))
plt.scatter(x5,y6, color='magenta', marker='d', linewidths = '3')
plt.xlabel("Number of days in Villa")
plt.ylabel("Number of times pied")
#plt.title('No correlation shown between leaving the villa and age')
plt.show()


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


# CASA AMOR EXPLORATORY ANALYSIS

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

