class Student:
   
    def __init__(self,name,age,skill):
        self.name = name
        self.age = age
        self.skill = skill
    #Method
    def introduce(self):
        print(f"Hi, I'm {self.name}.")
        print(f"I am {self.age} years old.")
        print(f"My skill is {self.skill}.")
#Objects(Instance)
student1 = Student("Alice", 22, "Python")
student2 = Student("Bob", 24, "Machine Learning")

#Using the objects
student1.introduce()
print()