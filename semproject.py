#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 08:47:47 2020

@author: hariniram
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Harini Ram
# Section: Engr 102-451
# Assignment: semester project
# Date: 11/22/20

# import numpy and matplotlib to use functions
import numpy as np
import matplotlib.pyplot as plt


def plotCountryConsumption (consumers, country):
    ''' Plots single histogram of the consumption of each country from 1990-2016
    
    Parameters:
        consumers (list): list of consumption values of each year for each country
        country (str): name of country code will plot
        
    Returns:
        None
    '''
    # loops through consumers to find country match
    for i in range(len(consumers)):
        if country == consumers[i][0]:
            # title
            name = country
            plt.title('Consumption of ' + name)
        
            # axes titles
            plt.xlabel('Consumption in MTOE')
            plt.ylabel('Number of years')
            consumer_data = consumers[i][1:]
            
        
            # plot graph
            plt.hist(consumer_data, bins = 20, edgecolor = 'black')
            
            # prevents overlapping
            plt.tight_layout()
            
            # save figure
            plt.savefig('/Users/hariniram/Desktop/countryConsumption'+ name + '.png')
        
            # display graph
            plt.show()
            
    

def plotYearConsumption (consumers, year):
    ''' Plots a single histogram of the consumption of countries for each year from 1990-2016
    
    Parameters:
        consumers (list): list of consumption values of each year for each country
        year (str): year will plot
        
    Returns:
        None
    '''
    # loops through consumers to find year match
    for i in range(len(consumers[0])):
        if year == consumers[0][i]:
            # pltYear: extracts data from consumers for all countries in a specific year
            pltYear = []
            # countries: extracts names from consumers of countries
            countries = []
            for index in range(1, len(consumers)):
                pltYear.append(consumers[index][i+1])
                countries.append(consumers[index][0])
                
            # title
            plt.title('Consumption of Countries in ' + year)
            
            # axes titles
            plt.xlabel('Consumption in MTOE')
            plt.ylabel('Number of countries')
            
            # plot histogram
            plt.hist(pltYear, bins = 20, edgecolor = 'black')
            
            # prevents overlapping
            plt.tight_layout()
            
            # save figure
            plt.savefig('/Users/hariniram/Desktop/yearConsumption'+ year + '.png')
            
            # display histogram
            plt.show()
            break
    
def plotCountryEnergyType (energyType, country):
    ''' Plots double line graph of electricity and natural gas consumption of each country from 1990-2016
    
    Parameters:
        energyType (list): list of electricity and natural gas consumption values of each year for each country
        country (str): name of country code will plot
        
    Returns:
        None
    '''
        
    # loops through list to find country match and append consumption values to respective energy type
    electricity = []
    naturalgas = []
    for i in range(len(energyType)):
        if country == energyType[i][0]:
            if 'Electricity' == energyType[i][2]:
                electricity.append(energyType[i][1])
            elif 'Natural Gas' == energyType[i][2]:
                naturalgas.append(energyType[i][1])
                
    
    # title
    fig, ax = plt.subplots()
    
    plt.title('Electricity and Natural Gas Consumption for ' + country)
    

    # axes title
    plt.xlabel('Year')
    plt.ylabel('Consumption in MTOE/bcm')

    # plots average temperature
    plt.plot(electricity, color = 'r', label = 'Electricity')

    # plots average pressure
    plt.plot(naturalgas, color = 'b', label = 'Natural gas')
    
    # sets labels
    labels = []
    for i in range(1990, 2016):
        labels.append(i)
    x = np.arange(len(labels))
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    plt.xticks(rotation=90)
    
    # adjusts labels
    plt.tight_layout()

    # legend
    plt.legend()
    
    # save figure
    plt.savefig('/Users/hariniram/Desktop/countryEnergyType' + country + '.png')
    
    # display graph
    plt.show()
    


