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

options=[]

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

    options.append(get_meal)
#using the code from the previous question, the users menu inputs are converted in to a list of dictionaries (or the defult menu is used) 

meal_selection = input()
#The meal_selection variable collects the dish that the customer wants.

if meal_selection.isdigit() and (int(meal_selection)-1) in range(len(options)):
#An if statement is used to see if: a) the input is made up of only digits (the function .isdigit() returns True if everything inside the () are digits)
                                   #b) and the meal_selection value - 1 is in the range of the options  

    meal_selection = 'now cooking ' + options[int(meal_selection)-1].get("name")
    print(meal_selection)
    #if the condition is true, the meal_selection variable is used to write out a string which includes all the required parts

else:
    print('invalid choice')
    #if the statement is false, "invalid choice" is printed  
