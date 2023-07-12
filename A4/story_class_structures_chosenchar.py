from story_class_structures import *
#from story_class_structures_bestchar import *
class StoryChosen(Story):
    '''
    This class takes the argument story which would be an instance of the story class.
    this method selects a chosen character which is in the option text and sets it as the active characrter otherwise the
    first character which is given in the story character option is selected. 
    it returns an integer that corresponds to the chosen character 
    Vivian Liu
    '''
    
    def select_character_for_check(self,skill_or_attribute_name, scene_chara=[],option_char=[]):
        '''
        this method takes 4 arguments:
            - self
            - skill_or_attribute_name (the name of the skill or attribute in that option)
            - scene_chara (a list of characters that are in the scene)
            - option_chara (a list of characters in the option)
        the method: 
            * looks at the characters in the option given and selects the first character to be the active character
            * if there are no characters in that option look in the scene and set the active character to the best character from those available
            * if there are no characters in that scene look in all available charcters and set the active character to the best character available
        
        return the number of the active character
        '''

        #check if there are any characters in the option 
        if option_char!=[]: 
            #if there are select the first character in the option list
            recommend_chara=option_char[0]
        else:
            #if there are not run the following:

            #check if there are any characters in this scene 
            if scene_chara!=[]:

                #if there are set the chara_score_list to a list of scores that each character 
                #in the list has for the particular skill_or_attribute_name given             
                chara_score_list=[chara.skill_attri_score_dict[skill_or_attribute_name] for \
                                  chara in scene_chara]
                
                #set the selected_chara_name to the name of the character with the highest score from the list extracted above
                selected_chara_name=scene_chara[chara_score_list.index(max(chara_score_list))].name
 
                #make sure that that character is in the dictionary of characters and iterate over their given number
                for _,chara in self.chara_dict.items():
                    if chara.name==selected_chara_name:
                        #if it is set that character's number to the recommend_chara (becuase it takes numerical values only)
                        recommend_chara=chara
            else:
                #otherwise when there are no characters in the scene, set the chara_score_list to the scores for the particular
                #skill_or_attribute_name given for all available chracters in the story instance 
                chara_score_list=[chara.skill_attri_score_dict[skill_or_attribute_name] for \
                                  chara_index, chara in self.chara_dict.items()]
                
                #set the recommend_chara to the character number with the highest score +1 (becuase character numbering starts at 1 not 0)
                recommend_chara=self.chara_dict[chara_score_list.index(max(chara_score_list))+1] 
                
        #set the active_chara attribute to the recommend_chara
        self.active_chara=recommend_chara
        #return the recommend_chara
        return recommend_chara
    
    def select_option(self,option_number,override=None):
        '''
        This method takes the arguments:
            - self 
            - option number (the number of the option being taken)
            - override (for testing purposes)
        
        this method collects all the characters in a scene and all the characters in an option as well as the 
        skill or attribute that will be required in that option.

        it then uses this information and runs the method above to get the most appropriate character for the option and 
        runs the story (parent) class with that character active
        '''
        #collect the skill or attribute reqiuired in this option 
        check_skillattri_name=self.active_scene.options_dict[option_number].skillattri_name

        # if the active_scene's character id lst (characters in the scene) is not empty set scene_ls_input as a list 
        # that is comprised of integers that are in both the keys for all characters dictionary in the story and 
        # characters in the active scene 
        # if the active_scene's character id lst is empty, the the scene_ls_input is empty lst 
        scene_ls_input=[self.chara_dict[index] for index in self.active_scene.chara_id_list] if\
                        self.active_scene.chara_id_list!=[] else []

        # if the active_character list in the current option of the active scene (list of characters in this option) is not empty,
        # set option_ls_input as a list that is comprised of an integer that represents the first character to appear in that option 
        # if the active_scene's current option's character id lst is empty, the the scene_ls_input is empty lst 

        option_ls_input=[self.chara_dict[self.active_scene.options_dict[option_number].active_chara[0]]] if \
                         self.active_scene.options_dict[option_number].active_chara!=[] else []

        #use function we created with scene_ls_input and option_ls_input
        self.select_character_for_check(check_skillattri_name,scene_ls_input,option_ls_input)

        #give the access to parent class for using select_option
        super().select_option(option_number,override)

