# Chapter 3: Automated Testing

So, this section of our coding adventure is NOT about the usual QA-style automated testing. Nope, it's all about us, the devs, and the kind of automated checks we do to make sure our code is doing exactly what we think it's doing. Whenever we talk about "testing" in these pages, imagine us putting on our detective hats to do some serious intention checking on our code.

Now, for the nitty-gritty of test-driven development (TDD) and that awesome cycle of red, green, and refactor, you’ll want to jump back to Chapter 2. There’s a ton of good stuff there and even more in the wild world of books, blogs, and the interwebs. And hey, check out Appendix A for a treasure trove of resources on TDD and test writing how-tos.

This chapter? It’s all about sharpening your testing skills with a focus on:
- Clarity: Crafting tests that speak for themselves
- Durability: Ensuring your tests can stand the test of time
- Hands-off: Aiming for tests that run themselves without a fuss

Automated testing is our best bud because it catches issues early, keeps future changes from turning into nightmares, shows how different code pieces should play nice together, and, of course, ensures our code is solid from the get-go.

And it’s not just about unit tests. We’re diving into a whole toolbox of testing types that can help us out, like:
- Unit testing (the bread and butter)
- Seam testing (a cool technique we’ll get into later)
- Integration testing, but make it automated
- Smoke testing (not as fun as it sounds)
- Keeping things stable and speedy with stability and performance tests
- Making sure our database isn’t going rogue

Seam testing is something special we’ll meet down the line. And let’s be real, the universe of automated testing is vast. We can’t possibly cover every single awesome technique out there, but grab onto the core ideas, and you’ll be set to apply them in all sorts of ways.

Here’s what we’re focusing on:
- Prioritize tests that won’t drive you nuts to maintain
- Pick names for your tests that actually tell you what they’re about
- Embrace the Arrange-Act-Assert pattern to keep things tidy
- Short and sweet tests for the win
- Keep it to one test-action per test
- Stick to one primary thing you’re checking per test
- Leave type hints out of your test code
- Use a `TestsContext` class to cut down on the chaos
- `TestHelper` classes are your friend for reusing bits of test code
- Use data-driven tests to cover more ground with less code
- Don’t forget boundary-value analysis to catch all those edge cases
- Stubs are the secret weapon for isolation
- Keep it to one mock per test when you’re checking interactions

Let's dive in and make our tests as smart as our code.


## Focus on Writing Maintainable Test Code

### Test Code Maintainability

Let's talk about something that doesn't get enough love in our world: making our test code not just work, but work beautifully. Yeah, I’m talking about readability and maintainability. You know the drill - you spend a lot of time writing tests, only to see them collect digital dust because they’re too darn complex or they break at the drop of a hat. It's super frustrating, right? You start wondering why you even bothered.

But here’s the kicker: a big reason why test code gets ditched is because it’s a pain to keep up with. We've all been there, trying to decode or fix test code that feels like it's held together with duct tape. The thing is, test code is just like any other code - it needs some TLC to stay useful. Testing a single method might need a half dozen test cases, and if each one is a headache to maintain, well, it's gonna feel like a chore.

So, what’s the game plan? It's all about keeping that test code as tidy and trouble-free as you can. If your test code is easy to handle, it stays valuable and doesn’t end up being a waste of your time and energy. This bit we're diving into? It's all about tricks and tips to keep your test code in top shape, making sure it’s helping, not hindering, your projects. Let’s save our test code from becoming digital fossils and keep it as lively and useful as the day we wrote it.

Here is a list of ways to make sure test code is maintainable:
* Adopt an effective naming convention for test namespaces, classes, and methods.
* Use a pattern for the test method body.
* Keep test methods short; strive for fewer than ten lines of code.
* Limit the test actions to one or two lines of code.
* Make one and only one primary assertion in the test method.
* Create a context class to encapsulate repeating arrangement code.
* Write helper classes to hold code that is common to tests across the suite.
* Pass data as arguments into the test method to data-drive the testing.


