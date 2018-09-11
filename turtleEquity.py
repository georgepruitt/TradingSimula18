#-------------------------------------------------------------------------------
# Name:        turtleEquity
# Purpose:
#
# Author:      George
#
# Created:     29/06/2016
# Copyright:   (c) George Pruitt 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle
import datetime

def drawLine (ttl, x1, y1, x2, y2):
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()

def labelPoint (ttl, x, y, label):
  ttl.penup()
  ttl.goto (x, y)
  ttl.pendown()
  ttl.write (label)
  ttl.penup()

def drawGridMark (ttl, x, y, isVertical,markSize):
  if isVertical :
    drawLine (ttl, x, y + markSize, x, y - markSize)
  else:
    drawLine (ttl, x - 5, y, x + 5, y)

def labelGridPoint (ttl, x, y, isVertical, text):
  if isVertical:
    labelPoint (ttl, x - 20, y - 20, text)
  else:
    labelPoint (ttl, x + 20, y, text)

def plotEquityCurve(portFolioClass):

    thePortfolio = portFolioClass
    maxEquity = 0
    minEquity = 0
    t=turtle.Turtle()


    screen = t.getscreen()
    screen.tracer(100)
    screen.title ('Combined Equity Curve')
    numDaysToPlot = len(thePortfolio.portEquityDate)

    for days in range(0,numDaysToPlot):
        portEquityVal = thePortfolio.portEquityVal[days]
        if(portEquityVal) > maxEquity : maxEquity = portEquityVal
        if(portEquityVal) < minEquity : minEquity = portEquityVal

    screen.setworldcoordinates(-20,minEquity-70,numDaysToPlot+70,maxEquity+70)
    t.goto(0,minEquity)
    t.color("#7D7EC0")
    t.fillcolor("#7D7EC0")
    t.begin_fill()
    for days in range(0,numDaysToPlot):
        portEquityVal = thePortfolio.portEquityVal[days]
        t.goto(days+10,portEquityVal+10)
    t.goto(numDaysToPlot,minEquity)
    t.goto(10,minEquity)
    t.end_fill()
    t.color("black")
# draw vertical axis
    drawLine (t,10, minEquity-50, 10, maxEquity+50)
# draw horizontal axix
    drawLine (t,10,0,numDaysToPlot+50,0)
    xGridMarkLen = int((maxEquity - minEquity)/20)
    yGridMarkLen = int(numDaysToPlot/20)
    for x in range(0,numDaysToPlot):
       if(x % 200 == 0):

           drawGridMark (t, x, 0, True,xGridMarkLen)
           labelGridPoint (t, x, 0, True, x)
    topXaxis = int(maxEquity/5000)
    botXaxis = int(minEquity/5000)

    for y in range(botXaxis,topXaxis):
        drawGridMark (t, 0, y*5000, False,yGridMarkLen)
        labelGridPoint (t, 0, y*5000, False, y*5000)

    screen.update()
    screen.exitonclick()






