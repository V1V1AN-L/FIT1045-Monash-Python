"""
This is the attemped code for task 8 _with_followers. 
The code is made up by orginal codes migrated from task 7 and new lines developed to enable the new features. 
Comments are added to only the additional codes for avoiding excessive replication
Wrote by: Vivian Liu 
"""
import datetime
people_dic={}
class Person:
    """
    Vivian Liu
    """
    global people_dic
    num_people=0

    def __init__(self,id:int,name,DOB):
        
        self.id=id
        self.name=name
        self.DOB=DOB
        self.friends=[]
        self.history=[]
        self.follows=[]
        self.owner_threadpost_id=0
        Person.num_people+=1
        people_dic[Person.num_people]=self

        
        
    def birthday_within_X_days_of_Y(self,days,comparison_date):
        
        upper = self.DOB + datetime.timedelta(days=days)
        lower = self.DOB - datetime.timedelta(days=days)
        
        ori_checkyear=self.DOB.year
        
        for possibleyear in (ori_checkyear-1,ori_checkyear,ori_checkyear+1):
            comparison_date = comparison_date.replace(year = possibleyear)
            checkdate = lower<=comparison_date<=upper
            if checkdate is True:
                break 
        return checkdate
        
    def make_follow(self,other_person):

        #this if statement prevents someone becoming friends with themselves (not possible)
        if self.name != other_person.name:
        
            self.follows.append(other_person.id)
    
    def make_friendship(self,other_person):
        
        if self.name != other_person.name:
        
            #the following two if statement make sure that an id that is already in friendlist is not added again.
            if self.id not in other_person.friends:
                other_person.friends.append(self.id)
            
            if other_person.id not in self.friends:
                self.friends.append(other_person.id)
     
    def end_friendship(self,other_person):

        #the following two if statement make sure that the id being removed is already in friendlist otherwise it cannot be removed.
            
        if self.id in other_person.friends:
            other_person.friends.remove(self.id)
        
        if other_person.id in self.friends:
            self.friends.remove(other_person.id)
                
    def find_my_friend(self,other_person):
        if other_person.id in self.friends:
            return self.friends.index(other_person.id)      

    def make_threaded_post(self,content,tagged,is_private):
        
        mutual_list=list(set(tagged).intersection(self.friends))
        
        self.owner_threadpost_id+=1
        Post(self.id,content,is_private,mutual_list,self.owner_threadpost_id)
        
        output=(content,self.id,mutual_list,is_private,[])
        
        self.history.append(output)
        return Post_dic[Post_id]
     
    def __str__(self):
        return (f'{self.id} ({self.name}, {self.DOB}) --> '
                f'FR {str(self.friends)[1:-1]} ==> Fo {str(self.follows)[1:-1]}')
    
Post_dic={}
Children_index_dic={}
Post_id=0

class Post:
    """
    A new class is set up here as post for each post created. 
    there are also several global variables assigned to serve for associated functions. 
    """ 
    def __init__(self,owner_id, content,is_private,tagged,owner_threadpost_id=0):
       
        global Post_dic,Children_index_dic,Post_id
        Post_id+=1
        #these instance variables are stored such that we could trace a post for 
        #its mother post, child post, post id, owner id, tagg, and privacy settings
        self.content=content
        self.tagged=tagged 
        self.children=[]
        self.childrenindex=[]
        self.owner_id=owner_id
        self.post_id=Post_id
        self.motherpost_id=0
        self.isprivate=is_private
        self.threaded_index=[owner_id,owner_threadpost_id]
        #the global variables are updated here for every post created. 
        Post_dic[Post_id]=self
        Children_index_dic[Post_id]=[]

    def makechildpost(self,childpost):
        global Post_id, Post_dic,Children_index_dic
        #this is to associate a post to a 'mother' post child list
        #stored in two different ways as child list for ids, and chidren for actual post class
        self.children.append(childpost)
        self.childrenindex.append(childpost.post_id)
       
        childpost.motherpost_id=self.post_id
        #also updating the global variable as well as define the mother post id for the given child post
        Children_index_dic[self.post_id].append\
            (childpost.post_id)
            
    def generatemessage(self):
        global Post_id, Post_dic,Children_index_dic
        #this is used to generate the base post tuple which for the children list only contains ids. 
        child_list=Children_index_dic[self.post_id].copy()
        output=(self.content,self.owner_id,self.tagged,\
                self.isprivate,child_list)
        return output
        
    
