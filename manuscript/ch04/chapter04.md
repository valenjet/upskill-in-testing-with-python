# Chapter 4: Testing Frameworks


### The xUnit Pattern

The xUnit test frameworks[^1], encompassing a variety of libraries such as JUnit for Java, NUnit for .NET, and pytest for Python. They adhere to an architectural pattern known as the xUnit test pattern. This foundational structure ensures consistency in unit testing across different languages and platforms. Here, we explore the key components of this pattern and its implementation in Python using the pytest framework.

#### Key Components of the xUnit Test Pattern

1. **Test Methods**: Individual unit tests encapsulated within a test class. These are the core of the testing suite, each method focusing on a specific unit of functionality.
   
2. **Setup Method**: A preparatory method that runs before each test method. It's designed to establish necessary preconditions and allocate resources for the test.
   
3. **Teardown Method**: A cleanup method executed after each test method. It's responsible for deallocating resources and restoring the test environment to its original state.
   
4. **Test Fixture/Test Context**: An initialization setup that ensures a consistent environment for tests to run. This includes setting up preconditions and allocating resources needed across multiple test methods.

#### Test Method Identification

In xUnit-style frameworks, test methods are distinguished by attributes. A primary attribute marks the basic test methods, which are public, argument-less, and return void. A secondary attribute is used for parameter-driven or data-driven tests, indicating methods that accept input values or data sources to run multiple scenarios within a single test method.

#### Implementing xUnit Test Pattern in Python with pytest

Python's pytest framework inherently supports the xUnit test pattern principles, without the explicit use of attributes to identify test methods. Here's how the concepts translate:

- **Test Methods**: Simply defined by functions prefixed with `test_` in files named `test_*.py` or `*_test.py`.
  
- **Setup and Teardown Methods**: Achieved through fixture functions using the `@pytest.fixture` decorator, with scope control for setup and teardown actions.

- **Test Fixtures**: Defined using the `@pytest.fixture` decorator to provide a reusable set of preconditions and resources for tests.


**Basic Test Method**:

```python
def test_basic_test_method_signature():
    pass
```

**Parameter-Driven Test Method**:

```python
import pytest

@pytest.mark.parametrize("ultimate_question,expected_answer", [
    ("How many roads must a man walk down?", 42),
    ("What is your favorite prime number?", 73),
])
def test_parameter_driven_test_method_signature(ultimate_question, expected_answer):
    pass
```

This Python code demonstrates the pytest framework's approach to implementing the xUnit test pattern's principles, offering a flexible and intuitive way to define and manage unit tests.


### Structuring Tests with Setup and Teardown

In the context of unit testing, ensuring tests run in isolation and in a repeatable manner is paramount. This often necessitates the implementation of setup and teardown routines to prepare and clean up the testing environment. In pytest, the framework automates these routines through fixtures, offering a powerful and flexible way to establish preconditions and clean up after tests.

#### Test Class and Fixture Concept

The terms "test class" and "fixture" in unit testing are closely related. A fixture refers to the setup and teardown mechanism that ensures a consistent environment for tests to execute. This setup might involve initializing objects, preparing data, or configuring mock objects necessary for the test methods within the class.

#### Setup and Teardown in pytest

pytest simplifies the setup and teardown process with fixtures, eliminating the need for specific attribute decorations used in xUnit frameworks. Here’s how pytest manages these tasks:

- **Fixture Setup**: Performed by defining a fixture function with the `@pytest.fixture` decorator. This function can execute setup code before each test method or once before all tests in the class, depending on the specified scope.

- **Fixture Teardown**: Achieved through the same fixture function by using yield statements or finalizer functions to execute cleanup code after the test execution.

#### Implementing Fixtures for Setup and Teardown

Consider this example that demonstrates the use of fixtures for setup and teardown tasks in a pytest test class:

```python
import pytest

@pytest.fixture(scope="module")
def fixture_setup_teardown():
    print("Fixture setup")
    yield
    print("Fixture teardown")

@pytest.fixture(autouse=True)
def test_setup_teardown():
    print("Before-test")
    yield
    print("After-test")

class TestExample:
    def test_method_no_parameters(self, fixture_setup_teardown):
        print("Executing 'test_method_no_parameters'")

    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_method_with_parameters(self, index, fixture_setup_teardown):
        print(f"Executing 'test_method_with_parameters' {index}")
```

