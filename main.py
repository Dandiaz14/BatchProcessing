from process import Process
from batchProcessing import BatchProcessing
from collections import deque
import os

processes = deque()

def createProcess(name,operation,time,number):
	newProcess = Process(name,operation,time,number)
	processes.append(newProcess)

def goToBatchProcess():
	newBatch = BatchProcessing(processes)
	newBatch.startProcess()

def validateId(id):
	for data in processes:
		if data.getNumber() == id:
			return True 
	return False

opc = int(input("\n\n\t\tCuantos Procesos quiere cargar? : "))
aux = 0
while(aux < opc):
	os.system('cls')
	print("\n\n\t\tIngresando Lote No. #",aux+1)
	name = input("\t\tNombre: ")
	while True:
		try:
			operation = input("\t\toperation: ")
			eval(operation)
			break
		except ZeroDivisionError:
	   		print( "\t\tNo se puede dividir por cero, prueba otro número" )
	time = int(input("\t\tTiempo: "))
	while time <= 0:
		print("\t\tTiempo tiene que ser mayor a 0. . .")
		time = int(input("\t\tTiempo: "))
	number = int(input("\t\tId: "))
	while validateId(number) == True:
		print("\t\tId Repetido, ingrese otro. . .")
		number = int(input("\t\tId: "))
	createProcess(name,operation,time,number)
	aux += 1

goToBatchProcess()

input()