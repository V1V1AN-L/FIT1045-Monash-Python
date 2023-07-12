## THIS PROGRAM IS THE COMBINATION OF THE PROGRAMS FROM QUESTION 5 AND 6
## TAKE IN UP FOR 6 ROWS AND FOR THE SET COLUMN CHECK IF THERE IS 4 CONSECUTIVE PLAY INDEX 
## DETAILED DESCRIPTIONS FOR EACH STEP ARE TO BE FOUND IN PREVIOUS QUESTIONS

## BLOCK OF VARIABLE ## 
#two input variables - the row (DigitLocation) and player index (Digit_Check), 
#two known variable - number of digit (DigitCount) and number of rows (RowCount)
#three updating variable of loop operation
Digit_Check=int(input())
DigitLocation=int(input()) 
DigitCount=7
RowCount=6
Count=0
Order=0
Identifier=0

## BLOCK OF OPERATION ##
#for each row first find the digit at the wanted location
#filter if it is the targeted player index 
#and perform counting when consecutive ones are found. output true when reached 4 
while Order<RowCount:
    string_input = input()
    Order=Order+1
    if string_input!='':
        Input_n=int(string_input)
        Digit=(Input_n//(10**(DigitCount-DigitLocation)))%10
        if Digit==Digit_Check:
            Count=Count+1
        else:
            Count=0
    
        if Count==4:
            print(True)
            Identifier=1
            break
    else:
        break

        
if Identifier==0:
    print(False)                  

