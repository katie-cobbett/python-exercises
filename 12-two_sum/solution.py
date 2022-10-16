from typing import List
class Solution():
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes= []
        #for number in nums: 
            #if number> target:
               # index_element_remove= nums.index(number)
               # nums[index_element_remove]= " "

       
        for new_number in nums: 
            if new_number<0:
                looking_for= target - abs(new_number)
            looking_for = target-new_number
            index_element2 = nums.index (new_number)
            nums[index_element2] = " "
            #print("nums is now", nums) 

            #print ("new number is", new_number, "looking for is", looking_for)

            if looking_for in nums:
                index_element1= nums.index(looking_for)
                indexes.append(index_element2)
                indexes.append(index_element1)
                #print ("index is now", indexes)
                break
            
                    


        
        return(indexes)