#### Execution Flow with pytest

1. **Fixture Setup**: Before any test methods are executed, the `fixture_setup_teardown` with `scope="module"` ensures setup tasks are performed once for the entire test class.

2. **Test Setup**: Before each test method, `test_setup_teardown` runs, marked with `autouse=True` to automatically apply to all test methods.

3. **Test Execution**: Test methods are executed, with parameterized tests running once for each parameter set.

4. **Test and Fixture Teardown**: After each test, the `test_setup_teardown` fixture handles post-test cleanup. Once all tests in the class complete, `fixture_setup_teardown` performs final cleanup tasks.

This example illustrates how pytest's fixtures provide a declarative approach to managing test setup and teardown, enhancing code reusability and maintainability across the test suite.


### Understanding Assertions in Test Code

In the realm of software testing, an assertion plays a critical role by serving as a boolean expression that evaluates to either true or false. Assertions are strategically placed within a test method to affirm the developer's expectation that a specific condition should hold true at that juncture. Should an assertion evaluate to false, it signifies a failure in the test scenario, prompting the test framework to mark the test as failed.

Assertions are instrumental in delineating the intended behavior of the code under test. They explicitly state the conditions that are expected to be met, allowing the developer to instruct the test framework to flag any deviation from these expectations as a test failure. This mechanism facilitates a direct line of communication between the developer and the test framework, ensuring that the software behaves as anticipated. For instance, to verify that a function's return value is not null, the test code would include an assertion like `assert result is not null`, clearly expressing the expectation for a non-null result.

#### Implementing Assertions in Python with pytest

Using Python's pytest framework, assertions are straightforward and intuitive. The pytest framework leverages Python's built-in `assert` statement, enabling developers to write clear and concise assertions directly in their test code. Here's a brief example to illustrate how assertions can be employed in pytest to validate that a function's return value is indeed not null:

```python
def test_function_returns_not_null():
    # Example function call
    result = example_function()

    # Assertion to ensure the result is not null
    assert result is not None, "Expected the result to be not null."
```

This example highlights the efficacy of assertions in confirming the expected outcomes of test cases. By making use of assertions, developers can succinctly articulate the prerequisites for their code's correctness, enhancing the reliability and maintainability of their tests.


Table 4-?: Classic Assertions with Examples in `pytest`
| Assert Type | Description                                    | Examples in `pytest` |
|:------------|:-----------------------------------------------|:-------------------|
| Utility     | Help control the test method evaluation logic  | `pass`, `pytest.fail()` |
| Conditional | Determine if a test condition is or is not met | `assert expr`, `assert not expr` |
|             |                                                | `assert var is None`, `assert var is not None` |
| Equality    | Determine whether the two arguments are equal  | `assert actual == expected`, `assert var1 != var2` |
| Comparison  | Determine how the two arguments compare        | `assert actual > expected`, `assert actual >= expected` |
|             |                                                | `assert actual < expected`, `assert actual <= expected` |
| Identity    | Determine if the object instances are the same or not the same instances | (via override of `__eq__`) |
|             |                                                | `assert obj1 == obj2`, `assert obj1 != obj2` |
| Type        | Determine if an object is an instance of or assignable from a type. | `assert type(var) is Type`, `assert type(var) is not Type` |



## Comparing `pytest` to `unittest`

Table 4-?: Comparison of `pytest` and `unittest` assertions
| Examples in `pytest`                                       | Examples in `unittest`                 |
|:-----------------------------------------------------------|:---------------------------------------|
| `pass`, `pytest.fail()`                                    | `pass`, `fail()`                       |
| `assert expr`, `assert not expr`                           | `assertTrue(expr)`, `assertTrue(expr)` |
| `assert var is None`, `assert var is not None`             | `assertIsNone(var)`, `assertIsNotNone(var)` |
| `assert actual == expected`, `assert var1 != var2`         | `assertEqual(actual, expected)`, `assertNotEqual(var1, var2)` |
| `assert actual > expected`, `assert actual >= expected`    | `assertGreater(actual, expected)`, `assertGreaterEqual(actual, expected)` |
| `assert actual < expected`, `assert actual <= expected`    | `assertLess(actual, expected)`, `assertLessEqual(actual, expected)` |
| `assert obj1 == obj2`, `assert obj1 != obj2`               | `assertEqual(obj1, obj2)`, `assertNotEqual(obj1, obj2)` |
| `assert type(obj) is Type`, `assert type(obj) is not Type` | `assertIsInstance(obj, Type)`, `assertNotIsInstance(obj, Type)` |



