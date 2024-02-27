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

Running
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


### Step 1: Think (small)

*Question:* What is the absolutely smallest behavior you can think of?

For me, the smallest behavior is about the freezing temperature. I know that if it's 32°F then I say that the temperature is 0°C.

Let's make that our first test.

We want to test a temperature converter function named `converter` and check that it returns 0.

First, we need to remove the line:
```python
@pytest.mark.skip(reason="Not yet started")
```

Then we add the `converter()` function, as follows:

```python
import pytest

def converter():
    return 0

def test_start():
    assert converter() == 0
```
