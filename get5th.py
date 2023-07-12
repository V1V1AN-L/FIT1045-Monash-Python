## THIS IS BUILT TO FIND THE ACTUAL DIGIT AT THE 5TH LOCATION OF A 7-DIGIT NUMBER ##

## BLOCK OF VARIABLE ## 
#requires mannual input of the row (Input_n) with preset where to look (DigitLocation) 
#and total digit count (DigitCount)
Input_n=int(input()) 
DigitLocation=5 
DigitCount=7 

## BLOCK OF OPERATION ##
#find the trimed interger with digits after the desired position cut off
#With the remaining interger the needed digit value is the last digit - remainder from devided by 10
Remainder=Input_n//10**(DigitCount-DigitLocation) 
Digit=Remainder%10 
print(Digit)