## Mock Object Frameworks

> Use a Mock Object Framework to Provide Stub and Mock Functionality

### Utilizing Mock Object Frameworks in pytest

Mock object frameworks play a pivotal role in automated testing by dynamically generating fake objects, known as stubs or mocks, during test execution. This capability streamlines the testing process by eliminating the need for manual creation of fake implementations or subclasses. The use of such frameworks significantly enhances testing efficiency and enriches test suites with robust features that are cumbersome to implement manually.

#### Dynamic Fake Objects in Python Testing

Python developers can leverage Mock object functionality through libraries such as `unittest.mock` included in the Python standard library. This module facilitates the creation of mock objects, offering a powerful and flexible way to produce stubs or mocks dynamically.

#### Implementing Mocks with `unittest.mock`

`unittest.mock` provides a comprehensive suite of tools for mocking, stubbing, and spying on dependencies. Mock objects can simulate the behavior of complex real-world objects, making it easier to test interactions within your code under test without relying on actual implementations.

#### Example: Testing with Mock Objects

Below is an example that demonstrates how to use `unittest.mock` in conjunction with pytest to test the `Student` class's `save` method. This example showcases both stub and mock object generation for testing different aspects of the `Student` class interactions.

```python
import pytest

from unittest.mock import Mock
from student import Student


def test_save_with_an_existing_student_improperly_created_expect_invalid_operation_exception(stub_individual_repo, stub_student_repo):
    # Arrange
    today = datetime(2003, 5, 17)
    expected_student_id = 897931
    stub_student_repo.retrieve.return_value = None
    stub_student_repo.create.return_value = 23

    class_under_test = Student(stub_individual_repo, stub_student_repo)
    class_under_test.id = expected_student_id
    class_under_test.today = today
    class_under_test.date_of_birth = today.add_years(-19)

    # Act & Assert
    with pytest.raises(InvalidOperationException):
        class_under_test.save()

def test_save_with_an_existing_student_expect_individual_dal_update_is_called_once(stub_student_repo):
    # Arrange
    today = datetime(2003, 5, 17)
    expected_student_id = 897931
    student_entity = StudentEntity(id=expected_student_id)
    stub_student_repo.retrieve.return_value = student_entity

    mock_individual_repo = Mock()
    class_under_test = Student(mock_individual_repo, stub_student_repo)
    class_under_test.id = expected_student_id
    class_under_test.today = today
    class_under_test.date_of_birth = today.add_years(-19)

    # Act
    class_under_test.save()

    # Assert
    mock_individual_repo.update.assert_called_once_with(expected_student_id)
```

#### Key Points in Using Mocks and Stubs

- **Dynamic Behavior**: Mock objects can simulate any behavior needed for tests, including raising exceptions or returning specific values, enhancing test reliability and isolation.
  
- **Interaction Testing**: Mocks are invaluable for verifying interactions between the code under test and its dependencies, ensuring methods are called with expected arguments.

- **Efficiency**: Leveraging mock frameworks like `unittest.mock` reduces the overhead associated with setting up complex object states, focusing solely on the behavior relevant to each test.

Mock object frameworks are indispensable tools in the modern developer’s testing arsenal, offering an efficient pathway to creating isolated, repeatable, and meaningful tests. By dynamically generating stubs and mocks, developers can focus on the logic and interactions that matter, ensuring their code behaves as expected in a controlled testing environment.


## Database Testing Frameworks

> For Database Testing, Ensure That the Database State Is Consistent Before Each Test

### Database State Management for Testing

Testing the data access layer (DAL) comprehensively, especially when using Object-Relational Mapping (ORM) technologies, requires that the database be in a known state before each test to ensure reliability and repeatability. Python test projects can achieve these outcomes using pytest fixtures and potentially integrating with database management libraries for setup and teardown processes.

#### Ensuring Database State Consistency

Achieving consistency in database state before each test is crucial for accurate integration testing. This involves preparing the database with the necessary data and structure, and cleaning up after tests to maintain isolation and repeatability.

