from multiprocessing import Value
from typing import List
# The class list has a capital
# string doesn;t have a capital S because it is a primative type of code, done early on in python so has to be 
# lower case s
class Solution(object): 
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        time_needed_minimum=0

        # split_colours= slice(colors)
        # print(split_colours)



        for index in range(1,len(colors)):
            this_char = colors[index]
            previous_char = colors[index-1]
            
            #print(index)
            if this_char == previous_char:
                #print("index {} has same character {} cost of previous {}  cost of this one {}".format(
                    index,this_char,neededTime[index], neededTime[index-1]))
                # Remove the previous char.
                if neededTime[index-1]< neededTime[index]:
                    time_needed_minimum+= neededTime[index-1]
                    

                else: 
                    time_needed_minimum +=neededTime[index]
                    value= neededTime[index-1]
                    neededTime[index]= value
                    

                   
                #print(time_needed_minimum)
            

        return(time_needed_minimum)
