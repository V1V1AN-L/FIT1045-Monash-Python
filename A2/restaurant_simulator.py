def get_meals_list_from_user():
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
        info_place = 0
        for info in meal_list:
            if '.' in info:
                meal_list[info_place] = float(info)
            elif info.isdigit():
                meal_list[info_place] = int(info)
            info_place += 1
        key_index = 0

        for key_name in get_meal.keys():
            get_meal[key_name] = meal_list[key_index]

            key_index += 1

        options.append(get_meal)
        
    return options

options = get_meals_list_from_user()

def display_menu(options):
    order = 0
    for meal in options:
        print(str(order+1)+'. Name:' + meal.get('name') + ' Sells:$' + str(meal.get('sell_for')) + ' Costs:$' + str(meal.get('cost_to_make')) + ' Takes:' + str(meal.get('cook_time')) + ' mins')
        order +=1

#print(display_menu(options)) #print?

def validate_user_choice(options, users_input):
    if users_input.isdigit() and (int(users_input)-1) in range(len(options)):
        result = True   
    else: result = False
    
    return result
 


def classify_cook_time(average_cook_time, stdev_cook_time, actual_cook_time):

    if actual_cook_time < average_cook_time - 2*stdev_cook_time:
        category = "very undercooked"

    elif average_cook_time - stdev_cook_time >= actual_cook_time >= average_cook_time - 2*stdev_cook_time:
        category = "slightly undercooked"

    elif average_cook_time - stdev_cook_time < actual_cook_time < average_cook_time + stdev_cook_time:
        category = "well cooked"

    elif average_cook_time + stdev_cook_time <= actual_cook_time <= average_cook_time + 2*stdev_cook_time:
        category = "slightly overcooked"

    elif actual_cook_time > average_cook_time + 2*stdev_cook_time:
        category = "very overcooked"

    return category



def get_cooking_tip(classification, base_tip):
    if classification == "very undercooked" or classification == "very overcooked":
        tip = -100

    elif classification == "slightly undercooked" or classification == "slightly overcooked":
        tip = 0

    elif classification == "well cooked":
        tip = base_tip
    
    return tip

def random_tip_compute(tip_chance, base_tip_value, random_comparison):
    if random_comparison < tip_chance:
        tip = int(base_tip_value)
    elif random_comparison > (1 - tip_chance):
        tip = int(base_tip_value) * -1

    else:
        tip = 0
    
    return tip

import random 
def order(options):
    print('Please enter your order. The options are given below')
    display_menu(options)  
    userinput=input('please enter a number to make your choice: ')
    indicator=validate_user_choice(options, userinput)    

    while indicator==False:
        userinput=input('please enter a number to make your choice: ')
        indicator=validate_user_choice(options, userinput)    
    userinput=int(userinput)
    print('now cooking '+options[userinput-1]['name'])
    
    cook_time_avg=options[userinput-1]['cook_time']
    cook_time_std=options[userinput-1]['cook_time_stdev']

    tip_chance=0.1
 
    continue_indi=True
    trial_count=0
    profit_total=0
    while continue_indi==True:
        trial_count=trial_count+1
        if trial_count>3:
            break
        
        cook_time_actual=random.gauss(cook_time_avg, cook_time_std)
        category_current=classify_cook_time(cook_time_avg, cook_time_std, cook_time_actual)
            
        print('Cook attempt: ',trial_count)
        print(options[userinput-1]['name']+' was '+category_current)
        print('The target cook time is', format(float(cook_time_avg),'.2f'),
              'mins and the actual cook time is',format(float(cook_time_actual),'.2f'),'mins')

        final_cooking_tip=get_cooking_tip(category_current, 10)    
        random_tip_score=random.random()
        final_random_tip=random_tip_compute(tip_chance, 10, random_tip_score) 

        print('The cook tip hence is '+str(final_cooking_tip)+'%')
        print('The random tip is '+str(final_random_tip)+
              '% given the random score is '+str(format(random_tip_score,'.2f'))+
              ' with a '+str(tip_chance)+'% criteria')

        sell_price=options[userinput-1]['sell_for']
        cook_cost=options[userinput-1]['cost_to_make']
        final_sell_price=sell_price+sell_price*(final_cooking_tip/100)+sell_price*(final_random_tip/100)
        
        print('final selling price was $',format(float(final_sell_price),'.2f'))
        current_profit=final_sell_price-cook_cost
        print('total profit was $',format(float(current_profit),'.2f'))
       
        profit_total=profit_total+current_profit
        if final_cooking_tip!=-100:
            continue_indi=False
    
    print('overall, the profit for this meal was $',format(profit_total,'.2f'))
    return profit_total



num_customer=int(input('How many guests do we have today?'))

def order_for_x_people(X):
    running_profit=0
    for i_customer in range(num_customer):
        
        print('Now serving customer',i_customer+1,)
        
        indi_profit=order(options)
        running_profit=running_profit+indi_profit
        print('This order, the resturant made a profit of $',format(indi_profit,'.2f'))
        
        print('The total running profit to now is $',format(running_profit,'.2f'))


order_for_x_people(num_customer)
