# test_application.py

from application import Application

# Test function with too many actions in the Act step
def test_save_when_principal_is_changed_expect_new_principal_value_in_database():
    """
    Test case: Too many action steps
    When the principal is changed, expect the new principal value in the database.
    """
    # Arrange
    class_under_test = Application()
    class_under_test.principal = 999.91
    class_under_test.save()
    id = class_under_test.id

    # Act
    class_under_test.get_by_id(id)
    class_under_test.principal = 1009.81
    class_under_test.save()
    actual = class_under_test.get_by_id(id)

    # Assert
    assert actual.principal == 1009.81, "Expected the principal value to be updated in the database"


from application_tests_context import ApplicationTestsContext

# Assume that the ApplicationTestsContext class is defined 
# with the necessary methods (setup_test_database, create_instance, retrieve)

# Test function with only one action in the Act step
def test_save_when_principal_is_changed_expect_new_principal_value_in_db():
    """
    Test case: One action step
    Verify that when the principal is changed, the new principal value is correctly saved in the database.
    """
    # Arrange
    expected_principal = 1009.81
    tests_context = ApplicationTestsContext('ApplicationTestsScenario01.json')

    class_under_test = tests_context.retrieve(97)
    assert class_under_test.id == 97
    assert class_under_test.principal == 999.91

    class_under_test.principal = expected_principal
    
    # Act
    class_under_test.save()
    
    # Assert
    actual = tests_context.retrieve(97)
    assert expected_principal == actual.principal, 'The principal value in the database should match the expected value.'

def test_get_by_id_when_73_expect_student_high_school_is_massachusetts():
    """
    Tests that the student's high school is Massachusetts with
    a guard and a secondary assertion to help out
    """
    # Arrange
    expected_state = "Massachusetts"

    application = Application.get_by_id(73)
    class_under_test = application.student
    # guard checks that class_under_test is not None
    assert class_under_test is not None, "'class_under_test' not found"

    # Act
    high_school = class_under_test.high_school

    # Assert
    # this secondary assertion helps check that we can get to the primary assertion
    assert high_school is not None, "'high_school' not found"
    # primary
    assert high_school.state == expected_state, f"'state' should be '{expected_state}'"
