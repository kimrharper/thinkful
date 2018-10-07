'''
Chris McPherson
Homework set #1
545
'''

#!/usr/bin/python
import sys
import random
import copy
import numpy
import numpy as np;from mnist import MNIST;import pandas as pd
from pathlib import Path

print(sys.path)
mndata = MNIST('data/mnist')
images, labels = mndata.load_training()

perceptrons = []
trainData = []
testData = []
confusionM = [] 
trainFile = "data/mnist/mnist_train.csv"
testFile = "data/mnist/mnist_test.csv"
perFile = "data/mnist/perceptrons.csv"
# resFile1 = "/Users/chrism/Python/ML/results1.csv"
# resFile2 = "/Users/chrism/Python/ML/results2.csv"
# resFile3 = "/Users/chrism/Python/ML/results3.csv"
defEpoch = 5

class Perceptron:
	#def __init__(self, target_, ):
	#	self.target = target_


	def __init__(self, target_ ,values_ = None):
		self.target = target_
		self.weights = []
		#self.values.append(float(random.random() - 0.5))
		
		if (values_ != None):
			self.weights = numpy.asarray(values_,float)
		else:
			for i in range (0,785):
				#self.weights.append(float(0.1))
				self.weights.append(float(random.random() - 0.5))
				#print (values[i])
		
	def printP(self):
		print (self.target)
		#print (self.values)
		printstr =""
		for i in self.weights:
			printstr = printstr + "," + str(i)
		print (printstr)

class Data:
	def __init__(self, number_ ,values_ ):
		self.number = number_
		values_.insert(0,255)
		self.values = numpy.asarray(values_, float)/255
		#for i in self.values:
		#	print (i)


def loadPer():
	try:
		my_file = Path(perFile)
		if (my_file.is_file()):
			file = open(perFile, "r")
			for line in file:
				vals = line.split(",")
				#print("per ",len(vals))
				weights = []
				weights = vals[1:]
				#print (vals[0], weights)
				#tempP =
				#tempP.printP()
				perceptrons.append(Perceptron(vals[0], weights ))
		else:
			for i in range(0,10):
				perceptrons.append(Perceptron(i))
			print ("new perceptrons created")
			file = open(perFile, 'w')
			for i in range (0,10):
				outStr = str(perceptrons[i].target)
				for j in range (0,785):
					outStr = outStr + "," + str(perceptrons[i].weights[j])
				outStr = outStr + "\n"
				file.write(str(outStr))
	except:
		for i in range(0, 10):
			perceptrons.append(Perceptron(i))
		print("new perceptrons created")
		file = open(perFile, 'w')
		for i in range(0, 10):
			outStr = str(perceptrons[i].target)
			for j in range(0, 785):
				outStr = outStr + "," + str(perceptrons[i].weights[j])
			outStr = outStr + "\n"
			file.write(str(outStr))
	
def loadTrain():
	for i in range(len(images)-200):
		trainData.append(Data(labels[i],images[i]))
		
def loadTest():
	for i in range(len(images)-200,len(images)):
		trainData.append(Data(labels[i],images[i]))
		
def train(learn, epoch, per):
	#print("training perceptron #" , per)
	target = perceptrons[int(per)].target
	input('Perceptron: {}'.format(target))
	bias = perceptrons[int(per)].weights[0]
	input('Bias: {}'.format(bias))
	#correct = 0
	#trials = 0
	for e in range(0,epoch):
		input('Epoch {}'.format(e))
		for t in trainData:
			#trials += 1
			number = int(t.number)
			#print (perceptrons[int(per)].weights)
			#print (t.values)
			a = perceptrons[int(per)].weights
			#print("pers " ,len(a))
			b = t.values
			sum = numpy.dot(a,b)
			if (float(sum) > 0):
				output = 1
			else:
				output = 0
			if (int(target) == int(number)):
				result = 1
			#print("correct")
			else:
				result = 0
		#print (sum , " ",number ," ", result -output)

			if (output != result):
			#update(output-result, learn, per, 0)
				temp = b * learn * (result - output)
				print(temp)
				perceptrons[int(per)].weights = perceptrons[int(per)].weights + temp
				for i in range(0,785):
					if (perceptrons[int(per)].weights[i] > 0.5):
						perceptrons[int(per)].weights[i] = 0.5
					if (perceptrons[int(per)].weights[i] < -0.5):
						perceptrons[int(per)].weights[i] = -0.5
			#else:
				#correct +=1
		#print ("accuracy is ", str(float(correct/trials)*100), " %")

