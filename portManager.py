#-------------------------------------------------------------------------------
# Name:        portManager
# Purpose:
#
# Author:      georg
#
# Created:     11/09/2018
# Copyright:   (c) georg 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from marketDataClass import marketDataClass
from equityDataClass import equityClass

class portManagerClass(object):
    def __init__(self):
        self.portDate = list()
        self.marketSymbols= list()
        self.individEquity = list()
        self.combinedEquity = list()
        self.numConts = list()

class systemMarkTrackerClass(object):
    def __init__(self):
        self.marketData = marketDataClass
        self.entryPrice = list()
        self.entryQuant = list()
        self.exitQuant = list()
        self.entryName =list()
        self.mp = list()
        self.curShares = 0
        self.tradesList = list()
        self.equity = equityClass
        self.totProfit = 0
        self.barsSinceEntry = 0
        self.cumuProfit = 0
        self.equItm = 0

    def setSysMarkTrackingData(self,marketData):
        self.marketData = marketData

    def setSysMarkTrackingInfo(self,entryName,cumuProfit,mp,barsSinceEntry,curShares):
#        self.entryPrice = entryPrice
#        self.entryQuant = entryQuant
        self.entryName.append(entryName)
        self.mp.append(mp)
        self.cumuProfit = cumuProfit
        self.curShares = curShares

    def setSysMarkTrackingEquity(self,equity):
        self.equity = equity
