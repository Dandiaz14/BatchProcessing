from process import Process
from collections import deque
import math
import os
import time
from threading import Timer

class BatchProcessing():
	myQueue = deque()
	def __init__(self,processes):
		self.myQueue = processes
		#self.startProcess()
		self.copy = deque()
		self.finishedQueue = deque()
		self.flag = 0
		self.pendientes = 0
		self.cont = 0
		self.pos = 0
		self.totalBatches = math.ceil(len(self.myQueue)/3)
		

	def startProcess(self):
		aux = 0
		for self.i in range(len(self.myQueue)):#Saca los primeros 3
			if (len(self.myQueue) >= 3):
				if aux < 3:
					value = self.myQueue[self.i]
					self.copy.append(value)
				elif aux == 3:
					break
			else:
				if aux < len(self.myQueue):
					value = self.myQueue[self.i]
					self.copy.append(value)
				else:
					break	
			aux += 1
		j = 0
		while j<aux :
			self.myQueue.popleft()
			j += 1

		while len(self.copy) > 0:
			os.system('cls')#Limpia Pantalla
			self.drawActual(self.copy,(self.totalBatches-self.pendientes))
			#*****************************************************************
			myValue = self.copy.popleft()
			tt = 0
			tr = myValue.getTime() 
			while tt < myValue.getTime():
				tt += 1
				tr -= 1
				self.cont += 1
				#os.system('cls')#Limpia Pantalla
				#self.drawActual(self.copy,cont)
				self.drawInProcess(self.copy,myValue,tt,tr,self.cont)
			self.finishedQueue.append(myValue)
			self.drawFinished(self.finishedQueue)
			self.flag += 1
			if self.flag%3==0:
				self.pendientes += 1
		
		if len(self.myQueue) > 0:
			self.startProcess()



	def drawActual(self,copy,pendientes):
		print("\tNombre\t\t\tTME\n")
		for self.data in self.copy:#Hacer que imprima los primeros 3
			print("\t",self.data.getName(),"\t\t\t",self.data.getTime(),"\n")
		print("\n\n\n")
		print("No. Lotes Pendientes: ",pendientes)
		print("*******************************************************")

	def drawInProcess(self, copy, value, tt, tr,cont):
		print("ID: ",value.getNumber(),"\n")
		print("Operación: \t\t",value.getOperation(),"\n")
		print("TME: \t\t\t",value.getTime(),"\n")
		print("TT: \t\t\t",tt,"\n")
		print("TR: \t\t\t",tr,"\n")
		print("Nombre: \t\t",value.getName(),"\n\n")
		print("Contador: ",cont,"\n\n")
		print("*******************************************************")
		time.sleep(5)

	def drawFinished(self,finishedQueue):
		aux = 0
		for self.data in self.finishedQueue:#Hacer que imprima los primeros 3
			print("\t","ID: ","\t\t\t\t",self.data.getNumber())
			print("\t","Operación: ","\t\t\t",self.data.getOperation())
			print("\t","Resultado: ","\t\t\t",eval(self.data.getOperation()))
			print("\t","Lote: ","\t\t\t",self.pos+1)
			print("\n")
			aux += 1
			if aux==3:
				self.pos += 1
				aux = 0
		print("*******************************************************")
		time.sleep(5)
		self.pos = 0

		
