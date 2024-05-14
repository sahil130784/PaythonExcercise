'''
9)	You has to enter Basic salary of an employee , Present Days & Absent Days And you has to calculate the total net salary for the employee  with following conditions
1)	Two days salary will be deductible for each absent
2)	He can take 2 leaves with pay every month [means he is present for 28 days then he can get full month pay] 
3)	But if total leaves exceed more than four then he will not get any benefits for two leaves mentioned above. [means he is present for 25 days out of 30 then he will get pay for 25 days not for 27 days]
4)	If he has full presents for the month then he will get 5% bonus of  basic salary
5)	But if has 5 leaves then he will minus 5% penalty of basic salary. 
6)	But if has 10 leaves then he will minus 15% penalty of basic salary. 
7)	He will get DA 70% of Basic Salary [calculated, excluding bonus & penalty if any]
8)	He will get CA 80% of DA

'''
AbsentDays = int(input("Absent Days: "));
LeavesDays = int(input("No of leaves: "));
TotalLeaves=(AbsentDays*2)+LeavesDays;
if (TotalLeaves <=4) :
    TotalLeaves =TotalLeaves-2;
if (TotalLeaves <0) :
    TotalLeaves =0;
    
    
PresentDays= 30-TotalLeaves;

if (AbsentDays ==0 )     and (LeavesDays==0 ):
    BonusValue= 5;
else :
    BonusValue=0;
Penalty=0;
if (TotalLeaves >=10 ): 
    Penalty=15;
if (TotalLeaves >=5 ): 
    Penalty=5;
    
PerDaySalary = float(input("Enter per day salary: "));
GrossSalary = PerDaySalary * PresentDays;
DA =  GrossSalary * .7;
CA = DA* .8; 
GrossSalary = GrossSalary + (GrossSalary*BonusValue * .01 )  - (GrossSalary*Penalty * .01 )  ;
NetSalary= GrossSalary + DA+CA;
print("Your Net salary is :" + str(NetSalary));