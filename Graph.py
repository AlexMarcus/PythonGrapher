"""
Program Name: Graph.py
Authors: Max Piciullo and Alexander Marcus
Date Last Editted: May 10, 2013

The purpose of this program is to create classes to be used in the model for the GUI.  The first class
graphs the axes and extablishes tick marks along those axes.  The second class is graphs the equations and
draws a legend. 
"""

from turtle import *
from math import *
using_IDLE = True

class axes(object):
    """creates the axes and tick marks"""
    
    def __init__(self, maxX, minX):
        """constructs the calss"""
        # sets up instance variables
        self._xMax = maxX 
        self._xMin = minX
        self._factor = 0

    def drawAxes(self, turtle):
        """draws axes"""
        # establishes the turtle screen
        t = turtle
        t.speed(0) #increases drawing speed
        #draws axes from -200 to 200
        t.up()
        t.up()
        t.goto(-300,0)
        t.down()
        t.goto(300,0)
        t.up()
        t.goto(0,-300)
        t.down()
        t.goto(0,300)

    def drawXticks(self, turtle):
        """draws the tick marks"""
        t = turtle
        t.speed(0)
        #sets turtle color to black
        t.color('black')
        
        #accounts for when max is greater than min and min is less than 0
        if self._xMax >= abs(self._xMin) and self._xMin < 0:
            factor = 300/self._xMax #represents the space between each tick mark
            t.up()
            t.goto(0,-3)
            t.down()
            t.goto(0,3)
            count = 0
            for num in range(0,self._xMax): #draws positive ticks
                t.up()
                count += factor
                t.goto(count,-3)
                t.down()
                t.goto(count,3)
                t.up()
            count = 0
            for num in range(0,abs(self._xMin)): #draws negative ticks
                t.up()
                count -= factor
                t.goto(count, -3)
                t.down()
                t.goto(count, 3)
                t.up()
            self._factor = factor #sets value to the factor created
            
        #accounts for when max is greater than min and min is greater than 0
        if self._xMax > abs(self._xMin) and self._xMin > 0:
            factor = 300/self._xMax
            t.up()
            t.goto((factor*self._xMin),-3)
            t.down()
            t.goto((factor*self._xMin),3)
            count = factor*self._xMin
            for num in range(0,self._xMax-self._xMin):
                t.up()
                count += factor
                t.goto(count,-3)
                t.down()
                t.goto(count,3)
                t.up()
            self._factor = factor

        #accounts for when absolute value of min is greater than max and max is greater than 0
        if abs(self._xMin) > abs(self._xMax) and self._xMax > 0:
            factor = 300/abs(self._xMin)
            t.up()
            t.goto(0,-3)
            t.down()
            t.goto(0,3)
            count = 0
            for num in range(0, abs(self._xMin)):
                t.up()
                count -= factor
                t.goto(count, -3)
                t.down()
                t.goto(count, 3)
                t.up()
            count = 0
            for num in range(0,self._xMax):
                count += factor
                t.goto(count,-3)
                t.down()
                t.goto(count,3)
                t.up()
            self._factor = factor

        #accounts for when absolute value of min is greater than max and max is less than 0
        if abs(self._xMin) > abs(self._xMax) and self._xMax < 0:
            factor = 300/abs(self._xMin)
            t.up()
            t.goto((factor*self._xMin),-3)
            t.down()
            t.goto((factor*self._xMin),3)
            count = factor*self._xMin
            for num in range(0, abs(self._xMin)-abs(self._xMax)):
                count += factor
                t.up()
                t.goto(count,-3)
                t.down()
                t.goto(count,3)
                t.up()
            self._factor = factor

        #accounts for when max equals 0
        if self._xMax == 0 and self._xMin != 0:
            factor = 300/abs(self._xMin)
            t.up()
            t.goto(factor*self._xMin,-3)
            t.down()
            t.goto((factor*self._xMin),3)
            count = factor*self._xMin
            for num in range(0,abs(self._xMin)):
                count += factor
                t.up()
                t.goto(count,-3)
                t.down()
                t.goto(count,3)
                t.up()
            self._factor = factor

        #accounts for when min equals 0
        if self._xMin == 0 and self._xMax !=0:
            factor = 300/abs(self._xMax)
            t.up()
            t.goto(factor*self._xMax,-3)
            t.down()
            t.goto((factor*self._xMax),3)
            count = factor*self._xMax
            for num in range(0,abs(self._xMax)):
                count -= factor
                t.up()
                t.goto(count,-3)
                t.down()
                t.goto(count,3)
                t.up()
            self._factor = factor
            
    def drawYticks(self, turtle, yfactor):
        """draws y-tick marks"""
        t = turtle
        t.speed(0)
        t.color('black')
        t.up()
        t.goto(0,0)
        count = 0
        newfactor = self._factor * (1/yfactor) #creates a new factor depending on what the user inputs as their y-factor
        while count <= 300: #positive ticks
            t.goto(-3,count)
            t.down()
            t.goto(3,count)
            t.up()
            count += newfactor
        count = 0
        while count >= -300: #negative ticks
            t.goto(-3,count)
            t.down()
            t.goto(3,count)
            t.up()
            count -= newfactor

    def getFactor(self):
        """returns the factor"""
        return self._factor




class graphEquation(object):
    """graphs the equations"""
    
    def __init__(self, equation, factor, color, xMin, xMax):
        """constructs the graphing class"""
        #sets up instance variables
        self._factor = factor
        self._equation = equation
        self._color = color
        self._xMin = xMin
        self._xMax = xMax
        
    def graphTHEequation(self, turtle, yfactor):
        """graphs one equation at a time"""
        try:
            t = turtle
            t.speed(0)
            
            #setsup the first coordinate
            xFirst= self._factor * int(self._xMin)
            x = self._xMin
            y = (1/yfactor) * self._factor * eval(self._equation)
            t.color(self._color)
            t.up()
            t.goto(xFirst,y)

            #eval used to evaluate a string as a line of code
            #graphs from the min to the max
            for x in range((self._xMin),(self._xMax+1)):
                t.down()
                xNext = x*self._factor #creates each x value
                y = (1/yfactor) * self._factor * eval(self._equation) #creates each y value
                t.color(self._color)
                t.goto(xNext,y)
            return 1
        #accounts for all types of errors
        #if the GUI receives a 2, an error message pops up
        except SyntaxError:
            return 2
        except TypeError:
            return 2
        except NameError:
            return 2
        except ValueError:
            return 2

    def drawLegend(self, turtle, count, color):
        """draws the legend"""
        t = turtle
        t.color(color)
        t.speed(0)
        string = 'y'+str(count)+' = '
        t.up()
        yValue =(100 - 21*count) #each equation gets its own box
        #boxes stacked
        t.goto(210, yValue + 10)
        t.down()
        t.goto(210, yValue - 10)
        t.goto(290, yValue - 10)
        t.goto(290, yValue + 10)
        t.goto(210, yValue + 10)
        t.up()
        t.goto(215, yValue - 5)
        #writes the colors of the equations in the color
        t.write(string, True, font = ('Arial', 8, "normal"))
        t.write(color, True, font = ('Arial', 8, 'normal'))
        
        










        
