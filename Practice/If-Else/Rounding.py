import math;

'''
You has to enter a amount in Rs. [amount can be decimal or in numeric] you has to rounding the
amount with 1 or 5 or 10. The choice of rounding has to be enter by user

[ for example : If I enter 12.12 then rounding of 1 will give answer 12, rounding of 5 will give
10 and rounding of 10 will give 10 and if I enter 13.67 then rounding of 1 will give 14,
rounding of 5 will give 15 and rounding of 10 will give 10]

'''
InputRoundingMethod = int(input("Enter your input method (1,5,10): "))
InputNumber=float(input("Enter any number: "));
HalfValue=float(InputRoundingMethod/2);
ExcessValue= math.fmod(InputNumber,InputRoundingMethod);
if (ExcessValue > HalfValue):
    RoundedValue = InputNumber + (InputRoundingMethod-ExcessValue);
else:
    RoundedValue = InputNumber - ExcessValue;

print("Your final rounded values is : " + str(RoundedValue));    