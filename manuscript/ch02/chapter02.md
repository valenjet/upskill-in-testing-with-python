# Chapter 2

In this chapter we introduce the concept of a _code kata_ and the fundamentals of test-driven development (TDD).

## What is a _code kata_?

_Code kata_ is a term borrowed from martial arts, referring to a practice method in programming where developers engage in repetitive exercises to hone their skills. The idea is to perform these small, self-contained coding challenges repeatedly, each time trying to improve in some way, whether it be in code efficiency, design patterns, speed, or understanding of the language and its features. The term was popularized by Dave Thomas, co-author of "The Pragmatic Programmer," who likened the practice to karate exercises aimed at continuous improvement and mastery of programming techniques.

Code katas are designed to focus on the fundamentals of coding and software design, encouraging developers to explore new strategies, techniques, and technologies in a controlled, practice-based environment. They are not about finding a single correct answer to a problem, but rather about exploring different solutions and approaches, learning from each attempt, and gradually improving one's craft. By regularly practicing Code katas, developers can enhance their problem-solving skills, deepen their understanding of programming paradigms, and become more proficient in their chosen languages and tools.

## What is Test-Driven Development?

Test-Driven Development (TDD) is a software development methodology where tests are written before the actual code. The process follows a short, repeatable development cycle designed to ensure that code meets its requirements and is of high quality. The typical TDD cycle follows three basic steps, often described as red-green-refactor:

1. **Red**: Write a failing test. Before adding or modifying a feature, a developer writes a test that defines a desired improvement or new function. This test will naturally fail since the feature hasn't been implemented yet.

2. **Green**: Write the minimal amount of code required to make the test pass. This step involves writing just enough code to make the test succeed, thus meeting the requirements specified by the test.

3. **Refactor**: Clean up the new code, if necessary. After the test passes, the developer can refactor the code to improve its structure, performance, or readability while ensuring that the test still passes. This step helps maintain code quality and reduce technical debt.

The benefits of TDD include:
- **Improved Code Quality**: TDD leads to code that's more thoroughly tested and less prone to bugs.
- **Better Design**: The need to write tests first encourages better software design and more maintainable code.
- **Documentation**: Tests serve as documentation that explains what the code is supposed to do.
- **Confidence**: Developers can make changes or refactor code with confidence that existing functionality is preserved, as indicated by tests passing.

TDD is part of the Agile development methodologies and encourages a disciplined approach to programming, focusing on requirements and continuous feedback through testing.

### TDD and Thinking

In "The Art of Agile Development", James Shore explains that the first step in the TDD cycle is "Think". You want to be sure that the following steps (Red, Green, Refactor) are based on an understanding of the problem. Not in the larger sense of the word "problem" but in the simplest increment of behavior.

With the perspective of focusing on small increments of behavior during the "Think" step, the Test-Driven Development (TDD) cycle can be described as follows:

1. **Think (small)**: Before writing any code or tests, carefully consider only the next small increment of behavior that needs to be implemented. This step involves understanding the specific piece of functionality or improvement to be added, without getting lost in big upfront designs. The goal is to focus on what's immediately necessary, determining the simplest test that can drive the development of this new behavior.

2. **Red**: Write a failing test that defines the expected outcome of the small increment of behavior identified in the Think step. This test should initially fail because the functionality it describes does not yet exist. Writing this failing test first ensures that any new code written is directly tied to an improvement in functionality and adheres closely to the requirements.

3. **Green**: Implement just enough code to pass the failing test written in the Red step. The emphasis here is on simplicity and effectiveness, aiming to quickly achieve a passing state for the test with minimal code. This encourages writing code that is directly relevant to the feature or fix being developed, without over-engineering or introducing unnecessary complexity.

4. **Refactor**: Once the test passes, examine the code for opportunities to improve its structure, readability, or performance without altering its external behavior. This may involve cleaning up redundancies, applying design patterns where appropriate, or simplifying complex logic. Refactoring with the safety net of tests ensures that improvements do not break existing functionality.

