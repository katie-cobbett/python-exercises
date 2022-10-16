class Solution:

    def convert(self, input_string: str, rows: int) -> str:
        # amount of intermediate (singly-filled) lists in between two possibly full comumns = number_rows - 2

        # characters = []
        
        # for index in range(0,len(input_string)): 

        columns = [] # [ ['c','a','t'],['d'] ]
        current_column = [] # 
        is_fill_full_column = True
        num_singly_filled_columns = 0

        for character in input_string:
            #making a list with the characters spaced out and seperate items 
            # characters.append(character)
            
            if is_fill_full_column:
                current_column.append(character)
                if len(current_column) >= rows:
                    columns.append(current_column)
                    current_column = []
                    if rows >= 3:
                        is_fill_full_column = False
                        num_singly_filled_columns = rows-2
                    else:
                        is_fill_full_column = True
                    
            else: 
                for _ in range(0,num_singly_filled_columns): # for something in a loop that you don't care about, can put _ 
                    current_column.append(' ')
                current_column.append(character)
                columns.append(current_column)
                current_column = []
                num_singly_filled_columns -=1
                if num_singly_filled_columns <= 0 :
                    is_fill_full_column = True

            #print("Current:{}".format(current_column))
            #print("columns:{}".format(columns))
            #print("is_fill_full_column:{}".format(is_fill_full_column))

        columns.append(current_column)
        print("Final columns:{}".format(columns))


        # We have a list of column lists...
        # Now we need to extract the data back into a results string...


        # for row in number_rows: ########
        # maybe need to 
        results_string = ""

        # [c, a, t]
        # [ , d]
        for i in range(0,rows):
            for column in columns:
                if len(column) > i:
                    if column[i] != ' ':
                        results_string += column[i]
        
        return results_string 
