import math
import csv
import matplotlib.pyplot as plt
import numpy as np

file="PatientTemperature_CSV.csv"
tem=[0]
age=[0]
with open(file,'r') as f_in:
    csv_reader = csv.reader(f_in)
    for line in csv_reader:
        tem.append(float(line[0]))
        age.append(int(line[1]))
dem=len(tem)-1
for i in range(1,dem):
    for j in range (i+1,dem+1):
        if tem[i]>tem[j]:
            a=tem[i]
            tem[i]=tem[j]
            tem[j]=a
        if age[i]>age[j]:
            b=age[i]
            age[i]=age[j]
            age[j]=b

# mean
sumt = 0
suma = 0
for i in range(1,dem+1):
    sumt = sumt+tem[i]
    suma = suma+age[i]
meant = sumt / dem
meana = suma / dem
# mean

# mode
count = 1
s = [tem[1]]
max = 1
for i in range(2,dem+1):
    if abs(tem[i]-tem[i-1])<0.001:
        count = count+1
    else:
        if count > max:
            s=[tem[i]]
            max = count
        elif count == max:
            s.append(tem[i])
        count=1
if count > max:
    s=[tem[i]]
    max = count
elif count == max:
    s.append(tem[i])
modet=s

count = 1
s = [age[1]]
max = 1
for i in range(2,dem+1):
    if abs(age[i]-age[i-1])<0.001:
        count = count+1
    else:
        if count > max:
            s=[age[i]]
            max = count
        elif count == max:
            s.append(age[i])
        count=1
if count > max:
    s=[age[i]]
    max = count
elif count == max:
    s.append(age[i])
modea=s
#mode

#median
if dem%2==1:
    p1=int((dem-1)/2+1)
    mediant=tem[p1]
    dediana=age[p1]
else:
    p1=int(dem/2)
    p2=p1+1
    mediant=(tem[p1]+tem[p2])/2
    mediana=(age[p1]+age[p2])/2
#median

#variance
vart=0
vara=0
for i in range(1,dem+1):
    vart=vart+(tem[i]-meant)**2
    vara=vara+(age[i]-meana)**2
#variance

#standard deviation
stat=math.sqrt(vart/(dem-1))
staa=math.sqrt(vara/(dem-1))
#standard deviation
n, bins, patches = plt.hist(x=tem, bins=[95,96,97,98,99,100,101,102])
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.title('Temperature sample')
plt.show()

print("Data for temperature")
print("mean: ",meant)
print("mode: ",modet)
print("median: ",mediant)
print("variance: ",vart)
print("standard deviation: ",stat)

print()

print("Data for age")
print("mean: ",meana)
print("mode: ",modea)
print("median: ",mediana)
print("variance: ",vara)
print("standard deviation: ",staa)