By emphasizing thinking in small increments, the TDD cycle promotes a focused, efficient approach to software development. It encourages developers to maintain a narrow scope, reducing the risk of scope creep or becoming overwhelmed by the broader system's complexities. This iterative process leads to a well-designed, well-tested codebase that evolves incrementally with each cycle, ensuring steady progress and high-quality outcomes.

In [this blog post](https://www.kaizenko.com/what-is-test-driven-development-tdd/), Fadi Stephan illustrates the TDD Cycle like this:

![The TDD Cycle](https://www.kaizenko.com/wp-content/uploads/2019/06/kaizenko-Test-Driven-Development-TDD.png)


## Before We Start Coding

Let's look at the two additional lines in our `test_temperature_converter.py` file.

```python
import pytest

@pytest.mark.skip(reason="Not yet started")
def test_start():
    assert True == False
```

With `import pytest` we import the pytest module so that we can use the `@pytest.mark.skip()` marker.

The `skip` marker tells the pytest runner to skip the `test_start` function. The `reason` parameter is optional, but it’s helpful to provide a reason.

Running this command:
```zsh
$ pytest --verbose test_temperature_converter.py
```

Returns the following output:
```zsh
======================================= test session starts ========================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0 -- /Users/sdr/ ... /venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/sdr/ ... /code/ch02
collected 1 item                                                                                                                                                                                          

test_temperature_converter.py::test_start SKIPPED (Not yet started)                           [100%]

======================================= 1 skipped in 0.00s =========================================
```


## Fahrenheit to Celsius Code Kata

I have cousins who live in Ireland. Like much of the world, the local temperature there is reported in degrees Celsius. However, I live in the U.S. and our local temperature is reported in degrees Fahrenheit.

Occasionally, while we're messaging, I'd like to convert today's temperature in Fahrenheit to Celsius, so that I can chat with them about the weather.

Let's write that as a use case:
```text
As a friendly cousin,
I want to convert temperature in degrees Fahrenheit to degrees Celsius,
So that I can chat about the weather to my Irish cousins.
```

In this chapter, we will use TDD to write a Python program to convert a temperature in degrees Fahrenheit to its equivalent in degrees Celsius.


### Step 1: Think

Don't just think; _think small_.

*Question:* What is the absolutely smallest behavior you can think of?

For me, the smallest behavior is about the freezing temperature. I know that if it's 32°F outside then I say it's freezing. And I know that that's 0°C.

Let's make that our first test.

We want to test a temperature converter function named `convert` and check that it returns 0.

### Step 2: Red (test)

In this step, you should have one, and only one failing test.

We want to remove the import and the skip marker. Remove these lines and save:
```python
import python

@pytest.mark.skip(reason="Not yet started")
```


Your `test_temperature_converter.py` file should look like this:
```python
def test_start():
    assert convert() == 0
```

Running:
```zsh
$ pytest --verbose test_temperature_converter.py
```

Returns:
```zsh
============================================== test session starts ==============================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0 -- /Users/sdr/ ... /venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/sdr/ ... /code/ch02
collected 1 item                                                                                                

test_temperature_converter.py::test_start FAILED                                                          [100%]

=================================================== FAILURES ====================================================
__________________________________________________ test_start ___________________________________________________

    def test_start():
>       assert convert() == 0
E       NameError: name 'convert' is not defined

test_temperature_converter.py:4: NameError
============================================ short test summary info ============================================
FAILED test_temperature_converter.py::test_start - NameError: name 'convert' is not defined
=============================================== 1 failed in 0.01s ===============================================
```

#### Three Rules of TDD

TDD has three core rules[^2]:

* Only write production code to make a failing unit test pass.
* Only write enough of a unit test to make it fail, including compilation errors.
* Write only the necessary amount of production code required to pass the failing unit test.

[^2]: [Canon TDD](https://tidyfirst.substack.com/p/canon-tdd)


### Step 3: Green (code)

Then we need only add the `convert()` function to make the test pass, as follows:

```python
def convert():
    return 0

def test_start():
    assert convert() == 0
```

Running:
```zsh
$ pytest --verbose test_temperature_converter.py
```

Returns:
```zsh
============================================== test session starts ==============================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0 -- /Users/sdr/ ... /venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/sdr/ ... /code/ch02
collected 1 item                                                                                                

test_temperature_converter.py::test_start PASSED                                                          [100%]

=============================================== 1 passed in 0.00s ===============================================
```

### Huzzah!

We have 1 passing test! 🎉

Let's review the output.

You may have a couple of questions:

* Why isn't the `convert()` function seen as at test function?
* Why does pytest see `test_start()`  as a test function?

The answer is that `pytest` implements a standard test discovery convention described in the [Conventions for Python test discovery](https://docs.pytest.org/en/latest/explanation/goodpractices.html#conventions-for-python-test-discovery) of the documentation.

Here's what you need to know:

1. `pytest` looks in the current directory and recursively into sub-directories.
2. In those directories, it searches for `test_*.py` files.
3. From those files, `pytest` collects test items that are:
  - `test` prefixed test functions or methods outside of class
  - `test` prefixed test functions or methods inside `Test` prefixed test classes

NOTE: We're not going to show examples of how to customize test discovery. However, the folks at `pytest` have documented [Changing standard (Python) test discovery](https://docs.pytest.org/en/latest/example/pythoncollection.html#changing-standard-python-test-discovery).


### Step 4: Refactor

We want to clean up or refactor our code. Let's move the `convert()` function to its own file with the name `temperature_converter.py`.

1. Create the `temperature_converter.py` file.
2. From the `test_temperature_converter.py` file, move this code to the new file:
```python
def convert():
    return 0
```
3. Now, save the `temperature_converter.py` and `test_temperature_converter.py` files.

Running:
```zsh
$ pytest --verbose test_temperature_converter.py
```

Returns:
```zsh
============================================== test session starts ==============================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0 -- /Users/sdr/ ... /venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/sdr/ ... /code/ch02
collected 1 item                                                                                                

test_temperature_converter.py::test_start FAILED                                                          [100%]

=================================================== FAILURES ====================================================
__________________________________________________ test_start ___________________________________________________

    def test_start():
>       assert convert() == 0
E       NameError: name 'convert' is not defined

test_temperature_converter.py:2: NameError
============================================ short test summary info ============================================
FAILED test_temperature_converter.py::test_start - NameError: name 'convert' is not defined
=============================================== 1 failed in 0.01s ===============================================
```

This failed test is tell you that you need to add the following line to the `test_temperature_converter.py` file so that the function name 'convert' is defined.
```python
from temperature_converter import convert
```

Adding this import to the top of `test_temperature_converter.py` and save.

The `test_temperature_converter.py` file should contain:
```python
from temperature_converter import convert

def test_start():
    assert convert() == 0
```

Running:
```zsh
$ pytest --verbose test_temperature_converter.py
```

Returns:
```zsh
============================================== test session starts ==============================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0 -- /Users/sdr/ ... /venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/sdr/ ... /code/ch02
collected 1 item                                                                                                

test_temperature_converter.py::test_start PASSED                                                          [100%]

=============================================== 1 passed in 0.00s ===============================================
```

### Huzzah!

You have successfully refactored and you are back to 1 passing test! 🎉

Let's go back to thinking again.

### Step 1: Think

Again, we have to _think small_.

*Question:* What is the next smallest behavior you can think of?

For me, the next smallest behavior is about the boiling temperature of water. I know from science class that water boils at 212°F and at 100°C.

Let's make that our second test.

We want to test our `convert()` function and check that it returns 100°C when we pass it 212°F.

I think we're going to need a parameter, but let's focus on adding one failing test.

### Step 2: Red (test)

Let's add this failing test to the bottom of the `test_temperature_converter.py` file:
```python

def test_when_passed_212_expect_100():
    assert convert(212) == 100
```

Save `test_temperature_converter.py` and run:
```zsh
$ pytest --verbose test_temperature_converter.py
```

This returns:
```zsh
============================================== test session starts ==============================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0 -- /Users/sdr/ ... /venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/sdr/ ... /code/ch02
collected 2 items                                                                                               

test_temperature_converter.py::test_start PASSED                                                          [ 50%]
test_temperature_converter.py::test_when_passed_212_expect_100 FAILED                                     [100%]

=================================================== FAILURES ====================================================
________________________________________ test_when_passed_212_expect_100 ________________________________________

    def test_when_passed_212_expect_100():
>       assert convert(212) == 100
E       TypeError: convert() takes 0 positional arguments but 1 was given

test_temperature_converter.py:7: TypeError
============================================ short test summary info ============================================
FAILED test_temperature_converter.py::test_when_passed_212_expect_100 - TypeError: convert() takes 0 positional arguments but 1 was given
========================================== 1 failed, 1 passed in 0.01s ==========================================
```

We can see
* `test_temperature_converter.py::test_start` PASSED, as expected.
* `test_temperature_converter.py::test_when_passed_212_expect_100` FAILED, also as expected.

This is a good thing!

### Step 3: Green (code)

Then we need only add the parameter `fahrenheit` to the `convert()` function to make the test pass, as follows:

```python
def convert(fahrenheit):
    if fahrenheit == 212:
        return 100
    return 0
```

Running:
```zsh
$ pytest --verbose test_temperature_converter.py
```

Returns:
```zsh
============================= test session starts ==============================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0 -- /Users/sdr/ ... /venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/sdr/ ... /code/ch02
collected 2 items                                                              

test_temperature_converter.py::test_start FAILED                         [ 50%]
test_temperature_converter.py::test_when_passed_212_expect_100 PASSED    [100%]

=================================== FAILURES ===================================
__________________________________ test_start __________________________________

    def test_start():
>       assert convert() == 0
E       TypeError: convert() missing 1 required positional argument: 'fahrenheit'

test_temperature_converter.py:4: TypeError
=========================== short test summary info ============================
FAILED test_temperature_converter.py::test_start - TypeError: convert() missing 1 required positional argument: 'fahrenheit'
========================= 1 failed, 1 passed in 0.01s ==========================
```

Oops! It's good that `test_temperature_converter.py::test_when_passed_212_expect_100` PASSED, as expected. However, `test_temperature_converter.py::test_start` FAILED.

The error explains:
```zsh
convert() missing 1 required positional argument: 'fahrenheit'
```

Let's add a reasonable default so that that test will pass again. Here's the new `convert()` function:
```python
def convert(fahrenheit=0):
    if fahrenheit == 212:
        return 100
    return 0
```

Save all the files.

Now, running:
```zsh
$ pytest --verbose test_temperature_converter.py
```

Returns:
```zsh
======================================================= test session starts ========================================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0 -- /Users/sdr/ ... /venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/sdr/ ... /code/ch02
collected 2 items                                                                                                                  

test_temperature_converter.py::test_start PASSED                                                                             [ 50%]
test_temperature_converter.py::test_when_passed_212_expect_100 PASSED                                                        [100%]

======================================================== 2 passed in 0.00s =========================================================
```


### Step 4: Refactor

Nothing says we have to refactor. If we're happy with everything as it stands, we can certainly move back to Step 1.

For me, the test function name `test_start` is not descriptive of the test. This is really supposed to check that when the `convert()` function is passed 32 it should return 0. Let's rename that test to `test_when_passed_32_expect_0`.

The refactored tests look like this:
```python
from temperature_converter import convert

def test_when_passed_32_expect_0():
    assert convert(32) == 0

def test_when_passed_212_expect_100():
    assert convert(212) == 100
```

Running:
```zsh
$ pytest --verbose test_temperature_converter.py
```

Returns:
```zsh
======================================================= test session starts ========================================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0 -- /Users/sdr/ ... /venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/sdr/ ... /code/ch02
collected 2 items                                                                                                                  

test_temperature_converter.py::test_when_passed_32_expect_0 PASSED                                                           [ 50%]
test_temperature_converter.py::test_when_passed_212_expect_100 PASSED                                                        [100%]

======================================================== 2 passed in 0.00s =========================================================
```

### Huzzah!

We've successfully refactored the tests and are back to 2 passing test! 🎉

Let's start thinking again.


### Step 1: Think

Although we alway want to _think small_, as we perform TDD our understanding grows. Our thinking can grow as our understanding grows.

The key concept with thinking: **keep the incremental changes small**
