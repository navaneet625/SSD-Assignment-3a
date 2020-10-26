class dATe:
	def __init__(self,d,m,y):
		self.d = d
		self.m = m
		self.y = y

Months=['January','February','March','Aprail','May','June','July','August','September','October',
'November','December','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
Month_Day=[31,28,31,30,31,30,31,31,30,31,30,31]
date1=input()
if('/' in date1):
	dATE1=date1.split('/')
	print(dATE1)
else:
	Date1=date1.replace("th","-")
	DATE1=Date1.replace(",","-")
	DATe1=DATE1.split("-")
	#print(DATE1)
	month1=DATe1[1]
	#print(month1)
	day1=month1
	for i in range(24):
		if(month1==Months[i]):
			if(i<12):
				day1=i+1
			else:
				day1=i%12+1
				#print(i)	
	#print(day1)
	dATE1=DATE1.replace(month1,str(day1))	
	#print(dATE1)
	dATE1=dATE1.split('-')
	print(dATE1)
	
date2 = input()	
if('/' in date2):
	dATE2=date2.split('/')
	print(dATE2)		
else:
	Date2=date2.replace("th","-")
	DATE2=Date2.replace(",","-")
	DATe2=DATE2.split("-")
	#print(DATE2)
	month2=DATe2[1]
	#print(month2)
	day2=month2
	for i in range(24):
		if(month2==Months[i]):
			if(i<12):
				day2=i+1
			else:
				day2=i%12+1
				#print(i)	
	#print(day2)
	dATE2=DATE2.replace(month2,str(day2))	
	#print(dATE2)
	dATE2=dATE2.split('-')
	print(dATE2)
	
def numberOfDays(dt1,dt2):
	n1 = dt1.y*365 + dt1.d
	for i in range(0,dt1.m-1):
		n1+=Month_Day[i]
	years1=dt1.y
	if(dt1.m <= 2):
		years1-=1
	n1+=int(years1//4+years1/400-years1//100)		
	#n1 +=numberOfLY(dt1)	
	n2=dt2.y*365 + dt2.d
	for i in range(0,dt2.m-1):
		n2+=Month_Day[i]
	years2=dt2.y
	if(dt2.m <= 2):
		years2-=1
	n2+=int(years2//4+years2/400-years2//100)	
	#n2+=numberOfLY(dt2)	
	return (n2 - n1)

#print(dATE2)
dt1 = dATe(int(dATE1[0]),int(dATE1[1]),int(dATE1[2]))
dt2 = dATe(int(dATE2[0]),int(dATE2[1]),int(dATE2[2]))

print(abs(numberOfDays(dt1,dt2)))