### Naming Convention

Diving into the jungle of test code naming conventions, you'll find a bunch of different paths, each with its own cheerleaders and naysayers. This book goes with the flow of the [Conventions for Python test discovery](https://docs.pytest.org/en/latest/explanation/goodpractices.html#conventions-for-python-test-discovery) that `pytest` uses.

Here’s the lowdown on how `pytest` finds tests:
- If you don’t tell it otherwise, `pytest` starts looking for tests where you are, in the current directory. You can change things with command line arguments, pointing it at specific directories or files, or set up a `testpaths`.

- It will look in subdirectories, unless the subdirectory is on the `norecursedirs` list.

- Within those directories, it’s looking for files named `test_*.py` (or named `*_test.py`).

#### Test Functions

`pytest` collects test items from within theses `test_*.py` files. It looks for functions outside classes that start with `test_`.

So, for every test function outside a class, we'll start its name off with `test_`, such as `test_whatchamacallit`.

Three important facts need to be clear from the test function's name:
- Method-under-test
- Conditions under which the test is performed
- Expected result needed to pass the test

The test method naming convention fits a readability pattern and clearly communicates the intention of the test. The following are examples of test methods that follow the naming convention:
- `test_compute_payment_with_provided_loan_data_expect_proper_amount`
- `test_approve_loan_when_loan_data_is_valid_expect_loan_save_called_exactly_once`
- `test_compute_balance_for_negative_balance_scenarios_expect_out_of_range_error`

This test function naming convention is used by the code samples and throughout the book. The important principle is to establish a naming convention that clearly states how the system-under-test is expected to behave under the conditions provided by the test.

#### Test Classes

Also, `pytest` collects test classes from within the `test_*.py` files it discovers. It looks for classes that start with a `Test` prefix (and no `__init__` method). For example, a class that start them with a `Test` prefix, such as `TestWhatchamacallit`, is a test class. Again, it looks for methods of the `Test` class that start with `test_`.

Up until now, we've been writing test functions and organizing them into test modules within a directory in the file system. This approach does a pretty good job and meets the needs of most projects.

By using a _Test class_ approach, `pytest` does allow us to group tests together using classes. The can be helpful.

#### Directory and file structure

- For files, we'll be starting with `test`, like `test_whatchamacallit.py`
- Putting tests into an extra directory outside the system-under-test code is useful

##### Listing 3-1: Tests file structure
```
.
├── pyproject.toml
├── src
│   └── mypkg
│       ├── __init__.py
│       ├── app.py
│       ├── view.py
│       └── db.py
├── tests
│   ├── app
│   │   ├── __init__.py
│   │   ├── test_delete.py
│   │   ├── test_list.py
│   │   ├── test_update.py
│   │   └── test_version.py
│   ├── view
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── test_delete.py
│   │   ├── test_list.py
│   │   ├── test_update.py
│   │   └── test_version.py
│   └── conftest.py
```

**NOTE:** We'll cover the `conftest.py` files and the special `__init__.py` files you see under the `tests` folder in a later section. We'll also revisit the topic of how to abbreviate test function names when they get too long.


#### Naming Is Important

Since test code is a lot different than production code and serves a completely different purpose that the code-under-test, we name test functions differently.

We use a naming convention for our test code that's clear and makes our lives easier when test fail.

We want to pinpoint why the test failed without needing to decipher the output. We keep the function names distinct, structured, and clear. This makes our test code as maintenance-friendly as possible.

The naming convention presented here is helpful in these ways:
- The test directory and filename identifies the modules being tested.
- The test function name describes two key aspects of the test:
  - The function under test
  - Conditions of the test
  - Expected results of the test
- The test class name identifies the class-under-test, which is the class that the tests are testing.

