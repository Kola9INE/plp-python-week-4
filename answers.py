"""
TASK: 
1. CREATE A PYTHON CLASS NAMED PERSON
2. THE PERSON CLASS SHOULD HAVE THE FOLLOWING ATTRIBUTES:

* NAME: REPRESENTING THE PERSON'S NAME
* AGE: REPRESENTING THE PERSON'S AGE
* GENDER: REPRESENTING THE PEROSN'S GENDER

- IMPLEMENT A METHOD CALLED INTRODUCE THAT PRINTS A MESSAGE INTRODUCING THE PERSON WITH THERI NAME, AGE AND GENDER
- CREATE AN INSTANCE OF THE PERSON CLASS AND CALL THE INTRODUCE METHOD TO DISPLAY THE PERSON'S INFORMATION.
- CREATE A GITHUB REPO FOR YOUR ASSIGNMENT AND SUBMIT THE LINK.
"""

class Person:
    def __init__(self, name:str, age:int, gender:str):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"\nHello {self.name.capitalize()}, you are {self.age} years old and a {self.gender}!\n")
    
if __name__ == '__main__':
    new_user = Person('Kolawole', 24, 'male')
    new_user.introduce()