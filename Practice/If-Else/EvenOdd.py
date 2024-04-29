import math;
"""
Write a program to check whether a number is even or odd.
	User Inputs:
	Number
"""
InputNumber= int(input("Enter a Number: "));
if (math.fmod(InputNumber, 2)==0): 
    print("Even Number");
else:    
    print("Odd Number");
    
    '''
    Write a program to check whether a year is a Leap year or not.
    User Inputs:
     Year
    '''
    inputYear= int(input("Enter a Year: "));
    if ((math.fmod(inputYear,100) ==0 and math.fmod(inputYear,400) ==0) or 
         (math.fmod(inputYear,100) !=0 and math.fmod(inputYear,4) ==0 ) ):
        print("Its a leap year");
    else:
        print("Its non-leap year");