For example, in Chapter 2, the `test_temperature_converter.py` file contained the `test_when_passed_10000_pt_1_expect_raises_message` function:
- tests the temperature converter (we get that from the file name)
- when passed 10000.1 as input
- expect that it raises an error with a message

That's the idea for now.


### Is it expected/actual or actual/expected order

#### JUnit
`assertEquals(expected, actual)`

#### pytest

`assert actual == expected`

For example:
```python
def test_actual_versus_expected():
    expected = 'blue`
    actual = 'gold'
    assert actual == expected
```

### Test Function Structure

It is imperative for the test function structure to adhere to a consistent convention. This uniformity ensures that all developers within a project can easily locate and comprehend the test code. Adherence to a common convention accelerates familiarity and efficiency, especially when extended across the entire organization. Such consistency facilitates smoother transitions for developers joining new projects or initiating new endeavors.

### Arrange-Act-Assert Framework

While various methodologies exist for structuring test functions, the Arrange-Act-Assert (triple-A or 3As) framework stands out for its effectiveness and widespread adoption. This framework segments the test function into three distinct sections:

- **Arrange**: This section of the test function is dedicated to setting up preconditions and dependencies. It involves initializing the class or object under test and assigning any necessary values required for the test scenario.
  
- **Act**: This segment of the test function executes the specific actions or operations that are being tested. It is the core phase where the test's main functionality is performed.
  
- **Assert**: The final section focuses on validating the outcomes of the test. It verifies that the results meet the expected conditions, and it will trigger a failure if the test does not conform to the anticipated outcomes.

Incorporating comments such as `# Arrange`, `# Act`," and `# Assert` within the test code is a recommended practice. These comments serve as clear markers delineating each section, thereby enhancing the readability and maintainability of the test code.

Here is an example that uses the `TestLoan` class to group tests that test the `compute_payment()` method of the `Loan` class.

##### Listing 3-2: Using the `TestLoan` class to group tests
```python
# test_loan.py

from loan import Loan

class TestLoan():

    def test_compute_payment_with_provided_loan_data_expect_proper_payment_amount(self):
        # Arrange
        loan = Loan(
            principal=12000,
            annual_percentage_rate=12
        )

        # Act
        actual = loan.compute_payment(300)

        # Assert
        assert actual == 126.39
```


### Keep Test Short

> Prefer Many Short Tests Over Few Long Tests

#### Simplifying Test Method Complexity

Maintaining brevity within test methods is crucial for readability and comprehension. Short test methods simplify the management of test complexity, proving particularly beneficial when diagnosing and resolving issues with tests developed by others. A variety of factors, such as new requirements, inconsistent behaviors, or obsolete test cases, can cause a test to fail following modifications to the codebase. Each test method should clearly delineate the functionality of the code under test and its expected behavior.

#### Principle of Singular Focus in Test Methods

Adhering to the principle that each test method should verify a single specific intention is essential for enhancing the longevity and utility of test code. This approach facilitates rapid identification and resolution of failures by any developer, reducing the likelihood of tests being overlooked or ignored. The simplicity and focus of short, well-defined test methods increase the willingness and ability of developers to address and rectify issues promptly.

### Limit Test Actions

> Avoid More Than One Line of Action

#### Streamline Test Actions for Clarity

In the context of constructing a test, particularly within the "Act" section, it's important to adhere to the principle of minimalism. A common pitfall is the incorporation of multiple actions within a single test, which not only complicates the test but also might require extensive setup code. The objective is to refine the "Act" section to a singular, clear line of code whenever possible. The primary rationale behind this approach is to simplify debugging when a test fails. Multiple actions within a test can hide the root cause of failure, requiring additional effort to pinpoint the exact line responsible.

Consider a scenario in a `pytest` framework where the "Act" section comprises five lines of code. Should an error arise within the `Get` method, distinguishing whether the first or second invocation of `Get` is at fault becomes less straightforward. Moreover, in the event of a test failure, identifying the specific action line that triggered the issue becomes a challenge. This underscores the importance of limiting actions within the "Act" phase to enhance test clarity and facilitate easier troubleshooting.

