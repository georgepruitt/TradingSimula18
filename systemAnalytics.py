from operator import itemgetter
import random
def calcSystemResults(systemMarketList):
    masterDateList = list()
    cumulativeEquity = list()
    monthList = list()
    monthEquity = list()
    yearEquity = list()
    printToTerminal = 0
    fileName1 = systemMarketList[0].systemName + "-Summary.txt"
    target1 = open(fileName1,"w")
    fileName2 = systemMarketList[0].systemName + "-Trades.txt"
    target2 = open(fileName2,"w")
    fileName3 = systemMarketList[0].systemName + "-StrtTrdDD.txt"
    target3 = open(fileName3,"w")
    fileName4 = systemMarketList[0].systemName + "-MonteCarlo.txt"
    target4 = open(fileName4,"w")

    tradeTuple = list()
    startTradeTuple = list()
    for i in range(0,len(systemMarketList)):
        monthList[:] = []
        monthEquity[:] = []
        yearEquity[:] = []
        cumulativeEquity[:] =[]
        if printToTerminal == 1: print('-----------------------------------------')
        target1.write('-----------------------------------------\n')
        if printToTerminal == 1: print("Sys Name : ",systemMarketList[i].systemName)
        lineOutPut = "Sys Name : " + systemMarketList[i].systemName
        target1.write(lineOutPut)
        target1.write("\n")
        if printToTerminal == 1: print("Mkt Symb : ",systemMarketList[i].symbol)
        lineOutPut = "Mkt Symb : " + systemMarketList[i].symbol
        target1.write(lineOutPut)
        target1.write("\n")
        if printToTerminal == 1: print("Profit/Loss : ",round((systemMarketList[i].profitLoss),2))
        lineOutPut = "Profit/Loss : " + str(round((systemMarketList[i].profitLoss),2))
        target1.write(lineOutPut)
        target1.write("\n")
        if printToTerminal == 1: print("Num Trades : ",round((systemMarketList[i].numTrades),0))
        lineOutPut = "Num Trades : " + str(round((systemMarketList[i].numTrades),0))
        target1.write(lineOutPut)
        target1.write("\n")
        if printToTerminal == 1: print("Percent Wins : ",round((systemMarketList[i].perWins),3))
        lineOutPut = "Percent Wins : " + str(round((systemMarketList[i].perWins),3))
        target1.write(lineOutPut)
        target1.write("\n")

        if printToTerminal == 1: print("Avg Win  : ",round((systemMarketList[i].avgWin),2))
        lineOutPut = "Avg Win  : " + str(round((systemMarketList[i].avgWin),2))
        target1.write(lineOutPut)
        target1.write("\n")

        if printToTerminal == 1: print("Avg Loss : ",round((systemMarketList[i].avgLoss),2))
        lineOutPut = "Avg Loss : " + str(round((systemMarketList[i].avgLoss),2))
        target1.write(lineOutPut)
        target1.write("\n")

        if printToTerminal == 1: print("Avg Trade: ",round((systemMarketList[i].avgTrade),2))
        lineOutPut = "Avg Trade: " + str(round((systemMarketList[i].avgTrade),2))
        target1.write(lineOutPut)
        target1.write("\n")

        if printToTerminal == 1: print("MAX DrawDown: ",round((systemMarketList[i].equity.maxDD),2))
        lineOutPut = "MAX DrawDown: " + str(round((systemMarketList[i].equity.maxDD),2))
        target1.write(lineOutPut)
        target1.write("\n")

        if printToTerminal == 1: print("Avg Monthly Return: ",round((systemMarketList[i].avgMonthlyReturn),5))
        lineOutPut = "AVG Monthly Return: " + str(round((systemMarketList[i].avgMonthlyReturn),5))
        target1.write(lineOutPut)
        target1.write("\n")

        if printToTerminal == 1: print("Monthly StdDev: ",round((systemMarketList[i].avgMonthlyStdDev),5))
        lineOutPut = "Monthly StdDev: " + str(round((systemMarketList[i].avgMonthlyStdDev),5))
        target1.write(lineOutPut)
        target1.write("\n")


        if printToTerminal == 1: print('-----------------------------------------')
        target1.write('-----------------------------------------\n')
