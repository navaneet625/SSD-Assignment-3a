import json
with open('org.json') as json_file:
	data = json.load(json_file)
	
def LCA(emp1,emp2):
	while(emp1!='000' and emp2!='000'):
		if(empdata[emp1][1]==empdata[emp2][1]):
			if(empdata[emp1][0]==empdata[emp2][0]):
				return (empdata[emp1][0])
			else:
				emp1=empdata[emp1][0]
				emp2=empdata[emp2][0]
		elif(empdata[emp1][1]>empdata[emp2][1]):
			emp1=empdata[emp1][0]
		else:
			emp2=empdata[emp2][0]


def LCA1(emp1,emp2):
	while(emp1!='000' and emp2!='000'):
		if(empdata[emp1][1]==empdata[emp2][1]):
			if(empdata[emp1][0]==empdata[emp2][0]):
				return (emp1)
			else:
				emp1=empdata[emp1][0]
				emp2=empdata[emp2][0]
		elif(empdata[emp1][1]>empdata[emp2][1]):
			emp1=empdata[emp1][0]
		else:
			emp2=empdata[emp2][0]

def levlBt2node(emp1,emp2):
	if emp1 in empdata:
		x=empdata[emp1][1]
	if emp2 in empdata:
		y=empdata[emp2][1]
	print("Leader",emp1,"is",(int(y)-int(x)),"level above from",emp2)		

			
empdata = {}
x=0
for i in data:
	for j in data[i]:
		if i in empdata:
			empdata[j['name']].append(j['parent'],x)
		elif(i=='L0'):	
			empdata[j['name']]=('000',x)
		else:
			empdata[j['name']]=(j['parent'],x)
	x=x+1			
print(empdata)
q=input()
if (q=='2'):
	emp1=input()
	emp2=input()
	leader=None
	if(emp1=='001' or emp2=='001'):
		print("No any common leader for these employee")
	else:
		leader=LCA(emp1,emp2)
		print(leader)
	if(emp1=='001' or emp2 =='001'):
		print("No leader then no any level")
	else:
		levlBt2node(leader,emp1)
		levlBt2node(leader,emp2)	
elif(q=='3'):
	emp1=input()
	emp2=input()
	emp3=input()
	leader=None
	if(emp1=='001' or emp2 =='001' or emp3=='001'):
		print("No any common leader for these employee")
	else:
		empx=LCA(emp1,emp2)
		empy=LCA(emp2,emp3)
		if(empx == empy):
			print(empx)
			leader=empx
		else:
			leader=LCA1(empx,empy)
			print(leader)
	if(emp1=='001' or emp2 =='001' or emp3=='001'):
		print("No leader then no any level")
	else:
		levlBt2node(leader,emp1)
		levlBt2node(leader,emp2)
		levlBt2node(leader,emp3)			
elif(q=='4'):
	emp1=input()
	emp2=input()
	emp3=input()
	emp4=input()
	leader=None
	if(emp1=='001' or emp2 =='001' or emp3=='001' or emp4=='001'):
		print("No any common leader for these employee")
	else:
		empx=LCA(emp1,emp2)
		empy=LCA(emp2,emp3)
		empz=LCA(emp3,emp4)
		if(empx==empy and empx==empz):
			leader=empx
			print(leader)
		elif(empx==empy):
			leader=LCA1(empy,empz)
			print(leader)
		elif(empx==empz):
			leader=LCA1(empx,empy)
			print(leader)
		elif(empy==empz):
			leader=LCA1(empx,empy)
			print(leader)
		else:
			e1=LCA1(empx,empy)
			e2=LCA1(empy,empz)
			leader=LCA1(e1,e2)
			print(leader)
		if(emp1=='001' or emp2 =='001' or emp3=='001' or emp4=='001'):
			print("No leader then no level")
		else:
			levlBt2node(leader,emp1)
			levlBt2node(leader,emp2)
			levlBt2node(leader,emp3)
			levlBt2node(leader,emp4)
elif(q=='5'):
	emp1=input()
	emp2=input()
	emp3=input()
	emp4=input()
	emp5=input()
	leader=None
	if(emp1=='001' or emp2 =='001' or emp3=='001' or emp4=='001' or emp5=='001'):
		print("No any common leader for these employee")
	else:
		empA=LCA(emp1,emp2)
		empB=LCA(emp2,emp3)
		empC=LCA(emp3,emp4)
		empD=LCA(emp4,emp5)
		if(empA==empB and empA==empC and empA==empD):
			leader=empA
			print(leader)
		elif(empA==empB and empA==empC):
			leader=LCA1(empA,empD)
			print(leader)
		elif(empA==empB and empA==empD):
			leader=LCA1(empA,empC)
			print(leader)
		elif(empA==empC and empA==empD):
			leader=LCA1(empA,empB)
			print(leader)
		elif(empB==empC and empB==empD):
			leader=LCA1(empB,empA)
			print(leader)
		elif(empA==empB):
			e1=LCA1(empA,empC)
			e2=LCA1(empA,empD)
			leader=LCA1(e1,e2)
			print(leader)
		elif(empA==empC):
			e1=LCA1(empA,empB)
			e2=LCA1(empA,empD)
			leader=LCA1(e1,e2)
			print(leader)
		elif(empA==empD):
			e1=LCA1(empA,empC)
			e2=LCA1(empA,empB)
			leader=LCA1(e1,e2)
			print(leader)
		elif(empB==empC):
			e1=LCA1(empB,empA)
			e2=LCA1(empB,empD)
			leader=LCA1(e1,e2)
			print(leader)
		elif(empB==empD):
			e1=LCA1(empB,empC)
			e2=LCA1(empB,empA)
			leader=LCA1(e1,e2)
			print(leader)
		elif(empC==empD):
			e1=LCA1(empA,empC)
			e2=LCA1(empB,empD)
			leader=LCA1(e1,e2)
			print(leader)
		else:
			empx=LCA1(empA,empB)
			empy=LCA1(empB,empC)
			empz=LCA1(empC,empD)
			if(empx==empy and empx==empz):
				leader=empx
				print(leader)
			elif(empx==empy):
				leader=LCA1(empy,empz)
				print(leader)
			elif(empx==empz):
				leader=LCA1(empx,empy)
				print(leader)
			elif(empy==empz):
				leader=LCA1(empx,empy)
				print(leader)
			else:
				e5=LCA1(empx,empy)
				e6=LCA1(empy,empz)
				leader=LCA1(e5,e6)
				print(leader)
	if(emp1=='001' or emp2 =='001' or emp3=='001' or emp4=='001' or emp5=='001'):
		print("No leader then no level")
	else:
		levlBt2node(leader,emp1)
		levlBt2node(leader,emp2)
		levlBt2node(leader,emp3)
		levlBt2node(leader,emp4)
		levlBt2node(leader,emp5)			
else:
	print("select correct number of emp")	
