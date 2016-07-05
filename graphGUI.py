"""
Program: graphGUI.py
Authors : Alex Marcus and Max Piciullo
Date Last Edited: May 10, 2013


The purpose of the program is to graph equations, and return x/y values for each equation.  The
inputs are equations, maximum and minimum x values, and a y factor.  The output is a graph
drawn in turtle.  The user may also click the 'X/Y Values' button to get individual values for
each equation

"""
# The program imports all needed modules
from tkinter import *
from turtle import *
from math import *
from Graph import *
using_IDLE = True

class grapher(Frame):
    """Creates the grapher"""

    def __init__(self):
        """constructs the graphing GUI"""

        #Sets up instance variables for the 10 equations and sets up widgets
        self.rowcount = 2
        self.count = 2
        Frame.__init__(self)
        self.master.title('Grapher')
        self.grid()
        
        self.funct1Var = StringVar()
        funct1Entry = Entry(self, textvariable = self.funct1Var)
        funct1Entry.grid(row = 1, column = 1)
        YLabel = Label(self, text = "y1=" )
        YLabel.grid(row = 1, column = 0)
        
        self.funct2Var = StringVar()
        self.funct2Entry = Entry(self, textvariable = self.funct2Var)
    
        self.funct3Var = StringVar()
        self.funct3Entry = Entry(self, textvariable = self.funct3Var)

        self.funct4Var = StringVar()
        self.funct4Entry = Entry(self, textvariable = self.funct4Var)
        
        self.funct5Var = StringVar()
        self.funct5Entry = Entry(self, textvariable = self.funct5Var)

        self.funct6Var = StringVar()
        self.funct6Entry = Entry(self, textvariable = self.funct6Var)

        self.funct7Var = StringVar()
        self.funct7Entry = Entry(self, textvariable = self.funct7Var)

        self.funct8Var = StringVar()
        self.funct8Entry = Entry(self, textvariable = self.funct8Var)

        self.funct9Var = StringVar()
        self.funct9Entry = Entry(self, textvariable = self.funct9Var)

        self.funct10Var = StringVar()
        self.funct10Entry = Entry(self, textvariable = self.funct10Var)
        
        graphButton = Button(self, text = 'Graph', command = self.graph)
        graphButton.grid(row=1,column=3)

        newButton = Button(self, text = 'New Equation', command = self.newequation)
        newButton.grid(row = 1, column = 4)
        
        maxxlabel=Label(self, text = 'Maximum X Value')
        maxxlabel.grid(row = 2, column = 3)
        
        self.maxxVar = DoubleVar()
        maxxEntry = Entry(self, textvariable = self.maxxVar)
        maxxEntry.grid(row = 2, column = 4)
        
        minxlabel=Label(self, text = 'Minimum X Value')
        minxlabel.grid(row = 3, column = 3)
        
        self.minxVar = DoubleVar()
        minxEntry = Entry(self, textvariable = self.minxVar)
        minxEntry.grid(row = 3, column = 4)

        yfactorlabel=Label(self, text = 'Y Factor')
        yfactorlabel.grid(row = 4, column = 3)
        
        self.yfactorVar = DoubleVar()
        yfactorEntry = Entry(self, textvariable = self.yfactorVar)
        yfactorEntry.grid(row = 4, column = 4)
        self.yfactorVar.set(1)
        
        y1valuesButton = Button(self, text = "X/Y Values", command = self.displayValues)
        y1valuesButton.grid(row = 1, column = 2)

        clearButton = Button(self, text = 'Clear', command = self.clearAll)
        clearButton.grid(row = 1, column = 5)

        
        
        
    def newequation(self):
        """callback for the New Equation button to create new entries for fucntions"""

        # Each time the New Equation Button is pushed, the program will make strings to set up new
        # widgets
        columncount = 1
        if self.count >10:
            messagebox.showerror(title="Error", message = "Only 10 functions can be graphed at once.")
        else:
            grid = 'self.funct'+str(self.count)+'Entry.grid(row = '+str(self.rowcount)+',column ='+str(columncount)+")"
            label = 'YLabel'+str(self.count)+"= Label(self, text ="+"'y"+str(self.count)+"='"+")"

        # The function exec() is used to execute the strings as python code
            exec(label)
            ygrid = 'YLabel'+str(self.count)+'.grid(row = '+str(self.rowcount)+', column = '+str(columncount-1)+")"
            exec(ygrid)
            exec(grid)
            self.count += 1
            self.rowcount += 1

    def graph(self):
        """graphs each equation"""
        try:

            # A list of colors is made and counters are initiated
            colors = ['black','blue','red','green','orange','purple','yellow','pink','brown','grey']
            index = 0
            count = 1
            color = 'black'
            equation = ""
            xMin = int(self.minxVar.get())
            xMax = int(self.maxxVar.get())

            # Validation for X Minimum and X Maximum
            if xMax == xMin or xMax < xMin:
                messagebox.showerror(title = "Domain Error", message = 'The Maximum and Minimum values must not be the same and the Maximum must be greater than the Minimum')
            else:

                # A Turtle window is established and the axes class is called to draw axes, tickmarks
                # and to change the color of the pen for each equation
                t = Turtle()
                yfactor = self.yfactorVar.get()
                ax = axes(xMax, xMin)
                ax.drawAxes(t)
                ax.drawXticks(t)
                ax.drawYticks(t, yfactor)
                factor = ax.getFactor()
                for num in range(self.count-1):
                    string = 'self.funct'+str(count)+'Var.get()'
                    equation = eval(string)
                    if equation != "":
                        color = colors[index]
                        g = graphEquation(equation, factor, color, xMin, xMax)

                        #Validation for the equation if the entry is improper syntax. e.g. (2x isntead of 2*x)
                        ValidEquation = g.graphTHEequation(t, yfactor)
                        
                        if ValidEquation == 2:
                            messagebox.showerror(title = "Equation Error", message = "The equation must be a single variable equation where the variable is x with correct Python syntax.") 
                        else:
                            g.drawLegend(t, count, color)
                    else:

                        # If the equation is blank in the entry field, the turtle returns home
                        t.up()
                        t.home()
                    count += 1
                    index += 1

                # After the turtle is done drawing, it will hide itself and the erase command appears
                # in the Shell
                t.hideturtle()

                input('Hit enter to delete the turtle screen')
                t.screen.bye()
                del t
                
        #If the X/Y Value is inputted as a letter an error will appear
        except ValueError:
            messagebox.showerror(title = 'Value Error', message = 'All values must be floats from 1 to 10')

    def clearAll(self):
        """clears all values and turtle screen"""
        count = 1
        for i in range(self.count -1):
            string = 'self.funct'+str(count)+'Var.set("")'
            exec(string)
            count += 1


    def displayValues(self):
        """" callback for main window's button """

        # A second window is created for when the 'X/Y Values button is pressed
        second = self.createSecondWindow()
        self.wait_window(self.window2)

    def createSecondWindow(self):
        """ create the second window """

        # The second window is created with all of its widgets
        self.window2 = Toplevel()
        self.window2.title('X/Y Values')
        
        xValueLabel = Label(self.window2, text = 'X Value')
        xValueLabel.grid(row = 1, column = 0)
        
        yValueLabel = Label(self.window2, text = "Y Value")
        yValueLabel.grid(row = 2, column = 0)
        
        equationLabel = Label(self.window2, text = "Equation Number")
        equationLabel.grid(row = 0, column = 0)
        
        self.window2.equationVar = IntVar()
        equationVarEntry = Entry(self.window2, textvariable = self.window2.equationVar)
        equationVarEntry.grid(row = 0, column = 1)
        
        self.window2.xValueVar = DoubleVar()
        xValueEntry = Entry(self.window2, textvariable = self.window2.xValueVar)
        xValueEntry.grid(row = 1, column = 1)
        
        self.window2.yValueVar = DoubleVar()
        yValueEntry = Entry(self.window2, textvariable = self.window2.yValueVar)
        yValueEntry.grid(row = 2, column = 1)
        
        button = Button(self.window2, text = 'Display Y Value', command = self.showValue)
        button.grid(row = 3, column = 0, columnspan = 2)
        self.window2.grab_set()

    def showValue(self):
        """ callback for second window's button """

        # The program will attempt to evaluate the equation for the given X value
        try:
            xValue = self.window2.xValueVar.get()
            equation = self.window2.equationVar.get()
            if equation >10 or equation < 1:
                messagebox.showerror(parent = self.window2, title = 'Equation Error',
                                                 message = 'The equation number must be an integer from 1 to 10')
            else:
                string = 'self.funct'+str(equation)+'Var.get()'
                newEquation = eval(string)
                if newEquation == "":
                    messagebox.showerror(parent = self.window2, title = 'Equation Error',
                                                 message = 'The equation does not exist')
                else:
                    x = xValue
                    y = eval(newEquation)
                    self.window2.yValueVar.set(y)

        # All errors in the X/Y value window are accounted for and error messages will pop up
        except ValueError:
            messagebox.showerror(parent = self.window2, title = 'Equation Error',
                                                 message = 'The equation number must be an integer from 1 to 10 and all X-Values must be floats')
        except NameError:
            messagebox.showerror(parent = self.window2, title = 'Equation Error',
                                                 message = 'The equation is invalid')
        except SyntaxError:
            messagebox.showerror(parent = self.window2, title = 'Equation Error',
                                                 message = 'The equation is invalid')
        except TypeError:
            messagebox.showerror(parent = self.window2, title = 'Equation Error',
                                                 message = 'The equation is invalid')
 
def main():
    """instantiate and pop up the window"""
    grapher().mainloop()
    
main()
