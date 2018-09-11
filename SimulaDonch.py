#System Tester.py - programmed by George Pruitt
#Feel free to distribute and improve upon
#Version 2.0
#/////////////////////////////////////////////////////////////////////////////////
#--------------------------------------------------------------------------------
#Import Section - inlcude functions, classes, variables
#from external modules
#--------------------------------------------------------------------------------
from getData import getData
from equityDataClass import equityClass
from tradeClass import tradeInfo
from systemMarket import systemMarketClass
from indicators import highest,lowest,rsiClass,stochClass,sAverage,bollingerBands
from portfolio import portfolioClass
from systemAnalytics import calcSystemResults
from utilityFunctions import getDataAtribs,getDataLists,roundToNearestTick,calcTodaysOTE
from utilityFunctions import setDataLists,removeDuplicates
from portManager import portManagerClass,systemMarkTrackerClass

def exitPos(myExitPrice,myExitDate,tempName,myCurShares):
    global tradeName,entryPrice,entryQuant,exitPrice,numShares,myBPV,cumuProfit
    if mp < 0:
        trades = tradeInfo('liqShort',myExitDate,tempName,myExitPrice,myCurShares,0)
        profit = trades.calcTradeProfit('liqShort',mp,entryPrice,myExitPrice,entryQuant,myCurShares) * myBPV
        profit = profit - myCurShares *commission
        trades.tradeProfit = profit
        cumuProfit += profit
        trades.cumuProfit = cumuProfit
    if mp > 0:
        trades = tradeInfo('liqLong',myExitDate,tempName,myExitPrice,myCurShares,0)
        profit = trades.calcTradeProfit('liqLong',mp,entryPrice,myExitPrice,entryQuant,myCurShares) * myBPV
        profit = profit - myCurShares * commission
        trades.tradeProfit = profit
        cumuProfit += profit
        trades.cumuProfit = cumuProfit
    curShares = 0
    for remShares in range(0,len(entryQuant)):
       curShares += entryQuant[remShares]
    return (profit,trades,curShares)

def bookTrade(entryOrExit,lOrS,price,date,tradeName,shares):
    global mp,commission,totProfit,curShares,barsSinceEntry,listOfTrades
    global entryPrice,entryQuant,exitPrice,numShares,myBPV,cumuProfit
    if entryOrExit == -1:
        profit,trades,curShares = exitPos(price,date,tradeName,shares)
        mp = 0
    else:
        profit = 0
        curShares = curShares + shares
        barsSinceEntry = 1
        entryPrice.append(price)
        entryQuant.append(shares)
        if lOrS == 1:
            mp += 1
            trades = tradeInfo('buy',date,tradeName,entryPrice[-1],shares,1)
        if lOrS ==-1:
            mp -= 1
            trades = tradeInfo('sell',date,tradeName,entryPrice[-1],shares,1)

    return(profit,curShares,trades)

dataClassList = list()


def main():
    pass

