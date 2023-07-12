import datetime

#1. Representing a person as a Python dict
def make_person(this_id, name,date_of_birth):
    '''
    This function which takes an id (integer), name (string) and DOB (datetime fromat)
    From this it creates a dictionary (person) that includes each piece of information plus a some more.
    This function also creates keys for for friends and history (both with empty lists as their value) within the dicationary.
    This funciton returns the completed dicationary (person)
    Author: Akira Abe
    '''
    person = {'friends': [],
              'history': [],
              'id': this_id,
              'name': name,
              'date_of_birth': date_of_birth
              }
    return person

def find_friendX_inY(person_X,person_Y):
    '''
    This function takes in two dictionaries that are formatted in the same way as the output of make_person.
    The function identifies if the id of person_X is in the friendlist of person_Y and find that index
    It returns the index that was found
    Author: Akira Abe
    '''
    #iterate over each value in the list friends of perosn_Y and check if the value of friends is equal to the value of the id of person_X.
    #if it is return the index of that id value inthe list fiends.
    if person_X.get('id') in person_Y.get('friends'):
        return person_Y.get('friends').index(person_X.get('id'))

def make_friendship(person_X,person_Y):
    '''
    This function takes in two dictionaries that are formatted in the same way as the output of make_person.
    The function makes person X and Y friends by adding their respective ids to each other's friendlist.
    This funciton returns None
    Author: Akira Abe
    '''
    #this if statement prevents someone becoming friends with themselves (not possible)
    if person_X != person_Y:
    
        #the following two if statement make sure that an id that is already in friendlist is not added again.
        if person_X.get('id') not in person_Y.get('friends'):
            person_Y.get('friends').append(person_X.get('id'))
        
        if person_Y.get('id') not in person_X.get('friends'):
            person_X.get('friends').append(person_Y.get('id'))

def end_friendship(person_X,person_Y):
    '''
    This function takes in two dictionaries that are formatted in the same way as the output of make_person.
    The function ends person X and Y's friendship by removing their respective ids from each other's friendlist.
    This funciton returns None
    Author: Akira Abe
    '''
    #the following two if statement make sure that the id being removed is already in friendlist otherwise it cannot be removed.
    if person_X.get('id') in person_Y.get('friends'):
        person_Y.get('friends').remove(person_X.get('id'))
    
    if person_Y.get('id') in person_X.get('friends'):
        person_X.get('friends').remove(person_Y.get('id'))

def birthday_within_X_days_of_Y(person,days,comparison_date):
    '''
    This function takes an argument "person" which is a dictionary that is formatted in the same way as the output of make_person.
    It also takes the number of days in which a birhtday should lie an a date (in datetime format) to compare to.

    The function returns a boolean statement (True/False) about whether the DOB of the person lies within +/- days of the compariosn date
    Author: Akira Abe
    '''

    upper = person.get('date_of_birth') + datetime.timedelta(days=days)
    lower = person.get('date_of_birth') - datetime.timedelta(days=days)
    
    ori_checkyear=person.get('date_of_birth').year
    
    for possibleyear in (ori_checkyear-1,ori_checkyear,ori_checkyear+1):
        comparison_date = comparison_date.replace(year = possibleyear)
        # print(comparison_date)
        checkdate = lower<=comparison_date<=upper
        if checkdate is True:
            break
    return checkdate