def plotYearEnergyType (energyType, year, country):
    ''' Plots double bar graph of electricity and natural gas consumption of each year from 1990-2015
    
    Parameters:
        energyType (list): list of electricity and natural gas consumption values of each year for each country
        year (int): year of countries code will plot
        country (str): name of country code will plot
        
    Returns:
        None
    '''
    
    # loops through list to find year match and append consumption values to respective energy type
    electricity = []
    naturalgas = []
    for i in range(len(energyType)):
        if str(year) == energyType[i][3]:
            if 'Electricity' == energyType[i][2]:
                electricity.append(energyType[i][1])
            else:
                naturalgas.append(energyType[i][1])
                
    # w: width of bars
    w = 0.4
    # x: sets up x axis
    x = np.arange(len(country))

    # plot bar graph
    fig, ax = plt.subplots()
    
    ax.bar(x - w/2, electricity, w, label = 'Electricity')
    ax.bar(x + w/2, naturalgas, w, label = 'Natural Gas')

    # title
    plt.title('Electricity and Natural Gas Consumption for countries in ' + str(year))

    # axes titles
    ax.set_ylabel('Consumption in MTOE/bcm')
    ax.set_xlabel('Countries')

    # set labels on x-axis
    ax.set_xticks(x)
    ax.set_xticklabels(country)
    plt.xticks(rotation = 90)

    # legend
    ax.legend()

    # save figure
    plt.savefig('/Users/hariniram/Desktop/yearEnergyType' + str(year) + '.png')
    
    
    # display graph
    plt.show()
    
   


def plotCountryInd(ind, country):
    ''' Plots single histogram of the industrial usage consumption of each country from 1990-2016
    
    Parameters:
        ind (list): list of industrial usage consumption values of each year for each country
        country (str): name of country code will plot
        
    Returns:
        None
    '''
    
    # loops through ind to find country match
    for i in range(len(ind)):
        if country == ind[i][0]:
            # title
            name = country
            plt.title('Industrial Usage of ' + name)
        
            # axes titles
            plt.xlabel('Industrial Usage in MTOE')
            plt.ylabel('Number of years')
            
            # sort data into two lists -- pre 2000s and post 2000s
            ind_data = ind[i][1:]
            # ind_data1: data prior to 2000
            ind_data1 = []
            # ind_data2: data post 2000
            ind_data2 = []
            for i in range(len(ind_data)):
                if i <= 9:
                    ind_data1.append(ind_data[i])
                else:
                    ind_data2.append(ind_data[i])
                
            
            
            # plot graph
            plt.hist([ind_data1, ind_data2], bins = 20,  edgecolor = 'black', label = ['Up to 2000', 'After 2000'])
            
            # displays legend
            plt.legend()
            
            # prevents overlapping
            plt.tight_layout()
            
            # save figure
            plt.savefig('/Users/hariniram/Desktop/countryInd' + country + '.png')
            
            # display graph
            plt.show()
            
        
def plotYearInd (ind, year, consumers):
    ''' Plots a single histogram of the industrial usage consumption of countries for each year from 1990-2016
    
    Parameters:
        consumers (list): list of industrial usage consumption values of each year for each country
        year (int): year will plot
        
    Returns:
        None
    '''
    # loops through ind to find year match
    for i in range(len(ind[0])):
        if str(year) == consumers[0][i]:
            # pltYear: extracts data from ind for all countries in a specific year
            pltYear = []
            for index in range(len(ind)):
                pltYear.append(ind[index][i+1])
            
            # title
            plt.title('Industrial Usage of Countries in ' + str(year))
            
            # axes titles
            plt.xlabel('Industrial Usage in MTOE')
            plt.ylabel('Number of countries')
            
            # plot histogram
            if i <= 10:
                plt.hist(pltYear, bins = 20, color = 'b', edgecolor = 'black')
            else:
                plt.hist(pltYear, bins = 20, color = 'r', edgecolor = 'black') 
            
            # prevents overlapping
            plt.tight_layout()
            
            # save figure
            plt.savefig('/Users/hariniram/Desktop/yearInd' + str(year) + '.png')
            
            # displays histogram
            plt.show()
            break
        
        
        
        
