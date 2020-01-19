def barCountCalc(masterDateList,startDate,stopDate,rampUp):
    barCount= 0;endBarCount = 0
    while (masterDateList[barCount]) <= startDate:
        barCount +=1
 #   barCount -=1
    if barCount < rampUp:
        while barCount <= rampUp:
            barCount +=1
    endBarCount = barCount + 1
    maxNumBars = len(masterDateList)
    while masterDateList[endBarCount] <= stopDate and endBarCount < maxNumBars-1:
        endBarCount +=1
    #endBarCount -=1
    return(barCount,endBarCount)