#2. Representing a dictionary of people
def add_person(dict_of_people,name,date_of_birth):
    '''
    This function takes a dictionary (empty or fomatted with key being is and its value being a dictionary formatted as per make_person), a name (string) and a DOB (in datetime format)
    This function adds a new person with name: name and DOB: date_of_birth to the dict_of_people and makes the key equal to the highest value of key already in the list + 1
    If the dictionary is empty the key begins with 1.
    It returns a list of length one with a single dictionary which is the newest person added to the dict_of_people.
    Author: Akira Abe
    '''
    #checking if the dictionary is empty. If so making the the key for the new person 1 and adding a value to it by running the function make_person().
    if len(dict_of_people) == 0:
        current_key = 1
        dict_of_people[current_key] = make_person(current_key,name,date_of_birth)
    
    #when the dictionary is not empty, the highest key value is found and saved as current_key. 
    #The key for the new person is current_key + 1 and the corresponding value to it is made by running the function make_person() with its id being equal to the key value.
    else:
        current_key = (list(sorted(dict_of_people.keys()))[-1]) + 1
        dict_of_people[current_key] = make_person(current_key, name, date_of_birth)
    
    #finally a list with one dictionary is returned with the current_key (which is updated in the else statement once a new person has been added) being the newest person added to the dict_of_people.
    return [current_key, dict_of_people.get(current_key)]

def get_person_by_id(dict_of_people,find_id):
    '''
    This funciton takes a dictionary of dictionaries (formated as per add_person) and an id (integer) 
    it is used to find whether a person's id is in the dict_of_people

    If the id is found it returns the value of that key
    If the id is not found, it returns None
    Author: Akira Abe
    '''
    #iterating over evey key in the dictionary (which is equal to the id value), the key is check to see if it equal to the query id
    #if it is the value of that, key is returned
    for key in dict_of_people:
        if key == find_id:
            return dict_of_people.get(key)

#3. Creating a network from input
def convert_lines_to_friendships(lines):
    '''
    This function takes the list of strings which represent the people and relationship of between them
    It creates this list of strings into a dicrionary of people by:
            - breaking the stings up to thier indiviual parts of information
            - adding a person listed in the argument to the dictionary if they have not previously been seen on the list using add_person.
            - If "<->" is seen in the string both of people's ids are added to each others friend list using the function make_friendship()
    
    The function returns the dicationary of people made.

    Author1: Rui Qin
    Author2: Zecan Liu
    '''
    dict_of_people = {}
    #total name list is created to append the string inputs (the default people's names and birthdays ) to in the later code
    total_name_list = []
    for each_line in lines: # Use a for loop to iterate over each line in a list of strings in the format given in the supporting information
        #Using "<->" to slice the string (the friendship between people)
        each_relationship = each_line.split('<->')
        #a tempoary list to store people's names
        temp_name_ls=[]
        #Use the for loop to deal with each person in each relationship
        for each_person in each_relationship:
            #Slice the information string of a single person by ","
            person_info = each_person.split(',')
            #Name is the first item (index 0)
            info_name = person_info[0]
            # Add the name at the end of the name list of the people relationship
            temp_name_ls.append(info_name)
            # Birthday is the second item
            # Dates are represented in the format of Year-Month-Day
            info_dob = datetime.datetime.strptime(person_info[1], "%Y-%m-%d").date()
             # Check if the name is duplicate or not
            if info_name not in total_name_list:
                # Put the name in total_name_list if this name is unique
                total_name_list.append(info_name)
                # Call add_person to add this unique person in dictionary
                add_person(dict_of_people,info_name,info_dob)
        # The If statement checks is there is more than one person in the line. if there is then there are two people that need to be made friends,
        # The make_friendship function is run to alter the friendlist in each individual
        # 1 is added to the indexing value beacuae it extracted from total_name_list will be one less than the corresponding key value in the dicationary (becuase it starts at 1 not 0)
        if len(temp_name_ls) > 1:
            make_friendship(dict_of_people[total_name_list.index(temp_name_ls[0])+1],
                            dict_of_people[total_name_list.index(temp_name_ls[1])+1])
    return dict_of_people

