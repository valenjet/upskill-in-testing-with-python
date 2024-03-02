# application.py


import pytest

class School:
    def __init__(self, state: str):
        self.state = state

class Student:
    def __init__(self, name: str = ''):
        self.name = name
        self.high_school = School(state='Massachusetts')
    
    def set_name(self, name: str):
        self.name = name

class Application:
    @staticmethod
    def get_by_id(id):
        # Implementation to retrieve data from the database by ID
        return Application(id=97, principal=1009.81)

    # Assuming there's an Application class implementation
    def __init__(self, id: int = None, principal:float = None):
        self.principal = principal
        self.id = id
        self.student = Student()
    
    def save(self) -> None:
        # Implementation to save the Application instance state to a database
        pass
