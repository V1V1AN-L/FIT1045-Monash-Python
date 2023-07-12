#the datetime package must be imported 
import datetime

#people dictionary includes each people's information.
people_dic={}

#This is where you define the days input for within X days of Y function (question 6 needs it to be 1 week i.e 7 days)
days=7

#Class is used to describe a collection of objects (person) that have the same properties and methods.
#It defines the properties and methods common to every object in the collection.
class Person:
    """
    This class is used to describe a set of attributes and methods. 
    These attributes and methods are made to perform the tasks that were defined in the dictionary based task. 
    The benefit of making a class is to streamline this process and make it faster and simpler to create the social network. 
    Zecan Liu
    """

    #When defining a function, if we want to operate with global variables we need to declare it as global inside the function.
    #Here, we declare the variable people_dic as a global variable
    global people_dic

    #Initialising the number of the people as 0.
    num_people=0

    #Every class should have a method with the special name __init__ (constructor).
    #'__init__' sets up the attributes required within the new instance by giving them their initial values.
    #The self parameter is automatically set to reference the newly created object(person's integer ID, name and date of birthday) that needs to be initialized.

    def __init__(self,id:int,name,DOB):
        '''
        In the dictionary based model the make_person function represented constuctor. 
        The attributes will be assigned to this instance instead of making a dictionary
        '''

        #Assigning each attribute a value
        self.id=id
        self.name=name
        self.DOB=DOB
        self.friends=[]
        self.history=[]
        #The number of people increases by one as new instances of the person are added
        Person.num_people+=1
        people_dic[Person.num_people]=self

    def birthday_within_X_days_of_Y(self,days,comparison_date):
        '''
        Definig a new method with the same code as the previously defined function in the dictionary based model with the same name.
        instead of accepting person as an argument, it instead refers to this instance of the class i.e self
        the DOB attribute from the instance required rather than accessing the key of the person (done in dictionary based)
        '''

        upper = self.DOB + datetime.timedelta(days=days)
        lower = self.DOB - datetime.timedelta(days=days)
        
        ori_checkyear=self.DOB.year
        
        for possibleyear in (ori_checkyear-1,ori_checkyear,ori_checkyear+1):
            #It still takes the number of days in which a birthday should lie an a date (in datetime format) to compare to
            comparison_date = comparison_date.replace(year = possibleyear)
            #Then the function returns a boolean statement about whether the DOB of the person lies within +/- days of the compariosn date
            checkdate = lower<=comparison_date<=upper
            if checkdate is True:
                break
        return checkdate

    def make_friendship(self,other_person):
        '''
        Defining a new method with the same code as the previously defined function in the dictionary based model with the same name.
        instead of accepting person as an argument, it instead refers to this instance of the class i.e self

        the argument other_person must also be an instance of the class person
        '''

        #this if statement prevents someone becoming friends with themselves (not possible)
        if self.name != other_person.name:
            #the following two if statement make sure that an id that is already in friendlist is not added again.
            if self.id not in other_person.friends:
                other_person.friends.append(self.id)
            if other_person.id not in self.friends:
                self.friends.append(other_person.id)

    def end_friendship(self,other_person):
        '''
        defining a new method with the same code as the previously defined function in the dictionary based model with the same name.
        instead of accepting person as an argument, it instead refers to this instance of the class i.e self

        the argument other_person must also be an instance of the class person
        '''

        #the following two if statement make sure that the id being removed is already in friendlist otherwise it cannot be removed.
        if self.id in other_person.friends:
            other_person.friends.remove(self.id)
        if other_person.id in self.friends:
            self.friends.remove(other_person.id)
                
    def find_my_friend(self,other_person):
        '''
        Defining a new method with the same purpose as the previously defined function 'find_friendX_inY' in the dictionary based model.
        instead of accepting person_X as an argument, it instead refers to this instance of the class i.e self

        This method takes the arguments self and other_person which both must be instances of the class person
        This method checks whether 'other_person' is a friend of this instance. 
        If this is True, then return the index of the first match of other_person.id from the self.friends list otherwose None will be returned.
        '''
    #The if statement checks whether the attribute id of the instance 'other_person' is in the Attribute friend of the self instance
    #If this is True, then return the index of the first match of other_person.id from the self.friends list otherwose None will be returned.
        if other_person.id in self.friends:
            return self.friends.index(other_person.id)

    def make_post(self,content,tagged=[]):
        '''
        defining a new method with the same code as the previously defined function in the dictionary based model with the same name.
        instead of accepting author as an argument, it instead refers to this instance of the class i.e self
        '''
    #use the instance of the class instead of the owner attribute
    #create a list that includes onle values in set of tagged that intersect with instances the attribute of friends
        mutual_list=list(set(tagged).intersection(self.friends))
        #Append new object(content) at the end of the instance attribute of the history
        self.history.append(content)
        post=(content,self.id,mutual_list)
        return post

    def __str__(self):
        '''
        defines a method which outputs a string according the the code below.
        This method is intended to create a string that represents the whole person defined in self
        '''

    #construct a string representation of this particular person using the following format:
    #         "id (their name, their date of birth) --> the ids of their friends separated by commas"
        return f'{self.id} ({self.name}, {self.DOB}) --> {str(self.friends)[1:-1]}'# delete the square brackets by excluding the first and last items in the sting ([ and ])





