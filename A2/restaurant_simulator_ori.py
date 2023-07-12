def get_meals_list_from_user():
    DefaultInput=['Budda Bowl (vg),25,20,10,3',
    'Eye Fillet Steak,55,25,7,1',
    'Spaghetti Bolognese,30,22,40,5',
    'Pad Thai (seafood),22,17,30,1']

    meal_list_raw=[]
    meal_input=input()
    #First, the default menu is set in the variable DefaultInput which is used if the user inputs '.' as their first list input.
    #A blank list (meal_list_raw) is created to append the string inputs to in later code

    if meal_input=='.':
        meal_list_raw=DefaultInput
    #If statement to insert the defult list if the user inputs '.' as the first list input

    while meal_input !='.':
        meal_list_raw.append(meal_input)
        meal_input = input()
    #While statement is used to stop adding to the list when the stop input '.' is entered
    #Each iteration appends the last raw input to the raw list and then asks for a new meal to repeat until '.' is entered.

    options=[]
    #Another empty list is created (options) to add the final dictionaries of each meal list into

    for order in range(len(meal_list_raw)):
        get_meal = {'name': '', 'sell_for': '', 'cost_to_make': '', 'cook_time': '', 'cook_time_stdev': '' }
        meal_list = meal_list_raw[order].split(',')
        key_index = 0
    #The for loop is used to iterate over each order in the meal_list_raw. 
    #Within the loop a dictionary is created (get_meal) and each string within the list meal_list_raw are each split into a list using the delimiter ",". 

        for key_name in get_meal.keys():
            if key_index >0:        
                get_meal[key_name] = float(meal_list[key_index])

            else: 
                get_meal[key_name] = meal_list[key_index]

            key_index += 1
    #An if statement is used to differentitate the string element of the list (Name) and all other float elements in the list and converts them accordingly.

        options.append(get_meal)
    
    
    
    return options
  
options = get_meals_list_from_user()



def display_menu(options):
    for meal_order in range(len(options)):
        get_meal = options[meal_order]
        print(str(meal_order+1)+'. Name:' + get_meal['name'] + ' Sells:$' + str(get_meal['sell_for']) + ' Costs:$' + str(get_meal['cost_to_make']) + ' Takes:' + str(get_meal['cook_time']) + ' mins')
        
        
        
display_menu(options)


###### End of Q2 ########

users_input = input()
def validate_user_choice(options, users_input):
    
    if users_input.isdigit() and (int(users_input)-1) in range(len(options)):
                            
        
        return True
    else:
        return False

validate_user_choice(options,users_input))
###################END OF Q3#################