##### Listing 3-3: Too many actions in the Act step
```python
# test_application.py

from application import Application

# Test function with too many actions in the Act step
def test_save_when_principal_is_changed_expect_new_principal_value_in_database():
    """
    Test case: Too many actions in the Act step
    When the principal is changed, expect the new principal value in the database.
    """
    # Arrange
    class_under_test = Application()
    class_under_test.principal = 999.91
    class_under_test.save()
    id = class_under_test.id

    # Act
    class_under_test.get(id)
    class_under_test.principal = 1009.81
    class_under_test.save()
    actual = class_under_test.get(id)

    # Assert
    assert actual.principal == 1009.81, "Expected the principal value to be updated in the database"
```

### Simplification of Action Steps in Test Functions

In the example provided as Listing 3-4, the test method is structured to contain a single action within the _Act_ section, specifically invoking the `save` method of the `Application` class. This illustrates the principle of focusing each test on a specific action, which is stated in the test function's name. Notice that the _Arrange_ section is intentionally more involved. We'll explore that topic in a later discussion.

For the purpose of maintaining high readability and clarity within test code, it's recommended that you limit the _Act_ section to a single line of action. This practice ensures that the test's intent remains focused and straightforward.

Additionally, something worth noting is the use of the hard-coded value `97` at multiple points within the test. Subsequent sections will discuss techniques to parameterize such values, allowing them to be injected into the test method as arguments, thereby enhancing the test's flexibility and reducing redundancy.

##### Listing 3-4: Only one action in the Act step
```python
# test_application.py

from application import Application

from application_tests_context import ApplicationTestsContext
# Assume that the ApplicationTestsContext class is defined 
# with the necessary retrieve method

# Test function with only one action in the Act step
def test_save_when_principal_is_changed_expect_new_principal_value_in_db():
    """
    Test case: Only one action in the Act step
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
    actual = tests_context.retrieve(97) # Retrieve the Application from the database.
    assert actual.principal == expected_principal

```

### Primary Assertion

> Avoid More Than One Primary Assertion

When designing test methods, it's crucial to maintain a narrow focus by limiting each function to one primary assertion.

This principle ensures that:
- tests' _Assert_ section are straightforward
- tests directly verify the functionality described in the test function's name

#### Avoiding Multiple Primary Assertions

For clarity and precision, tests should avoid including more than one primary assertion.

Consider a test function named `test_expect_correct_payment_amount_of_126_39`; its primary assertion should validate that the actual payment amount matches the expected value of $126.39.

This approach minimizes ambiguity, ensuring that if the test fails, the reason is clearly related to the test's primary focus.

#### Types of Assertions

Assertions can be categorized based on their verification methods, including:

| ||
|:---|:---|
| Comparison | Validating the equivalence, difference, or relational comparison between expected and actual values. |
| Expected Interaction | Ensuring a dependency is called a specific number of times, with certain arguments, or validating that it is not called with invalid arguments. |
| Exception Handling | Confirming an expected exception is thrown under specific conditions. |
| Collection Assertions | Verifying the presence or absence of elements within a collection. |
| Instance Verification | Checking whether an object is null, not null, or an instance of a specific type. |
| Boolean Checks | Assessing the truthfulness of an expression. |
| Constraint-Based | Evaluating whether an instance meets a set of defined constraints. |

#### Primary Versus Secondary Assertions

The concept of a primary assertion raises the question of secondary assertions.

Secondary assertions are additional checks that, while useful, are less critical than the primary assertion. They often _precede_ the primary assertion to clarify the _secondary_ reasons why a test may fail. Secondary assertions can make explicit any implicit assumptions, turning them into direct assertions for clearer understanding.

#### Guard and Secondary Assertions

