class positionMatrixClass(object):
    def __init__(self):
        self.posMatrixDate = list()
        self.numMarkets = 0
        self.marketNames = list()
        self.posMatrixSize = list()
    def setPositionMatrix(date,posArray):
        self.posMatrixDate.append(date)
        self.posMatrixSize.append(posArray)


    def printPositionMatrix(self,systemMarketList,portManager):
        printToTerminal = 0
        fileName1 = systemMarketList[0].systemName + "-PosMatrix.txt"
        target1 = open(fileName1,"w")
        cnt = 0
        lineOutPut = "Date,"
        for numMarkets in range(0,len(systemMarketList)):
        	lineOutPut += systemMarketList[numMarkets].symbol + ","
        target1.write(lineOutPut)
        target1.write("\n")
        for numDays in range(0,len(self.posMatrixDate)):
            lineOutPut = ""
            lineOutPut = str(self.posMatrixDate[numDays]) + ","
            for numMarkets in range(0,len(systemMarketList)):
                mySize = str(self.posMatrixSize[cnt])
                lineOutPut += str(self.posMatrixSize[cnt]) + ","
                cnt +=1
            lineOutPut += str(round(portManager.combinedEquity[numDays],0))
#            print(lineOutPut)
            target1.write(lineOutPut)
            target1.write("\n")

def getPortPositions(dayPosList):
    mktWPos = 0
    for mkt in range(0,len(dayPosList)):
        if dayPosList[mkt] > 0:
            mktWPos+=1
    return(mktWPos)



