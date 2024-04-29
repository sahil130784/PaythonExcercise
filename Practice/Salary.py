
#Write a program to calculate net salary of a person. 
#Assumptions:
#	DA = 70% of basic salary
#	CA = 80% of basic salary
	
#	User Inputs:
#	Basic Salary 


BasicSalary = 1000;
DA = BasicSalary * .7;
CA = BasicSalary * .8;
NetSalary = BasicSalary+DA+CA;
print(NetSalary);



#Write a program to calculate net salary of a person.
	
#	User Inputs: 
#	Basic Salary in Rupees
#   DA in term of %
#   CA in term of %
 
BasicSalary = int(input("Enter Basic Salary: "));
DA=BasicSalary * (int(input("Enter DA %: ")) * 0.01);
CA = BasicSalary * (int(input("Enter CA %: "))*.01);
NetSalary = BasicSalary+DA+CA;
print(NetSalary);


