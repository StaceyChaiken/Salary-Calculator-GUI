"""
Program: salaryGUI_SC2@.py
Author: Stacey Chaiken 7/19/2023

GUI- Version using a "Salary Calculator" created in past projects. This program will allow the user to input an employee's hourly pay and also the amount of hours worked. Buttons will be used to calculate and display that employee's earnings.

NOTE: the file breezypythongui.py MUST be in the same directory file for the app to run correctly!
"""

from breezypythongui import EasyFrame
from tkinter.font import Font

# Other imports go here

# Class header (application name will change project to project )
class SalaryCalculator(EasyFrame):
	# Definition of our class constructor method
	def __init__(self):

		#Call to the Easy Frame constructor method 
		EasyFrame.__init__(self, title = "Salary Calculator!", width = 300, height = 180, resizable = False, background = "lightgrey")
		self.normalFont = Font(family = "Tahoma", size = 16)

		# Add the vaious components to the window
		self.addLabel(text = "Salary Calculator", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "grey", foreground = "white", font = Font(family = "Arial", size = 26))
		self.addLabel(text = "Hourly Wage:", row = 2, column = 0, sticky = "NE", background = "lightgrey", font = self.normalFont)
		self.hourlyWage = self.addIntegerField(value = 0, row = 2, column = 1, sticky = "NW", width = 4)
		self.addLabel(text = "No. of Hours Worked:", row = 3, column = 0, sticky = "NE", background = "lightgrey", font = self.normalFont)
		self.hoursWorked = self.addIntegerField(value = 0, row = 3, column = 1, sticky = "NW", width = 4)

		self.button = self.addButton(text="Calculate", row=4, column=0, columnspan=2, command=self.calculate)
		

		self.addLabel(text = "The employee's salary is: ", row = 5, column = 0, sticky = "NE", background = "grey", foreground = "white", font = self.normalFont)
		self.total = self.addFloatField(value = 0.0, row = 5, column = 1, sticky = "NW", precision = 2, width = 10)

	# Definition of the calculate() function
	def calculate(self):

		# grab the user input from the GUI window
		hourly_wage = self.hourlyWage.getNumber()
		hours_worked = self.hoursWorked.getNumber()

		# processing phase
		result= (hourly_wage) * (hours_worked)


		# output phase 
		self.total.setNumber(result)

# Global definition of the main() method 
def main():
	#instantiate an object from the class into mainloop()
	SalaryCalculator().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()