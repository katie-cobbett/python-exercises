class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #return len(s)
        amount_of_letters= 0 
        newlist= list()
       
        record_letters = 0 

        for index in range (0,len(s)):
            this_letter= s[index]
            
            
            if this_letter in newlist: 
                # duplicate detected 

                if amount_of_letters > record_letters:
                    record_letters = amount_of_letters
                    
                    # this is removing the letter from the start but 
                    # adding it onto the end so the list could continue cycling though 
                
                else: 
                    place_in_list_of_letter = newlist.index(this_letter)
                    amount_of_letters -= (place_in_list_of_letter)  
                    newlist.append(this_letter)
                    # this loop removes letters from the start until we get up to the 
                    # first duplicate, because this is the next place we can consider
                    # the list to be from 
                    for i in range(0,place_in_list_of_letter+1):
                        newlist.pop(0)
                        
                    

            if this_letter not in newlist:
                amount_of_letters +=1
                newlist.append(this_letter)
                if amount_of_letters > record_letters:
                    record_letters = amount_of_letters
               

        return record_letters