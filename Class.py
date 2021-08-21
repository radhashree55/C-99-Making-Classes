class Student(object):
    def __init__(self, name, age, gender, level, grades=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}

    # def setGrade(self, course, grade):
    #   self.grades[course] = grade

    # def getGrade(self, course):
    #   return self.grades[course]

    def getGPA(self):
        return sum(self.grades.values()) / len(self.grades)


# Define some students
john = Student("John", 12, "male", 6, {"math": 3.3, "science": 4, "english": 4.5})
jane = Student("Jane", 12, "female", 6, {"math": 3.5, "science": 3, "english": 4})

# Now we can get to the grades easily
print(john.getGPA())
print(john.grades)
print(jane.getGPA())
print(jane.grades)
