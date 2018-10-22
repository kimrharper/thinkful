
'''
Chris McPherson
Homework set #2
545
'''

#!/usr/bin/python
import sys
import random
import copy
import numpy
import math
from pathlib import Path

#allows for arguments to be entered from the command line
if (len(sys.argv) > 1):
	learningRate = float(sys.argv[1])
	momentum = float(sys.argv[2])
	HLsize = int(sys.argv[3])
	trainDataSZ = float(sys.argv[4])
	testNum = int(sys.argv[5])
	#print ("learningRate: "+ str(learningRate) + ", momentum: " + str(momentum) + ", HLsize: " + str(HLsize)) 

else:
	trainData = []
	testData = []
	learningRate = 0.1
	momentum = 0.9
	HLsize = 20
	trainDataSZ = 1
	testNum = 1
	
trainFile = "/Users/chrism/Python/ML/mnist_train.csv" 
testFile = "/Users/chrism/Python/ML/mnist_test.csv"
OLFile = "/Users/chrism/Python/ML/Outlayer" + str(HLsize) + str(testNum) + ".csv"
ILFile = "/Users/chrism/Python/ML/inlayer" + str(HLsize) + str(testNum) + ".csv"
resFile1 = "/Users/chrism/Python/ML/results" + str(HLsize) + str(testNum) + ".csv"
resFile2 = "/Users/chrism/Python/ML/results" + str(HLsize) + str(testNum) + ".csv"
resFile3 = "/Users/chrism/Python/ML/results" + str(HLsize) + str(testNum) + ".csv"
trainData = []
testData = []

class Layer:
	def __init__(self, in_ , out_, weights_ = None):
		self.outData = []
		self.weights = []
		self.feedback = 0
		self.inData = []
		self.inDimension = in_
		self.outDimension = out_ 
		self.momentumM = []

		#initializing the arrays for the data objects
		for n in range (0, self.outDimension ):
			self.weights.append([]) 
			for m in range (0, self.inDimension):
				self.weights[n].append([])
		for r in range(0, self.outDimension ):
			self.outData.append(0.0)
		for q in range(0, self.inDimension):
			self.inData.append(0.0)
		
		for s in range(0, self.inDimension):
			self.momentumM.append((0.0))
		
		if (weights_ != None):
			self.weights = copy.deepcopy(weights_,float)


	#initialization for the first run
	def newW(self):
		for m in range (0, self.outDimension ): 
			for i in range (0,self.inDimension):
				self.weights[m][i] = (float(random.random() - 0.5)* 0.1)
		
	#a function to save the generated weights
	def save(self, file_):
		file = open(file_, 'w')
		outStr = str(self.inDimension) + "," + str(self.outDimension) + "\n"
		for i in range (0,self.outDimension):
			for j in range (0,self.inDimension):
				outStr = outStr  + str(self.weights[i][j]) + ","
				#print(str(self.weights[i][j]))
			outStr = outStr[:-1]
			outStr = outStr + "\n"
		file.write(str(outStr))
		
	#load the weights from a specific file
	def load(self, file_):
		file = open(file_, "r")
		header = file.readline()
		dimensions = header.split(",")
		self.inDimension = int(dimensions[0])
		self.outDimension = int(dimensions[1])
		i = 0
		for line in file:
			weights = line.split(",")
			for j in range (0,self.inDimension):
				#print (self.weights[i][j])
				self.weights[i][j] = float(weights[j])
			#print( str((self.weights[i][self.inDimension-2])))
			i = i +1

	def forwardProp(self, data):
		#initializing so 
		for i in range(0, self.inDimension): 
			self.inData[i] = float(data[i])
		tempDat = numpy.asarray(self.inData,float)
		
		for o in range (0, self.outDimension ):
			tempW = numpy.asarray(self.weights[o], float)
			tempDot = numpy.dot(tempDat,tempW)
			sigma = 1 /(1 + math.exp(-tempDot))
			self.outData[o] = sigma
			#print(str (self.outData[o]))
		return self.outData

	def backPropToH(self, adjustment ):
		#for each output calculate loss function for bias and use that to find new weights
		errork = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
		errorj = []
		delta = []
		for index in range (0,self.inDimension -1 ):
			errorj.append(0.0)
		#calculate delta k for values of the input layer
		#	for each k output o*(1-o)(t-o)
		for i in range (0, self.outDimension ):
			errork[i] = self.outData[i] * (1 - self.outData[i])*(float(adjustment[i] - self.outData[i]))

		#calculate delta j values for the hidden layer
		weightsByNode = numpy.transpose(self.weights)
		for k in range (1, self.inDimension):
			multTerm = numpy.dot(weightsByNode[k], (errork))
			errorj[k-1] = self.inData[k] * (1 - float(self.inData[k])) * multTerm
		#calculate delta w for each node of hidden layer
		ek= numpy.asarray(errork, float)
		ek = learningRate * ek
		for r in range (0,self.inDimension):
			delta = weightsByNode[r]* ek
			weightsByNode[r] = weightsByNode[r] + delta
		self.weights = numpy.transpose(weightsByNode)
		#self.momentumM = delta
		#pass delta j
		return errorj
		
	def backPropToI(self, errorj ):
		weightsByNode = numpy.transpose(self.weights)
		deltaW = []
		ej  = numpy.asarray(errorj, float)
		ej = ej *learningRate
		for index in range (0,self.outDimension  ):
			deltaW.append(0.0)
		for k in range (0,self.inDimension):
			deltaW = ej * numpy.asarray(weightsByNode[k], float)
			weightsByNode[k]= weightsByNode[k] + deltaW
			

			print (str(weightsByNode[19])+ " "  + "\n" + str(deltaW) )
			
			#print(str(self.weights[k][l]) )
			#self.momentumM = deltaW
		self.weights = numpy.transpose(weightsByNode)
		#print (str(self.weights[0]))
		#print(str(self.weights))
		# float(self.momentumM[l])
		
		
	def printW(self):
		printstr =""
		for i in self.weights:
			printstr = printstr  + str(numpy.asarray(self.weights)) + "\n"
		print (printstr)
		
	def printO(self):
		print (numpy.asarray(self.outData, float))


