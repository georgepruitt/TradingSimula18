


def trade(order,actionPrice,curPos,curEntryPrice,numShares):
    profit = 0
    if order == 'buy':
        mp = 1
        if curPos == -1:
            profit = (curEntryPrice - actionPrice) * numShares
    elif order == 'sell':
        mp = -1
        if curPos == 1:
            profit = (actionPrice - curEntryPrice) * numShares
    elif order == 'liqLong':
        mp = 0
        if curPos == 1:
            profit = (actionPrice - curEntryPrice) * numShares
    elif order == 'liqShort':
        mp = 0
        if curPos == -1:
            profit = (curEntryPrice - actionPrice) *numShares           
    return profit
