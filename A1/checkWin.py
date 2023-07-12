## BLOCK OF VARIABLE ## 
#two input variables - the row (DigitLocation) and player index (Digit_Check), 
#one known variable - number of digit (DigitCount) 
#three updating variable of loop operation
Input_n=int(input()) 
Digit_Check=int(input()) 
DigitCount=7
Count=0
Identifier=0
DigitLocation=1

## BLOCK OF OPERATION ##
## FILTER DOWN EACH DIGIT OF THE ROW ##
#the while loop performs the digit check up to 7 digit 
#count the number of consecutive digit locations of the play index
#for a digit location of different index, return the count variable to 0
#once a 4-consecutive index is found, update the identifier to 1 indicating there is a winning situation
#else output wrong once the filtering is finished 
while DigitLocation<DigitCount+1:
    Digit=(Input_n//(10**(DigitCount-DigitLocation)))%10    
    if Digit==Digit_Check:
        Count=Count+1
    else:
        Count=0
           
    if Count==4:
        print(True)
        Identifier=1
    DigitLocation=DigitLocation+1
        
if Identifier==0:
    print(False)




