print("hiya")

# class Person():
#     def __init__(self, name):
#         self.name = None
#         self.age = None
#         self.profession = None
#         self.height = None
#         self.hobbies = []

# new_person = Person("Will")

# new_person.age = 31

# print (new_person.age)

# jay_person = Person("Jay")
# jay_person.age = 31
# jay_person.profession = "Instructor"

# print(jay_person)

# print(new_person)

class Person():
    def __init__(self, person_name, person_age, person_height):
        self.name = person_name
        self.age = person_age        
        self.height = person_height

    def set_hair(self, person_hair):
        self.hair = person_hair

    def get_hair(self):
        print(self.hair)

person_x = Person("Will", 31, "6'0")

print(person_x.height)