def test():
	for m in range(0,10):
		for n in range(0,10):
			confusionM[m][n] = 0
	outputs = []
	correct = 0
	trials = 0
	for i in range(0,10):
		outputs.append(0)
	for t in trainData:	
		trials += 1
		number = int(t.number)
		b = t.values
		for i in range(0,10):
			outputs[i] = 0
		for p in perceptrons:
			a = p.weights
			sum = numpy.dot(a,b)
			outputs[int(p.target)] = sum 

		outp = outputs.index(max(outputs))
		#print(number str( outp)

		confusionM[number][outp] += 1
	
	for a in range(0,10):
		correct = correct + confusionM[a][a]

	return  str(float(correct/trials)*100)


	
def printCon():
	arrayStr = ""
	for m in range(0,10):
		arrayStr = arrayStr + str(confusionM[m][0])
		for n in range(1,10):
			arrayStr = arrayStr + " ," + str(confusionM[m][n])
		arrayStr = arrayStr + "\n"
	return arrayStr
	
#Menu
for l in range(0,10):
	confusionM.append([])
for m in range(0,10):
	for n in range(0,10):
		confusionM[m].append(0)

loadPer()
loadTrain()
option = '3'
while (option != 'q'):
	print ("please select option")
	print ("(1) Train perceptron")
	print ("(2) Test perceptron")
	print ("(3) Run automated testing suite")
	print ("(4) Print perceptron")
	print ("(5) Print confusion matrix")
	print ("(q) quit")
	option = input("> ")

	if (str(option) == "1"):
		print("ready to train")
		'''
		learn = input("what is the learning rate? > ")
		epoch = input("how many epochs? > ")
		'''
		perceptron = input("which perceptron? > ")
		if (str(perceptron) == "a"):
			for i in range (0,10):
				train(0.01, 50, i)
		else:
			train(0.1, 20, perceptron)

	if (str(option) == "2"):
		print("starting test")
		print ("accuracy is ",test() , " %")



	if (str(option) == "3"):
		print("starting test")
		outStr = ""

		cur = 1
		interval = 50
		for c in range (0,interval):
			for i in range (0,10):
				train(0.1, 1, i)
			outStr = outStr + str(cur) + ","+ str(test())+ "\n"
			cur += 1
		file = open(resFile3, 'w')
		print (outStr)
		file.write(outStr)
		file.write(printCon())
		file.close()
		'''
		print("starting test")
		outStr = "0," + test()+ "\n"
		interval = 1
		for c in range (0,1):
			for i in range (0,10):
				train(0.01, interval, i)
			outStr = outStr + str(interval) + " "+ str(test())+ "\n"
			interval += interval
		file = open(resFile2, 'w')
		print (outStr)
		file.write(outStr)
		file.write(printCon())
		file.close()

		loadPer()
		print("starting test")
		outStr = "0," + test()+ "\n"
		interval = 5
		for c in range (0,1):
			for i in range (0,10):
				train(0.1, interval, i)
			outStr = outStr + str(interval) + " "+ str(test())+ "\n"
			interval += interval
		file = open(resFile3, 'w')
		print (outStr)
		file.write(outStr)
		file.write(printCon())
		file.close()
		'''
		print("all done")
		option = "q"

	if (str(option) == "4"):
		print ("which perceptron would you like to print?")
		num = input("> ")
		perceptrons[int(num)].printP()

	if (str(option) == "5"):
		print (printCon())

''''
if (str(sys.argv[1]) != None):
	newP = int(sys.argv[1])
	p0 = Perceptron(newP)
	p0.printP()
'''


	
#Load training file
#initialize perceptron
#load perceptron
#normalize data
#train perceptron
#	take each of the normalized values
#	put them into list x
#	sum weights*x
#	subtract sum from bias
#	check y != t
#	update if needed
#		adj = l*(y-t) 
#		loop over weight where w[i] = w[i] - adj*x[i]
#	
#load testdata
#


#def createP(target):
	