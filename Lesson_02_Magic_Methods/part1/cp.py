# class Student:
#     pass

# text = 'hello'
# if __name__ == '__main__':
#     student = Student()
#     print(student)
#     print(type(student))
#     print(type(text))
#     print(dir(student))

class Student:
    def __init__(self, name, major, grade):
        self.name = name
        self.major = major
        self.grade = grade
    def __repr__(self):
        return f"Student(name = {self.name}, major = {self.major}, grade = {self.grade})"
    def __str__(self):
        return f"{self.name} is a {self.grade} grade student majoring in {self.grade}"
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name and self.major == other.major and self.grade == other.grade
        return False
if __name__ == '__main__':
    student1 = Student('Betancur', 'CompSci', 10)
    student2 = Student('Skibidi', 'Com Art', 12)
    student3 = Student('Betancur', 'CompSci', 10)
    print(repr(student1))
    print(student1 == student2)
    print(student1 == student3)