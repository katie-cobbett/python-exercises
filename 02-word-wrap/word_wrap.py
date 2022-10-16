
from re import X
import types

# importing types allows you to annotate the wrap function 
# with the type of function. 


# Word wrap problem:
# "the fat cat sat on the mat",10
# "the fat \ncat sat on\nthe mat"
# Trying to wrap words so they don't get cut in half.

def wrap( input , columns ) :
    words = input.split(" ")
    print(words)
        
    output=""
    # output.append(words[0])
    chars_in_line_so_far=0
    for word in words:
        word_length = len(word)
        print("word is {} word length is {} chars_in_line_so_far length is {}".format(word,word_length,chars_in_line_so_far))
        if word_length>columns:
            second_part= word[columns-1:word_length]
            output = output + word[0:columns-1]+"-"+ "\n"+ second_part
            chars_in_line_so_far = len(second_part)
        elif word == words[0]:
            output = output + word
            chars_in_line_so_far = chars_in_line_so_far + word_length
        elif chars_in_line_so_far +1 + word_length <= columns:
            print("it fits!")
            output = output + " " + word
            chars_in_line_so_far = chars_in_line_so_far + 1 + word_length
        else:
            print("it didn't fit!")
            output = output + "\n"
            output = output + word
            chars_in_line_so_far = word_length
        print("output is {}".format(output))
        
    return output



