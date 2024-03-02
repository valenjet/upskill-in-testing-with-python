# helper_test_data.py

import random
import string

# pytest ignores classes that don't begin with 'Test'
class HelperTestData:
    DEFAULT_MAX_STRING_LENGTH = 50  # default maximum length

    # pytest ignores classes with an __init__ method
    def __init__(self):
      pass

    @staticmethod
    def build_name_string(length=None):
        """
        Generates a random string of a specified length. If no length is provided,
        a random length is chosen within predefined limits.
        """
        length = length or random.randint(1, HelperTestData.DEFAULT_MAX_STRING_LENGTH)
        
        # Ensure the generated length is positive
        assert length > 0, "Generated string length must be greater than 0"
        
        # Generate the name with the first letter upper case and the rest lower case.
        first_letter = random.choice(string.ascii_uppercase)
        other_letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(length - 1))
        
        return first_letter + other_letters
