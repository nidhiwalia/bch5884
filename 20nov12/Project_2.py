#!/usr/bin/env python3
#Nidhi Walia
#https://github.com/nidhiwalia/bch5884


import numpy
from matplotlib import pyplot as plt
from scipy.signal import find_peaks

#Reading the sec file and generating the array for time as x and absorbance as y

f=open("superose6_50.asc")
lines=f.readlines()
f.close()

x=[]
y=[]
for line in lines[3:]:
	words=line.split()
	try:
		x.append(float(words[0]))
		y.append(float(words[1]))
	except:
		#print("Parsed the file",line)
		continue
x=numpy.array(x)
y=numpy.array(y)

#Finding peaks.
#Finding the x and y coordinates for the peaks using 3 points(p,q,r) such that q will be the highest.The point q should be greater than p,r and threshold.

threshold=75
peak_x=[]
peak_y=[]
peak_xy=[]
index_peak=[]
for i in range((len(y))-1):
	p=y[i-1]
	q=y[i]
	r=y[i+1]
	if q>=p and q>=r and q>threshold:
		peak_x.append(x[i])
		peak_y.append(y[i])
		peak_xy.append((x[i],y[i]))
		index_peak.append(i)

#Finding the slopes at all the points.

m=[]
for i in range((len(y))-1):
	dy=y[i+1]-y[i]
	dx=x[i+1]-x[i]
	m.append(dy/dx)

#Finding the dips in between the peaks.

dip_xvalue=[]
dip_yvalue=[]

for i in range(len(index_peak)-1):
	list_x=x[index_peak[i]:index_peak[i+1]]
	list_y=y[index_peak[i]:index_peak[i+1]]
	y_values=numpy.array(list_y)
	inv_data=1/y_values
	dips,_=find_peaks(inv_data)
	dip_xvalue.append(float(list_x[dips]))
	dip_yvalue.append(float(list_y[dips]))


#Finding the start and end point.Initial point of the first peak and end point of the last peak.
	
start_x=[]
start_y=[]
end_x=[]
end_y=[]
n=index_peak[0]-5
while(m[n]>5):
	n=n-1
start_x.append(float(x[n-4]))
start_y.append(float(y[n-4]))

k=index_peak[len(index_peak)-1]
while(m[k+5]<-5):
	k=k+1
end_x.append(float(x[k+4]))
end_y.append(float(y[k+4]))

#Printing the coordinates of the peaks and the boundaries of the peaks.
print("The x,y coordinates of the peak1 are",peak_xy[0])
print("The x,y coordinates of the peak2 are",peak_xy[1])
print("The x,y coordinates of the peak3 are",peak_xy[2])
print("The x,y coordinates of the peak4 are",peak_xy[3])


print("The boundaries of peak1 are", start_x[0],"mins to",dip_xvalue[0],"mins")
print("The boundaries of peak2 are",dip_xvalue[0],"mins to",dip_xvalue[1],"mins")
print("The boundaries of peak3 are",dip_xvalue[1],"mins to",dip_xvalue[2],"mins")
print("The boundaries of peak4 are",dip_xvalue[2],"mins to",end_x[0],"mins")


#Plot x and y (time and absorbance),red dots shows the peaks,green dots shows the boundary values of x,(x,y) shows the coordinates of the peaks,x axis labelled as time, y axis labelled as absorbance.
plt.plot(x,y)
plt.scatter(peak_x,peak_y,color='red')
plt.plot(dip_xvalue,dip_yvalue,'go')
for x,y in zip(peak_x,peak_y):
	plt.text(x,y,'(%.1f,%.1f)'%(x,y),ha='right',va='bottom')

plt.title('Size Exclusion Chromatogram',pad=20,color='blue',fontsize=18)
plt.xlabel('time',color='blue')
plt.ylabel('absorbance',color='blue')
plt.scatter(start_x,start_y,color='green',marker='o')
plt.scatter(end_x,end_y,color='green',marker='o')
plt.show()