#        target.close()

        tempLen = len(systemMarketList[i].tradesList)

        if printToTerminal == 1: print('-----------------------------------------')
        target2.write('-----------------------------------------\n')
        if printToTerminal == 1: print("Sys Name : ",systemMarketList[i].systemName)
        lineOutPut = "Sys Name : " + systemMarketList[i].systemName
        target2.write(lineOutPut)
        target2.write("\n")
        if printToTerminal == 1: print("Mkt Symb : ",systemMarketList[i].symbol)
        lineOutPut = "Mkt Symb : " + systemMarketList[i].symbol
        target2.write(lineOutPut)
        target2.write("\n")

        for j in range(0,len(systemMarketList[i].tradesList)):
            myTradeDate = systemMarketList[i].tradesList[j].tradeDate
            if systemMarketList[i].tradesList[j].tradeProfit != 0:
                tradeTuple += ((systemMarketList[i].tradesList[j].tradeDate,systemMarketList[i].tradesList[j].tradeProfit),)
            if printToTerminal == 1: print( '%8.0f %12s %2.0d %9.5f %10.2f %10.2f' % (systemMarketList[i].tradesList[j].tradeDate,
                                                             systemMarketList[i].tradesList[j].tradeName[0:11],
                                                             systemMarketList[i].tradesList[j].quant,
                                                             systemMarketList[i].tradesList[j].tradePrice,
                                                             systemMarketList[i].tradesList[j].tradeProfit,
                                                             systemMarketList[i].tradesList[j].cumuProfit))
#           print( '%8.0f %10s' % (systemMarketList[i].tradesList[j].tradeDate,systemMarketList[i].tradesList[j].tradeName))


            target2.write('%8.0f %12s %2.0d %9.5f %10.2f %10.2f\n' % (systemMarketList[i].tradesList[j].tradeDate,
                                                                     systemMarketList[i].tradesList[j].tradeName[0:11],
                                                                     systemMarketList[i].tradesList[j].quant,
                                                                     systemMarketList[i].tradesList[j].tradePrice,
                                                                     systemMarketList[i].tradesList[j].tradeProfit,
                                                                     systemMarketList[i].tradesList[j].cumuProfit))
#            systemMarketList[i].tradesList[j].printTrade()


        masterDateList = systemMarketList[i].equity.equityDate
        monthList = createMonthList(masterDateList)
#        for j in range(0,len(systemMarketList[i].equity.dailyEquityVal)):
#            print(systemMarketList[i].equity.equityDate[j],' ',systemMarketList[i].equity.dailyEquityVal[j])
        begOfYearEquity = 0
        numOfMonths = len(monthList)
        for j in range(0,numOfMonths):
            idx = masterDateList.index(monthList[j])
            if j == 0:
                monthEquity.append(systemMarketList[i].equity.dailyEquityVal[idx])
                prevDailyCum = monthEquity[-1]
                cumulativeEquity.append(prevDailyCum)
            else:
                whichMonth = monthList[j]
                dailyCum = systemMarketList[i].equity.dailyEquityVal[idx]
                cumulativeEquity.append(dailyCum)
                monthEquity.append(dailyCum - prevDailyCum)
                newMonthEquity = dailyCum - prevDailyCum
                prevDailyCum = dailyCum
                if(int(monthList[j]/100) % 100) == 12 or (j == numOfMonths-1):
                    yearEquity.append(cumulativeEquity[-1] - begOfYearEquity)
                    begOfYearEquity = cumulativeEquity[-1]
        yearInc = 0
        for j in range(0,numOfMonths):
            isDecember = False
            if(int(monthList[j]/100) % 100) == 12 or (j == numOfMonths-1):
                isDecember = True;
            if isDecember == False:
                if printToTerminal == 1: print('%8d %10.0f %10.f' % (monthList[j],monthEquity[j],cumulativeEquity[j]))
                target1.write('%8d %10.0f %10.f\n' % (monthList[j],monthEquity[j],cumulativeEquity[j]))
            if isDecember:
                if printToTerminal == 1: print('%8d %10.0f %10.f 10%f' % (monthList[j],monthEquity[j],cumulativeEquity[j],yearEquity[yearInc]))
                target1.write('%8d %10.0f %10.f %10.f\n' % (monthList[j],monthEquity[j],cumulativeEquity[j],yearEquity[yearInc]))
                yearInc +=1
        if printToTerminal == 1: print('-----------------------------------------')
        target1.write('-----------------------------------------\n')