#### Using pytest Fixtures for Database Testing

In Python, the pytest framework offers a powerful mechanism for setup and teardown through fixtures. These fixtures can be used to manage database state, loading predefined data before tests and cleaning up afterwards.

#### Implementing Database Testing with pytest

Here's an illustrative example of setting up and tearing down database states in Python tests, mirroring the principles discussed with NDbUnit but utilizing Python's flexibility and the pytest framework.

```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_application.model import Base, Individual
from your_application.dal import IndividualDal

# Define a fixture for setting up the database
@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine('sqlite:///test_database.db')
    Base.metadata.create_all(engine)  # Assuming declarative base
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()
    
    # Pre-load data from XML or any predefined dataset here
    # For simplicity, data loading is omitted

    yield session
    session.close()
    transaction.rollback()
    connection.close()

# Example test that uses the db_session fixture
def test_retrieve_individual_with_scenario_data_in_database(db_session):
    # Arrange
    individual_dal = IndividualDal(db_session)
    # Pre-populate database with test data, omitted for brevity

    # Act
    actual = individual_dal.retrieve(37)  # Assuming a method to retrieve Individual by ID

    # Assert
    assert actual is not None
    assert actual.last_name == "Roosevelt"
```

#### Key Concepts and Features for Database Testing in pytest

- **Database Fixtures**: Use pytest fixtures to manage database connections, session transactions, and state cleanup. This ensures each test starts with a clean slate.
  
- **Test Data Management**: Integrate data loading and cleanup within the fixtures. This can involve reading from XML files or any other data source to populate the test database before each test.

- **Scoped Fixtures**: By leveraging pytest's fixture scope management, you can control the setup and teardown processes to run once per session, module, class, or function, depending on the test's requirements.

#### Note on Data Loading

Python offers various libraries that can parse JSON or CSV data, which can then be used to populate the test database within the fixture setup phase.

This approach to database testing in Python, using pytest and potentially integrating with ORM technologies like SQLAlchemy, provides a robust framework for ensuring database state consistency across tests.



### User Interface Testing Frameworks

User interface (UI) testing plays a critical role in the comprehensive validation of software systems, encompassing a broad spectrum from web applications to mobile and desktop interfaces. The primary objective of UI testing frameworks is to simulate user interactions with the application to verify that it functions as expected. This involves automating the UI to perform actions such as clicking buttons, entering data, and navigating through the application, thereby facilitating the identification of discrepancies between actual and expected outcomes.

#### Web Application Testing

Automating UI tests for web applications entails a series of complex steps, including but not limited to deploying the application to a server, automating browser interactions, and verifying the responses against expected outcomes. Browser automation is central to web application testing, enabling the simulation of user actions within a web browser programmatically.

#### Python Approach to Web UI Testing

In Python, the Selenium WebDriver stands out as a prominent tool for automating web browsers, providing a robust platform for executing UI tests across various browsers. Selenium allows for the automation of browser actions such as page navigation, form submission, and content verification, making it an invaluable asset in the creation of automated UI test suites.

**NOTE:** Selenium is a free and open source suite of tools that helps you to automate and control web browsers through a testing framework. Selenium supports many browsers, operating systems, programming languages, and testing frameworks.

#### Implementing Browser Testing with Selenium

Below is an illustrative example of setting up a basic UI test for a web application using Selenium WebDriver in Python, aligned with the pytest testing framework.

```python
from selenium import webdriver
import pytest

@pytest.fixture(scope="function")
def browser():
    # Setup the WebDriver instance (e.g., Chrome, Firefox)
    driver = webdriver.Chrome()
    yield driver
    # Teardown the WebDriver instance
    driver.quit()

def test_user_login(browser):
    # Arrange
    # Navigate to the application login page
    browser.get("http://example.com/login")

    # Enter login credentials
    username_field = browser.find_element_by_id("username")
    password_field = browser.find_element_by_id("password")
    username_field.send_keys("user@example.com")
    password_field.send_keys("securepassword")

    login_button = browser.find_element_by_id("submit")

    # Act
    login_button.click()

    # Assert
    assert "Dashboard" in browser.title
```


#### Mobile and Other UI Testing Frameworks

