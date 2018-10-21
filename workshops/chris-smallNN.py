
import math
import numpy

inputD = [1,1,0,1,0,1,0,1] #,[1,0.8,0.4,0.9,0.1,0.1,0.6,0.9]
inputW = [[ -0.2,-0.2,-0.1,-0.1,0.1,0.1,0.2,0.2],[0.2,0.2,0.1,0.1,-0.1,-0.1,-0.2,-0.2],
		[-0.2,-0.1,0.1,0.2,0.2,0.1,-0.1,-0.2]]
hiddenN = [0.0,0.0,0.0]
hiddenW = [[-0.1,0.0,0.1,0.2],[0.2,0.3,0.1,-0.2]]
out = [0.0,0.0]
target =[[0.9,0.9],[0.1,0.9],[0.9,0],[0.1,0.1]]
LR = 0.1

def FpropIH(data, weights):
	dotP = [[],[],[]]
	for i in range (0,3):
		a = numpy.asarray(data, float)
		b = numpy.asarray(weights[i], float)
		tempDot = a@b 
		print("tempDot: " + str(i) + " " + str(tempDot))
		dotP[i] =  1 /(1 + math.exp(-tempDot))
	return dotP
	
def FpropHO(data, weights):
	dotPO =[[],[]]
	
	for i in range (0,1):
		tempDot1 = 0.0
		a = data
		b = weights[i]
		print(str(a) + "   " +str(b))
		for j,k in zip(a,b):
			#print(tempDot1)
			tempDot1 +=  j*k
			print (str(j* k))
			print(tempDot1)
		
		#tempDot = data @ weights[i]
		#print (str(a[3]* b[3]))
		print("tempDot1: " + str(i) + str(tempDot1))
		
		dotPO[i] =  1 /(1 + math.exp(-tempDot1))
	dotPO[1] = 1 /(1 + math.exp(-0.3))
	print(str(dotPO))
	return dotPO
	
def calculateEk(output, targets ):
	errork = [[0.0],[0.0]]
	print("output in function: " + str(output))
	print("targets in function: " + str(targets))
	for i in range(0,2):
		tempNum = (targets[i] - output[i])
		errork[i] = output[i]  * (1 - output[i])* tempNum
	return errork

def calculateEj(Ek, hW,hN):
	errorj = [0.0,0.0,0.0]
	sumTerm = 0.0
	for j in range(1,4):
		for k in range (0,2):
			sumTerm = sumTerm + ((Ek[k]) * (hW[k][j]))
		errorj[j-1] = hN[j] * (1 -hN[j]) * sumTerm
	return errorj


def updateHW(errork, hW, hN):
	for j in range (0,4):
		for k in range (0,2):
			hW[k][j] = hW[k][j] + hN[j]* LR * errork[k]
	print("new weights: " + str(hW))
	hiddenW = hW
	
def updateIW(errorj,iW, iD):
	for j in range (0,3):
		for i in range(0,8):
			iW[j][i] = 	iW[j][i] + LR* errorj[j]* iD[i]	
	print("new weights: " + str(iW))
	inputW = iW
	
	
hData = FpropIH(inputD, inputW)
errork = [0.0,0.0]
errorj = [0.0,0.0,0.0]
hiddenN = hData
hiddenN.insert(0,1.0)
print (hiddenN)
out = FpropHO(hiddenN, hiddenW)
print ("outputs:  " + str(out))

errork = calculateEk(out, target[0])
print ("errork: " + str(errork))
errorj = calculateEj(errork, hiddenW,hiddenN)
print ("errorj: " + str(errorj))
print("old weights: " + str(hiddenW))
updateHW(errork,hiddenW,hiddenN)
print("old weights: " + str(inputW))
updateIW(errorj,inputW,inputD)
