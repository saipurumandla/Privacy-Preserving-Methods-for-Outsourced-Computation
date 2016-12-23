import numpy as np
from random import gauss
import sys,os
from scipy.linalg import qr

def  orthogonal(n):
	H = np.random.randn(n, n)
	Q, R = qr(H)
	A = np.array(Q)
def readSVM(fn):
	labels = []
	records = []
	f = open(fn)
	ncols = 0
	for line in f.readlines():
		fields = line.strip().split(" ")
		labels.append(int(fields[0])) #assume labels are integers
		r = {}
		for v in fields[1:]:
			i, u = v.split(":")
			i = int(i)
			r[i] = float(u)
			if i> ncols:
				ncols = i
		records.append(r)

	records2=[]
	for r in records:
		v = [0]*ncols # if the field is not mentioned, the default value is 0
		for i in r:
			# the field id starts from 1
			v[i-1] =r[i]
		records2.append(v)

	return labels, records2
def transpose(rec):
	return np.array(rec).transpose()

def randommatrix(n,m):
	H = np.random.rand(1, m)
	H1 = []
	H2 = [abs(k) for k in H[0]]
	for i in range(0,n):
		H1.append(H2)
	return H1

def gaussianmatrix(n,std):
	values = []
	while len(values) < n:
		while True:
			value = gauss(0,std)
			if 0 < value < std:
				values.append(value)
				break;
	return values
def generategaussian(n,m,std):
	gauss=[]
	for i in range(0,m):
		gauss.append(gaussianmatrix(n,std))
	return gauss



if __name__ == '__main__':
	lab,rec = readSVM(sys.argv[1])
	variance = float(sys.argv[2])
	rec_transpose = transpose(rec)
	orthogonal = orthogonal(len(rec_transpose))
	Rx = np.dot(R,rec_transpose)
	T = randommatrix(len(Rx),len(Rx[0]))
	D = generategaussian(len(Rx),len(Rx[0]),variance)
	print Rx[0]
	print len(Rx),len(Rx[0])

