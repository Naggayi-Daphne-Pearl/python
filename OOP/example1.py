#  Object oriented programming 
class Student: 
    """Details for each student"""
    def __init__(self,name,age, grade):
        self.name = name
        self.age = age
        self.grade = grade # range from 0 to 100
    def get_grade(self):
        return self.grade
    
class Course:
    """Course class for each student"""
    def __init__(self,name, max_students):
        self.name = name 
        self.max_students = max_students
        self.students = []
    def add_student(self, student):
        """If the lenght of each student is less than the max_students add students to the list"""
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True 
        return False
    def get_average_grade (self):
        pass


# Intiante the students 
s1 = Student("Pearl", 23, 95)
s2 = Student("Daphne", 25, 74)
s3 = Student("Naggayi", 26, 66)

course = Course("Math", 3)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.students[0].name)



 
    