Testing mobile and other specialized UI technologies introduces unique challenges, distinct from those encountered in web UI testing. The selection of an appropriate UI testing framework for these platforms often necessitates thorough exploration and experimentation to identify a solution that aligns with the specific requirements and constraints of the project.

#### Considerations for UI Testing

- **Investment in Infrastructure**: Automating UI tests, especially for complex applications, requires significant setup, development, and ongoing maintenance efforts.
  
- **Framework Selection**: The choice of a UI testing framework depends on various factors, including the target platform (web, mobile, desktop), the languages and tools already in use, and the specific needs of the application being tested.

- **Continuous Integration**: Integrating UI tests into a continuous integration pipeline enhances the ability to detect regressions early, ensuring the stability and quality of the application over time.

UI testing frameworks are indispensable tools in the software development lifecycle, enabling teams to verify application functionality from the perspective of the end-user. By automating user interactions and validating the UI's response, developers can ensure that their applications meet the highest standards of quality and usability.


### Acceptance Testing Frameworks

> Acceptance Test with Business Specifications and Behaviors, Not Test Scripts

### Ensuring Software Meets Requirements

Acceptance testing represents a crucial phase in the software development lifecycle, aimed at verifying if the software fulfills the specified requirements and delivers the desired features. This process is pivotal in determining the software's readiness for production. It involves a thorough evaluation against a set of defined criteria to ensure the software encompasses all necessary functionalities and adheres to the minimum essential requirements.

#### The Essence of Acceptance Testing

The essence of acceptance testing lies in its ability to bridge the gap between customers, analysts, developers, and testers, facilitating a collaborative effort towards achieving a common goal: delivering software that meets user expectations and requirements. The process leverages examples and scenarios provided by stakeholders to form acceptance tests, which serve as a benchmark for evaluating the software's compliance with its intended objectives.

#### Implementing Acceptance Testing in Python

pytest can be utilized to implement acceptance tests effectively. pytest is a versatile testing framework that supports behavior-driven development (BDD) through plugins such as `pytest-bdd`, allowing for the creation of tests that are closely aligned with business specifications and behaviors.

The following illustrates a basic acceptance test implementation using pytest, focusing on behavior specifications rather than test scripts. This approach emphasizes the conditions, outcomes, and desired behaviors in a language that is accessible to analysts, developers, and testers alike.

##### Listing 4-?: Example of Acceptance Testing with pytest

[To Do]

#### Advantages of Automated Acceptance Testing

Automated acceptance testing offers several benefits, including:

- **Focus on Requirements**: Ensures developers remain aligned with the full spectrum of features and requirements.
  
- **Regression Testing**: Facilitates feature verification and regression testing to maintain software integrity over time.
  
- **Progress Metrics**: Generates metrics to gauge progress towards achieving desired outcomes.
  
- **Guidance and Direction**: Provides actionable insights based on predefined acceptance criteria to steer development efforts.

#### Emphasizing Specifications Over Scripts

The shift from test scripts to business specifications and behaviors marks a significant paradigm in acceptance testing. This approach fosters a shared understanding among project stakeholders regarding the system's expected behavior, thereby facilitating clearer, more effective communication of requirements.

Acceptance testing frameworks, particularly when automated, play a vital role in guiding development teams towards delivering software that aligns with business goals and user expectations. By focusing on specifications and behaviors, teams can ensure that their testing efforts are both efficient and effective, ultimately leading to software products that meet or exceed the acceptance criteria.



### Business-Logic Acceptance Testing with pytest

> Develop a Purpose-Built Acceptance Testing Framework to Monitor Key Business Logic

Business-logic acceptance testing focuses on verifying and validating the components of software systems that are governed by specific business rules or principles. Such testing is essential for modules like a depreciation calculation engine in a fixed-asset accounting system, which must comply with generally accepted accounting principles (GAAP) and tax regulations. Analysts and testers play a pivotal role in detailing requirements and developing test cases to ensure these components function as intended. Automated acceptance testing frameworks can significantly aid developers by providing a structured way to validate these critical business-logic modules.

#### Automated Acceptance Testing for Business Logic

Automated acceptance testing can be particularly beneficial for testing individual business-logic modules without needing to integrate the entire system. This approach allows for continuous verification of modules such as calculation engines, which are often the cornerstone of systems in domains like payroll, insurance, banking, and benefits administration.