# 4. Making a post
def new_post(content,owner,tagged):
    '''
    This function takes:
        - content which is a sting for a post that is to be made
        - author which is the dictionay of the peron writing the post
        - tagged whcih is a list of integers that specify the id's of the people tagged in this post
    
    The function creates a tuple (result_tuple) that includes the content, the author's id and a list of id's pf people in tagged that are seen in the owners frinedlist
    This tuple is appended to the author's history
    This function returns the tuple created (result_tuple)
    Author1: Rui Qin
    Author2: Zecan Liu
    '''
    # the id representing the author of the post
    owner_id = owner['id']
    
    #create list mutual_list which includes only the id's of people in the argument tagged which are also seen in the owner's friend list
    #Then reorder the list using sort()
    mutual_list = list(set(tagged).intersection(owner['friends']))
    mutual_list.sort()

    # Create a tuple containing the text content, ID of the author and list of tagged IDs
    result_tuple = (content, owner_id, mutual_list)
    # Append new tuple at the end of the key history in the author's dictionary which is a list representing the post history of the person
    owner['history'].append(result_tuple)

    #return the newly made tuple
    return result_tuple


# 5. Birthday posts
def birthdays_within_a_week_of(person_id,people_dict,comparison):
    '''
    This function takes the arguments: 
        - person_id which is the id of the person in query (integer) 
        - people_dict which is the dictionary to hold all unique people (dictionary)
        - comparison date to compare birthdays against in datetime format (datetime)

    This function gets the friends of the person whose ID matches person_id in the people_dict.
    It then creates a list of ids of friends who's birthdays lie within 1 week (7 days) of the comparison date by using the function birthday_within_X_days_of_Y
    This function returns a list of IDs of all friends of person_id who have a birthday within 7 days of the comparison date
    Author1: Xiaowen Zhou
    Author2: Zecan Liu
    '''
    #Creates a list of IDs for those friends of person_id from the people_dict
    friends_list = people_dict[person_id]['friends']
    #Upcoming birthday list is created to append the interger ID (the friends IDs) whos birthdays lie within a week of the comparsion date used in the later code
    upcoming_bday = []

    #Use the for loop to iterate over every friend's id in the person_id's friendlist
    for friends_id in friends_list:

        #The if statement checks whether the friend's birthday lie within 7 days (either side) of the comparison date. 
        #this is done by running the funciton birthday_within_X_days_of_Y() and testing if the return value is true
        if birthday_within_X_days_of_Y(people_dict [friends_id],7,comparison) is True:
            #Put the friends IDs that are identified as True in the upcoming birthday list
            upcoming_bday.append(friends_id)

    #return the list once iteration is complete
    return upcoming_bday

def make_birthday_posts(people_dict,from_person_id,for_people_ids):
    '''
    This function takes: 
        - people_dict which is the dictionary to hold all unique people (dictionary)
        - from_person_id which is the id of the person to look at (integer)
        - for_people_ids which is the list of friends of from_person_id with birthdays coming up (list)

    This function gets information from a list of friend IDs and birthday dates that contain from_person_id, 
    and sends birthday posts with specific names to the author's friends who have upcoming birthdays
    This function returns a list of birthday posts created
    Author1: Xiaowen Zhou
    Author2: Zecan Liu
    '''
    #post list is created to append the string (birthday posts with friend names) to in the later code
    post_list = []
    #Use the for loop to deal with each id in the list of friends of from_person_id with birthdays coming up
    for each_id in for_people_ids:
        #The selected friend_name is the corresponding name after finding the each_id from the people_dict
        friend_name = people_dict [each_id] ['name']
        #The content to be sent is a string, including the friend_name and the unified birthday greeting.
        content_str = 'Happy birthday ' + friend_name + '! Hope you have a good one!'
        #Append new objects which include the content string, author and tagged at the post_list representing the whole post content with the person integer ID and the friend's ID
        post_list.append (content_str,from_person_id,[each_id])
    return (post_list)

    
#python3 social_network_dictionary_based.py
if __name__ == "__main__":
    author = {'friends': [6,99,200], 'id': 1, 'name': 'Niklaus Mikaelson', 'date_of_birth': datetime.date(980, 10, 30), 'history': []}
    new_post("Always and forever", author, [4,99,5,6,7])
    print(author)