In addition to secondary assertions within the _Assert_ section, "guard assertions" in the _Arrange_ section help clarify the conditions necessary for the _Act_ section to proceed correctly. These assertions explicitly state assumptions critical to the test's setup, providing clarity and avoiding ambiguous failures.

##### Listing 3-5: Guard and Secondary Assertion
```python
# test_application.py

import pytest

from application import Application

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
```

#### Caution Against Over-Specification

While guard and secondary assertions are useful, it's important to avoid over-specifying test expectations.

Secondary assertions _should only support_ reaching the primary assertion, without introducing unnecessary complexity or maintenance overhead.

##### Listing 3-6: Over-Specified Expectations
```python
# test_loan.py

import pytest

from loan import Loan

def test_compute_payment_when_invalid_term_in_months_is_zero_expect_value_error():
    """
    Test that providing a zero value for term_in_months to compute_payment raises a ValueError.
    """
    # Arrange
    class_under_test = Loan(principal=7499, annual_percentage_rate=1.79)

    # Act
    with pytest.raises(Exception) as exc_info:
        class_under_test.compute_payment(0)

    # Assert
    assert exc_info.type == ValueError
    assert "term_in_months" in str(exc_info.value), "Expected an error for invalid 'term_in_months' parameter"
```

Now take a look at Listing 3-6; there are two assertions. Together these assertions over-specify the requirements of the code-under-test:
- Is there really a requirement that the `compute_payment` method’s parameter be named `term_in_months`?
- Will the message in the exception change over time?

If we really need to test the exception message, it should really be in a separate test function.


### Test Context Classes

> Use a Tests Context Class to Reduce Repetition and Manage Complexity

### Test Context Classes Enhance Maintainability

As tests evolve to cover more complex scenarios, the code within the _Arrange_ section of the test method can become very lengthy, leading to repetition across test methods. To streamline this process and manage the complexity, using a "Test Context Class" is recommended.

#### The Test Context Class

The introduction of a "Test Context Class", following the Library Class pattern[^1], offers a structured solution to minimize redundant setup code in tests. This strategy involves creating a class equipped with static methods that encapsulate common arrangement tasks tailored to specific tests. This approach not only reduces code duplication but also enhances the readability and maintainability of test code.

#### Implementing a Test Context

To illustrate this concept in Python using the `pytest` framework, consider transitioning duplicate test code into a dedicated context class. This class will contain static methods responsible for creating instances and setting up mocks or stubs as required. Listing 3-7 provides an example.

##### Listing 3-7: Test Context for Testing Application
```python
# application_tests_context.py

from student import Student
from application import Application

class ApplicationTestsContext:
    @staticmethod
    def create_instance(student=None):
        # Create and return an Application instance with defaults or provided repositories
        application = Application()

        # Setup default properties for the application instance
        if student == None:
          application.student = Student('Last', 'First')
        else:
          application.student = student

        return application
```

```python
# test_application.py

from application_tests_context import ApplicationTestsContext

from student import Student
from application import Application

def test_save_with_valid_new_application_expect_application_repo_create_called_once():
    # Arrange
    student = Student('Smith', 'John')
    class_under_test = ApplicationTestsContext
        .create_instance(student)

    application_id = class_under_test.id
    class_under_test.student.last_name = 'Jones'

    # Act
    class_under_test.save()

    # Assert
    actual = class_under_test.get_by_id(application_id)
    assert actual.student.last_name == 'Jones'
```

##### Key Considerations

- **Maintain Test Isolation**: The test context class should be used exclusively within the scope of its corresponding test class to prevent unintended dependencies between tests.
- **Avoid Test Class Inheritance**: While tempting, using inheritance to share code between test classes can introduce maintenance challenges. A notable exception is leveraging a base test class for shared testing infrastructure, which does not compromise test isolation. This is an advanced topic we hope to cover later.

By adopting a Test Context Class, developers significantly reduce the redundancy of setup code across tests, making the tests easier to read, write, and maintain. This practice aligns with the goal of keeping test methods focused and manageable, especially as the complexity of the scenarios they cover increases.


