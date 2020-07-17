#Decorate-sort-undecorate (Old Way)

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))
    
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 18),
    Student('dave', 'B', 10),
]

decorated = [ (student.age, i, student) for i, student in enumerate(student_objects)]
print("original :", decorated)
decorated.sort()
print( "sorted :", decorated)
undecorated = [student for grade, i, student in decorated]
print("original sorted form :", undecorated)

#Implementation of sorted() and sort()
