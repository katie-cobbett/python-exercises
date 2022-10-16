class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #return len(s)
        amount_of_letters= 0 
        newlist= list()
       
        record_letters = 0 

        for index in range (0,len(s)):
            this_letter= s[index]
            #print(this_letter)
            #print("amount of letters", amount_of_letters)
            
            if this_letter in newlist: 
                # duplicate detected 

                if amount_of_letters > record_letters:
                    record_letters = amount_of_letters
                    #print("amount of letters", amount_of_letters)
                #if this_letter == newlist[0]:
                    #newlist.remove(this_letter)
                    #newlist.append(this_letter)
                    # this is removing the letter from the start but 
                    # adding it onto the end so the list could continue cycling though 
                
                else: 
                    place_in_list_of_letter = newlist.index(this_letter)
                    # the index of the clashed letter is found 
                    #print ("place in list", place_in_list_of_letter)
                    #print("amount of letters", amount_of_letters)
                    amount_of_letters -= (place_in_list_of_letter)  
                    # the amount of letters in the running total is decreased by the amount of
                    # letters up to and including the clash
                    newlist.append(this_letter)
                    # the new letter is added 
                    #print("running sequence before is", newlist)
                    for i in range(0,place_in_list_of_letter+1):
                        newlist.pop(0)
                        
                    #print("running sequence after is", newlist)

            if this_letter not in newlist:
                amount_of_letters +=1
                newlist.append(this_letter)
                if amount_of_letters > record_letters:
                    record_letters = amount_of_letters
            #print("running sequence is", newlist)   

        return record_letters