### Reusable Test Helper Classes

> Build Test Helper Classes to Promote Reuse

To enhance code reuse across test suites, implementing "Test Helper Classes" is a good approach, analogous to employing a "Test Context Class".

These _helper classes_ leverage the Library Pattern to consolidate commonly used test code. This facilitate building up a repository for shared test functions and code that's applicable across various tests.

#### Strategy for Reuse Through Test Helpers

Test Helper Classes provide functions that address general needs across multiple testing scenarios. This approach ensures that reusable code is accessible, maintaining a focus on broad applicability rather than being tailored to specific test cases.

#### Implementing Test Helper Functions

Consider translating the concept of generating random strings for test data. Such a utility can be particularly useful for generating dynamic values like names, addresses, or any string-based data, with the flexibility to specify length or complexity through optional parameters. Listing 3-8 provides the `build_name_string` function as an example of how to generate random names.

**NOTE:** Because `pytest` ignores classes that do not begin with 'Test', we use the `helper_test*.py` file name and prefix these class names with `HelperTest`.

##### Listing 3-8: Test Data Helper
```python
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
```

Now, `build_name_string` generates a large random name.
```python
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
```

#### Guidelines for Test Helper Utilization

- **Generalization over Specialization**: Test helpers should be designed to provide utility across the testing spectrum without embedding logic specific to the system under test. This ensures their relevance and applicability across different test scenarios.
  
- **Domain-Specific Logic**: Avoid incorporating application-specific logic within test helpers. That risks coupling test suites too closely, potentially leading to widespread changes if domain-specific assumptions are altered. Helpers should remain as agnostic as possible to the domain of the application being tested.

By adhering to these practices, developers can create a suite of Test Helper Classes that significantly reduce redundancy and enhance the efficiency of the testing process. This approach promotes a more organized and maintainable testing framework, enabling developers to focus on the specifics of each test case without duplicating common setup or utility code.

### Data Scenarios

> Data-Drive Test Methods for Multiple Test Cases

#### Leverage Data-Driven Testing

In the development of comprehensive test suites, it becomes obvious that many test methods can be structurally identical, differing only in the data that each test uses. To address this, `pytest` offers functionality to execute a single test method with varying sets of input data. This can enhance test coverage without multiplying the test code unnecessarily.

#### Data-Drive Test Functions

Data-driven testing allows for the efficient checking of multiple scenarios using a single test function, by feeding it different sets of input values and expected values. This approach significantly reduces the test code maintenance burden by consolidating what would otherwise require multiple individual test methods.

#### Implementing Data-Driven Tests

The `pytest` framework supports parameterized testing. Listing 3-9 shows how to use the `pytest.mark.parametrize` decorator for data-driven testing.

##### Listing 3-9: Using the `parametrize` keyword
```python
# test_loan.py

import pytest

from loan import Loan

@pytest.mark.parametrize("principal, annual_percentage_rate, term_in_months", [
    (7499, 1.79, 0),
    (7499, 1.79, -1),
    (7499, 1.79, -73),
    (7499, 1.79, MIN_INT),
    (7499, 1.79, Loan.MAX_TERM_IN_MONTHS + 1),
    (7499, 1.79, Loan.MAX_TERM_IN_MONTHS * 5),
    (7499, 1.79, MAX_INT),
])
def test_compute_payment_with_invalid_term_in_months_expect_value_error_exception(
        principal, annual_percentage_rate, term_in_months):

    # Arrange
    loan = Loan(principal, annual_percentage_rate)
    
    # Act & Assert
    with pytest.raises(ValueError):  # expect the ValueError exception
        loan.compute_payment(term_in_months)
```

#### Practical Tips for Data-Driven Testing

- **Use of Prime Numbers**: To reduce the risk of coincidental arithmetic, using prime numbers in test data is recommended. This helps ensure that test validations are genuine and not accidentally passing due to arithmetic coincidences.