if __name__ == '__main__':

    marketMonitorList = list()
    masterDateList = list()
    masterDateGlob = list()
    marketPosition = list()
    entryPrice= list()
    entryQuant= list()
    exitQuant= list()
    trueRanges= list()
    marketDataInc= list()
    myBPVList = list()
    myComNameList = list()
    myMinMoveList= list()
    portManager = portManagerClass()
    marketList = getData()
    marketDataInc.append(0)
    curShares = 0
    commission = 50
    systemMarketList = list()
    portfolio = portfolioClass()
    numMarkets = len(marketList)
    for i in range(0,numMarkets):
        systemMarkTracker = systemMarkTrackerClass()
        equity = equityClass()
        systemMarkTracker.setSysMarkTrackingData(marketList[i])
        systemMarkTracker.setSysMarkTrackingEquity(equity)
        marketMonitorList.append(systemMarkTracker)
        marketDataInc.append(0)
        myBPV,myComName,myMinMove= getDataAtribs(marketMonitorList[i].marketData)
        myBPVList.append(myBPV)
        myComNameList.append(myComName)
        myMinMoveList.append(myMinMove)
        sysName = 'CrossTrader1' #System Name here

    masterDateGlob = list()
    for i in range(0,numMarkets):
        numDaysInData = len(marketMonitorList[i].marketData.date)
        masterDateGlob += marketMonitorList[i].marketData.date
    masterDateList = removeDuplicates(masterDateGlob)
    masterDateList = sorted(masterDateList)
    x= 1
    jCnt = 0
    k=5
    barsSinceEntry = 0
    portEquItm = 0
    for i in range(len(masterDateList)-700,len(masterDateList)):
        portManager.portDate.append(masterDateList[i])
        kCnt = 0
        dailyPortCombEqu = 0
        for j in range(0,numMarkets):
            myDate,myOpen,myHigh,myLow,myClose,myVolume,myOpInt = setDataLists(marketMonitorList[j].marketData)
            if j == 0 : dailyPortCombEqu = 0
            equItm = marketMonitorList[j].equItm
            equItm += 1
            myBPV = myBPVList[j]
            myComName = myComNameList[j]
            myMinMove = myMinMoveList[j]
            if myComName not in portManager.marketSymbols:
                portManager.marketSymbols.append(myComName)
                portManager.numConts.append(1)
##                portManager.individEquity.append(0)
            curShares = 0
            todaysCTE = todaysOTE = 0
            mktsToday = 0

            if masterDateList[i] in marketMonitorList[j].marketData.date:
                k = marketMonitorList[j].marketData.date.index(masterDateList[i])
                mp = 0
                if len(marketMonitorList[j].mp) !=0:
                    mp = marketMonitorList[j].mp[-1]
                entryPrice = marketMonitorList[j].entryPrice
                entryQuant= marketMonitorList[j].entryQuant
                curShares = marketMonitorList[j].curShares
                cumuProfit = marketMonitorList[j].cumuProfit

                barsSinceEntry = marketMonitorList[j].barsSinceEntry
                cumuProfit = marketMonitorList[j].cumuProfit
                if k > 5:
                    if myHigh[k] >= highest(myHigh,40,k,1) and mp !=1:
                        price = max(myOpen[k],highest(myHigh,40,k,1))
                        if mp <= -1:
                            profit,curShares,trades = bookTrade(-1,0,price,myDate[k],"RevshrtLiq",curShares)
                            marketMonitorList[j].tradesList.append(trades)
                            todaysCTE = profit
                        tradeName = "Test B"
                        numShares = 4
                        profit,curShares,trades = bookTrade(1,1,price,myDate[k],tradeName,numShares)
                        barsSinceEntry = 1
                        marketMonitorList[j].setSysMarkTrackingInfo(tradeName,cumuProfit,mp,barsSinceEntry,curShares)

                        marketMonitorList[j].tradesList.append(trades)
                    if myLow[k] <= lowest(myLow,40,k,1) and barsSinceEntry > 1 and mp !=-1:
                        price = min(myOpen[k],lowest(myLow,40,k,1))
                        if mp >= 1:
                            profit,curShares,trades = bookTrade(-1,0,price,myDate[k],"RevLongLiq",curShares)
                            marketMonitorList[j].tradesList.append(trades)
                            todaysCTE = profit


                        tradeName = "Test S"
                        numShares = 4
                        profit,curShares,trades = bookTrade(1,-1,price,myDate[k],tradeName,numShares)
                        barsSinceEntry = 1
                        marketMonitorList[j].setSysMarkTrackingInfo(tradeName,cumuProfit,mp,barsSinceEntry,curShares)
                        marketMonitorList[j].tradesList.append(trades)
                    if mp != 0 :
                        barsSinceEntry += 1
                        todaysOTE = calcTodaysOTE(mp,marketList[j].close[k],marketMonitorList[j].entryPrice,marketMonitorList[j].entryQuant,myBPV)

                    marketMonitorList[j].barsSinceEntry = barsSinceEntry
                    marketMonitorList[j].curShares = curShares
                    marketMonitorList[j].equItm = equItm
                    marketMonitorList[j].equity.setEquityInfo(marketList[j].date[k],equItm,todaysCTE,todaysOTE)
                    portManager.individEquity.append((j,marketMonitorList[j].equity.dailyEquityVal[-1]))
                    dailyPortCombEqu += portManager.individEquity[portEquItm][1]
                    portEquItm += 1
