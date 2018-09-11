
class marketDataClass(object):
    def __init__(self):
        self.symbol = ""
        self.minMove = 0
        self.bigPtVal = 0
        self.seed = 0
        self.date = list()
        self.open = list()
        self.high = list()
        self.low = list()
        self.close = list()
        self.volume = list()
        self.opInt = list()
        self.dataPoints = 0
    def setDataAttributes(self,symbol,bigPtVal,minMove):
        self.symbol = symbol
        self.minMove = minMove
        self.bigPtVal = bigPtVal
    def readData(self,date,open,high,low,close,volume,opInt):
        self.date.append(date)
        self.open.append(open)
        self.high.append(high)
        self.low.append(low)
        self.close.append(close)
        self.volume.append(volume)
        self.opInt.append(opInt)
        self.dataPoints += 1
        
                         
