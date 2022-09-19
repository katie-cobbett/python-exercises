# the rules of fizz buzz boing are as follows: 
# If a number is divisible by 3, the student says “fizz” rather than the number. 
# If a number is divisible by 5, they say “buzz” 
# rather than the number. If a number is divisible by both, they say “fizz buzz"

import types 
def fizz_buzz_boing(lowest_number,highest_number):
    output = []
    for number in range(lowest_number,highest_number+1):
        #print("The number is", number)
        div_by_3=number%3
        if div_by_3==0:
            temp=""
            temp= temp +"Fizz"
            div_by_5=number%5
            if div_by_5==0:
                temp= temp+ " buzz"
            print("The temp string is ", temp)
            output.append(temp)
        else: 
            div_by_5=number%5
            #print(number, "div_by_5 number is ", div_by_5)
            if div_by_5==0:
                output.append("Buzz")
            else:
                output.append(str(number))
    return output
