class Student:
    pass


class Marks:
    pass


s1 = Student()
m1 = Marks()

print(isinstance(s1, Student))
print(isinstance(m1, Marks))
print(isinstance(s1, Marks))
print(isinstance(m1, Student))

print(issubclass(Student, object))
print(issubclass(Marks, object))
