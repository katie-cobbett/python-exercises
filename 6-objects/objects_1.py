import typing

# here we will learn about classes and objects 
# objects are a block of memory and they store data like name inside of them 
# self is a reference to where that memory is 
class Person: 

    def __init__(self, name: str , age: int , cashpoint_pin : str = "1234"):
        self.name = name
        self.age = age
        self._pin = cashpoint_pin

    # the property thing 
    # @property
    # def name(self) -> str:
    #     return self._name

    # @property
    # def age(self) -> int:
    #     # Record the fact tha someone is asking Katie's age...
    #     # decide whether we want to lie...
    #     return self._age

    def __str__(self) -> str :
        # result = "name:{}\n".format(self.name) + "age:{}\n".format(self.age)
        return str(self.__dict__) 
    
    
    # the property thing is an annotation, a hint to the programme. 
    @property 
    def pin(self) -> str :
        return "secret"

    # @property.setter
    # def pin(self,new_value):
    #     self._pin = new_value
    
    def one_year_older(self):
        self.age += 1
    
def a(value:str):
    print(value)

def main():

    katie = Person("katie", 20)
    print("Katie printed is : {}".format(katie))

    print("katie is {} years old".format(katie.age))

    katie.one_year_older()
# you are allowed to get a function to change something inside the class, as long as the function you are calling is 
# inside the class. 
# 
    print("katie is {} years old".format(katie.age))

    # unsafe...
    # katie_as_a_dict=katie.__dict__
    # print("dict:{}".format(katie_as_a_dict))
    # print("age:{}".format(katie_as_a_dict['age']))

    fred = Person("fred",39)
    print(fred)
    

    print(katie.pin)
    print(katie._pin)

    # katie.pin = "8237"

    a("asjdhsad")



        

if __name__ == "__main__":
    main()


