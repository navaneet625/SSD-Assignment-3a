#Assignment3.c
##Q1
**..same as Assignment3b..**
solution steps
1. Read data from file `org.jason` and stored in the `empdata`dictionary
   In the dictionary data store in format `"empno":"parent,level of emp in hierachy tree"`
2. for find leader of 3 employee
   inputs are
   `<number_of_employee>` 
   `<empid 1>` 
   `<empid 2>`
   `<empid 3>`
   `<empid 4>` 
   `<empid 5>` 
   employee id's are 001,002,003,004,005,006,......,999
   similarly for 4 and 5 employee
   
   in employee tree 001 considered as root node and no leader for root node.
   
   changes between q1.a and q1.b
   1. 2 extra function created for computing leaders of leader  and compute level between leader and emp i.e.`LCA1` and `levlBt2node`
   2. Adding some condition statements according for cases 3,4,5
   3. previous q1.a in `LCA` fuction doest not return empnumber only print function are used
      but in the q1.b in `LCA` fuction it return employee number and the return value are used further thatswhy this changes are done.
   4.    
##Q2
**..same as Assignment3b..**
solution steps
1. Read  2 dates from `date_calculator.txt` in this file dates are in 2 rows i.e
   ex. date.calculator.txt
       Date1: 2/12/2020
       Date2: 12/12/2020
2. for Days calculation inputs are
    (a). `DD/MM/YYYY`
     for this input in the file dates are must be in following format.
     `12thJune,2020  12thJun,2020  12/6/2020 12.6.2020  12-6-2020`
    (b). `MM/DD/YYYY`
     for this input inthe file dates are must be in the follwoing format
     `6/12/2020  6.12.2020  6-12-2020`
And final output are saved in the file `Output.txt`

    changes between q2.a and q2.b
    (a). adding one extra date format ex. 12.6.2020
    (b). for MM/DD/YYYY maked separate code this input 
    (c). previously read date input from command line but q2.b date  inputs are taken from `date_calculator.txt`

##Q3
**..changes..**
Created Extra function `abc(time1,time2)` and `pqr(time1,time2)` because these code are repeated in all functions `employee1(),employee2(),employee3(),employee4() and employee5()`.
**..Reamaing all are same..**
output foramt:
1. enter number of emp ex.2 or 3 or 4 or 5
2. enetr number of hour ex. 1,2,3,....
3. All assumptions are same as previous q3.a part
4. changes betwwen q3.a and q3.b
   1. separate function for all 5 employe to extract data form coressponding `Employee"X".txt` files where X=1,2,3,4,5
   2. And operation are done according  to the emp
   3. Reamaining all are same as q3.a
5. All final output are saved int the file `output.txt` 