#Class is used to describe a collection of objects (SocialNetwork) that have the same properties and methods.
#It defines the properties and methods common to every object in the collection.
class SocialNetwork:
    """
    This class is used to define a whole social network (as oposed to a single perosn in the class person)
    Zecan Liu
    """
    #we need to declare it as global inside the function, and declare the variable days as a global variable
    global days

    def __init__(self,people_friendship_data,post_history):
        '''
        Every class should have a constructor __init__ to initalise the values of the attributes of the instance of that class.
        The self parameter is automatically set to reference the newly created object(a dictionary of people in the network and a list of posts) that needs to be initialized.

        This method takes the arguments 
            - self (the instance of the object)
            - people_friendship_data a list of strings which contain data for the social network in the layout defined in part 3
            - post_history which is a list of posts (as would be generated by the make_post method) listed in order of creation
        '''
    

        #initialise the SocialNetwork class instance and asign values to the attributes people and posts
        self.people={}
        self.posts=[]

        #total name list is a class variable created to append the string inputs (the default people's names and birthdays ) to in the later code
        #people count is a class variable initalised at 0 to keep track of the number of people in the social network
        total_name_list = []
        people_count = 0

        #the code below converts the people_friendship_data into individual people using a similar method to convert_lines_to_friendships in the dictionary based model
        #iterate over each line in the list of strings of people_friendship_data
        for each_line in people_friendship_data:
            #split the line by <-> to indicate each person in the data
            each_relationship = each_line.split('<->')
            #create a tempoary name list to store the data for each person in this line's data 
            temp_name_ls = []

            #iterate over each person in the line of data
            for each_person in each_relationship:
                #split the persons data by the delimiter ","
                person_info = each_person.split(',')
                #info_name is the name of ther person and is always the first element of the broken list
                info_name = person_info[0]
                #converting the birthday in string format to datetime format (alsways second element of list)
                info_bday=datetime.datetime.strptime(person_info[1], "%Y-%m-%d").date()
                #addng the info_name to the temp_name_ls
                temp_name_ls.append(info_name)
                
                #if statement to prevent duplicates of the same person being in the total_name_list
                if info_name not in total_name_list:
                    #As the info_name is added one by one, the count of people is also gradually assigned plus one
                    people_count += 1
                    total_name_list.append(info_name)
                    self.people[people_count] = Person(people_count,info_name,info_bday)

            # If the temp_name_ls is greater than one then there is a friendship that has to be made.
            # Use the ID of the first person (index of person 1 in the temp_name_ls + 1 (plus one as they key starts at 1 not 0)) and get thier corresponding dictionary found in the people attribute of this instance 
            # do the same for the second person (the second person in the temp_name_ls +1 (for the same reason above)) 
            # pass these two as arguments in the method make_friendship()
            if len(temp_name_ls) > 1:
                self.people[total_name_list.index(temp_name_ls[0])+1].make_friendship(
                    self.people[total_name_list.index(temp_name_ls[1])+1])

            #set the value of the attribute history for this person to be the post_history argument
            self.posts = post_history

    def add_person(self,name,date_of_birth):
        '''
        Defining a new method with the same code as the previously defined function in the dictionary based model with the same name.
        instead of accepting dict_of_people as an argument, it instead refers to this instance of the class i.e self
        '''

        #This if statement checks if the people attribute for this instance is equal to 0 i.e there is no one in the dictionary. 
        if len(self.people) == 0:
            #If this is true then set 1 for the new person's key and adding a value to it by making an instance of class person with name and date_of_birth.
            current_key = 1
            self.people[current_key] = person(current_key,name,date_of_birth)

        else:
            #when the people attribute for this instance is not empty, save the highest key value as current_key.
            current_key = list(sorted(self.people.keys()))[-1] + 1
            #The key for the new person is current_key + 1 and assign the corresponding value by making an instance of class person with name and date_of_birth.
            self.people[current_key] = person(current_key, name, date_of_birth)
         
    def get_person_by_id(self,find_id):
        '''
        Defining a new method with the same code as the previously defined function in the dictionary based model with the same name.
        instead of accepting dict_of_people as an argument, it instead refers to this instance of the class i.e self
        '''        

        #iterating over evey key in the people attribute for this instance (which is equal to the id value), the key is checked to see if it equal to the query id
        for key in self.people:
            #if it is the value of that key is returned
            if key == find_id:
                return vars(self.people[key])
                
    def make_birthday_posts(self,from_person_id,comparison_date):
        '''
        Defining a new method with the same code as the previously defined function in the dictionary based model with the same name.
        instead of accepting dict_of_people as an argument, it instead refers to this instance of the class i.e self
        
        This method aims to
            - determine the appropriate friends of from_person_id who have birthday within a week on either side of comparison_date (a datetime.date object)
            - then produce a birthday post for each of these friends
            - make this post appear in both the author's history attribute and the posts attribute of this SocialNetwork instance
        '''
        
        #make a friend list compling of the friends of the perosn with ID from_person_id by looking inside the instance's people attribue's and again inside that attribute's friends attribute.
        #male an empty list called bday_friends for later use
        friends_ls=self.people[from_person_id].friends
        bday_friends=[]

        #iterate over each friend in the friends_ls
        for friends_id in friends_ls:

            #if that person's DOB is within 1 week of the comparison date, append it to bday_friends
            if self.people[friends_id].birthday_within_X_days_of_Y(days,comparison_date):
                bday_friends.append(friends_id)
        
        #iterate over each friend in bday_friends
        for friends_id in bday_friends:
            #create a content sting including what will be said in the post
            #define what each element will be by creating another variable current_post
            #this has the id from the people attribute from this instance and uses it in the method make_post using the content_str and the list of friends in friend_id
            #finally append the newly made post to the posts attribute of this instance
            content_str = f"Happy birthday {self.people[friends_id].name}! Hope you have a good one!"
            current_post = self.people[from_person_id].make_post(content_str,[friends_id])
            self.posts.append(current_post)
            
    def __str__(self):
        '''
        This method construct a string representation of the entire social network
        '''

        #if statement to check if there is no people attribute for instance in the SocialNetwork
        if len(self.people)==0:
            #then just print string '' as none
            print_string=''
        else:
            #otherwise there should be one line for every person in the network (in increasing ID order)
            for everyone in range(len(self.people)):
                everyone += 1
                #it will be returned as a single string
                if everyone == 1:
                    #initalise the first line of test as below
                    #use the \n (escape character) to change to the next line
                    print_string=f'{self.people[everyone].id} ({self.people[everyone].name}, {self.people[everyone].DOB}) --> {str(self.people[everyone].friends)[1:-1]}\n'
                else:
                    #add onto the print string every time after that
                    print_string=f'{print_string}'+f'{self.people[everyone].id} ({self.people[everyone].name}, {self.people[everyone].DOB}) --> {str(self.people[everyone].friends)[1:-1]}\n'
        
        #return the completed print_string
        return print_string


