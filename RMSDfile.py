#!/usr/bin/env python3
#https://github.com/nidhiwalia/bch5884

import sys
def readpdb(pdbfilename):
	'''defining function to read pdbfiles and return lines as lines of the file'''
	pdbfile=open(pdbfilename,'r')
	lines=pdbfile.readlines()
	pdbfile.close()
	return lines

def createList(list):
	'''defining function to make lists and return record as a list of lists of x,y andz values of the pdbfiles'''
	record=[]
	for line in list:
		if line[:4]=="ATOM":
		 d=[]
		 d.append(float(line[30:38]))
		 d.append(float(line[38:46]))
		 d.append(float(line[46:54]))
		 record.append(d)
	
	return record

def rmsd(list1,list2):
	'''defining function to take both the lists and return RMSD as value of RMSD'''
	n=len(list1)
	sumx=0.0
	sumy=0.0
	sumz=0.0
	for i in range(n):
		file1=list1[i]
		file2=list2[i]
		x=round((float(file1[0])-float(file2[0]))**2,3)
		y=round((float(file1[1])-float(file2[1]))**2,3)
		z=round((float(file1[2])-float(file2[2]))**2,3)
		sumx=sumx+x
		sumy=sumy+y
		sumz=sumz+z		
	RMSD=round((((sumx+sumy+sumz)/n)**0.5),3)
	return RMSD
		
if __name__=="__main__":
	filename=sys.argv[1]
	filename2=sys.argv[2]
	line1=readpdb(filename)
	line2=readpdb(filename2)
	list1=createList(line1)
	list2=createList(line2)

	rmsdList=rmsd(list1,list2)
	print("The RMSD between the two given PDB structurs is",rmsdList)
