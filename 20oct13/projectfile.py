#!/usr/bin/env python3
#Nidhi Walia
import sys

pdbname=sys.argv[1]
f=open(pdbname,'r')
lines=f.readlines()
list=[]
#this will give all the lists in a list
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


l=[]
x=[]
y=[]
z=[]
#This will give the list of x values, y values, z values of atoms and the list of atoms. 
for line in lines:
	words=line.split()
	xvalues=float(words[6])
	yvalues=float(words[7])
	zvalues=float(words[8])
	element=str(words[11])
	l.append(element)
	x.append(xvalues)
	y.append(yvalues)
	z.append(zvalues)	
#print ("The x values are\n", x)
#print ("The y values are\n", y)
#print ("The z values are\n", z)

#this will give the list of masses of each atom
m=[]
for atoms in list:
	if atoms[11]=="N":
	 m.append(14)
	elif atoms[11]== "C":
	 m.append(12)
	elif atoms[11]== "O":
	 m.append(16)
	else:
	 m.append(32)
#print (m, type(m))

#this will give the product of masses with coordinates (m1x1,m2x2,m3x3....;m1y1,m2y2,m3y3....;m1z1,m2z2,m3z3.....)
mx=[]
my=[]
mz=[]

for i in range(1337): 
	 xv=round((m[i]*x[i]),2)
	 mx.append(xv)
	 yv=round((m[i]*y[i]),2)
	 my.append(yv)
	 zv=round((m[i]*z[i]),2)
	 mz.append(zv)
#print("The mx values are\n",mx)
#print("The my values are\n",my)
#print("The mz values are\n",mz)


#this will give the sum of products of masses with their coordinates and sum of mass of atoms (m1x1+m2x2+m3x3+.....;m1y1+m2y2+m3y2+....;m1z1+m2z2+m3z3+.....;m1+m2+m3+....)	
mxv=sum(mx)
myv=sum(my)
mzv=sum(mz)
tm=sum(m)
#print ("The value of mx sum %.2f" % (mxv))
#print ("The value of my sum %.2f" %  (myv))
#print ("The value of mz sum % .2f" % (mzv))
#print ("The value of sum of masses % .2f" % (tm))


#this will give the values of x,y and z  centre of mass coordinates
p=mxv/tm
q=myv/tm
r=mzv/tm

#print("The x coordiante of centre of mass %.2f" % (p))
#print("The y coordiante of centre of mass %.2f" % (q))
#print("The z coordiante of centre of mass %.2f" % (r))

#this will give the centered x,y and z coordinates of all the atoms 
centeredX=[]
centeredY=[]
centeredZ=[]
for i in range(1337):
	 cenX=round(x[i]-p,2)
	 cenY=round(y[i]-q,2)
	 cenZ=round(z[i]-r,2)
	 centeredX.append(cenX)
	 centeredY.append(cenY)
	 centeredZ.append(cenZ)
#print("The centered x coordinate is\n", centeredX)
#print("The centered Y coordinate is\n", centeredY)
#print("The centered Z coordinate is\n", centeredZ)

#this will give the sum of all x, y and z coordinates of the atoms
sum_x=sum(x)
sum_y=sum(y)
sum_z=sum(z)
#print(sum_x,sum_y,sum_z)

#this will give the geometric centred x,y and z coordinates
gmx=sum_x/1337
gmy=sum_y/1337
gmz=sum_z/len(z)

#print("The x coordinate of geometric mean is %.2f" % (gmx))
#print("The y coordinate of geometric mean is %.2f" % (gmy))
#print("The z coordinate of geometric mean is %.2f" % (gmz))



#sum=0.0
#for data in mx:
	#for i in range(0,1337):
	 #sum=float(sum+mx[i])
#print(sum)

	 
f.close()


f=open("newpdb.out",'w')

#this will ask the user that whether the choice is to have coordinates of  centre of mass or geometric mass
s=input("Choose the required output, write CM for centre of mass or GM for  geometric mass: ")
if s=="CM":
	print ("The x,y and z coordinates of centre of mass are: %.2f, %.2f, %.2f" %(p,q,r))
elif s=="GM":
	print ("The x,y and z coordinates of geometric  mass are: %.2f, %.2f, %.2f" %(gmx,gmy,gmz))

else: 
	print ("please input your choice as mentioned in above statement")


#this will give the centered pdb file with name outfile having all x,y and z centered coordinates
for i in range(1337):
	#print"The x values %d\n,the y values %d\n, the z values %d\n" % (centeredX[i],centeredY[i],centeredZ[i])
	#outlist.append(final)
	outfile="{xval:6.2f} {yval:6.2f} {zval:6.2f}\n"
	f.write(outfile.format( xval=centeredX[i], yval=centeredY[i], zval=centeredZ[i]))


#f.write(str(outfile))
