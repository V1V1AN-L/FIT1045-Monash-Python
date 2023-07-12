DefaultInput = ['Budda Bowl (vg),25,20,10,3',
'Eye Fillet Steak,55,25,7,1',
'Spaghetti Bolognese,30,22,40,5',
'Pad Thai (seafood),22,17,30,1']

meal_list_raw = []
meal_input = input()

if meal_input == '.':
    meal_list_raw = DefaultInput

while meal_input != '.':
    meal_list_raw.append(meal_input)
    meal_input = input()


options = []

for order in range(len(meal_list_raw)):
    get_meal = {'name': '', 'sell_for': '', 'cost_to_make': '', 'cook_time': '', 'cook_time_stdev': '' }
    meal_list = meal_list_raw[order].split(',')
    key_index = 0

    for key_name in get_meal.keys():
        if key_index > 0:
            get_meal[key_name] = float(meal_list[key_index])

        else:
            get_meal[key_name] = meal_list[key_index]
        key_index += 1

    options.append(get_meal)
#using the code from the previous question, the users menu inputs are converted in to a list of dictionaries (or the defult menu is used) 

meal_sel_co_time=input().split(',')


cook_time_avg=options[int(meal_sel_co_time[0])-1].get('cook_time')
cook_time_std=options[int(meal_sel_co_time[0])-1].get('cook_time_stdev')
cook_time_factor=(float(meal_sel_co_time[1])-cook_time_avg)/cook_time_std

tip_case=['10%','0%','-100%']
if float(meal_sel_co_time[1]) < cook_time_avg:
    category_case=['well cooked','slightly undercooked','very undercooked']
else:
    category_case=['well cooked','slightly overcooked','very overcooked']

if abs(cook_time_factor)<1:
    tip_current=tip_case[0]
    category_current=category_case[0]
elif abs(cook_time_factor)>=1 and abs(cook_time_factor)<=2:
    tip_current=tip_case[1]
    category_current=category_case[1]
else:
    tip_current=tip_case[2]
    category_current=category_case[2]

print(options[int(meal_sel_co_time[0])-1].get('name')+' was '+category_current
      +' and cooking tip was '+tip_current)