# start trade draw down analysis - utilizing the tradeTuple
    tupleLen = len(tradeTuple)
    tradeTuple = sorted(tradeTuple,key=itemgetter(0))
    for x in range(0,tupleLen):
        cumStartTradeEquity = 0
        maxStartTradeDD = -99999999
        maxCumEquity = 0
        for y in range(x,tupleLen):
#            if printToTerminal == 1: print("Trade Tuple ",tradeTuple[y][0]," ",tradeTuple[y][1]);
            cumStartTradeEquity += tradeTuple[y][1]
            maxCumEquity = max(maxCumEquity,cumStartTradeEquity)
            maxStartTradeDD = max(maxStartTradeDD,maxCumEquity - cumStartTradeEquity)
        if x ==0:
            maxClsTrdDD = maxStartTradeDD
#        target3.write('Trade num: %6d cumuEquity: %7d maxDD:  %7d\n'%(x,cumStartTradeEquity,maxStartTradeDD))
        startTradeTuple += ((x,cumStartTradeEquity,maxStartTradeDD),)
    minDD = 99999999
    maxDD = 0
    for y in range(0,len(startTradeTuple)):
#        if printToTerminal == 1: print(startTradeTuple[y][0],' ',startTradeTuple[y][1],' ',startTradeTuple[y][2])
        if startTradeTuple[y][2] < minDD: minDD =startTradeTuple[y][2]
        if startTradeTuple[y][2] > maxDD: maxDD =startTradeTuple[y][2]
    numBins = 20
    binTuple = list()
    binMin = minDD
    binMax = maxDD
    binInc = (maxDD - minDD)/float(numBins)
    binBot = binMin
    for y in range(0,numBins):
        binTop = binBot + binInc
        binTuple += ((y,binBot,binTop),)
        if printToTerminal == 1: print(binTuple[y][1],' ',binTuple[y][2])
#        target3.write('Bin Number %2d : Bin Bottom %10d : Bin Top %10d\n'%(y,binTuple[y][1],binTuple[y][2]))
        binBot = binTop + y
    bins = list()
    bins[:] = []
    for x in range(0,numBins):
        bins.append(0)
    for x in range(0,len(startTradeTuple)):
        for y in range(0,numBins):
            tempDD = startTradeTuple[x][2]
            tempBot = binTuple[y][1]
            tempTop = binTuple[y][2]
            if (tempDD >= binTuple[y][1] and tempDD < binTuple[y][2]):
#                tempVal = bins(y) + 1
#                bins.insert(y,tempVal)
                bins[y] += 1
#                target3.write("Bin Number %2d : BinCount : %4d\n"%(y,bins[y]))
    freqSum = sum(bins)
    if freqSum == 0 :
        freqSum = 1
#    target3.write("Sum of Bins : %4d\n"%(freqSum))
    binProb = list()
    for y in range(0,numBins):
        if y == 0:
            binProb.append(bins[y]/freqSum)
        else:
            binProb.append(bins[y]/freqSum + binProb[y-1])
