"""
Created on Wed May 18 11:36:54 2022

@author: Vivian Liu
"""

import random
import itertools

class Character:
    """
    Character class for representing an individual character (there can be multiple characters in a story)
    Author: Rui Qin
    Modified: Vivian Liu
    """
    #creating a class variable (constant for all instances of Character) which is a list that tells us the 3 types of attributes
    attribute_ref_ls = ['acumen','body','charm']
    #creating a class variable (constant for all instances of Character) which is a dictionary.
    #the dictionary has the Key referring to the abbreviation and the value referring to one of the 6 skills
    skill_dict  =  {'Di': 'diplomacy',
                    'In': 'investigation',
                    'Me': 'medicine',
                    'La': 'language',
                    'Ac': 'acrobatics',
                    'Cr': 'craft'}
    #creating a class variable (constant for all instances of Character) which is a dictionary.
    #This dictionary has the key as the possible outcomes (overwhelming success (++), success(+), failure(-), overwhelming failure(--))
    #the values of those outcomes are the intervals in which the score must be within to have the corresponding outcome
    #   eg. for a success the score must be between 0 and 2 (inclusive)
    score_rule={'++':[3,float('inf')],
                '+':[0,2],
                '-':[-3,-1],
                '--':[float('-inf'),-4]}
    # character_count=0
    # character_dict={}
    def __init__(self,string_input):
        '''
        This constructor initializes that values for this character class
        It requires teh arguments:
            - self
            - sting_input (character information set out in a list (see supporting information 2: characters))
        This will set up all the information required in the Character class in a usable format
        '''

        #attribute_score_ls is a list holding the scores for each attribute as integers.
        #it is created by splitting the second element of string_input by the default (whitespace " ")
        #then iterating over each element and if there is a digit join it to the empty string otherwise a whitespace is joined
        #each element is then made an integer and the list is complete
        attribute_score_ls = [int(attribute_score) for attribute_score in
                            ''.join((element if element.isdigit() else ' ')
                                    for element in string_input[1]).split()]

        #this for loop along with the enumerate function tracks which number(in attribute_score_ls) belong to which index of that list
        #if the number is not in the range 1-4 a ValueError is raised
        for count, number in enumerate(attribute_score_ls):
            if number <= 0 or number >= 5:
                raise ValueError(f'invalid value for {self.attribute_ref_ls[count]};'
                                f' {number} is not in the range 1 to 4')

        #This if statement checks whether the sum of the values in attribute_score_ls is equal to 7
        #If they are not a ValueError is raised
        if sum(attribute_score_ls) != 7:
            raise ValueError(f'{string_input[1]} is invalid, sum of attributes does not equal 7')

        #create a list (proficient_skills)
        #first, string_input[2] is split by the default (whitespace " ")
        #next only the elements with "*" present are selected
        #the selected elements have the "*" removed by splitting at "*" and selecting the first element
        #using each element (with * replaced with nothing) of the result of splitting the string_input[2] (will all the skills) using a whitespace " " (the default)
        proficient_skills = [element.split('*')[0]
                                for element in string_input[2].split() if "*" in element]
        #check if there is one and only one proficient skill, if not then raise a ValueError
        if len(proficient_skills)!=1:
            raise ValueError(f'{string_input[2]} is invalid; exactly one proficiency asterisk expected')
        #check if the skills given are the same as those expected
        #This is done by checking the skills in string_input[2] (when split by whitespace and "*" removed)
        #correspond to at least one of the keys in skill_dict
        #if not raise a ValueError
        elif set([element.split('*')[0] for element in string_input[2].
                    split()])!= set(Character.skill_dict.keys()):
            raise ValueError(f'{string_input[2]} is invalid; unexpected skill name given')

        #defining the objects of the instance

        #name is the same as the first index of the string_input
        self.name = string_input[0]
        #acumen score is the first element of the attribute_score_ls
        self.acumen = attribute_score_ls[0]
        #body score is the second element of the attribute_score_ls
        self.body = attribute_score_ls[1]
        #charm score is the third element of the attribute_score_ls
        self.charm = attribute_score_ls[2]
        #proficient skill is the first element of the proficient_skills list.
        self.proficient = Character.skill_dict[proficient_skills[0]]
        #setting up a dictionary where keys are either the name of the attribute or
        #skill and the value is the corresponding score for them
        self.skill_attri_score_dict={'acumen':self.acumen,
                            'body':self.body,
                            'charm':self.charm,
                            'diplomacy': self.charm,
                            'investigation': self.acumen,
                            'medicine': self.acumen,
                            'language': self.charm,
                            'acrobatics': self.body,
                            'craft': self.body}

        #adding 2 to the skill that is in proficient.
        self.skill_attri_score_dict[self.proficient]=self.skill_attri_score_dict[self.proficient]+2
        # Character.character_count+=1
        # Character.character_dict[f'C{Character.character_count}']=self

    def get_acumen(self):
        '''
        a method to retrieve the acumen score of a Character instance
        '''
        return self.acumen

    def get_body(self):
        '''
        a method to retrieve the body score of a Character instance
        '''
        return self.body

    def get_charm(self):
        '''
        a method to retrieve the charm score of a Character instance
        '''
        return self.charm

    def get_name(self):
        '''
        a method to retrieve the name of a Character instance
        '''
        return self.name

    def get_proficient(self):
        '''
        a method to retrieve the score for the proficient skill of a Character instance
        '''
        return self.proficient


    def make_check(self,skill_or_attribute_name,difficulty,override_random=None):
        '''
        a method to check the outcome for a Character instance in a scene
        this method takes the arguments
            - self
            - skill_or_attribute_name: the full name of the skill or attribute that is required for the task as a string
            - the difficulty of the task (an integer)
            - an override score (set at None as default) which must be an integer

        it will return one of 4 outcomes:
            "++" (an overwhelming success)
            "+" (a success)
            "-" (a failure)
            "--" (an overwhelming failure)
        '''

        #base score is the score that that character has for that attribute or skill
        #this score is retrieved form the dictionary skill_attri_score_dict in the character instance
        base_score=self.skill_attri_score_dict[skill_or_attribute_name]
        #if statement is in place to make an add_score variable equal to the randomised element of the score if override_random == None
        #else statement is in place to make an add_score variable equal to the override_random if it is not a None (i.e it is an integer).
        if override_random == None:
            add_score=random.randint(-1, 1)+random.randint(-1, 1)+random.randint(-1, 1)
        else:
            add_score=override_random
        #final_score is equal to the base_score + the add_score
        final_score=base_score+add_score-difficulty
        #This for loop iterates over each of the lists(named the_interval) in score_rule
        for the_key, the_interval in self.score_rule.items():
            if the_interval[0]<=final_score<=the_interval[1]:
                break
        #the return value is the key of the corresponding interval which final score is within.
        return the_key

    def __str__(self):
        '''
        this is a string representation of the instance in class Character
        it returns a string in the format:
            "name [A(acumen_score) B(body_score) C(charm_score)] is proficient in (proficient_skill)"
        '''

        return f"{self.name} [A{self.acumen} B{self.body} C{self.charm}] is proficient in {self.proficient}"



