import types
import math 

# importing types allows you to annotate the wrap function 
# with the type of function. 


# Word wrap problem:
# "the fat cat sat on the mat",10
# "the fat \ncat sat on\nthe mat"
# Trying to wrap words so they don't get cut in half.

def wrap( input , columns ) :
    words = input.split(" ")
    # print(words)
        
    output=""
    # output.append(words[0])
    chars_in_line_so_far=0
    for word in words:
        word_length = len(word)
        # print("word is {} word length is {} chars_in_line_so_far length is {}".format(word,word_length,chars_in_line_so_far))
        amount_of_columns_for_word=math.ceil(word_length/columns)
        print("The amount of columns needed for word " + word + " is" + amount_of_columns_for_word)
        if word_length>columns:
            second_part= word[columns-1:word_length]
            if len(second_part)<columns+1:  
                output = output + word[0:columns-1]+"-"+ "\n"+ second_part
                chars_in_line_so_far = len(second_part)
           #elif: 
                #third_part = word[columns*2-2:word_length]
                #output = output + word[0:columns-1]+ "-"+ "\n" + second_part + "-" + "\n" + third_part 
                #chars_in_line_so_far = len(third_part)

        elif word == words[0]:
            output = output + word
            chars_in_line_so_far = chars_in_line_so_far + word_length
        elif chars_in_line_so_far +1 + word_length <= columns:
            # print("it fits!")
            output = output + " " + word
            chars_in_line_so_far = chars_in_line_so_far + 1 + word_length
        else:
            # print("it didn't fit!")
            output = output + "\n"
            output = output + word
            chars_in_line_so_far = word_length
        # print("output is {}".format(output))
        
    return output


# Ask the user for a file
word_wrap_file=input("please may I have a file:")

# Ask the user for columns
number_of_columns=input("How many characters would you like it to be wrapped per row?")

# Open the file
open_file = open(word_wrap_file,"r")

text = open_file.read()
# print(text)
# text2 = open_file.read(10) # won't read the first 10 characters again. 
# # Reading a file means that the Prgramme opens the file and then puts a cursor at the first character. 
# print(text2)

result = wrap(input=text, columns=int(number_of_columns))
print(result)
# the code is not perfect, I would like to clean it up. (but not today)

open_file.close() # This will close the "open file" variable. 

# Data types. 
