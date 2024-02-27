# Fahrenheit to Celsius Code Kata 

In Chapter 2, we use TDD to write a Python program to convert a temperature in degrees Fahrenheit to its equivalent in degrees Celsius.

To learn more, please read the:
* [What is a _code kata_?](/manuscript/ch02/chapter02.md#what-is-a-code-kata) section in Chapter 2.
* [What is Test-Driven Development?](/manuscript/ch02/chapter02.md#what-is-test-driven-development) section in Chapter 2.

## Too Long; Didn't Read

This README file is the TL;DR version of Chapter 2. If you want the complete explanation, you may want to read [Chapter 2](/manuscript/ch02/chapter02.md).

## Fahrenheit to Celsius Code Kata

We'll use TDD to write a Python function to convert a temperature in degrees Fahrenheit to its equivalent in degrees Celsius.

## Iteration 1

### Step 1: Think (🤔)

The smallest behavior is to return 0. We'll make that our first test.

Test a temperature converter function named `converter` and check that it returns 0.

### Step 2: Test (red 🔴)

We should have one, and only one failing test.

In the `test_temperature_converter.py` file, remove theses import and the skip marker lines:
```python
import python

@pytest.mark.skip(reason="Not yet started")
```

Your `test_temperature_converter.py` file should look like this:
```python
def test_start():
    assert convert() == 0
```

Run this command:
```zsh
$ pytest --verbose test_temperature_converter.py
```

It should return:
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

### Step 3: Code (green 🟩)

Add the `convert()` function to make the one test pass:

```python
# test_temperature_converter.py

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

We now have 1 passing test! 🎉


### Step 4: Refactor (tidy 🧹)

We want to clean up or refactor our code. Let's move the `convert()` function to its own file with the name `temperature_converter.py`.

1. Create the `temperature_converter.py` file.
2. From the `test_temperature_converter.py` file, move this code to the new file:
```python
# temperature_converter.py

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
from temperature_converter import converter
```

Adding this import to the top of `test_temperature_converter.py` and save.

The `test_temperature_converter.py` file should contain:
```python
# test_temperature_converter.py

from temperature_converter import converter

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

You have successfully refactored and you are back to 1 passing test! 🎉


## Iteration 2


### I2-S1: Think (🤔)

Let's make that our second test.

Test the `convert()` function such that when we pass 212°F expect that it returns 100°C.

For this we're going to need a parameter.

But we just focus on adding the one failing test.


### I2-S2: Test (red 🔴)

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


### I2-S3: Code (green 🟩)

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


### I2-S4: Refactor (tidy 🧹)

Nothing says we have to refactor. If we're happy with everything as it stands, we can certainly move back to Step 1.

For me, the test function name `test_start` is not descriptive of the test. This is really checking that when the converter is passed 32 it should return 0. Let's rename that test to `test_when_passed_32_expect_0`.

The refactored tests look like this:
```python
from temperature_converter import converter

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

We've successfully refactored the tests and are back to 2 passing test! 🎉

Let's start thinking again.


## Iteration 3


### I3-S1: Think (🤔)

Although we alway want to _think small_, as we perform TDD our understanding grows. Our thinking can grow as our understanding grows.

The key concept with thinking: **keep the incremental changes small**

From a conversion chart, we learn some facts
* 0°C = 32°F
* 100°C = 212°F
* 40°C = 104°F

With that information, we create a "truth table".

| Fahrenheit   | Celsius     |
| ------------ |:-----------:|
|       32°F   |       0°C   |
|      212°F   |     100°C   |
|      104°F   |      40°C   |

The first two _truths_ are already tested. Let's add the next truth.

### I3-S2: Test (red 🔴)

Let's add this failing test to the bottom of the `test_temperature_converter.py` file:
```python

def test_when_passed_104_expect_40():
    assert convert(104) == 40
```

Running:
```zsh
$ pytest --verbose test_temperature_converter.py
```

Returns:
```zsh
================================================== test session starts ==================================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0 -- /Users/sdr/ ... /venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/sdr/ ... /code/ch02
collected 3 items                                                                                                       

test_temperature_converter.py::test_when_passed_32_expect_0 PASSED                                                [ 33%]
test_temperature_converter.py::test_when_passed_212_expect_100 PASSED                                             [ 66%]
test_temperature_converter.py::test_when_passed_104_expect_40 FAILED                                              [100%]

======================================================= FAILURES ========================================================
____________________________________________ test_when_passed_104_expect_40 _____________________________________________

    def test_when_passed_104_expect_40():
>       assert convert(104) == 40
E       assert 0 == 40
E        +  where 0 = convert(104)

test_temperature_converter.py:12: AssertionError
================================================ short test summary info ================================================
FAILED test_temperature_converter.py::test_when_passed_104_expect_40 - assert 0 == 40
============================================== 1 failed, 2 passed in 0.01s ==============================================
```

As expected, only `test_when_passed_104_expect_40` failed.


### I3-S3: Code (green 🟩)

Let's write just enough code to make all the tests pass.

And that looks like this:
```python
# temperature_converter.py

def convert(fahrenheit=0):
    if fahrenheit == 212:
        return 100
    if fahrenheit == 104:
        return 40
    return 0
```

Running:
```zsh
$ pytest --verbose test_temperature_converter.py
```

Returns:
```zsh
================================================== test session starts ==================================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0 -- /Users/sdr/ ... /venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/sdr/ ... /code/ch02
collected 3 items                                                                                                       

test_temperature_converter.py::test_when_passed_32_expect_0 PASSED                                                [ 33%]
test_temperature_converter.py::test_when_passed_212_expect_100 PASSED                                             [ 66%]
test_temperature_converter.py::test_when_passed_104_expect_40 PASSED                                              [100%]

=================================================== 3 passed in 0.00s ===================================================
```


### I3-S4: Refactor (tidy 🧹)

Let's skip the refactoring step and move to the next iteration.


## Iteration 4


### I4-S1: Think (🤔)

From a conversion chart, we learn another fact:
* -20°C = -4°F

Let's add that to our "truth table".

| Fahrenheit   | Celsius     |    |
| ------------ |:-----------:|---:|
|       32°F   |       0°C   | 🟩 |
|      212°F   |     100°C   | 🟩 |
|      104°F   |      40°C   | 🟩 |
|       -4°F   |     -20°C   | 🤔 |

The first three _truths_ are already tested. Let's test that next truth.


### I3-S2: Test (red 🔴)

Let's add this failing test to the bottom of the `test_temperature_converter.py` file:
```python

def test_when_passed_minus_4_expect_minus_20():
    assert convert(-4) == -20
```

Running:
```zsh
$ pytest --verbose test_temperature_converter.py
```

Returns:
```zsh
================================================== test session starts ==================================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0 -- /Users/sdr/ ... /venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/sdr/ ... /code/ch02
collected 4 items                                                                                                       

test_temperature_converter.py::test_when_passed_32_expect_0 PASSED                                                [ 25%]
test_temperature_converter.py::test_when_passed_212_expect_100 PASSED                                             [ 50%]
test_temperature_converter.py::test_when_passed_104_expect_40 PASSED                                              [ 75%]
test_temperature_converter.py::test_when_passed_minus_4_expect_minus_20 FAILED                                    [100%]

======================================================= FAILURES ========================================================
_______________________________________ test_when_passed_minus_4_expect_minus_20 ________________________________________

    def test_when_passed_minus_4_expect_minus_20():
>       assert convert(-4) == -20
E       assert 0 == -20
E        +  where 0 = convert(-4)

test_temperature_converter.py:15: AssertionError
================================================ short test summary info ================================================
FAILED test_temperature_converter.py::test_when_passed_minus_4_expect_minus_20 - assert 0 == -20
============================================== 1 failed, 3 passed in 0.01s ==============================================
```


### I3-S3: Code (green 🟩)

Let's write just enough code to make all the tests pass.

And that looks like this:
```python
# temperature_converter.py

def convert(fahrenheit=0):
    if fahrenheit == 212:
        return 100
    if fahrenheit == 104:
        return 40
    if fahrenheit == -4:
        return -20
    return 0
```

Running:
```zsh
$ pytest --verbose test_temperature_converter.py
```

Returns:
```zsh
================================================== test session starts ==================================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0 -- /Users/sdr/ ... /venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/sdr/ ... /code/ch02
collected 4 items                                                                                                       

test_temperature_converter.py::test_when_passed_32_expect_0 PASSED                                                [ 25%]
test_temperature_converter.py::test_when_passed_212_expect_100 PASSED                                             [ 50%]
test_temperature_converter.py::test_when_passed_104_expect_40 PASSED                                              [ 75%]
test_temperature_converter.py::test_when_passed_minus_4_expect_minus_20 PASSED                                    [100%]

=================================================== 4 passed in 0.01s ===================================================
```

All four tests are passing!

And the truth table looks like this:

| Fahrenheit   | Celsius     |    |
| ------------ |:-----------:|---:|
|       32°F   |       0°C   | 🟩 |
|      212°F   |     100°C   | 🟩 |
|      104°F   |      40°C   | 🟩 |
|       -4°F   |     -20°C   | 🟩 |


### I3-S4: Refactor (tidy 🧹)

We could go on forever with the truth table concept, but we want to handle any arbitrary temperature in degrees Fahrenheit and convert it to the correct degrees Celsius.

Wiktionary defines [refactor](https://en.wiktionary.org/wiki/refactor) as:
> To rewrite existing source code in order to improve its readability, reusability or structure without affecting its meaning or behavior.

So, this is the right place to restructure the code-under-test so as to improve it without altering it's functionality. For this, we might like to have a mathematical formula.

Let's ask our trusted Business Analyst to provide us with the formula.

Here is what we get:
```text
To convert temperatures in degrees Fahrenheit to Celsius, 
multiply by 9, divide by 5, and add 32.

celsius = ((9 * fahrenheit * 9) / 5) + 32

Example: ((-40°F * 9) / 5) + 32 = -40°C
```

And we code it up as follows:
```python
# temperature_converter.py

def convert(fahrenheit=0):
    return ((9 * fahrenheit * 9) / 5) + 32
```

Running:
```zsh
$ pytest --verbose test_temperature_converter.py
```

Returns:
```zsh
================================================== test session starts ==================================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0 -- /Users/sdr/ ... /venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/sdr/ ... /code/ch02
collected 4 items                                                                                                       

test_temperature_converter.py::test_when_passed_32_expect_0 FAILED                                                [ 25%]
test_temperature_converter.py::test_when_passed_212_expect_100 FAILED                                             [ 50%]
test_temperature_converter.py::test_when_passed_104_expect_40 FAILED                                              [ 75%]
test_temperature_converter.py::test_when_passed_minus_4_expect_minus_20 FAILED                                    [100%]

======================================================= FAILURES ========================================================
_____________________________________________ test_when_passed_32_expect_0 ______________________________________________

    def test_when_passed_32_expect_0():
>       assert convert(32) == 0
E       assert 550.4 == 0
E        +  where 550.4 = convert(32)

test_temperature_converter.py:6: AssertionError
____________________________________________ test_when_passed_212_expect_100 ____________________________________________

    def test_when_passed_212_expect_100():
>       assert convert(212) == 100
E       assert 3466.4 == 100
E        +  where 3466.4 = convert(212)

test_temperature_converter.py:9: AssertionError
____________________________________________ test_when_passed_104_expect_40 _____________________________________________

    def test_when_passed_104_expect_40():
>       assert convert(104) == 40
E       assert 1716.8 == 40
E        +  where 1716.8 = convert(104)

test_temperature_converter.py:12: AssertionError
_______________________________________ test_when_passed_minus_4_expect_minus_20 ________________________________________

    def test_when_passed_minus_4_expect_minus_20():
>       assert convert(-4) == -20
E       assert -32.8 == -20
E        +  where -32.8 = convert(-4)

test_temperature_converter.py:15: AssertionError
================================================ short test summary info ================================================
FAILED test_temperature_converter.py::test_when_passed_32_expect_0 - assert 550.4 == 0
FAILED test_temperature_converter.py::test_when_passed_212_expect_100 - assert 3466.4 == 100
FAILED test_temperature_converter.py::test_when_passed_104_expect_40 - assert 1716.8 == 40
FAILED test_temperature_converter.py::test_when_passed_minus_4_expect_minus_20 - assert -32.8 == -20
=================================================== 4 failed in 0.02s ===================================================
```

We got 4 failed tests! What happened!?! 🤯


#### Requirement Defect

Here's what happened: _we uncovered a defect in the formula_ (a.k.a. a requirement defect).

The Business Analyst unwittingly (and we assume with the best of intentions) provided us the incorrect formula.

But the good news, and the beauty of TDD, is that our four failing tests revealed the issue.

Our tests were built up from known truths. They helped to guard us from moving forward with a defective formula.

Now, let's go back to that Business Analyst.

We can use a calculator to show that the formula does not work for our four test cases.


#### Correct Formula

Now, we receive the correct formula.

```text
To convert temperatures from Fahrenheit to Celsius

celsius = (5 * (fahrenheit - 32)) / 9

Example: ((50°F - 32) * 5) / 9 = 10°C
```

And we code it up as follows:
```python
# temperature_converter.py

def convert(fahrenheit=0):
    return (5 * (fahrenheit - 32)) / 9
```

Running:
```zsh
$ pytest --verbose test_temperature_converter.py
```

Returns:
```zsh
================================================== test session starts ==================================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0 -- /Users/sdr/ ... /venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/sdr/ ... /code/ch02
collected 4 items                                                                                                       

test_temperature_converter.py::test_when_passed_32_expect_0 PASSED                                                [ 25%]
test_temperature_converter.py::test_when_passed_212_expect_100 PASSED                                             [ 50%]
test_temperature_converter.py::test_when_passed_104_expect_40 PASSED                                              [ 75%]
test_temperature_converter.py::test_when_passed_minus_4_expect_minus_20 PASSED                                    [100%]

=================================================== 4 passed in 0.00s ===================================================
```

#### Refactoring

As the name suggests, refactoring is done in the "Refactor" step of the TDD cycle.

Refactoring allows you to improve the structure and clarity of the code without changing its behavior.

The automated tests you've built up in prior TDD iterations play a crucial role in supporting refactoring. They provide a safety net that checks and ensures that the behavior of the code-under-test remains unchanged while that code is modified, restructure, or otherwise improved.


## Iteration 4

### I4-S1: Think (🤔)

### I4-S2: Test (red 🔴)

### I4-S3: Code (green 🟩)

### I4-S4: Refactor (tidy 🧹)
