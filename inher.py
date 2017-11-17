class Parent:
	''' Parent Class '''
	def __init__(self, data):
		''' constructor '''
		self.data = data

	def __str__(self):
		''' Parent tostring method '''
		return 'Data: ' + str(self.data)
	
	def say_hello(self):
		''' Function to say hello :-) '''
		print 'Hello!'

class Child1(Parent):
	''' Child Class '''
	def __init__(self, data, sub_data):
		''' constructor '''
		Parent.__init__(self, data)
		self.sub_data = sub_data
	
	def __str__(self):
		''' Child tostring '''
		return 'Data: ' + str(self.data) + ' Sub Data: ' + str(self.sub_data)

def main():
	''' Main function to show example of the inheritance '''

	p = Parent('Parent Data')
	c = Child1('p dat', 'c_data')

	print(p)
	print(c)

if __name__ == '__main__':
	main()