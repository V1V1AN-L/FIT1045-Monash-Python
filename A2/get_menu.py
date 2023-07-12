DefaultInput=['Budda Bowl (vg),25,20,10,3',
'Eye Fillet Steak,55,25,7,1',
'Spaghetti Bolognese,30,22,40,5',
'Pad Thai (seafood),22,17,30,1']


meal_list_raw=[]
meal_input=input()

if meal_input=='.':
    meal_list_raw=DefaultInput

while meal_input !='.':
    meal_list_raw.append(meal_input)
    meal_input = input()



for order in range(len(meal_list_raw)):
    meal_list = meal_list_raw[order].split(',')
    get_meal = [ '', ' Name:', '' , ' Sells:$', '' , ' Costs:$' ,''  , ' Takes:' , '',' mins']
    key_index = 2
    
    for order_item in range(len(get_meal)):
        get_meal[0] = str(order+1)+'.'
        
        if  key_index == 2: 
            get_meal[key_index] = meal_list[order_item]
        
        elif key_index <=8:
            get_meal[key_index] = str(float(meal_list[order_item]))

        key_index += 2
        order_item +=1
      
       
    menu_str=''.join(get_meal)
    print(menu_str)
