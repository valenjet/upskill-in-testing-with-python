# test_data_helper.py

from application import Student

from helper_test_data import HelperTestData

def test_something_():
   # Arrange
   excepted = 'Smith'
   random_name = HelperTestData.build_name_string()

   class_under_test = Student(name=random_name)
   assert class_under_test.name != excepted
   
   # Act
   class_under_test.set_name(excepted)

   # Assert
   actual = class_under_test.name
   assert actual == excepted
