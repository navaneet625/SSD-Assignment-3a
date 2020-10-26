import math

file1 = open("Employee1.txt","r")
emp1 = str(file1.readlines())
date = emp1
dateS = date.find(":{'") + len(":{'")
dateE = date.find("':['")
DATE = date[dateS:dateE]
#print (DATE)
start1 = emp1.find(":[") +len(":[")
end1 = emp1.find("]}}")
substring1 = emp1[start1:end1]
emP1=substring1.replace("'","")
eMP1=emP1.replace(" ","")
EMP1=eMP1.replace("-",",")
Emp1=EMP1.split(",")
stslot = input()
Emp1.insert(0,stslot)
enslot = input()
Emp1.append(enslot)

list1=[]
temp1=None
for i in range(1,len(Emp1),2):
	if(Emp1[i-1]!=Emp1[i]):
		temp1 = Emp1[i-1]+"-"+Emp1[i]
		list1.append(temp1)
f1 = open("output.txt","w")
f1.write('Employee1: '+repr(list1)+'\n')

file2 = open("Employee2.txt","r")
emp2 = str(file2.readlines())
start2 = emp2.find(":[") +len(":[")
end2 = emp2.find("]}}")
substring2 = emp2[start2:end2]
emP2=substring2.replace("'","")
eMP2=emP2.replace(" ","")
EMP2=eMP2.replace("-",",")
Emp2=EMP2.split(",")
Emp2.insert(0,stslot)
Emp2.append(enslot)
list2=[]
temp2=None
for i in range(1,len(Emp2),2):
	if(Emp2[i-1]!=Emp2[i]):
		temp2 = Emp2[i-1]+"-"+Emp2[i]
		list2.append(temp2)
f2 = open("output.txt","a")
f2.write('Employee2: '+repr(list2)+'\n')


#print(len(b1list[0][0]))
alist=[0]*16
boollist1=[0]*16
boollist2=[0]*16

def removeAndCut(s):
	if(len(s)==6):
		if(int(s[:1])<=5):
			v=int(s[:1])+12
			s=str(v)+s[2:4]
		else:
			s=s[:1]+s[2:4]	
	if(len(s)==7):
		if(int(s[:2])<=5):
			v=int(s[:1])+12
			s=str(v)+s[3:5]
		else:
			s=s[:2]+s[3:5]
	return int(s)

b1list=[]
for i in range(0,len(list1)):
	num=list1[i].split("-")
	b1list.append(num)
print(b1list)	


for i in range(0,len(b1list)):
	time1=removeAndCut(b1list[i][0])
	#print(time1)
	time2=removeAndCut(b1list[i][1])
	#print(time2)
	hourDiff = time2//100-time1//100-1
	minDiff = time2%100 +(60-time1%100)
	if(minDiff>=60):
		hourDiff+=1
		minDiff=minDiff-60
	res=hourDiff*60+minDiff	
	res=res//30
	index=math.ceil((time1-900)/50)
	#print(index)
	#print(boollist1)
	for i in range(0,res):
		boollist1[index]=1
		index=index+1
	#print(boollist1)	

b2list=[]
for i in range(0,len(list2)):
	num=list2[i].split("-")
	b2list.append(num)
print(b2list)	 

for i in range(0,len(b2list)):
	time1=removeAndCut(b2list[i][0])
	#print(time1)
	time2=removeAndCut(b2list[i][1])
	#print(time2)
	hourDiff = time2//100-time1//100-1
	minDiff = time2%100 +(60-time1%100)
	if(minDiff>=60):
		hourDiff+=1
		minDiff=minDiff-60
	res=hourDiff*60+minDiff
	res=res//30
	index=math.ceil((time1-900)/50)
	#print(index)
	#print(boollist2)
	for i in range(0,res):
		boollist2[index]=1
		index=index+1
	#print(boollist2)
print(boollist1)
print(boollist2)

# print(len(boollist1),len(boollist2))
for i in range(0,len(boollist1)):
	alist[i]=boollist1[i] and boollist2[i] 
print(alist)
slot=float(input())
slot=int(slot*2)
print(slot)
m=None
flag=0
count=0
k=0
for i in range(0,len(boollist1)):
	if count==slot:
		if (i-slot)%2 ==0:
			m=900+(i-slot)*50
		else:
			m=900+(i-slot-1)*50+30
		flag=1
		k=i
		# print(i-slot)
		break	
	else:
		if alist[i]==1:
			count=count+1
		else:
			count=0

# print(k)
n=None
if k%2==0:
	n=900+k*50
else:
	n=900+(k-1)*50+30							
	
#print(m,n)
m=str(m)
n=str(n)
if (len(m)==3):
	x=m[:1]+":"+m[1:]
else:
	x=m[:2]+":"+m[2:]	

if (len(n)==3):
	y=n[:1]+":"+n[1:]
else:
	y=n[:2]+":"+n[2:]	

h="{"+"'"+DATE+"':['"+x+"-"+y+"']}"
print(h)
f21= open("output.txt","a")
f21.write(repr(h)+'\n')