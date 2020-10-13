#!/usr/bin/env python3
#Nidhi Walia
import sys

pdbname=sys.argv[1]
f=open(pdbname,'r')
lines=f.readlines()
list=[]
for line in lines:
	words=line.split()
	words[1]=int(words[1])
	words[5]=int(words[5])
	words[6]=float(words[6])
	words[7]=float(words[7])
	words[8]=float(words[8])
	words[9]=float(words[9])
	words[10]=float(words[10])
	list.append(words)
	#print (list)
f.close()

f=open("file.out",'w')
#print ("The list in lists \n")
s= "The new list of list is %s \n" % (list)
f.write(str(s))






	