#            target3.write("Bin Count %5d freqSum %5d\n"%(bins[y],freqSum))
    target3.write('Start Trade Drawdown Analysis Of : %15s : Max. ClsTrd Draw Down %10d\n'% (systemMarketList[0].systemName,maxClsTrdDD))
    lineOutPut = '-----------------------------------------\n'
    target3.write(lineOutPut)
    for y in range(0,numBins):
        if printToTerminal == 1: print("Probability of DD < %8d is %4.3f" % (binTuple[y][2], binProb[y]))
        target3.write('Probability of DD < %8d is %4.3f\n' %(binTuple[y][2], binProb[y]))
 # Monte Carlos Analysis

    mcTradeTuple = list()
    altHistories = 100
    for x in range(0,altHistories): # number of alternate histories
        for y in range(0,len(tradeTuple)):
            randomTradeNum = random.randint(0,len(tradeTuple)-1)
            mcTradeTuple += ((x,y,tradeTuple[randomTradeNum][1],tradeTuple[randomTradeNum][0]),)
    mcTradeResultsTuple = list()
    whichAlt = -1
    for x in range(0,len(mcTradeTuple)):
        if mcTradeTuple[x][1]==0:
#            print('New Alternate History Generated')
            cumEquity = 0
            maxTradeDD = -99999999
            maxCumEquity = 0
        cumEquity += mcTradeTuple[x][2]
#        print('Randomized trade listing : ',mcTradeTuple[x][3],' ',mcTradeTuple[x][2])
        maxCumEquity = max(maxCumEquity,cumEquity)
        maxTradeDD = max(maxTradeDD,maxCumEquity - cumEquity)
        if mcTradeTuple[x][1] == len(tradeTuple)-1 :
            mcTradeResultsTuple += ((cumEquity,maxTradeDD,cumEquity/len(tradeTuple)),)
    target4.write('Monte Carlo Simulation Of : %15s \n'% (systemMarketList[0].systemName))
    lineOutPut = '--------------------------------------------------------------------------\n'
    target4.write(lineOutPut)
    mcAvgCumEquity = 0
    mcAvgMaxDD = 0
    mcAvgAvgTrd = 0
    for x in range(0,len(mcTradeResultsTuple)):
        mcCumEquity = mcTradeResultsTuple[x][0]
        mcAvgCumEquity += mcCumEquity
        mcMaxDD = mcTradeResultsTuple[x][1]
        mcAvgMaxDD += mcMaxDD
        mcAvgTrd = mcTradeResultsTuple[x][2]
        mcAvgAvgTrd += mcAvgTrd
#        if printToTerminal == 1: print('Alt history %5d Profit: %10d MaxDD: %10d Avg Trade %6d\n' % (x,mcCumEquity,mcMaxDD,mcAvgTrd))
        target4.write('Alt history %5d Profit: %10d MaxDD: %10d Avg Trade %6d\n' % (x,mcCumEquity,mcMaxDD,mcAvgTrd))
    lineOutPut = '-----------------------------------------\n'
    target4.write(lineOutPut)
    target4.write('Monte Carlo Avg   $ P/L: %8d\n' % (mcAvgCumEquity/altHistories))
    target4.write('Monte Carlo Avg $ MaxDD: %8d\n' % (mcAvgMaxDD/altHistories))
    target4.write('Monte Carlo Avg $ Trade: %8d\n' % (mcAvgAvgTrd/altHistories))

    target4.close()
    target3.close()
    target2.close()
    target1.close()

def removeDuplicates(li):
    my_set = set()
    res = []
    for e in li:
        if e not in my_set:
            res.append(e)
            my_set.add(e)
    return res

def createMonthList(li):
    myMonthList = list()
    for i in range(0,len(li)):
        if i != 0:
            tempa = int(li[i]/100)
            pMonth = int(li[i-1]/100) % 100
            month = int(li[i]/100) % 100
            if pMonth != month:
                myMonthList.append(li[i-1])
            if i == len(li)-1:
                myMonthList.append(li[i])
    return myMonthList