A common coincidental arithmetic problem occurs when a test uses the number 2. These three expressions: `2 + 2`, `2 * 2`, and `2**2` all equal to 4. When using the number 2 as a test value, there are many ways the test falsely passes. Arithmetic errors are less likely to yield an improper result when the test values are different prime numbers. Consider a loan that has a principal of $12,000.00, a term of 360 payments, an annual interest rate of 12%, and, of course, there are 12 months in a year. Because there is a coincidental factor of 12 in all these numbers, that data scenario yields a lot of very bad test cases.

For this reason, prefer large prime numbers like 73 or 7499. Pick decimals like 1.79 or 15.43 to avoid these arithmetic coincidences. Consider bookmarking this list of [The First 1,000 Primes](https://t5k.org/lists/small/1000.txt).
  
- **Avoiding Hardcoded Strings**: For dynamic test data, especially where uniqueness is crucial, avoid hardcoded strings. Use a Test Helper Class function to generate something unique and variable. These helpers can make the input consistently large and random.

Through data-driven testing, developers can achieve thorough coverage with fewer test methods, streamlining the testing process and maintaining code simplicity. This approach not only enhances the efficiency of writing and maintaining tests but also contributes to the reliability and robustness of the software testing strategy.


## Conclusion

Here’s a cheat sheet to make your test code better:
- **Naming is important**: Pick the right naming convention for your test functions, classes, modules and folders.
- **Use a consistent pattern for the test method body**: Consistency is key.
- **Short and sweet**: Aim to keep your test methods under ten lines.
- **Limit the test actions to one or two lines of code**: Don’t make your tests run a marathon.
- **One primary assertion rule**: Focus to one primary thing you’re checking per test.
- **Context classes are your friends**: Test code that sets up your tests goes in a context class.
- **Helper classes to the rescue**: Common code across your tests? Offload it into helper classes.
- **Data-drive your tests**: Feeding different data into your tests? Pass them as parameters.

### Comprehensive Test Method Implementation

The following Python code exemplifies the application of best practices in unit testing as outlined. This test method incorporates:

- A clear naming convention
- The Arrange-Act-Assert (AAA) pattern for structured testing
- Concise arrangement of test data
- A singular action within the test
- One assertion per test case to validate the expected outcome
- Data-driven approach to evaluate multiple scenarios within a single test method
- Utilization of prime numbers to enhance the reliability of test outcomes and facilitate debugging


Listing 3-10 shows test code that follows the recommended approach. It applies a data-driven approach to validate the functionality of a loan payment computation across several scenarios. By adhering to these practices, you can be sure that your tests are both efficient and effective, facilitating easier maintenance and debugging.

##### Listing 3-10: Putting it all together
```python
# test_loan.py

import pytest

from loan import Loan
from decimal import Decimal

# Data-drive the test function with multiple data sets
@pytest.mark.parametrize("principal, annual_percentage_rate, term_in_months, expected", [
    (7499, 1.79, 113, Decimal('72.16')),
    (8753, 6.53, 139, Decimal('89.92')), # use prime or arbitrary numbers in test data
    (61331, 7.09, 359, Decimal('412.08')),
])
def test_compute_payment_with_provided_loan_data_expect_proper_monthly_payment(
        principal, annual_percentage_rate, term_in_months, expected):
    """
    Test to verify that the Loan.compute_payment method calculates the correct 
    monthly payment given specific loan data.
    """
    # Arrange
    loan = Loan(principal, annual_percentage_rate)

    # Act
    actual = loan.compute_payment(term_in_months)

    # Assert
    assert actual == expected, "Computed payment does not match the expected payment."
```


[^1]: The Library Pattern is described by Kent Beck in _Implementation Patterns_ (Upper Saddle River, NJ: Addison-Wesley Professional, 2008).

[Continue to Chapter 4](../ch04/chapter04.md)