if __name__ == "__main__":

    '''
    Vivian
    This is for the Q7
    to convert back to Q6 and run through the test file you need to comment out these lines
    '''
    days = 0

    inputstatement=['Fred,2022-02-01<->Jenny,2004-11-18',
                'Jiang,1942-09-16<->Sasha,1834-02-02',
                'Corey,2015-05-22',
                'Sasha,1834-02-02<->Amir,1981-08-11',
                'Saa,1844-02-02<->Corey,1981-08-11',
                'Saa,1844-02-02<->Fred,2022-02-01',
                'Fred,2022-02-01<->Jiang,1942-09-16',
                'Fred,2022-02-01<->Biao,2022-03-16',
                'Fred,2022-02-01<->Corey,2015-05-22',
                'Dai,2022-09-12<->Fred,2022-02-01']

    #Receive a social network structure as input.
    SampleNetWork=SocialNetwork(inputstatement,[])
    #Use the current year as part of the comparison date.
    current_year = datetime.datetime.now().year
    #Initialise the current date as the 1st of January
    current_date = datetime.date(current_year,1,1)
    #Stop at the end of the year day that is Dec 31th.
    end_date = datetime.date(current_year,12,31)

    #Use the while statement to run through all the days of the year,deal with upcoming birthdays of friends in each year
    while current_date <= end_date:
        for people_id in range(len(SampleNetWork.people)):
            SampleNetWork.make_birthday_posts(people_id + 1, current_date)#here just put a another funciton, it always starts from the zeroth item, so it needs to add one on people_id as the firt item

        #print(current_date)
        current_date += datetime.timedelta(days=1)

    #print off all the posts in the SocialNetwork instance in the order they appear
    for post in SampleNetWork.posts:
       print(post)