##                    if len(marketMonitorList[j].mp)!= 0 :
##                        print(masterDateList[i]," Market # ",j," entryPrice ",marketMonitorList[j].entryPrice[-1]," mp ",marketMonitorList[j].mp[-1]," name ",marketMonitorList[j].entryName[-1]," equ ",portManager.individEquity[-1]," combined equ ",dailyPortCombEqu)
                    if i == len(masterDateList)-1:
                        if mp >= 1:
                            price = marketList[j].close[k]
                            exitDate = marketList[j].date[k]
                            profit,trades,curShares = exitPos(price,marketList[j].date[k],"L-EOD",curShares)
                            marketMonitorList[j].tradesList.append(trades)
                        if mp <= -1:
                            price = marketList[j].close[k]
                            exitDate = marketList[j].date[k]
                            profit,trades,curShares = exitPos(price,marketList[j].date[k],"S-EOD",curShares)
                            marketMonitorList[j].tradesList.append(trades)

            else:
                print("Missing Date", masterDateList[i] )
                portManager.individEquity.append((j,marketMonitorList[j].equity.dailyEquityVal[-1]))
                dailyPortCombEqu += portManager.individEquity[portEquItm][1]
                portEquItm += 1
#        if len(marketMonitorList[0].mp) > 0 and len(marketMonitorList[1].mp) > 0 : print(i," ",marketMonitorList[0].mp[-1]," ",marketMonitorList[1].mp[-1])
#        if len(marketMonitorList[0].tradesList) > 0 : print(marketMonitorList[0].tradesList[-1].tradeName," ",marketMonitorList[0].tradesList[-1].tradeDate," ",marketMonitorList[0].tradesList[-1].tradePrice)
    for j in range(0,numMarkets):
        systemMarket = systemMarketClass()
        systemMarket.setSysMarkInfo(sysName,myComNameList[j],marketMonitorList[j].tradesList,marketMonitorList[j].equity,100000)
        systemMarketList.append(systemMarket)

    portfolio.setPortfolioInfo("PortfolioTest",systemMarketList)
    calcSystemResults(systemMarketList)

##    for j in range(0,numMarkets):
##        myCumuProfit = 0
##        nummarketMonitorListTrades = len(marketMonitorList[j].tradesList)
##        systemMarketList[j].tradesList = marketMonitorList[j].tradesList
##        for i in range(0,len(marketMonitorList[j].tradesList)):
##            myCumuProfit += marketMonitorList[j].tradesList[i].tradeProfit
####            print(i," ",nummarketMonitorListTrades," ",marketMonitorList[j].tradesList[i].tradeDate,",",marketMonitorList[j].tradesList[i].tradeName,",",marketMonitorList[j].tradesList[i].tradePrice,",",marketMonitorList[j].tradesList[i].tradeProfit," ",myCumuProfit)
####            print(marketMonitorList[j].tradesList[i].tradeName)
####            print(marketMonitorList[j].tradesList[i].tradePrice)
####            print(marketMonitorList[j].tradesList[i].tradeProfit)
##        for i in range(0,len(marketMonitorList[j].equity.equityItm)):
##            print(i," ",marketMonitorList[j].equity.equityItm[i]," ",marketMonitorList[j].equity.equityDate[i]," ",marketMonitorList[j].equity.dailyEquityVal[i])
##
##    for j in range(0,len(portManager.combinedEquity)):
##        print(portManager.portDate[j],' ',portManager.combinedEquity[j])
