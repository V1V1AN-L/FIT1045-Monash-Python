# import all the classes and function from file story_class_structures.py
from story_class_structures import *
# StoryBest class which inherits from the Story class
class StoryBest(Story):
    '''
    This class is given the argument of a story
    # sills or attributes, compare, and return the best character's name
    # for the required skill
    Vivian Liu
    '''
    def select_character_for_check(self,skill_or_attribute_name):
        '''
        given a specific skill, this method go through each character's skills or attributes and;
            - compare outcomes of them them
            - set the recommend character to the active character
        this method returns the best character's name (character with the most optimal outcome)
        '''
        #gets the scores of skill_or_attribute_name for each of the characters in the story instance and puts it in a list
        chara_score_list=[chara.skill_attri_score_dict[skill_or_attribute_name] for \
                          chara_index, chara in self.chara_dict.items()]
        #set the recommend_chara as the index of character that has the highest score fot the particular attribute = 1 (because the numbering of characters starts at 1 not 0)
        recommend_chara=self.chara_dict[chara_score_list.index(max(chara_score_list))+1]
        #set the active_chara to the recommend_chara
        self.active_chara=recommend_chara
        #return the recommend_chara
        return recommend_chara

    def select_option(self,option_number,override=None):
        '''
        this method uses the best character for the option selected by running the above method
        and runs the select_option method from the parent class (story class) to continue the story but this time with the optimal character active
        '''
        #check_skillattri_name is the skill or attribute that is required in the option being chosen
        check_skillattri_name=self.active_scene.options_dict[option_number].skillattri_name
        #run the select_character_for_check method (above) to extract the best character for this option
        self.select_character_for_check(check_skillattri_name)
        #use the parent class (story) and run its method select_option to run the story as normal (but with the optimal character selected)
        super().select_option(option_number,override)




