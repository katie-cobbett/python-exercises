

import random
dog=1 
cat=2
mutant=dog+ cat
print(mutant)
frog="3"
mutant2=int(frog)+cat
mouse="eek"
mutant3=frog+" "+mouse
print(mutant3)
print(mutant2)
print("hello mate")
dog=1.2
mutant4=dog+cat
print(mutant4)
print(type(mutant4))
is_furry=True
print(is_furry)
if cat==2:
    print("yes it is furry")
else: 
    print("no not furry")
    print("same")
print("rat")
def add(a,b):
    c=a+b
    return c 
print(add(2,3))

def subtract(x,y=1):
    """
    """
    z=x-y
    return z 
print(subtract(y=3,x=5))

#lists# 

fruit=["mango","apple","pear"]
print(fruit)

fruit.remove("mango")

fruit.append("grape")

fruit.insert(0,"pineapple")
print(fruit)
def is_expensive(number):
    if number>2:
        return"expensive"
    else:
        return"cheap"

fruit_prices={}
for x in fruit:
    price= random.randint(1,5) 
    details = [ price , is_expensive(price) ]
    fruit_prices[x] = details
    print("{0} smoothie {2} {1}".format(x,str(price),is_expensive(price )))

#dictionaries#
print("------- dictionaries: -------")
menu={"lasagne":15, "bolognaise":20}
print(menu)
print("dish names:{}".format( menu.keys() ))

print(fruit_prices)
print(fruit_prices['apple'] )


fruit_prices['apple'] = None
del fruit_prices['apple']

for fruit_name in fruit_prices:
    print(fruit_name)
    print(fruit_prices[fruit_name] )

# strings #
a="the quick brown fox"
print(a)
print(a[4:9])
parts=a.split(" ")
print(parts[2][2])

#input from terminal#

#b=input("give me an adjective")
#print(b)
#print("dad is {}".format(b))

# number1=int(input("give me a number: "))
# operation=input("give me an operation: ")
# number2=int(input("give me another number: "))
# if operation in ["plus","+"]:
#     outcome=add(number1,number2)
# elif operation in ["-", "minus"]:
#     outcome=subtract(number1,number2)
# else:
#     outcome="garbage"
# #else:
#     #outcome=subtract(number1,number2)
# print(outcome)



# Sets
# {} = set , [] = list  {} = dictionary
# you add to all of them 
# dictionaries are pairs of things, sets just are like a list with {}
fruit={"apple","mango","apple","pear"}
fruit.add("grape")
print(fruit)
fruit.add("grape")
print(fruit)
# won't add something twice if it's already in the set, so you would have to use a list 

veg={"carrot","onion"}

edible=fruit.union(veg) # links them with random order. 
print(edible)
# if you want an order you can't rely on it in sets and 
# dictionaries, you would need to sort it 

print("------------")

# Tuple
tuple=(5,6,7)
print(tuple[0])
print(tuple[1])
print(tuple[2])

(a,b,c)=tuple
print(a)
print(b)
print(c)

print("------------")

def give_me_3() :
    return (5,6,"hello")

(a,b,c)=give_me_3()
print(a)
print(b)
print(c)

print("------------")

def give_me_one():
    outcome="sd"
    return outcome

result=give_me_one()