# Define classes Actor, Line, Play 
#  open_file1 = open(play1.txt)
from pickle import NONE
from ssl import ALERT_DESCRIPTION_UNRECOGNIZED_NAME
from typing import Set,Tuple,List

# you can use the word name twice. 
class Actor:
    def __init__(self, name: str):
        self.name = name 
        self.lines : List[Line] = list()
        
    
    def you_have_another_line(self, line : 'Line' ) -> None :
        self.lines.append(line)

    # Define a method on Actor called all_lines() which returns a list all the Lines for that Actor
    # the actor in actor class will have the lines and the actor name, in order to call the actor 
    def all_lines(self) -> List[str]:
        results = list()
        for line in self.lines:
            results.append(line.text)
        return results





#     def __key(self) -> Tuple[str]:
#         """
#         Returns a Tuple containing all the things which makes the Actor unique.
#         """
#         return ( self.name )

# # Trying to tell if one thing is already in the set, if the actor name is, then the new actor name will not be added. 
# # # of an object is getting a number that is based on a load of different factors. 
#     def __eq__(self, other) -> bool:
#         """
#         This is a special method (as it uses __ before and after the name )
#         Checks to see if one Actor object is the same as another.
#         If you want to add an object of this class to a collection, you need to implement this method.
#         """
#         if not isinstance(other, Actor):
#             # don't attempt to compare against unrelated types
#             return NotImplemented

#         is_same = True
#         if self.__key() != other.__key():
#             is_same = False
        
#         return is_same
    

#     def __hash__(self):
#         """
#         This is a special method (as it uses __ before and after the name )
#         Allows things like the Set class and other collections of Actors to quickly
#         get a single value which identifies a particular Actor.
#         So if two references to Actor objects exist, and they have the same __hash__ values
#         then they must be referring to the same Actor.
#         If you want to add an object of this class to a collection, you need to implement this method.
#         """
#         return hash(self.__key())


class Line:
    def __init__(self, text : str ):
        self.text = text


class Play:
    # The next function is going to return the actor and his lines when called 
    def get_actor(self, actor_name:str):
        """
        For a given actor name, return the Actor with that name.
        """
        return self.actors[actor_name]
        

    def __init__(self, file_name :str ):
        self.file_name = file_name
        self.title = None
        self.url = None 

        # Key is the actors name. it is in the class of play because we want to 
        # have all of the actors in the play at once. 
        
        self.actors = dict() # only variables that are shared within all methods in the class 
        # have a self. as part of them
        self.lines = list()
        
        with open(file_name,"rt") as open_file: # this will make the file close when the code is left. It means you never accidently forget to write the code. 
            play_text = open_file.read()
        # The file is already closed by this point. Whew!
            
        lines_from_file = play_text.split("\n")
        # lines is a list
        # a = []    or   a = list()    or   a = List() to get an empty list.

        # cycle through each line in the text, and split out the actor from the 'line' they have to say
        for line_from_file in lines_from_file: 
            line_pieces= line_from_file.split(": ")
            
            actor_name = line_pieces[0].strip()

            if len(line_pieces)<2:
                line_text=NONE
            else: 
                line_text = line_pieces[1].strip()
                
                if actor_name == "Title": 
                    self.title = line_text
                
                elif actor_name == "Url":
                    self.url= line_text
                    
                else:
                    if actor_name in self.actors.keys():
                        our_actor = self.actors[actor_name]
                    else:
                        our_actor = Actor(actor_name)
                        self.actors[actor_name] = our_actor
                    #... our_actor is set to refer to either a new Actor, or one we've seen already.

                    line_obj = Line(line_text) # Construct a line object from the Line class.
                    self.lines.append(line_obj)
                    # This was the code that made this class earlier 
                    #class Line:
                    #def __init__(self, text : str ):
                    #self.text = text
                
                    our_actor.you_have_another_line(line_obj)






            

        
# citizen1= Actor(citizen1)


# class Play: 
#     def __init__(self, Play_name):

# class Line(Play):
#     def __init__(self, line_words: str):

