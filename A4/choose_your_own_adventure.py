# import all the classes and functions from the file story_class_structures.py
from story_class_structures import *
# open and read the file, making contents of each file into a list of strings by using ".strip()"
def read_file(file_name):
    with open(file_name, 'r') as fileref:
        lines = fileref.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
    
    return lines

if __name__ == "__main__":
    # making each file's info into a list of strings so can use story class to make an instance
    characters = read_file("sample_chars.txt")
    story = read_file("sample_story.txt")
    # new_story is created as an instance of story class
    new_story = Story(story, characters)
    print(new_story.__str__())
    # the following code helps keep running the code until "end = true" is reached
    # when end = false, it shows that it hasn't gone to the end scene and select another option
    # end = true means that it goes to the end scene and stop running code
    end = False
    while end == False:
        print(new_story.show_current_scene())
        #asks the user to input an option to take
        new_story.select_option(int(input("select an option ")))
        if "E" in new_story.active_scene.id:
            print(new_story.show_current_scene())
            end = True
