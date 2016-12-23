
import os, sys, random,math
from readsvm import readSVM

def usage():
	print "usage : python crypto-index-query original_data transformed_data bin_encoding_file dimenion_i start end bin_width"

def getIDs(binIDs, marks, start, end):
	r=[]
	for i in range(len(binIDs)):
		if marks[i]>=start and marks[i+1]<=end:
			r.append(binIDs[i])
		elif marks[i]<=start and marks[i+1]>=start:
			r.append(binIDs[i])
		elif marks[i]<=end and marks[i+1]>=end:
			r.append(binIDs[i])
	return r
def calculatePrecision(r,trans):
	count =0
	for i in range(len(r)):
		count = count+trans.count(r[i])
	return float(count)/len(trans),count,len(trans)

def crypto(input_data,dim,bin_width,enc_file,transformed_data,start,end):
	target, records = readSVM(input_data)
	# dim starts from 0
	vec_i = [rec[dim] for rec in records]
	max_i = max(vec_i)
	min_i = min(vec_i)
	precision =0
	num = 0
	total = 0
	if min_i>start or min_i>end or max_i<start or max_i<end or start>=end:
		print "Invalid start or/and stop"
	else:
		nbins = int (1.0/bin_width)
		bin_size = float(max_i-min_i)/nbins
		marks = [min_i+bin_size * i for i in range(nbins)]
		marks.append(max_i)
		binIDs = random.sample(xrange(10000000), nbins)
		f= open(enc_file, "w+")
		for i in range(nbins):
			print >>f, marks[i], marks[i+1], binIDs[i]
		lists = getIDs(binIDs, marks, start, end)
		dimension =[]
		for i in range(len(records)):
			binid = int(math.floor ((records[i][dim]-min_i)/bin_size))
			if binid == nbins: # upper bound
				binid -=1
			records[i][dim] = binIDs[binid]
			dimension.append(binIDs[binid])
		precision,num,total = calculatePrecision(lists,dimension)
		o = open(transformed_data,"w+")
		for i in range(len(records)):
				if target[i]<0:
					val= str(target[i])+" "
				else: 
					val = "+"+str(target[i])+" "
				for j in range(len(records[i])):
					val =val+str(j+1)+":"+str(records[i][j])+" "
				print >>o,val
		print "Number of records exactly in ["+str(start)+" , "+str(end)+"] "+str(num)
		print "Precision of the query: "+str(precision)
if __name__ == '__main__':
	if len(sys.argv)!=8:
		print len(sys.argv)
		usage()
	else:
		input_data = sys.argv[1]
		transformed_data = sys.argv[2]
		enc_file = sys.argv[3]
		dim = int(sys.argv[4])
		start = float(sys.argv[5])
		end = float(sys.argv[6])
		bin_width = float(sys.argv[7])
		crypto(input_data,dim,bin_width,enc_file,transformed_data,start,end)

			
	
	