class Option:
    """
    Option class for representing an single option in a given scene (each scene can have multiple options).

    Author: Vivian Liu
    """

    def __init__(self,option_id,skillattri,option_descrip,next_scenescore_dict):
        '''
        constructor to initialise an instance of class Option

        takes the arguments
            - self
            - option_id (this option's id in a sting format "[num]." e.g. "1.")
            - skillattri (this option's skill or attribute required followed by its difficulty in a string format "skill/attri [num]" )
                    * e.g. "diplomacy 5"
            - option_descrip (this option's description in a string format "text")
                    * e.g "use their diplomacy skills to ask for a freebie"
            - next_scenescore_dict (a dictionary where:
                                        - the key is the integer value of the outcome (eg -2)
                                        - the value is the sting of the outcome (eg "++[num]"))
        '''
                #initialise the id of the option for this instance as option_id
        self.id=option_id
        #initialise the check_skillattri as a boolean statement checking if the length is non-zero
        #this checks whether there is a skill or attribute associated with the option
        self.check_skillattri= len(skillattri)!=0
        #if check_skillattri is True (there is skill attribute information)
        if self.check_skillattri:
            #initialise difficulty as the integer part of the string (the second part after splitting with whitespace)
            self.difficulty=int(skillattri.split()[1])
            #initialise skillattri_name as the first part of the string after splitting with whitespace
            self.skillattri_name=skillattri.split()[0]

        #if there is no information in skillattri
        else:
            #set difficulty to 0
            self.difficulty=0
            #set skillattri_name to an empty string
            self.skillattri_name=''
        #set the description as option_descrip
        self.description=option_descrip
        #set the next_scene_dict as the next_scenescore_dict
        self.next_scene_dict=next_scenescore_dict

        #finding the start and end indecies for the character element that must be replaced in the option description
        chara_id_indexstart=[index+2 for index, chara in enumerate(self.description) if chara == '{']
        chara_id_indexend=[index for index, chara in enumerate(self.description) if chara == '}']

        #initialise an empty list to stor the ids of the characters that will have to take the places of the replaceable elements
        chara_id_list=[]
        #initialise the active character as an empty list
        self.active_chara=[]

        #if there are replaceable elements in the option description
        if chara_id_indexstart!=[]:

            #iterate over the index for the length of the chara_id_indexstart
            for index in range(len(chara_id_indexstart)):
                #create a temprary id to store the id (integer) of the character that will replace the replaceable element
                temp_id=int(self.description[chara_id_indexstart[index]:chara_id_indexend[index]])
                #append this to the chara_id_list
                chara_id_list.append(temp_id)
            #append the first character id in the character id list as the active Character in this instance
            self.active_chara.append(chara_id_list[0])

    def __str__(self):
        printid=self.id.replace('.', '')
        return ('the option info is as below\n' + f'this is option {printid}\n'+
                f'option description is "{self.description}"\n'+
                f'relying on "{self.skillattri_name}" for a difficulty of {self.difficulty}\n'
                f'possible next scenes are {self.next_scene_dict}')

