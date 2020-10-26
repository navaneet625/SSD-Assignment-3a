import json
with open('org.json') as json_file:
	data = json.load(json_file)
# empdata = {}
# for i in range(0, len(data)):
# 	k=0
# 	for j in range(0, len(data[str(i)])):
# 		k=k+1
# 		if i in empdata:
# 			empdata[data[str(i)][j]['name']].append(data[str(i)][j]['parent'])
# 		elif(i==0):	
# 			empdata[data[str(i)][j]['name']]='000'
# 		else:
# 			empdata[data[str(i)][j]['name']]=data[str(i)][j]['parent']
# 	print(type(i),"Level",i)		
# print(empdata)	

def LCA(emp1,emp2):
	if(emp1=='001' or emp2=='001'):
		print('No data for this input')
		return
	while(emp1!='000' and emp2!='000'):
		if(empdata[emp1][1]==empdata[emp2][1]):
			if(empdata[emp1][0]==empdata[emp2][0]):
				print(empdata[emp1][0])
				break
			else:
				emp1=empdata[emp1][0]
				emp2=empdata[emp2][0]
		elif(empdata[emp1][1]>empdata[emp2][1]):
			emp1=empdata[emp1][0]
		else:
			emp2=empdata[emp2][0]	
						
empdata = {}
x=0
for i in data:
	#print(i)	
	for j in data[i]:
		if i in empdata:
			empdata[j['name']].append(j['parent'],x)
		elif(i=='L0'):	
			empdata[j['name']]=('000',x)
		else:
			empdata[j['name']]=(j['parent'],x)
	x=x+1			
#print(empdata)
#print(empdata['011'][1])
#print(empdata['011'][0])
emp1=input()
emp2=input()

LCA(emp1,emp2)		