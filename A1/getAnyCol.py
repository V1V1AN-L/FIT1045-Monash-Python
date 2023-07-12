##  SAME AS THAT OF THE PREVIOUS QUESTION BUT WITH ONE ADDITIONAL INPUT ##

## BLOCK OF VARIABLE ## 
DigitLocation=int(input()) #inputing the column number - wanted digit location
Input_n=int(input())
DigitCount=7 

## BLOCK OF OPERATION ##
Remainder=Input_n//10**(DigitCount-DigitLocation) 
Digit=Remainder%10 
print(Digit)
