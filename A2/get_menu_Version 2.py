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


complete_meal_lst=[]

for order in range(len(meal_list_raw)):
    get_meal = {'name': '', 'sell_for': '', 'cost_to_make': '', 'cook_time': '', 'cook_time_stdev': '' }
    meal_list = meal_list_raw[order].split(',')
    key_index = 0

    for key_name in get_meal.keys():
        if key_index >0:        
            get_meal[key_name] = float(meal_list[key_index])

        else: 
            get_meal[key_name] = meal_list[key_index]

        key_index += 1
        
    complete_meal_lst.append(get_meal)
    print(str(order+1)+'. Name:'+get_meal['name']+' Sells:$'
          ,get_meal['sell_for'],' Costs:$' ,get_meal['cost_to_make'],
          ' Takes:' ,get_meal['cook_time'],' mins')
          
