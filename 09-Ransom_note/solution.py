
class Solution(object):

    def canConstruct(self, ransomNote , magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
 
        answer = True 

        # Split the inputs into character parts.
        split_ransom = []
        split_magazine = []
        
        for character in ransomNote:
            split_ransom.append(character)

        for character in magazine:
            split_magazine.append(character)
        
        # conecpt of shallow copy vs deep copy. The deep copy is wanted here
        # because it copies the context and actually does make a new list instead of 
        # directing to the old list with a different naeme. 

        letters_remaining = split_magazine.copy()
        for letter in split_ransom: 
            if letter in letters_remaining:
                letters_remaining.remove(letter)
            else: 
                answer = False 
                
        # in order to copy this into leet code, removing print outs    
        # print(split_magazine)
        # print(split_ransom)

        return answer
    