def option_info_splitter(individual_option):
    '''
    This function takes the arguments:
        - individual_option is a string in the format:
            * for a non-ending option = "1. [skillOrAttribute Difficulty] text --ID -ID +ID ++ID"
            * for an ending option = "2. text --ID -ID +ID ++ID"

    This function returns:
        - option_id (a sting in the format "[num].")
        - skillattri (a string in the format "attribute [num]")
        - option_descrip (a string of text that explains the story option)
        - next_scenescore_dict (a dictionary where:
                                        - the key is the integer value of the outcome (eg -2)
                                        - the value is the sting of the outcome (eg "++[num]"))
        - next_scene_id_str (a string of next outcomes that are possible ordered from best to worst outcomes)
    '''

    #option_id_locindex is the index where the '.' is in the string individual_option
    option_id_locindex=individual_option.find('.')

    #option_id is a variable that hold the string with the option id in the form "[num]."
    option_id=individual_option[0:option_id_locindex+1]

    #if statement finds whether the option is an ending or non ending option
    if individual_option[option_id_locindex+2] == '[':
        #if it is a non ending (i.e has the [attribute [num]]) option:
        #       select the string that is inside the []
        skillattri=individual_option[individual_option.find('[') +1 : individual_option.find(']')]
        #option_descrip_index holds the index where the text for the option description begins (2 indices past the "]" character)
        option_descrip_index=individual_option.find(']')+2
    else:
        #if it is not an ending option
        #skillattri is an empty string
        skillattri=''
        # option_descrip_index begins from 2 indices past the "." character
        option_descrip_index=individual_option.find('.')+2

    #next_scene_index is a variable that holds the indicies of where each next scene outcome begins (where the special characters listed begin)
    next_scene_index=[index for index, content in enumerate(individual_option)
                        if any(element in ['+','-','++','--'] for element in content)]

    #option_descrip is a variable that holds a string staring from the option_descrip_index
    #and ends at the lowest index for the next_scene_index - 1 (to remove whitespace)
    option_descrip=individual_option[option_descrip_index:min(next_scene_index)-1]

    #create a temporary scene id list which includes all the ids of the possible outcomes of these scene in the following format:
    #   - ["[success or failure characters][num]","[success or failure characters][num]"]
    #        * e.g ["++2","-3"]
    temp_scene_id=individual_option[min(next_scene_index)::].split()

    #create an empty dictionary for the information about the next possible scenes
    next_scenescore_dict={}

    #for loop to iterate over each of the strings in temp_scene_id
    for scene_id in temp_scene_id:

        #add to the dictionary (next_scenescore_dict) with key being the sum of:
        #    - the count of '+'s in the sting
        #    - the  count of '-'s in the string * -1
        #The corresponding value for this key is the scene_id (eg "++2")
        next_scenescore_dict[scene_id.count('+')+(-scene_id.count('-'))]=scene_id

        #if statement to check if the number of outcome values ('+'s or '-'s) is less than 2
        #if it is not a ValueError is raised
        if scene_id.count('+')+scene_id.count('-')>2:
            raise ValueError(f'check the scene input, {scene_id} is out of range of [++,+,-,--]')

    #create a keylist which is a list of all the keys in next_scenescore_dict (the keys will be values from -2 to 2 excluding 0)
    keylist=list(next_scenescore_dict.keys())
    #the list is sorted in reverse so that they are smallest to largest
    keylist.sort(reverse = True)
    #a list is created called next_scene_id and the items in the list will be ordered from most to least successful
    next_scene_id=[next_scenescore_dict[key] for key in keylist]
    #initalise an empty string
    next_scene_id_str=''
    #this for loop adds to the sucess indicator into a string in the correct order
    for pos,s_id in enumerate(next_scene_id):
        s_id=' '+s_id if pos!=0 else s_id
        next_scene_id_str=next_scene_id_str+s_id
    #return the following values in order:
    return option_id,skillattri,option_descrip,next_scenescore_dict,next_scene_id_str

