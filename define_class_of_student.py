class Student:
    """Store student info"""
    def __init__(self, name, age, sid):
        self.name = name
        self.age = age 
        self.sid = sid
    
    def get_name(self):
        """
        Get student name
        return self.name
        """
        return self.name 
    
    def get_age(self):
        """
        Get student age
        return self.age
        """
        return self.age 
    
    def get_sid(self):
        """
        Get student id
        return self.sid
        """
        return self.sid  

student = Student('bingbing', 18, 1)

print(student.get_name())