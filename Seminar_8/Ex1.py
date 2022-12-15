'''
Создать информационную систему позволяющую работать с 
сотрудниками некой компании \ студентами вуза \ учениками школы.

'''
class Student:
    is_login = False
    
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def login(self):
        self.is_login = True
        return True
    
    def view_homework(self):
        if self.is_login:
            return "data"

class Teacher(Student):
    pass

class Admin(Teacher):
    pass