#### cceptance Testing a Calculation Engine

Consider a scenario where an analyst has prepared an Excel spreadsheet detailing test cases for a depreciation calculation engine. These spreadsheets include input variables and the expected results for each scenario, providing a structured basis for acceptance testing.

While Python does not directly interact with Excel spreadsheets, libraries such as `pandas` can be used to read spreadsheet data, and pytest can be utilized to automate the acceptance testing process.

##### Listing 4-?: Purpose-Built Acceptance Testing
```python
import pandas as pd
import pytest
from calculation_engine import depreciation_engine  # Hypothetical module

# Reading test data from an Excel spreadsheet
@pytest.fixture(scope="module")
def test_data():
    return pd.read_excel("test_cases.xlsx")

# Acceptance test for the depreciation calculation engine
@pytest.mark.parametrize("scenario", test_data().to_dict('records'))
def test_depreciation_calculation(scenario):
    # Arrange
    input_variables = {key: scenario[key] for key in scenario if key.startswith('input')}
    expected_result = scenario['expected_result']
    
    # Act
    actual_result = depreciation_engine.calculate(**input_variables)

    # Assert
    assert actual_result == expected_result, f"Scenario {scenario['name']}: Expected {expected_result}, got {actual_result}"
```

#### Key Benefits of This Approach

- **Focused Verification**: Allows for targeted testing of crucial business logic, independent of UI or database integration.
  
- **Continuous Validation**: Facilitates ongoing validation of business-logic modules, ensuring they meet acceptance criteria.

- **Collaborative Development**: Supports a collaborative approach to testing, with analysts and testers contributing to a comprehensive set of test cases.

A purpose-built acceptance testing framework, leveraging the capabilities of pytest and additional libraries for data management, provides an effective tool for ensuring the correctness and completeness of business-logic modules. This method underscores the importance of automated acceptance testing in the development process, offering a systematic approach to validating software against business requirements.


## Conclusion

### Overview of Testing Frameworks and Tools

Throughout this discussion, we've explored a variety of testing frameworks and tools, each offering unique features and capabilities tailored to different aspects of software testing. From unit testing frameworks like pytest and unittest to mock object frameworks for stubbing and interaction testing, these tools play a critical role in ensuring software quality and reliability. Additionally, we delved into database state management and discussed methodologies for user interface (UI) and acceptance testing.

In the context of Python development, pytest emerges as a versatile and widely adopted testing framework. It accommodates a broad spectrum of testing needs, from basic unit tests to complex functional testing scenarios, including database interactions and UI testing. Pytest's plugin ecosystem further extends its capabilities, allowing integration with other tools and frameworks for comprehensive testing coverage.

#### Mock Object Testing

For mocking and stubbing in Python, the `unittest.mock` module provides a powerful and flexible way to create mock objects and test double objects, facilitating the testing of interactions between components without relying on their actual implementations. This approach is instrumental in isolating the unit under test, enabling precise and focused verification of software behavior.

#### Database Testing

For database testing, libraries like `pytest-django` for Django applications or the use of `sqlalchemy` for ORM-based applications offer mechanisms to manage database state for testing. These tools allow developers to preload test data, execute tests in transactional scopes, and rollback changes to maintain a consistent database state across tests.

#### UI and Acceptance Testing

For UI and acceptance testing, Python developers can leverage tools such as Selenium WebDriver for web applications, offering automated browser control for testing web interfaces. Additionally, frameworks like `pytest-bdd` support behavior-driven development (BDD), enabling acceptance tests to be written in a natural, human-readable language that describes the application's behavior from a user's perspective.

#### Summary

The exploration of testing frameworks and tools underscores the importance of a comprehensive testing strategy that includes unit tests, mock object testing, database state management, and UI/acceptance testing. By leveraging the appropriate tools and methodologies, developers can ensure their software meets the highest standards of quality and reliability. In the Python ecosystem, pytest stands out as a central tool for achieving these testing goals, supported by a rich set of libraries and plugins that cater to a wide array of testing requirements.




[^1]: Martin Fowler provides a nice background on xUnit at http://martinfowler.com/bliki/Xunit.html 
[^2]: For more information see https://docs.pytest.org/en/latest/how-to/xunit_setup.html 


[Continue to Chapter 5](../ch05/chapter05.md)