## BLOCK OF VARIABLE ## 
#where to add a piece (DigitLocation), column count (DigitCount), row count (RowCount), 
#and two updating variable of loop operation - order (counting loop) and 
#temporder (temporary avalable row index)
DigitLocation=int(input()) 
DigitCount=7 
RowCount=6
order=0 
temporder=0

## BLOCK OF OPERATION ##
## FIRST PART IS TO TAKE EACH ROW, FILTER IF THERE IS AVAILABLE SLOT ##
#using while loop for only performing filtering up to the number of rows (max 6), top to bottom. 
#for each row, allows an input (string), and filter if the input is empty, exit if it is empty
#use the same operation as previous questions to find the digit of a row at the desired location and 
#if the location is empty (Digit=0), store the row number (order) into temporary row index (temporder)
while order<RowCount:
    s = input()
    order=order+1
    if s!='':
              Input_n=int(s)
              Digit=(Input_n//(10**(DigitCount-DigitLocation)))%10
              if Digit==0:
                     temporder=order                    
    else:
       break  

## SECOND PART IS TO OUTPUT MESSAGE BASED ON FILTERING RESULT ##
#there is no available space is the temporary row index is not been updated 
#other wise the current temporary row index represents the lowest row (from top yo bottom) of empty space
#update this row number in the order of from bottom to top and print out        
if temporder!=0:   
    print(RowCount-temporder+1)
else: 
    print('no room in column',DigitLocation)
       
                     

              
