# Python Engineer #

## Simple Stack with No Type restriction ##

class MyStack:
	data = None

	def __init__(self):
		self.data = []

	def push(self,x):
		self.data.append(x)

	def pop(self):
		self.data.pop()

	def isEmpty(self):
		return len(self.data) == 0

	def getLast(self):
		return self.data[-1]

	def getFirst(self):
		return self.data[0]




	def __str__(self):
		return 'Stack total Items {}'.format(len(self.data))

	def getStackData(self):
		return self.data



####  ==================== Stack Version 2 ===========================  #######

## Stack with Data Type Restriction #### 

# class MyStackV:
# 	data = None
# 	ObjType = None

# 	def __init__(self):
# 		self.data = []

# 	def push(self,x):
# 		if self.isEmpty():
# 			self.ObjType = type(x)
# 			self.data.append(x)
# 		else:
# 			if self.ObjType == type(x):
# 				self.data.append(x)
# 			else:
# 				raise "Only add one type of data into stack"

# 	def pop(self):
# 		self.data.pop()

# 	def isEmpty(self):
# 		return len(self.data) == 0

# 	def getLast(self):
# 		return self.data[-1]

# 	def getFirst(self):
# 		return self.data[0]


# 	def __str__(self):
# 		return 'Stack total Items {}'.format(len(self.data))

# 	def getStackData(self):
# 		return self.data



#####=============  with inheritnce  implement of abow Stack Version 2 ======== ######

class MyStackI(MyStack):

	def push(self,x):
		if self.isEmpty():
			self.ObjType = type(x)
			self.data.append(x)
		else:
			if self.ObjType == type(x):
				self.data.append(x)
			else:
				raise "Only add one type of data into stack"





a = MyStackI()

# a.push(1000)
# a.push(94394239)
# a.push(100)
# a.pop()
# print(a.getLast())

print(a.getStackData())






















