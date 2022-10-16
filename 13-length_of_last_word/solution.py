
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_string= s.split()
        i = 0
        for words in split_string:
            i+= 1 
        length= len(split_string[i-1])
        return(length)

