class equityClass(object):
    def __init__(self):
        self.equityDate = list()
        self.equityItm = list()
        self.clsTrdEquity = list()
        self.openTrdEquity = list()
        self.cumuClsEquity = 0
        self.dailyEquityVal = list()
        self.peakEquity = 0
        self.minEquity = 0
        self.maxDD = 0
#        tempEqu = 0
#        cumEqu = 0
#        maxEqu = -999999999
#        minEqu = 999999999
#        maxDD = 0
    def setEquityInfo(self,equityDate,equityItm,clsTrdEquity,openTrdEquity):
        self.equityDate.append(equityDate)
        self.equityItm.append(equityItm)
        self.cumuClsEquity += clsTrdEquity
        tempEqu =self.cumuClsEquity+openTrdEquity
        self.dailyEquityVal.append(tempEqu)
        self.peakEquity = max(self.peakEquity,tempEqu)
        maxEqu = self.peakEquity
        self.minEquity = min(self.minEquity,tempEqu)
        minEqu = self.minEquity
        self.maxDD = max(self.maxDD,maxEqu-tempEqu)
#        print(self.equityDate[-1]," ",self.maxDD," ",maxEqu," ",tempEqu," ",self.cumuClsEquity)
        maxDD = self.maxDD
        maxDD = maxDD




