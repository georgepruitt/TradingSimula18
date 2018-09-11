from equityDataClass import equityClass
from math import sqrt

class systemMarketClass(object):
    def __init__(self):
        self.systemName = ""
        self.symbol = ""
        self.tradesList =list()
        self.equity = equityClass
        self.avgWin = 0
        self.avgLoss = 0
        self.avgTrade = 0
        self.profitLoss = 0
        self.numTrades = 0
        self.maxxDD = 0
        self.clsTrdDD = 0
        self.perWins = 0
        self.initCapital =0
        self.monthlyReturnTuple = list()
        self.yearlyReturnTuple = list()
        self.avgMonthlyReturn = 0
        self.avgMonthlyStdDev = 0
        self.avgYearlyReturn = 0
    def setSysMarkInfo(self,sysName,symbol,trades,equity,initCapital):
        self.systemName = sysName
        self.symbol = symbol
        self.tradesList = list(trades)
        self.equity = equity
        temp1 = 0
        temp2 = 0
        temp3 = 0
        temp4 = 0
        temp5 = 0
        temp6 = 0
        temp7 = 0
        temp8 = 0
        temp9 = 0
        temp10 = 0
        numTrades = 0
        bomEquity = 0
        boyEquity = 0
        tempMonthlyRetList = list()
        numEquityItems = len(self.equity.dailyEquityVal)
        for i in range(0,numEquityItems):
            tempEquityDate = self.equity.equityDate[i]
            if i==0: bomEquity = 0
            if i > 0:
                monthDate =self.equity.equityDate[i]
                monthYesDay = (int(self.equity.equityDate[i-1]/100) % 100)
                monthToDay =(int(self.equity.equityDate[i]/100) % 100)
                if monthYesDay != monthToDay:
                    self.monthlyReturnTuple += ((self.equity.equityDate[i-1],self.equity.dailyEquityVal[i-1] - bomEquity),)
                    bomEquity = self.equity.dailyEquityVal[i-1]
                    isDecember = False
                    whichMon = int(monthDate/100) % 100
                    if  whichMon == 1 or i == numEquityItems-1:
                        endOfYearDate = self.equity.equityDate[i-1]
                        endOfYearEquityChg = self.equity.dailyEquityVal[i-1] - boyEquity
                        self.yearlyReturnTuple += ((endOfYearDate,endOfYearEquityChg),)
                        boyEquity = self.equity.dailyEquityVal[i-1]
                if i == numEquityItems-1:
                    self.monthlyReturnTuple += ((self.equity.equityDate[i],self.equity.dailyEquityVal[i] - bomEquity),)
            temp5 = self.equity.dailyEquityVal[i]
            temp6 = max(temp6,temp5)
            temp7 = max(temp7,temp6-temp5)
            self.maxxDD = temp7

        tempMonthlyRetList = ([x[1] for x in self.monthlyReturnTuple])
        tempYearlyRetList = ([x[1] for x in self.yearlyReturnTuple])
        mean =sum(tempYearlyRetList) / len(tempYearlyRetList)
        self.avgYearlyReturn = mean
        mean = sum(tempMonthlyRetList) / len(tempMonthlyRetList)
        differences = [x - mean for x in tempMonthlyRetList]
        sq_differences = [d ** 2 for d in differences]
        ssd = sum(sq_differences)
        variance = ssd / ( len(tempMonthlyRetList) - 1)
        sd = sqrt(variance)
        self.avgMonthlyReturn = mean
        self.avgMonthlyStdDev = sd
        for i in range(0,len(self.tradesList)):
            temp8 += self.tradesList[i].tradeProfit
            temp9 = max(temp9,temp8)
            temp10= max(temp10,temp9-temp8)
            self.clsTrdDD = temp10
            if self.tradesList[i].entryOrExit == 1:
                numTrades += 1
            if self.tradesList[i].tradeProfit > 0:
                temp1 += self.tradesList[i].tradeProfit
                temp2 += 1
            if self.tradesList[i].tradeProfit < 0:
                temp3 += self.tradesList[i].tradeProfit
                temp4 += 1
        if temp2 != 0: self.avgWin = temp1/temp2
        if temp4 != 0: self.avgLoss = temp3/temp4
        if numTrades != 0: self.avgTrade = temp5/numTrades
        self.numTrades =numTrades
        self.profitLoss = temp5
        if numTrades != 0: self.perWins = temp2 / numTrades






