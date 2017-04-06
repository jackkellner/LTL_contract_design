import subprocess
from pprint import pprint

class Check(object):
	def __init__(self, data=''):
		"""Initialize a check object"""
		self.data = data
		

class Checks(object):
	def __init__(self):
		self.checks = []

	def add_check(check):
		self.checks.append(check)

	def compile(self):
		# function to compile a .smv file from the list of checks 
		return 'tests/waiter_customer_example.smv'

	def run(self):
		# Return the name of the .smv file to run in terminal
		file = self.compile()

		# Initialize an array to hold the results of the checks
		self.results = []

		# create the command and run in terminal
		self.output = subprocess.check_output(['NuSMV', file]).splitlines()
		# retain only the lines that return whether or not a specification is true/false
		self.output = [x for x in self.output if x[:16] == '-- specification']

		# Iterate throught the results and parse whether or not a statement is valid
		for i in range(len(self.output)):
			if 'is false' in self.output[i]:
				self.results.append(True)
			elif 'is true' in output[i]:
				self.results.append(False)

		# print output to console
		pprint(self.output)
		pprint(self.results)
