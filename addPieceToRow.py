##  FIRST PART SAME AS THAT OF THE PREVIOUS QUESTION BUT WITH SPECIFIED PLAYER TO LOOK AT (1 OR 2) ##

## BLOCK OF VARIABLE ## 
Input_n=int(input()) 
PlayToMove=int(input()) #this represents the player number - 1 OR 2
DigitLocation=int(input())
DigitCount=7 

## BLOCK OF OPERATION ##
Remainder=Input_n//10**(DigitCount-DigitLocation)
Digit=Remainder%10 

##  THIS SECOND PART IS TO UPDATE ROW AND FILTER ##

#update the original number regarless by adding player index to the desired digit location. 
#if occuppied, do not show the updated row and output the error message. 
#when empty, show the updated row. 
NewInt=Input_n+PlayToMove*10**(7-DigitLocation)
if(int(Digit))>0: 
    print('invalid move') 
else:
    print(NewInt)