def find_original_threadpost(post):
    global Post_dic, Ori_post_id

    """
    This function is used to trace back on a post to find the very first thread post 
    """
    if post.motherpost_id!=0: #the top thread post does not have a 'mother' post id. which is default to 0
        find_original_threadpost(Post_dic[post.motherpost_id]) # if not the case re-iterate the current 'mother' post
    else:
        Ori_post_id=post.post_id   #if found, update a global variable as Ori_post_id (Global)
        
        
def element_find(child_list,Post_2print_List):
    global Post_dic,Children_index_dic
    """
    This function is to take one thread post and find all posts on its tree with id stored in a list
    """
    for element in child_list:
        if isinstance(Children_index_dic[element], list):
            Post_2print_List.append(element)
            element_find(Children_index_dic[element],Post_2print_List)
        else:

            Post_2print_List.append(element)

def maketuple(index,Print_Tuple_Dic,Thread_Post_id):
    global Post_dic
    
    """
    This function is used to make Tuple type for a given post which contains its children posts 
    (thread post, [(child 1, child 2, .....)])
    """
    motherpost_list=[]
    for post in index:
        if Post_dic[post].post_id!=Thread_Post_id:

            moother_id=Post_dic[post].motherpost_id
            motherpost=Post_dic[Post_dic[post].motherpost_id]
            location_index=motherpost.childrenindex.index(post)

            Print_Tuple_Dic[moother_id][4][location_index]=Print_Tuple_Dic[post]

            motherpost_list.append(Post_dic[post].motherpost_id)

    if len(motherpost_list)>0 and motherpost_list[0]!=Thread_Post_id:
        maketuple(motherpost_list,Print_Tuple_Dic,Thread_Post_id)
        


def print_thread_post(Thread_Post_id,bottom_layer_index=[],Print_Tuple_Dic={}):
    """
    This function is to adds up all layers of posts back to the original thread post
    """
    global Post_dic,Children_index_dic
    
    Post_2print_List=[Thread_Post_id]   
    Thread_child_list=Children_index_dic[Thread_Post_id]        
    element_find(Thread_child_list,Post_2print_List)

    for post in Post_2print_List:
        Print_Tuple_Dic[post]=Post_dic[post].generatemessage()
        if len(Post_dic[post].childrenindex)==0:
            bottom_layer_index.append(post)

    maketuple(bottom_layer_index,Print_Tuple_Dic,Thread_Post_id)

    return Print_Tuple_Dic[Thread_Post_id]        
        



def add_child(threaded_post,content,new_post_owner,tagged,is_private):
    global people_dic,Children_index_dic
    """
    This function is the actual add_child function that performs the task by fist creating a child post 
    making it associated with the 'mother post'
    adding it to the 'mother post' history
    """   
    mother_content=threaded_post.content    
    mother_post_owner=people_dic[threaded_post.owner_id]
    
    if new_post_owner.id not in mother_post_owner.friends +[threaded_post.owner_id] \
        and threaded_post.isprivate is True:
        None
    elif new_post_owner.id not in mother_post_owner.friends +[threaded_post.owner_id] \
        and threaded_post.isprivate is False and mother_post_owner.id not in new_post_owner.follows:
        None
    
    else:
  
        for post_key in Post_dic.keys():
            post_content=Post_dic[post_key].content
            if post_content ==mother_content:
                motherpost=Post_dic[post_key]

        mutual_list=list(set(tagged).intersection(people_dic[new_post_owner.id].friends))       
        childpost=Post(new_post_owner.id,content,is_private,mutual_list) 
        motherpost.makechildpost(childpost)
        
        find_original_threadpost(motherpost)
        
        original_threadpost=Post_dic[Ori_post_id]
         
        history_updateindex=original_threadpost.threaded_index[1]
        updated_post_tuple=print_thread_post(Ori_post_id)
        people_dic[original_threadpost.threaded_index[0]].history[history_updateindex-1]=updated_post_tuple
        
    

