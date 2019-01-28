class Process():
	def __init__(self, myName, myOpn, myTime, myNumber):
		self.setName(myName)
		self.setOperation(myOpn)
		self.setTime(myTime)
		self.setNumber(myNumber)
		print("Nuevo Proceso Creado!")

	#Getters
	def getName(self):
		return self.name
	def getOperation(self):
		return self.operation
	def getTime(self):
		return self.time
	def getNumber(self):
		return self.number

	#Setters
	def setName(self,myName):
		self.name = myName
	def setOperation(self,myOpn):
		self.operation = myOpn
	def setTime(self,myTime):
		self.time = myTime
	def setNumber(self,myNumber):
		self.number = myNumber