class Scene:
    """
    Scene class for representing an individual scene that contains a set of options
    Author: Vivian Liu
    """

    def __init__(self,scene_id,scene_description,scene_index,temp_option_ls):
        '''
        This constructor initialise the Scene instance with values.

        The initialiser requires the values:
            - scene_id is a string that holds the scene's id (either "S", "[num]", "E")
            - scene_description is a string that holds the text describing the scene
            - scene_index is a tuple that holds the indices for where to split the scene information in the format:
                * (start of scene index, middle of scene index, end of scene index) or another way to describe it is:
                *  (index start "----", index "====", index end "----") for a single scene
            - temp_option_ls is a list that holds each of the options in the scene (starts from "====" and ends at "----")

        This sets up an instance of the class Scene
        '''

        #initializing the argument information for this instance
        self.id=scene_id
        self.description=scene_description
        self.index=scene_index
        self.options_ls=temp_option_ls

        #initializing an empty dictionary for the options in the scene
        self.options_dict={}

        #chara_id_indexstart is that starting index for when {C[num]} is found in the description.
        #it indexes the first digit value after the "{"
        chara_id_indexstart=[index+2 for index, chara in enumerate(self.description) if chara == '{']

        #chara_id_indexend is that ending index for when {C[num]} is found in the description.
        #it indexes the position of the "}" character
        chara_id_indexend=[index for index, chara in enumerate(self.description) if chara == '}']

        #initialise an empty list to store each character number required for the description string
        chara_id_list=[]

        #if statement to check if any character names must be added to the description
        if chara_id_indexstart!=[]:
            #if there are character names required
            #use for loop to iterate over each index in chara_id_indexstart
            for index in range(len(chara_id_indexstart)):

                #collect the digits in the string and convert into an integer by 
                #selecting the characters from chara_id_indexstart to chara_id_indexend
                temp_id=int(self.description[chara_id_indexstart[index]:chara_id_indexend[index]])

                #append this integer to the chara_id_list
                chara_id_list.append(temp_id)
            #sort these numbers from lowest to highest
            chara_id_list.sort()
            #define this instance's chara_id_list as a list where any double ups of the values is removed so only one of each integer is in the list
            self.chara_id_list = [chara_id for chara_id,_ in itertools.groupby(chara_id_list)]
        
        else:
            #if there are no characters needed hence initialise chara_id_list as an empty list
            self.chara_id_list=[]
        #for loop to enumerate (index along with iteration) for each of the options in options_ls for this instance.
        for index, individual_option in enumerate(self.options_ls):
            #define each of the variables as the return from running the option_info_splitter() function on the current option
            option_id,skillattri,option_descrip,next_scenescore_dict,next_scene_id_str = option_info_splitter(individual_option)         
            
            #initialise a options_dict (dictionary) with the key being the option_id with "." removed.
            #The value of teh item will be the result of running the option class with the information extracted form the line above
            self.options_dict[int(option_id.replace('.',''))] = Option(option_id,skillattri,option_descrip,next_scenescore_dict)

            #remove the whitespaces of skillattri so it looks like "attribute[num]"
            skillattri=skillattri.replace(' ','')
            #reformat it into the expected output by adding a whitespace to the front (if attribute is pesent)
            #if the skillattri is an empty string (no attribute in this option) return that empty string
            skillattri=' '+skillattri if len(skillattri)!=0 else skillattri
            #for the first option (index 0) initialise this instance's print_out with the below string
            if index ==0:
                self.print_out=f' [{option_id}{skillattri} {next_scene_id_str}]'
            #for all other options (not the first option) concatenate the next option onto the the already initialized sting called print_out
            else:
                self.print_out=self.print_out+f' [{option_id}{skillattri} {next_scene_id_str}]'
        #an if statement to indicate if there are no options in the list the print_out variable should be an empty string
        #otherwise it should be what has been constructed previously
        self.print_out='' if len(self.options_ls)==0 else self.print_out

    def __str__(self):
        '''
        a string instance of the class Scene is defined as the following string in the format
        "scene1_id > [1. skill_or_attribute ++id +id -id --id] [...] [n. skill_or_attribute ++id +id -id --id]"
        '''
        return (f'{self.id} >' + self.print_out)
   