def plotCountryResidential(continent, name, continent_name):
    ''' Plots single histogram of the residential usage consumption of each continent from 1990-2016
    
    Parameters:
        continent (list): list of residential usage consumption values of each year for each country
        name (str): name of continent code will plot
        continent_name (str): list of continent names
        
    Returns:
        None
    '''
    
    # loops through ind to find country match
    for i in range(len(continent_name)):
        if continent_name[i] == name:
            residential = []
            for j in range(len(continent[i])):
                residential_sub = []
                for k in range(1, len(continent[i][j])):
                    if k <= 10:
                        residential_sub.append(0.85*continent[i][j][k])
                    else:
                        residential_sub.append(0.65*continent[i][j][k])
                residential.append(residential_sub)
            # title
            plt.title('Residential Usage of ' + name)
        
            # axes titles
            plt.xlabel('Residential Usage in MTOE')
            plt.ylabel('Number of years')
                
                
            # sort data into two lists -- pre 2000s and post 2000s
            # ind_data1: data prior to 2000
            residential_data1 = []
            # ind_data2: data post 2000
            residential_data2 = []
            for i in range(len(residential)):
                for j in range(len(residential[i])):
                    if j <= 9:
                        residential_data1.append(residential[i][j])
                    else:
                        residential_data2.append(residential[i][j])
                
        
            # plot graph
            plt.hist([residential_data1, residential_data2], bins = 20,  edgecolor = 'black', label = ['Before 2000', 'After 2000'])
                
            
            # displays legend
            plt.legend()
            
            # prevents overlapping
            plt.tight_layout()
        
            # save figure
            plt.savefig('/Users/hariniram/Desktop/countryResidential' + name + '.png')
        
            # display graph
            plt.show()
            
            

#### 1. load file EnergyConsumers.txt into a 2D array named Consumers ####
# create empty list named consumers
consumers = []
country = []
# append in data by splitting each line by '\t'
with open('EnergyConsumers.txt', 'r') as f:
    f.readline()
    f.readline()
    for line in f.readlines():
       consumers.append(line.strip().split('\t'))
# cast consumption values as floats
for i in range(1, len(consumers)):
    for j in range(1, len(consumers[i])):
        consumers[i][j] = float(consumers[i][j])

for i in range(1, len(consumers)):
    country.append(consumers[i][0])

# convert list to numpy array
np.asarray(consumers)

        




#### 2. create single histogram of the consumption for each country and each year from consumers ####
for i in range(1, len(consumers)):
    plotCountryConsumption(consumers, consumers[i][0])
    
for i in consumers[0]:
    plotYearConsumption(consumers, i)




#### 3. load file EnergyRawDataFinal.txt into any container named EnergyType ####
# create empty list named energyType
energyType = []
# append in data by splitting each line by ','
with open('EnergyRawDataFinal.txt', 'r') as g:
    g.readline()
    for line in g.readlines():
        energyType.append(line.strip().split(','))
# cast consumption values as floats
for i in range(len(energyType)):
    energyType[i][1] = float(energyType[i][1])


#### 4. create a single graph comparing Electricity and Natural gas for each country and each year from EnergyType ####
for country_name in country:
   plotCountryEnergyType(energyType, country_name)
    

for i in range(1990, 2016):
   plotYearEnergyType(energyType, i, country)




#### 5. save 2d array name Ind with all data corresponding to industrial usage type in consumers ####
# creates empty list named Ind
ind = []
for i in range(1,len(consumers)):
   ind_sub = []
   for j in range(len(consumers[i])):
        if j == 0:
            ind_sub.append(consumers[i][j])
        elif j <= 10:
            ind_sub.append(0.15*consumers[i][j])
        else:
            ind_sub.append(0.35*consumers[i][j])
   ind.append(ind_sub)



#### 6. create single histogram of Ind for each country and each year ####
for i in range(len(ind)):
   plotCountryInd(ind, ind[i][0])
    
for i in range(1990, 2017):
  plotYearInd(ind, i, consumers)



#### 7. make histogram of consumption for China only from consumers ####
# title
plt.title('Consumption of China')

