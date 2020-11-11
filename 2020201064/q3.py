import math

list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
alist=[0]*16
boollist1=[0]*16
boollist2=[0]*16
boollist3=[0]*16
boollist4=[0]*16
boollist5=[0]*16
b1list=[]
b2list=[]
b3list=[]
b4list=[]
b5list=[]
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
def abc(time1,time2):
	hourDiff = time2//100-time1//100-1
	minDiff = time2%100 +(60-time1%100)
	if(minDiff>=60):
		hourDiff+=1
		minDiff=minDiff-60
	res=hourDiff*60+minDiff	
	res=res//30
	index=math.ceil((time1-900)/50)
	return index
def pqr(time1,time2):
	hourDiff = time2//100-time1//100-1
	minDiff = time2%100 +(60-time1%100)
	if(minDiff>=60):
		hourDiff+=1
		minDiff=minDiff-60
	res=hourDiff*60+minDiff	
	res=res//30
	index=math.ceil((time1-900)/50)
	return res		

def employee1():
	file1 = open("Employee1.txt","r")
	emp1 = str(file1.readlines())
	date = emp1
	dateS = date.find(":{'") + len(":{'")
	dateE = date.find("':['")
	global DATE
	DATE = date[dateS:dateE]
	#print (DATE)
	start1 = emp1.find(":[") +len(":[")
	end1 = emp1.find("]}}")
	substring1 = emp1[start1:end1]
	emP1=substring1.replace("'","")
	eMP1=emP1.replace(" ","")
	EMP1=eMP1.replace("-",",")	
	Emp1=EMP1.split(",")
	Emp1.insert(0,"9:00AM")
	Emp1.append("5:00PM")
	temp1=None
	for i in range(1,len(Emp1),2):
		if(Emp1[i-1]!=Emp1[i]):
			temp1 = Emp1[i-1]+"-"+Emp1[i]
			list1.append(temp1)
	f1 = open("output.txt","w")
	f1.write('Employee1: '+repr(list1)+'\n')
	for i in range(0,len(list1)):
		num=list1[i].split("-")
		b1list.append(num)
	print(b1list)
	for i in range(0,len(b1list)):
		time1=removeAndCut(b1list[i][0])
		#print(time1)
		time2=removeAndCut(b1list[i][1])
		#print(time2)
		index = abc(time1,time2)
		#print(index)
		#print(boollist1)
		res =  pqr(time1,time2)
		for i in range(0,res):
			boollist1[index]=1
			index=index+1
	#print(boollist1)	
def employee2():
	file2 = open("Employee2.txt","r")
	emp2 = str(file2.readlines())
	start2 = emp2.find(":[") +len(":[")
	end2 = emp2.find("]}}")
	substring2 = emp2[start2:end2]
	emP2=substring2.replace("'","")
	eMP2=emP2.replace(" ","")
	EMP2=eMP2.replace("-",",")
	Emp2=EMP2.split(",")
	Emp2.insert(0,"9:00AM")
	Emp2.append("5:00PM")
	temp2=None
	for i in range(1,len(Emp2),2):
		if(Emp2[i-1]!=Emp2[i]):
			temp2 = Emp2[i-1]+"-"+Emp2[i]
			list2.append(temp2)
	f2 = open("output.txt","a")
	f2.write('Employee2: '+repr(list2)+'\n')
	for i in range(0,len(list2)):
		num=list2[i].split("-")
		b2list.append(num)
	print(b2list)
	for i in range(0,len(b2list)):
		time1=removeAndCut(b2list[i][0])
		#print(time1)
		time2=removeAndCut(b2list[i][1])
		#print(time2)
		index = abc(time1,time2)
		#print(index)
		#print(boollist1)
		res =  pqr(time1,time2)
		for i in range(0,res):
			boollist2[index]=1
			index=index+1
	#print(boollist2)

def employee3():
	file3 = open("Employee3.txt","r")
	emp3 = str(file3.readlines())
	start3 = emp3.find(":[") +len(":[")
	end3 = emp3.find("]}}")
	substring3 = emp3[start3:end3]
	emP3=substring3.replace("'","")
	eMP3=emP3.replace(" ","")
	EMP3=eMP3.replace("-",",")
	Emp3=EMP3.split(",")
	Emp3.insert(0,"9:00AM")
	Emp3.append("5:00PM")
	temp3=None
	for i in range(1,len(Emp3),2):
		if(Emp3[i-1]!=Emp3[i]):
			temp3 = Emp3[i-1]+"-"+Emp3[i]
			list3.append(temp3)
	f3 = open("output.txt","a")
	f3.write('Employee3: '+repr(list3)+'\n')
	for i in range(0,len(list3)):
		num=list3[i].split("-")
		b3list.append(num)
	print(b3list)
	for i in range(0,len(b3list)):
		time1=removeAndCut(b3list[i][0])
		#print(time1)
		time2=removeAndCut(b3list[i][1])
		#print(time2)
		index = abc(time1,time2)
		#print(index)
		#print(boollist1)
		res =  pqr(time1,time2)
		for i in range(0,res):
			boollist3[index]=1
			index=index+1
	#print(boollist3)

