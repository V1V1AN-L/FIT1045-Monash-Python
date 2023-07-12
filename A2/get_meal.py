meal_list = input()

complete_meal_lst=[]

while meal_list !='.':
    get_meal = {'name': '', 'sell_for': '', 'cost_to_make': '', 'cook_time': '', 'cook_time_stdev': '' }
    meal_list = meal_list.split(',')
    key_index = 0

    for key_name in get_meal.keys():
        if key_index >0:        
            get_meal[key_name] = float(meal_list[key_index])

        else: 
            get_meal[key_name] = meal_list[key_index]

        key_index += 1
        
    complete_meal_lst.append(get_meal)
    meal_list = input()
   
print(complete_meal_lst)