class SocialNetworkWithFollowers:
    global days


    def __init__(self,people_friendship_data,post_history):
        self.people={}
        self.posts=[]
        total_name_list = []
        people_count = 0
        for each_line in people_friendship_data:
            
            split_crietria_list=['-->','<->','<--']
            R_Arrow_indicate=1 if '>' in each_line else 0
            L_Arrow_indicate=3 if '<' in each_line else 0
            Num_Dash=each_line.count('-')
            
            order_index=[0,1] if R_Arrow_indicate==1 else [1,0]
            
            Indication=R_Arrow_indicate+L_Arrow_indicate if Num_Dash==6 else 2           
         
            split_crietria=split_crietria_list[Indication-1]
            each_relationship=each_line.split(split_crietria)
            
            temp_name_ls = []
            
            
            for each_person in each_relationship:
        
                person_info = each_person.split(',')
                info_name = person_info[0]
                info_bday=datetime.datetime.strptime(person_info[1], "%Y-%m-%d").date()
                temp_name_ls.append(info_name)       
         
                if info_name not in total_name_list:
                    people_count += 1
                    total_name_list.append(info_name)
                    self.people[people_count] = Person(people_count,info_name,info_bday)
                    
            if len(temp_name_ls) > 1:
                
                if split_crietria=='<->':
                    self.people[total_name_list.index(temp_name_ls[0])+1].make_friendship(
                        self.people[total_name_list.index(temp_name_ls[1])+1])
                
                else:
                    
                    self.people[total_name_list.index(temp_name_ls[order_index[0]])+1].\
                        make_follow(self.people[total_name_list.\
                                                index(temp_name_ls[order_index[1]])+1])
                
                
            self.posts = post_history


    def add_person(self,name,date_of_birth):
        
        if len(self.people) == 0:
            current_key = 1
            self.people[current_key] = Person(current_key,name,date_of_birth)
        else:
            current_key = list(sorted(self.people.keys()))[-1] + 1
            self.people[current_key] = Person(current_key, name, date_of_birth)
         
    def get_person_by_id(self,find_id):

        for key in self.people:
            if key == find_id:
                return vars(self.people[key])
        
            
    def make_birthday_posts(self,from_person_id,comparison_date):
        
        friends_ls=self.people[from_person_id].friends
        bday_friends=[]
        
        for friends_id in friends_ls:
            if self.people[friends_id].birthday_within_X_days_of_Y(days,comparison_date):
                bday_friends.append(friends_id)
        
        for friends_id in bday_friends:
            
            content_str = f"Happy birthday {self.people[friends_id].name}! Hope you have a good one!"
            current_post = self.people[from_person_id].make_post(content_str,[friends_id],True,[])
            self.posts.append(current_post)
               
            

    def __str__(self):
        if len(self.people)==0:
            print_string=''
        else: 
            for everyone in range(len(self.people)):
                everyone += 1
                if everyone == 1:
                    print_string=(f'{self.people[everyone].id} ({self.people[everyone].name}, '
                    f'{self.people[everyone].DOB}) --> Fr{str(self.people[everyone].friends)}'
                    f' ==> Fo{str(self.people[everyone].follows)}\n')
                else:
                    print_string=(f'{print_string}'+f'{self.people[everyone].id} '
                    f'({self.people[everyone].name}, {self.people[everyone].DOB}) --> '
                    f'Fr{str(self.people[everyone].friends)} ==> '
                    f'Fo{str(self.people[everyone].follows)}\n')
        
        return print_string