# axes titles
plt.xlabel('Consumption in MTOE')
plt.ylabel('Number of years')

# plot graph
plt.hist(consumers[27][1:], bins = 15, edgecolor = 'black')

# save figure
plt.savefig('/Users/hariniram/Desktop/chinaConsumption.png')

# display graph
plt.show()





#### 8. create a new numpy object variable named Continent for usage by continent data from consumers ####
# continent_name: list of all continent names
continent_name = ['Europe', 'North America', 'South America', 'Asia', 'Africa', 'Middle East']
# continent: empty list that will append consumer data and sort based on continent, rather than country; 3D array
continent = []

# appends consumer data from all countries in Europe
europe = []
for i in range(1, 19):
    europe.append(consumers[i])
continent.append(europe)

# appends consumer data from all countries in North America
namerica = []
for i in list(range(19, 21)) + list(range(25, 26)):
    namerica.append(consumers[i])
continent.append(namerica)

# appends consumer data from all countries in South America
samerica = []
for i in list(range(21, 25)) + list(range(26, 27)):
    samerica.append(consumers[i])
continent.append(samerica)

# appends consumer data from all countries in Asia
asia = []
for i in range(27, 37):
    asia.append(consumers[i])
continent.append(asia)

# appends consumer data from all countries in Africa
africa = []
for i in range(37, 41):
   africa.append(consumers[i])
continent.append(africa)

# appends consumer data from all countries in the Middle East
middleEast = []
for i in range(41, 45):
    middleEast.append(consumers[i])
continent.append(middleEast)

# cast continent as an array object
np.asarray(continent)



#### 9. create histogram of continents for only residential usage ####
for i in range(len(continent_name)):
    plotCountryResidential(continent, continent_name[i], continent_name)




#### 10. load file CarbonEmissions.txt into list named CarbonEmissions ####
# create empty lists named carbonEmissions and countries
carbonEmissions = []
# append in data by splitting each line by '\t'
with open('CarbonEmissions.txt', 'r') as h:
    h.readline()
    for line in h.readlines():
        carbonEmissions.append(line.strip().split('\t'))

# cast carbon emission values as floats
for i in range(len(carbonEmissions)):
    carbonEmissions[i][2] = float(carbonEmissions[i][2])
        


#### 11. using a double bar graph, compare the 20 countries' carbon emissions to respective consumption in 2015 ####
# creates an empty list named countries
countries = []
# extrapolates list of countries from carbonEmissions
for i in range(len(carbonEmissions)):
    countries.append(carbonEmissions[i][1])

# create an empty list named consumption2015 
consumption2015 = []
# extrapolate consumption value of 2015 from consumers
for i in range(len(countries)):
    for j in range(len(consumers)):
        if countries[i] == consumers[j][0]:
            consumption2015.append(consumers[j][24])
            
# create an empty list named carbon
carbon = []
# extrapolate carbon emission values from carbonEmissions
for i in range(len(carbonEmissions)):
    carbon.append(carbonEmissions[i][2])
            
# w: width of bars
w = 0.4
# x: sets up x axis
x = np.arange(len(countries))

# plot bar graph
fig, ax = plt.subplots()

ax.bar(x - w/2, consumption2015, w, label = 'Consumption in 2015')
ax.bar(x + w/2, carbon, w, label = 'Carbon Emissions')

# title
ax.set_title('Comparing Consumption in 2015 and Carbon Emissions of Countries')

# axes titles
ax.set_ylabel('Mt/MTOE')
ax.set_xlabel('Countries')

# set labels on x-axis
ax.set_xticks(x)
ax.set_xticklabels(countries)
plt.xticks(rotation=90)

# legend
ax.legend()

# save figure
plt.savefig('/Users/hariniram/Desktop/carbonEmissions.png')

# display graph
plt.show()



#### 12. what are the countries with the highest energy usage? In what continent are they located? ####
print('The countries with the highest energy usage are China, United States, and India. '
      'China and India are located in Asia and the United States is located in North America.')