class Data:
	def __init__(self, number_ ,values_ ):
		self.number = number_
		values_.insert(0,255)
		#normalize data
		self.values = numpy.asarray(values_, float)/255
		#print(str(self.values))

	
def loadTrain():
	file = open(trainFile, "r")
	for line in file:
		vals = line.split(",")
		trainData.append(Data(vals[0], vals[1:785]))
		
def loadTest():
	file = open(trainFile, "r")
	for line in file:
		vals = line.split(",")
		testData.append(Data(vals[0], vals[1:785]))

	
def printCon():
	arrayStr = ""
	for m in range(0,10):
		arrayStr = arrayStr + str(confusionM[m][0])
		for n in range(1,10):
			arrayStr = arrayStr + " ," + str(confusionM[m][n])
		arrayStr = arrayStr + "\n"
	return arrayStr
	
def test(outerLayer,innerLayer):
	trials = 0
	correct = 0
	#initialize confusion matrix
	for m in range(0,10):
		for n in range(0,10):
			confusionM[m][n] = 0
	for t in trainData:
		temp = []
		for f in range(0,HLsize +1) :
			temp.append(0.0)
		temp[0] = 1.0
		temp[1:] =  outerLayer.forwardProp(t.values)
		output = innerLayer.forwardProp(temp)
		outp = int(output.index(max(output)))
		#print (str(outp))
		#print(str(output))
		'''
		#print(str(outp) + ", " + str(t.number))
		if (int(t.number) == int(outp)):
			print ("success")
		else:
			print("fail")
		'''
		confusionM[int(t.number)][outp] += 1
		trials += 1
	for a in range(0,10):
		correct = correct + confusionM[a][a]
	return  str(float(correct/trials)*100)

def train(outerLayer,innerLayer):
	trials = 0
	correct = 0
	#initialize confusion matrix
	for m in range(0,10):
		for n in range(0,10):
			confusionM[m][n] = 0
	
	targetList = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1, 0.1]
	temp = []
	for t in range(0,HLsize +1) :
		temp.append(0.0)
	temp[0] = 1.0
	#print (str(len(targetList)))
	for t in trainData:
		targetList = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1, 0.1]
		
		temp[1:] =  outerLayer.forwardProp(t.values)
		#print(str(innerLayer.weights[0]) + "\n")
		#print(str(temp))
		#temp.insert(0,1)
		
		output = innerLayer.forwardProp(temp)
		#print (output)
		
		outp = int(output.index(max(output)))
		confusionM[int(t.number)][outp] += 1
		trials += 1
		targetList[int(t.number)] = 0.9
		#print(outp)

		#print (numpy.asarray(targetList, float))# + numpy.asarray(output,float))
		errorj = innerLayer.backPropToH(targetList)
		#print (str(errork))

		outerLayer.backPropToI(errorj)
	for a in range(0,10):
		correct = correct + confusionM[a][a]
	return str(float(correct/trials)*100)
		
		

confusionM = [] 
for l in range(0,10):
	confusionM.append([])
for m in range(0,10):
	for n in range(0,10):
		confusionM[m].append(0)
'''
if (len(sys.argv) > 0):
	learningRate = float(sys.argv[1])
	momentum = float(sys.argv[2])
	HLsize = int(sys.argv[3])
	trainDataSZ = float(sys.argv[4])
	#print ("learningRate: "+ str(learningRate) + ", momentum: " + str(momentum) + ", HLsize: " + str(HLsize)) 
'''
loadTrain()
outLayer = Layer(785,HLsize)
#outLayer.newW()
#outLayer.save(OLFile)
outLayer.load(OLFile)
inLayer = Layer(HLsize +1 ,10)
#inLayer.newW()
inLayer.load(ILFile)
#inLayer.save(ILFile)
acc = test(outLayer, inLayer)
print (acc + " %") 
print (printCon())
for i in range (0,5):
	#inLayer.printW()
	acc = train(outLayer, inLayer)
	print (acc + " %") 
	print (printCon())

	#print("\n\n\n")

#print (printCon())

#print (printCon())
#testLayer.printO()


