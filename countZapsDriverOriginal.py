# driver for function countZaps
#
# inputs:
# 	none
#
# outputs:
#	number of zaps detected



import numpy as np
from scipy import signal

def countZaps(v,threshold):

	fs = 44.1e3
	N  = len(v)
	print('length of input array = ', N)
	
	f, Pxx_den = signal.periodogram(v, fs)

	myAvg = sum(Pxx_den[344:500])/len(Pxx_den[344:500])
	print('mean value = ', myAvg)
	print('threshold  = ', threshold)
	
	if myAvg>threshold:
		return 1
	else:
		return 0
		

def lookForSingleZap():
	fileName = 'singleZap.csv'
	print('input file: ', fileName)

	# read in audio data from csv file
	myFile = np.genfromtxt(fileName, delimiter=',')
	print('myFile: ', myFile)

	c=countZaps(myFile,1e-8)

	print('zap count = ', c)
	print('end zap counter')
	

fileName = 'LoudMusicArray.csv'
print('input file: ', fileName)

# read in audio data from csv file
myFile = np.genfromtxt(fileName, delimiter=',')
print('myFile: ', myFile[:10])

# partition data into segments of length 1024
lSeg = 1024
N    = len(myFile)
print("N = ", N)

numSegs = N // lSeg

print("numSegs: ", numSegs)

# Create an array of the desired size
w, h = lSeg, numSegs;
M = [[0 for x in range(w)] for y in range(h)]

myLen = len(M)
print("length(M): ", myLen)

zapCount = 0
for segNum in range(h):
	start = lSeg * segNum
	end   = start + lSeg
	print("segNum: ", segNum)
	
	segData = myFile[start:end]
	print("length segData: ", len(segData))
	
	zaps = countZaps(segData,1e-14)
	print("zaps: ", zaps)
	
	zapCount += zaps
	
print("final zap count: ", zapCount)







