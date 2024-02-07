#Imports
import matplotlib.pyplot as plt
import random


#Variable Initialisation
startingValue = 0
finalValue = 0


#SubPrograms

#A simple function to calculate percentage increase
def CalculateIncrease(startingValue, finalValue):
    differenceInValue = finalValue-startingValue
    percentageIncrease = (differenceInValue/startingValue)*100
    return percentageIncrease


#A function that will model a market with profit margins (not very accurate needs improving)
def ProjectProfitMargins(marketInstability,percentageIncrease,timeScale,startingValue):
    profitPredictions = []
    percentageIncrease += 100
    percentageIncrease /= 100
    
    for i in range(0,timeScale):
        randomPercentageIncrease = percentageIncrease +  (random.randint(marketInstability*-1,marketInstability)/100)
        print(randomPercentageIncrease)
        profitPredictions.append(startingValue * (randomPercentageIncrease**i))
    
    return profitPredictions
        

#A procedure to quickly plot a list of y coordinates
def DrawGraph(data):
    x = []
    for i in range(0, len(data)):
        x.append(i)
    
    plt.plot(x,data)


#A function that calculates the average profit for 200 months
def CalculateAverage(marketInstability,percentageIncrease,timeScale,startingValue):
    averageList = ProjectProfitMargins(marketInstability,percentageIncrease,timeScale,startingValue)
    for i in range(1,200):
        outcomeList = ProjectProfitMargins(marketInstability,percentageIncrease,timeScale,startingValue)
        for outcome in range(0,len(outcomeList)):
            averageList[outcome] = ((averageList[outcome] * i) + outcomeList[outcome])/(i+1)
    
    return averageList


#A procedure that draws all the simulated runs and upon closing that graph will then show the average result.
def DrawProfitGraph(marketInstability,percentageIncrease,runCount,startingValue):
    averageList = ProjectProfitMargins(marketInstability,percentageIncrease,runCount,startingValue)
    for i in range(1,200):
        outcomeList = ProjectProfitMargins(marketInstability,percentageIncrease,runCount,startingValue)
        for outcome in range(0,len(outcomeList)):
            averageList[outcome] = ((averageList[outcome] * i) + outcomeList[outcome])/(i+1)
        DrawGraph(outcomeList)
    plt.show()

    DrawGraph(averageList)
    plt.show()


#Main
DrawProfitGraph(5,CalculateIncrease(2.30,2.50),200,2.30)