def employee4():
	file4 = open("Employee4.txt","r")
	emp4 = str(file4.readlines())
	start4 = emp4.find(":[") +len(":[")
	end4 = emp4.find("]}}")
	substring4 = emp4[start4:end4]
	emP4=substring4.replace("'","")
	eMP4=emP4.replace(" ","")
	EMP4=eMP4.replace("-",",")
	Emp4=EMP4.split(",")
	Emp4.insert(0,"9:00AM")
	Emp4.append("5:00PM")
	temp4=None
	for i in range(1,len(Emp4),2):
		if(Emp4[i-1]!=Emp4[i]):
			temp4 = Emp4[i-1]+"-"+Emp4[i]
			list4.append(temp4)
	f4 = open("output.txt","a")
	f4.write('Employee4: '+repr(list4)+'\n')
	for i in range(0,len(list4)):
		num=list4[i].split("-")
		b4list.append(num)
	print(b4list)
	for i in range(0,len(b4list)):
		time1=removeAndCut(b4list[i][0])
		#print(time1)
		time2=removeAndCut(b4list[i][1])
		#print(time2)
		index = abc(time1,time2)
		#print(index)
		#print(boollist1)
		res =  pqr(time1,time2)
		for i in range(0,res):
			boollist4[index]=1
			index=index+1
	#print(boollist4)

def employee5():
	file5 = open("Employee5.txt","r")
	emp5 = str(file5.readlines())
	start5 = emp5.find(":[") +len(":[")
	end5 = emp5.find("]}}")
	substring5 = emp5[start5:end5]
	emP5=substring5.replace("'","")
	eMP5=emP5.replace(" ","")
	EMP5=eMP5.replace("-",",")
	Emp5=EMP5.split(",")
	Emp5.insert(0,"9:00AM")
	Emp5.append("5:00PM")
	temp5=None
	for i in range(1,len(Emp5),2):
		if(Emp5[i-1]!=Emp5[i]):
			temp5 = Emp5[i-1]+"-"+Emp5[i]
			list5.append(temp5)
	f5 = open("output.txt","a")
	f5.write('Employee5: '+repr(list5)+'\n')
	for i in range(0,len(list5)):
		num=list5[i].split("-")
		b5list.append(num)
	print(b5list)
	for i in range(0,len(b5list)):
		time1=removeAndCut(b5list[i][0])
		#print(time1)
		time2=removeAndCut(b5list[i][1])
		#print(time2)
		index = abc(time1,time2)
		#print(index)
		#print(boollist1)
		res =  pqr(time1,time2)
		for i in range(0,res):
			boollist5[index]=1
			index=index+1
	#print(boollist5)			

empno=int(input())
if(empno==2):
	employee1()
	print(boollist1)
	employee2()
	print(boollist2)
	for i in range(0,len(boollist1)):
		alist[i]=boollist1[i] and boollist2[i]
	print(alist)
elif (empno==3):
	employee1()
	print(boollist1)
	employee2()
	print(boollist2)
	employee3()
	print(boollist3)
	for i in range(0,len(boollist1)):
		alist[i]=boollist1[i] and boollist2[i] and boollist3[i]
	print(alist)
elif (empno==4):
	employee1()
	print(boollist1)
	employee2()
	print(boollist2)
	employee3()
	print(boollist3)
	employee4()
	print(boollist4)
	for i in range(0,len(boollist1)):
		alist[i]=boollist1[i] and boollist2[i] and boollist3[i] and boollist4[i]
	print(alist)
elif (empno==5):
	employee1()
	print(boollist1)
	employee2()
	print(boollist2)
	employee3()
	print(boollist3)
	employee4()
	print(boollist4)
	employee5()
	print(boollist5)
	for i in range(0,len(boollist1)):
		alist[i]=boollist1[i] and boollist2[i] and boollist3[i] and boollist4[i] and boollist5[i]
	print(alist)			

# print(len(boollist1),len(boollist2))

slot=float(input())
slot=int(slot*2)
#print(slot)
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

h="{"+"'"+str(DATE)+"':['"+x+"-"+y+"']}"
a=h[15]
if(a!="N"):
	f21=open("output.txt","a")
	print(h)
	f21.write(repr(h)+'\n')
else:
	f21=open("output.txt","a")
	print("No any comman free slot available ")
	f21.write("No any common free slot available"+'\n')	