class Story:
    """
    Story class for representing a story(game) that contains different scenes each with different options
    Author: Vivian Liu
    """
    #set an class variable called scoring reference to keep track of the numerical values given to the level of success in dictionary form
    scene_score_ref={2:'++',1:'+',-1:'-',-2:'--'}
    def __init__(self,story_text,char_text):
        '''
        This constructor initializes this instance of the story class with the required information.
        it requires three arguments
            - self
            - story_text (a list of strings in the format seen in supporting information 1)
            - char_text (a list of strings in the format seen in supporting information 2)
        '''

        #checking if the argument story_text is in the correct list format. If it is not raise a ValueError
        if isinstance(story_text, list)==False:
            raise ValueError('wrong input received when creating the story -'+
                                ' the story text input must be a list')

        #checking if the argument char_text is in the correct list format. If it is not raise a ValueError
        if isinstance(char_text, list)==False:
            raise ValueError('wrong input received when creating the story -'+
                                ' the char_text input must be a list')

        #collecting the enumerated indecies for the splitter string "----" that highlight the separation between scenes
        scene_sep_indice = [index for index, element in enumerate(story_text) if element == '----']

        #collecting the enumerated indicies for the in scene splitter '====' highlighting the separation between scene information and scene options
        inscene_indice = [index for index, element in enumerate(story_text) if element == '====']

        #selecting those scene splitters that represent the start of a scene
        #these include every second scene_sep_indice starting from the first (index 0)
        scene_start_indice=scene_sep_indice[0::2]

        #selecting those scene splitters that represent the end of a scene
        #these include every second scene_sep_indice starting from the second (index 1)
        scene_end_indice=scene_sep_indice[1::2]
        #an if statement to check if there is any formatting issues such as
            #   - if there is an uneven number scene separators
            #   - if there are not exactly half as many scene_start_indicie as there are scene_sep_indicie
            #   - if the number of start and end separators is not equal
            #   - if the number of inscene_indicie is not equal to the number of scene_start_indicies
        if len(scene_sep_indice) % 2!=0 or \
            len(scene_start_indice)!=len(scene_sep_indice)/2 or\
            len(scene_start_indice)!=len(scene_end_indice) or\
            len(inscene_indice)!=len(scene_start_indice):
            #if any of these raise a false, raise a ValueError saying that there has been a problem with the story_text input
            raise ValueError('something wrong with the story list input -'+
                                ' check divider ---- and ==== locations')

        #initializing a chara_dict and scene_dict for this instance to keep track of what is in the story
        self.chara_dict={}
        self.scene_dict={}
        #iterating over the number of items in the scene_end_indice list
        for num_scene in range(len(scene_end_indice)):

            #create a temporary index that holds the indecies that are relevant to this scene
            #because all lists are the same length and same format, each scene should have the same index in each of the following lists
            #   - scene_start_indice
            #   - scene_sep_indice
            #   - scene_end_indice
            #therefore using the index value num_scene the start, separator and end indicies can be simultaneously extracted and placed in a tuple
            temp_index=(scene_start_indice[num_scene],inscene_indice[num_scene],scene_end_indice[num_scene])

            #a temporary scene description is made to hold the description lines for this particular scene
            #the descriptions:
            #   - start 2 elements away from the start separator (temp_index[0]+2)
            #   - end at the inscene separator (temp_index[1])
            # starting with a newline whitespace each line within those explained above are added as a sting
            temp_des='\n'.join(line for line in story_text[temp_index[0]+2:temp_index[1]])

            #a temporary id holds the current scene's id found 1 element after the start separator (temp_index[0]+1)
            temp_id=story_text[temp_index[0]+1]

            #a temporary options list is creates to hold all of the options in this particular scene
            #the options:
            #   - start 1 elements away from the inscene separator (temp_index[1]+1)
            #   - end at the end scene separator (temp_index[2])
            temp_option_ls=story_text[temp_index[1]+1:temp_index[2]]

            #this if statement checks if there is an issue with the scene id
            #if it is absent a ValueError is raised
            if temp_id =='':
                raise ValueError(f'a scene ID is missing for scene number {num_scene+1}')

            #adding to the Story instance's variable scene_dict, the scene information extracted in temporary variables are
            #passed into the Scene class. The key of the dictionary will be the id of the scene and the value will be the instance of the Scene class created
            self.scene_dict[temp_id]=Scene(temp_id,temp_des,temp_index,temp_option_ls)

        #create a list of enumerated indicies for the separators '----' in the char_text + 1 so the actual separator is not included
        chara_start_indice = [index+1 for index, element in enumerate(char_text) if element == '----']
        #because we need to capture the fist character and the formatting does not have a '---' separator at the start of the char_text,
        #insert 0 at index 0.
        chara_start_indice.insert(0,0)

        #the number of characters in the char_text will be the length of the chara_start_indice
        chara_count=len(chara_start_indice)

        #This for loop iterates over the range of chara_count
        for chara_num in range(chara_count):
            #create a current character variable that holds all the information between the start indicie and the start indicie +3
            curr_chara=char_text[chara_start_indice[chara_num]:chara_start_indice[chara_num]+3]
            #update chara_dic with the key being the chara_num +1 (so it starts at 1 not 0).
            #the value of that key will be an instance of the Character class using curr_chara as the argument
            self.chara_dict[chara_num+1]=Character(curr_chara)

        #initalising the active scene as the start scene with scene_id as "S" and active character to be the first (key = 1)
        self.active_scene=self.scene_dict['S']
        self.active_chara=self.chara_dict[1]

    def get_scene_id(self):
        '''
        This method uses self as an argument to retrieve and return the active scene's id in a string format
        eg "S" or "3"
        '''
        return self.active_scene.id

    def show_current_scene(self):
        '''
        This method takes the argument self
        It uses the current instance of the Story class to print out all the relevant information in a scene in the format:
            "Scene [num]
            scene description
            ====
            [num]. option description
            [num]. option description
            ----"
        if a description requires the use of a character's name, that name is used.
        '''

        #collecting what will be in the scene description
        description_print=self.active_scene.description

        #collecting the index of where the chatacter's name must be inserted by
        #enumerating for all "{" charcters in the description_print
        chara_id_indexstart=[index for index, chara in
                                enumerate(description_print) if chara == '{']

        #collecting the index + 1 of where the chatacter's name must be inserted by
        #enumerating for all "}" charcters in the description_print
        chara_id_indexend=[index+1 for index, chara in
                            enumerate(description_print) if chara == '}']

        #if statement to say if there are character names that need to be inserted into the description
        if chara_id_indexstart!=[]:

            #for the number of start indicies, collect the content that must be replaced in a list
            replace_content=[description_print[chara_id_indexstart[index]:chara_id_indexend[index]]
                                for index in range(len(chara_id_indexstart))]

            #collect the character id that will be used in order to replace the {C[num]} with the character name for all {C[num]} in the string in a list
            replace_id=[int(description_print[chara_id_indexstart[index]+2:chara_id_indexend[index]-1])
                        for index in range(len(chara_id_indexstart))]

            #iterate over the length of the replace ids
            for index in range(len(replace_id)):
                #for each index replace the old content with the new content (using the get.name() method of the character instance corresponding to the chara_dict)
                description_print=description_print.replace(
                    replace_content[index],self.chara_dict[replace_id[index]].get_name())

        #creating the first part of the text that will be printed called the description_block in the format:
        #   - "Scene [num]
        #      description text
        #      ===="
        description_block=f'Scene {self.active_scene.id}'f'\n{description_print}'f'\n===='

        #create en empty string that will hold the text for the options that must be printed
        option_descrip_block=''

        #iterate over the option_key in the options dictionary which is in the active scene of the current instance.
        for option_key, option in self.active_scene.options_dict.items():
            # each of the options will get a description_print which is the description attribute of the current option
            option_description_print=option.description
            #getting the start index of the block that must be replaced with a character name from the option_description_print and put it in a list
            op_chara_id_indexstart=[index for index, chara in
                                    enumerate(option_description_print) if chara == '{']

            #getting the end index + 1 of the block that must be replaced with a character name from the option_description_print and put it in a list
            op_chara_id_indexend=[index+1 for index, chara in
                                    enumerate(option_description_print) if chara == '}']

            #if there are parts that do need to replace enter the if statement
            if op_chara_id_indexstart!=[]:
                #select the content that must be replaced. i.e {C[num]} for the whole string
                op_replace_content=[option_description_print[op_chara_id_indexstart[index]:op_chara_id_indexend[index]]
                                    for index in range(len(op_chara_id_indexstart))]

                #get the [num] value as an integer so that it can be used to reference to the character's name that will do the replacing
                op_replace_id=[int(option_description_print[op_chara_id_indexstart[index]+2:op_chara_id_indexend[index]-1])
                            for index in range(len(op_chara_id_indexstart))]

                #for looop to iterate over all the {C[num]} in the string
                for index in range(len(op_chara_id_indexstart)):

                    #replace what needs replacing with the corresponding name
                    option_description_print=option_description_print.replace(
                        op_replace_content[index],self.chara_dict[op_replace_id[index]].get_name())

                #delete these variables so that the loop will act normally when iterating (reset these lists)
                del op_replace_content,op_replace_id

            #concatenate the option.id and the option_description_print to the final option_descrip_block
            option_descrip_block=option_descrip_block+f'\n{option.id} {option_description_print}'

            #delete these variables so that the loop will act normally when iterating (reset these lists)
            del option_description_print,op_chara_id_indexstart,op_chara_id_indexend

        #once iteration is complete add a newline whitespace followed by ---- as per the formatting requirements
        description_block=description_block+option_descrip_block+'\n----'

        #return the completed description_block
        return description_block

    def select_option(self,option_number,override=None):
        '''
        this method takes the arguments
            - self
            - option_number(an integer from 1 to n (n being the number of options available in a scene))
            - override (an integer to add to the option number if a non-None value is given) the default value being None
        this method selects an option in a scene and moves the story to the next stage
        '''

        #this if statement checks if the game is over, if it is, a StopIteration is raised ending the game
        if self.active_scene.id[0]=='E':
            raise StopIteration('the game is over')

        #if it is not the ending scene
        else:
            #set the current option taken as the corresponding option from the active scene
            current_option=self.active_scene.options_dict[option_number]

            #this if statement is to check if there is an action that can be taken
            if current_option.skillattri_name!='':

                #if there is an action to be taken, set expected_outcome to the current Story instance's active character's make check function
                #use the current option's stored data (skillattri, difficulty, override) as the arguments
                expected_outcome=self.active_chara.make_check\
                                (current_option.skillattri_name,current_option.difficulty,override)

                #current outcome is a numerical value set as the '+' characters added and
                #the '-' characters subtracted from the expected_outcome calculated above
                curr_outcome_score=expected_outcome.count('+')+(-expected_outcome.count('-'))

            #if there is no action to be taken automatically set the curr_outcome to the worst possible outcome score (-2)
            else:
                curr_outcome_score=-2

            #score_ref is a list of scores that relate to the success of the outcome ranging form 2 to -2 excluding 0
            score_ref=list(current_option.next_scene_dict.keys())

            #check_fit_ls is the absolute value of the the current outcome minus the score reference that we have just extracted.
            #this will help find which of the possible outcomes is closest the current outcome
            check_fit_ls=[abs(curr_outcome_score-x) for x in score_ref]

            #the_key is a variable that holds the score of the best option which is found by
            #index of the lowest value in check_fit_ls (the most similar outcome )
            the_key=score_ref[check_fit_ls.index(min(check_fit_ls))]

            #the_nextscene_key is set to the "++[num]" of the most similar outcome by using the_key as the key for the next_scene_dict
            the_nextscene_key=current_option.next_scene_dict[the_key]

            #replace the digit with whitespace
            the_nextscene_key=the_nextscene_key.replace(self.scene_score_ref[the_key],'')

            #set the active scene to the newly selected scene from the scene dictionary
            self.active_scene=self.scene_dict[the_nextscene_key]

    def start_game(self):
        '''
        a method that initialises the start of the game
        takes the argument self
        prints a string in the format using the show_current_scene() method

        "
        Scene [id]
        [scene description]
        ====
        1. option 1
        2. option 2
        ...
        ----
        "

        '''
        print(self.show_current_scene())

    def __str__(self):
        '''
        a string constructor to create a string in the format

        CHARACTERS
        name [A[num] B[num] C[num]] is proficient in attribute
        name [A[num] B[num] C[num]] is proficient in attribute
        SCENES
        scene_id > [[num]. skill/attribute[num] ++id +id -id --id] [num. skill/attribute[num] ++id +id -id --id]]
        scene_id > [[num]. skill/attribute[num] ++id +id -id --id] [num. skill/attribute[num] ++id +id -id --id]]
        '''
        #initialise the character block of the sting that will be printed with 'CHARACTERS'
        string_chara_block='CHARACTERS'
        #iterate over the different characters in the story
        for key in self.chara_dict.keys():
            #concatenate a newline white space with the string constructor of the respective character instance
            string_chara_block=string_chara_block+'\n'+self.chara_dict[key].__str__()
        #initialise the character block of the sting that will be printed with 'CHARACTERS'
        string_scene_block='SCENES'
        #iterate over the different characters in the story
        for key in self.scene_dict.keys():
            #concatenate a newline white space with the string constructor of the respective scene instance
            string_scene_block=string_scene_block+'\n'+self.scene_dict[key].__str__()
        #concatenate the Character block with a newline whitespace and the scene block sting
        string_out=string_chara_block+'\n'+string_scene_block
        #return the final string
        return string_out
