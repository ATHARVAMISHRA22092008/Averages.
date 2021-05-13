import csv
from collections import Counter
with open("SOCR-HeightWeight.csv",newline="") as f:
   reader=csv.reader(f)
   fileData=list(reader)
fileData.pop(0)
newData=[]
for i in range(len(fileData)):
   x=fileData[i][1]
    newData.append(float(x))
weight=len(newData)
total=0
for i in newData:
   total=total+i
mean=total/weight
print("The mean is", mean)
   
   
newData.sort()
if weight%2==0:
   median1=float(newData[weight//2])
   median2=float(newData[weight//2-1])
   median=(median1+median2)/2
else:
   median=newData[weight//2]
print("The Median is", median)

data=Counter(newData)
datarange={"50-60":0,"60-70":0, "70-80":0}
for weight, occurence in data.items():
   if 50<float(weight)<60:
      datarange["50-60"]+=occurence
   elif 60<float(height)<70: 
      datarange["60-70"]+=occurence
   elif 70<float(height)<80:
      datarange["70-80"]+=occurence
mrange,moccurence=0,0
for range,occurence in datarange.items():
   if occurence>moccurence:
      mrange, moccurence=[int(range.split("-")[0]),int(range.split("-")[1])], occurence
mode=float((mrange[0]+mrange[1])/2)
print("The mode is", mode)
