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
|-------------:|------------:|
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
|-------------:|------------:|---:|
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
|-------------:|------------:|---:|
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

Refactoring allows you to improve the structure and clarity of the code without changing its behavior. The automated tests are there to help.

The automated tests you've built up in prior TDD iterations play a crucial role in supporting refactoring. They provide a _safety net_ that helps ensure the behavior of the code-under-test remains unchanged while that code is modified, restructured, or otherwise improved.

Good automated testing liberates refactoring.


## Iteration 4

Let's get real and talk about the real number line.

### I4-S1: Think (🤔)

There are many numbers between the whole numbers we've been testing so far.

And people commonly refer to a person's body temperate with a decimals, such as having a fever of 105.8°F.

So, let's write a test that checks that 105.8°F = 41°C[^1]

### I4-S2: Test (red 🔴)

Here's my next test:
```python

def test_when_passed_105_pt_8_expect_41():
    assert convert(105.8) == 41
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
collected 5 items                                                                                                       

test_temperature_converter.py::test_when_passed_32_expect_0 PASSED                                                [ 20%]
test_temperature_converter.py::test_when_passed_212_expect_100 PASSED                                             [ 40%]
test_temperature_converter.py::test_when_passed_104_expect_40 PASSED                                              [ 60%]
test_temperature_converter.py::test_when_passed_minus_4_expect_minus_20 PASSED                                    [ 80%]
test_temperature_converter.py::test_when_passed_105_pt_8_expect_41 PASSED                                         [100%]

=================================================== 5 passed in 0.00s ===================================================
```

Wait! ✋

That's not a failing test. Is that an error or did Python help us out here?

Let's see if we can write another test that fails to meet expectation.

For 105.6°F we can expect 40.89°C.

Here's the test code:
```python

def test_when_passed_105_pt_6_expect_40_pt_89():
    assert convert(105.6) == 40.89
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
collected 6 items                                                                                                       

test_temperature_converter.py::test_when_passed_32_expect_0 PASSED                                                [ 16%]
test_temperature_converter.py::test_when_passed_212_expect_100 PASSED                                             [ 33%]
test_temperature_converter.py::test_when_passed_104_expect_40 PASSED                                              [ 50%]
test_temperature_converter.py::test_when_passed_minus_4_expect_minus_20 PASSED                                    [ 66%]
test_temperature_converter.py::test_when_passed_105_pt_8_expect_41 PASSED                                         [ 83%]
test_temperature_converter.py::test_when_passed_105_pt_6_expect_40_pt_89 FAILED                                    [100%]

======================================================= FAILURES ========================================================
_______________________________________ test_when_passed_105_pt_6_expect_40_pt_89 ________________________________________

    def test_when_passed_105_pt_6_expect_40_pt_89():
>       assert convert(105.6) == 40.89
E       assert 40.888888888888886 == 40.89
E        +  where 40.888888888888886 = convert(105.6)

test_temperature_converter.py:21: AssertionError
================================================ short test summary info ================================================
FAILED test_temperature_converter.py::test_when_passed_105_pt_6_expect_40_pt_89 - assert 40.888888888888886 == 40.89
============================================== 1 failed, 5 passed in 0.02s ==============================================
```

There it is! One failed test 🔴

### I4-S3: Code (green 🟩)

Let's write just enough code to allow that test to pass. But what's the problem?

`pytest` reports the error as a rounding error.
```zsh
assert 40.888888888888886 == 40.89
```

Python `round()` is the built-in function that rounds. It takes two numeric arguments, `n` and `ndigits`, and returns the number `n` rounded to `ndigits`

Let's round to 1 digit by setting the value of `ndigits` to 1.

```python
def convert(fahrenheit=0):
    return round((5 * (fahrenheit - 32)) / 9, 2)
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
collected 6 items                                                                                                       

test_temperature_converter.py::test_when_passed_32_expect_0 PASSED                                                [ 16%]
test_temperature_converter.py::test_when_passed_212_expect_100 PASSED                                             [ 33%]
test_temperature_converter.py::test_when_passed_104_expect_40 PASSED                                              [ 50%]
test_temperature_converter.py::test_when_passed_minus_4_expect_minus_20 PASSED                                    [ 66%]
test_temperature_converter.py::test_when_passed_105_pt_8_expect_41 PASSED                                         [ 83%]
test_temperature_converter.py::test_when_passed_105_pt_6_expect_40_pt_9 PASSED                                    [100%]

=================================================== 6 passed in 0.01s ===================================================
```

Back to passing! 👍

### I4-S4: Refactor (tidy 🧹)

Looking at the function, I don't like a few things:

1. There is no sensible default for the input, yet we have the default `fahrenheit=0`.
2. We're doing a lot in just this one line:
```python
return round((5 * (fahrenheit - 32)) / 9, 2)
```
3. Let's add in some type hints for the function. We expect a `float` and we return a `float`.

Let's tidy those up, make things more readable, and see what happens.

Make the changes in `temperature_converter.py` and save. Here's what I did:
```python
# temperature_converter.py

def convert(fahrenheit: float) -> float:
    celsius = (5 * (fahrenheit - 32)) / 9
    return round(celsius, 2)
```

Running:
```zsh
$ pytest --quiet test_temperature_converter.py
```

Returns:
```zsh
......                                                                                                            [100%]
6 passed in 0.01s
```

Some excellent refactoring 😎

Notice that using the `--quiet` option (or abbreviated to `-q`) returns a lot less output. Let's use that for a while.

## Iteration 5

Let's perform boundary analysis to cover rounding scenarios.

Here's some of what you need to know about floating-point arithmetic[^2]:
- Any number that cannot be derived from exact powers of 2 cannot be accurately represented as a floating point number and requires approximation.
- Occasionally, the closest approximation might be less than the actual number.

But how do we find these special cases?

### I5-S1: Think (🤔)

When might `round(celsius, 2)` fail us?

Well, the number 36.815 degrees Fahrenheit equals 2.675 degrees Celsius but might erroneously return the number 2.68 instead of 2.67

The reason is that the Fahrenheit temperatures whose exact conversion to Celsius, when rounded to 2 significant figures, falls just above a rounding boundary.

This is case where floating-point arithmetic might result in a slightly lower approximation due to binary representation limitations.

### I5-S2: Test (red 🔴)

Let's add that test to the bottom of the `test_temperature_converter.py` file:
```python

def test_when_passed_36_pt_815_expect_2_pt_67():
    assert convert(36.815) == 2.67
```

Running:
```zsh
$ pytest --quiet test_temperature_converter.py
```

Returns:
```zsh
.......                                                                                                           [100%]
7 passed in 0.01s
```

That didn't fail. 🤔

How about another?

The number 221.1 degrees Fahrenheit equals 105.056 degrees Celsius but might erroneously return the number 105.05 instead of 105.06

Let's add that test to the bottom of the `test_temperature_converter.py` file:
```python

def test_when_passed_221_pt_1_expect_105_pt_06():
    assert convert(221.1) == 105.06
```


Running:
```zsh
$ pytest --quiet test_temperature_converter.py
```

Returns:
```zsh
........                                                                                                          [100%]
8 passed in 0.01s
```

How on earth are we going to find our next failing test?

Let's prompt ChatGPT
```text
Assume the role of a professional software tester who is testing a temperature converter function that takes a temperature in degrees Fahrenheit and returns the corresponding temperature in degrees Celsius, rounded to 2 significant figure.

Generate a list of input temperatures that might return an improper results. These inputs should consider potential problems with floating point arithmetic and rounding errors.

The format should follow: The number <Input> degrees Fahrenheit equals <Actual> degrees Celsius but might erroneously return the number <Unexpected> instead of <Expected>

This is an example, but don't include it in the generated list:
* The number 221.1 degrees Fahrenheit equals 105.0556 degrees Celsius but might erroneously return the rounded number 105.05 instead of 105.06

The Python code is provided within the three hash marks below.

###
def convert(fahrenheit: float) -> float:
    celsius = (5 * (fahrenheit - 32)) / 9

    return float(round(celsius, 2))
###
```

The generated response:
```text
Given the focus on potential problems with floating point arithmetic and rounding errors, let's identify and calculate specific input temperatures in degrees Fahrenheit that, when converted to Celsius and rounded to 2 significant figures, might reveal these issues.

To generate a list, we will consider:

Temperatures that convert to Celsius values just below a rounding threshold, which might be improperly rounded down instead of up due to floating point arithmetic precision.
Temperatures that result in Celsius values with a significant digit at the third place after the decimal, potentially leading to incorrect rounding.
Let's compute these examples, focusing on the edge cases where the actual conversion is very close to a value that would round differently if not for floating point representation issues.

After calculating the potential problematic inputs based on the criteria for floating point arithmetic and rounding errors, it appears that the provided conversion function accurately handles the rounding for the specified test cases. The function correctly rounds the Celsius values to two significant figures without introducing errors in the examples considered, which were specifically chosen to test the boundaries of rounding behavior.

Given this outcome, it seems that the function is robust against the rounding issues we anticipated might occur with inputs near rounding thresholds or where floating point precision could lead to unexpected results. Therefore, no specific examples fitting the format of demonstrating a discrepancy between the expected and actual rounded values were found among the chosen test cases.

This indicates that the temperature converter function is well-implemented for the range of inputs tested, accurately converting temperatures from degrees Fahrenheit to degrees Celsius and rounding to two significant figures without introducing the anticipated rounding errors.
```

That's good news.

## Iteration 6

It's a good idea to perform boundary-value analysis to cover all scenarios.

Boundary-value analysis is about finding the limits of acceptable values, which includes looking at the following:
- All invalid values
- Maximum values
- Minimum values
- Values just on a boundary
- Values just within a boundary
- Values just outside a boundary
- Values that behave uniquely, such as zero or one

### I6-S1: Think (🤔)

Let's prompt ChatGPT again to get some ideas:
```text
Assume the role of a professional software tester who is testing a temperature converter function that takes a temperature in degrees Fahrenheit and returns the corresponding temperature in degrees Celsius, rounded to 2 significant figure.

Suggest a list of input temperatures that might return an improper results. These inputs should consider only the potential problems that relate to boundary values:

Boundary-value analysis is about finding the limits of acceptable values, which includes looking at the following:
- All invalid values
- Maximum values
- Minimum values
- Values just on a boundary
- Values just within a boundary
- Values just outside a boundary
- Values that behave uniquely, such as zero or one

The Python code is provided between the three hash marks below.

###
def convert(fahrenheit: float) -> float:
    celsius = (5 * (fahrenheit - 32)) / 9

    return float(round(celsius, 2))
###
```

The generated response:
```markdown
Boundary-value analysis for the temperature converter function involves identifying Fahrenheit temperatures that, when converted to Celsius, test the limits of acceptable and expected values. This approach aims to uncover issues at the extremes of the input range and around specific critical points. Here's a list of suggested input temperatures for testing, based on boundary-value considerations:

### Invalid Values
- *Extremely Low Value:* Consider using a value like `-459.67°F`, which is below absolute zero in Fahrenheit and should be treated as an invalid input or edge case.
- *Extremely High Value:* A very high value, such as `10000°F`, to test the function's handling of unusually high temperatures.

### Maximum and Minimum Values
- *Maximum Valid Value:* Assuming the function has a defined maximum, test just below this value. If not defined, use a high value like `10000°F` as mentioned above.
- *Minimum Valid Value:* Assuming the function has a defined minimum, test just above this value. The minimum valid Fahrenheit temperature could be `-459.67°F` (absolute zero).

### Values on a Boundary
- *Freezing Point of Water (Just Below):* `31.9°F` to see if it rounds to below `0°C`.
- *Freezing Point of Water (Just Above):* `32.1°F` to see if it correctly rounds to above `0°C`.
- *Boiling Point of Water (Just Below):* `211.9°F` to test conversion just below `100°C`.
- *Boiling Point of Water (Just Above):* `212.1°F` to test conversion just above `100°C`.

### Values Within a Boundary
- *Just Above Absolute Zero:* `-459.66°F` to see how the function handles values just above the theoretical minimum.
- *Just Below a High Arbitrary Value:* If considering `10000°F` as a high test value, then `9999.9°F` could be used to test just below it.

### Values Outside a Boundary
- *Slightly Below Absolute Zero:* `-459.68°F` to test handling of impossible values.
- *Slightly Above a High Arbitrary Value:* If `10000°F` is used, then `10000.1°F` tests handling of values just outside the expected range.

### Values That Behave Uniquely
- *Zero Fahrenheit:* `0°F` to observe conversion at a significant numerical boundary.
- *One Fahrenheit:* `1°F` to test conversion just above zero, observing minimal increment behavior.
- *Intersection Point:* `-40°F` where Fahrenheit equals Celsius, testing a unique equivalence point.

These inputs are designed to explore how the temperature converter function handles a variety of boundary conditions, from extreme values to those just around critical thresholds like the freezing and boiling points of water, as well as absolute zero.
```

#### Slightly Below Absolute Zero

Testing for this _out of bounds_ value caught my eye:
> *Slightly Below Absolute Zero:* `-459.68°F` to test handling of impossible values.

Question: _What is absolute zero in degrees Fahrenheit?_

[Wikipedia](https://en.wikipedia.org/wiki/Absolute_zero) says:

Absolute zero is −459.67°F, which equals −273.15°C.

Question: _What would we want the function to do if it receives an input of less than −459.67°F?_

Let's make that failing test.

### I6-S2: Test (red 🔴)

Not sure how to write the failing test? Just `assert False` in the test code.

Let's add a failing test to the bottom of the `test_temperature_converter.py` file:
```python

def test_when_passed_minus_459_pt_68_expect_AssertionError():
    assert False
```

Running:
```zsh
$ pytest --quiet test_temperature_converter.py
```

Returns:
```zsh
.........F                                                                                                        [100%]
======================================================= FAILURES ========================================================
_______________________________ test_when_passed_minus_459_pt_68_expect_AssertionError _______________________________

    def test_when_passed_minus_459_pt_68_expect_AssertionError():
>       assert False
E       assert False

test_temperature_converter.py:33: AssertionError
================================================ short test summary info ================================================
FAILED test_temperature_converter.py::test_when_passed_minus_459_pt_68_expect_AssertionError - assert False
1 failed, 9 passed in 0.03s
```

There's a failing test, but is it really the test we want?

We want to know that the test failed because it did not raise the expected `AssertionError` exception.

For this we'll use [pytest.raises()](https://docs.pytest.org/en/latest/how-to/assert.html#assertions-about-expected-exceptions)

At the top of `test_temperature_converter.py` import `pytest`, like this:
```python
# test_temperature_converter.py

import pytest
from temperature_converter import convert

```

And at the bottom of `test_temperature_converter.py` let's use `pytest.raises()` like this:
```python

def test_when_passed_minus_459_pt_68_expect_AssertionError():
    with pytest.raises(AssertionError):
        convert(-459.68)
```


Running:
```zsh
$ pytest --quiet test_temperature_converter.py
```

Returns:
```zsh
.........F                                                                                                        [100%]
======================================================= FAILURES ========================================================
_______________________________ test_when_passed_minus_459_pt_68_expect_AssertionError _______________________________

    def test_when_passed_minus_459_pt_68_expect_AssertionError():
>       with pytest.raises(AssertionError):
E       Failed: DID NOT RAISE <class 'AssertionError'>

test_temperature_converter.py:34: Failed
================================================ short test summary info ================================================
FAILED test_temperature_converter.py::test_when_passed_minus_459_pt_68_expect_AssertionError - Failed: DID NOT RAISE <class 'AssertionError'>
1 failed, 9 passed in 0.06s
```

That looks like it failed properly.

### I6-S3: Code (green 🟩)

Now, let's make that failing test pass.

The simplest thing that will make it pass is to check for absolute zero.
```python
# temperature_converter.py

def convert(fahrenheit: float) -> float:
    assert fahrenheit > -459.67

    celsius = (5 * (fahrenheit - 32)) / 9

    return float(round(celsius, 2))
```

And it passes.
```zsh
$ pytest --quiet test_temperature_converter.py                   
..........                                                                                                        [100%]
10 passed in 0.01s
```

### I6-S4: Refactor (tidy 🧹)

Now, let's do some major refactoring of our tests with parameterization.

As the tests are written, it becomes apparent that many of the test methods are exactly the same code, only using different values as input.

`pytest` offers ways to call the same test method with different input data, which is described in the [How to parametrize fixtures and test functions](https://docs.pytest.org/en/latest/how-to/parametrize.html) section of the documentation.

Let's replicate the top two tests with parameterization:
```python
# test_temperature_converter.py

import pytest
from temperature_converter import convert

@pytest.mark.parametrize("valid_input, proper_result", [
    (32, 0),
    (212, 100)],
)
def test_when_passed_valid_input_expect_proper_result(
        valid_input, 
        proper_result):
    assert convert(valid_input) == proper_result

```

Running the tests:
```zsh
$ pytest --quiet test_temperature_converter.py
............                                                                                                      [100%]
12 passed in 0.01s
```

Note that there are 12 passed tests instead of two.

Running the tests using the verbose option:
```zsh
$ pytest --verbose test_temperature_converter.py
================================= test session starts ==================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0 -- /Users/sdr/ ... /venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/sdr/ ... /code/ch02
collected 12 items                                                                     

test_temperature_converter.py::test_when_passed_valid_input_expect_proper_result[32-0] PASSED [  8%]
test_temperature_converter.py::test_when_passed_valid_input_expect_proper_result[212-100] PASSED [ 16%]
test_temperature_converter.py::test_when_passed_32_expect_0 PASSED               [ 25%]
test_temperature_converter.py::test_when_passed_212_expect_100 PASSED            [ 33%]
test_temperature_converter.py::test_when_passed_104_expect_40 PASSED             [ 41%]
test_temperature_converter.py::test_when_passed_minus_4_expect_minus_20 PASSED   [ 50%]
test_temperature_converter.py::test_when_passed_105_pt_8_expect_41 PASSED        [ 58%]
test_temperature_converter.py::test_when_passed_105_pt_6_expect_40_pt_89 PASSED  [ 66%]
test_temperature_converter.py::test_when_passed_36_pt_815_expect_2_pt_67 PASSED  [ 75%]
test_temperature_converter.py::test_when_passed_221_pt_1_expect_105_pt_06 PASSED [ 83%]
test_temperature_converter.py::test_when_passed_50_pt_009_expect_10_pt_01 PASSED [ 91%]
test_temperature_converter.py::test_when_passed_minus_459_pt_68_expect_AssertionError PASSED [100%]

================================== 12 passed in 0.01s ==================================
```

In the output we see our two new tests:
```zsh
test_temperature_converter.py::test_when_passed_valid_input_expect_proper_result[32-0] PASSED [  8%]
test_temperature_converter.py::test_when_passed_valid_input_expect_proper_result[212-100] PASSED [ 16%]
```

Let's shorten that test name to `test_valid_input_expect_result` so it looks like this:
```python
@pytest.mark.parametrize("valid_input, expected_result", [
    (32, 0),
    (212, 100)],
)
def test_param_input_expect_result(
        valid_input, 
        expected_result):
    assert convert(valid_input) == expected_result
```

```zsh
$ pytest --verbose test_temperature_converter.py
======================================== test session starts =========================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0 -- /Users/sdr/ ... /venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/sdr/ ... /code/ch02
collected 12 items                                                                                   

test_temperature_converter.py::test_param_input_expect_result[32-0] PASSED                     [  8%]
test_temperature_converter.py::test_param_input_expect_result[212-100] PASSED                  [ 16%]
test_temperature_converter.py::test_when_passed_32_expect_0 PASSED                             [ 25%]
test_temperature_converter.py::test_when_passed_212_expect_100 PASSED                          [ 33%]
test_temperature_converter.py::test_when_passed_104_expect_40 PASSED                           [ 41%]
test_temperature_converter.py::test_when_passed_minus_4_expect_minus_20 PASSED                 [ 50%]
test_temperature_converter.py::test_when_passed_105_pt_8_expect_41 PASSED                      [ 58%]
test_temperature_converter.py::test_when_passed_105_pt_6_expect_40_pt_89 PASSED                [ 66%]
test_temperature_converter.py::test_when_passed_36_pt_815_expect_2_pt_67 PASSED                [ 75%]
test_temperature_converter.py::test_when_passed_221_pt_1_expect_105_pt_06 PASSED               [ 83%]
test_temperature_converter.py::test_when_passed_50_pt_009_expect_10_pt_01 PASSED               [ 91%]
test_temperature_converter.py::test_when_passed_minus_459_pt_68_expect_AssertionError PASSED [100%]

========================================= 12 passed in 0.01s =========================================
```

#### Parameterized Test Cases

Once these tests cases are parameterized, the entire `test_temperature_converter.py` looks like this:
```python
# test_temperature_converter.py

import pytest
from temperature_converter import convert

@pytest.mark.parametrize("valid_input, expected_result", [
    (32, 0),
    (212, 100),
    (104, 40),
    (-4, -20),
    (105.8, 41),
    (105.6, 40.89),
    (36.815, 2.67),
    (221.1, 105.06),
    (50.009, 10.01)],
)
def test_param_input_expect_result(
        valid_input, 
        expected_result):
    assert convert(valid_input) == expected_result

def test_when_passed_minus_459_pt_68_expect_AssertionError():
    with pytest.raises(AssertionError):
        convert(-459.68)
```

Running:
```zsh
$ pytest --verbose test_temperature_converter.py
```

Returns:
```zsh
========================================= test session starts ==========================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0 -- /Users/sdr/ ... /venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/sdr/ ... /code/ch02
collected 10 items                                                                                     

test_temperature_converter.py::test_param_input_expect_result[32-0] PASSED                       [ 10%]
test_temperature_converter.py::test_param_input_expect_result[212-100] PASSED                    [ 20%]
test_temperature_converter.py::test_param_input_expect_result[104-40] PASSED                     [ 30%]
test_temperature_converter.py::test_param_input_expect_result[-4--20] PASSED                     [ 40%]
test_temperature_converter.py::test_param_input_expect_result[105.8-41] PASSED                   [ 50%]
test_temperature_converter.py::test_param_input_expect_result[105.6-40.89] PASSED                [ 60%]
test_temperature_converter.py::test_param_input_expect_result[36.815-2.67] PASSED                [ 70%]
test_temperature_converter.py::test_param_input_expect_result[221.1-105.06] PASSED               [ 80%]
test_temperature_converter.py::test_param_input_expect_result[50.009-10.01] PASSED               [ 90%]
test_temperature_converter.py::test_when_passed_minus_459_pt_68_expect_AssertionError PASSED  [100%]

========================================== 10 passed in 0.01s ==========================================
```

There we are, we have 10 passed!

## Iteration 7

Let's review where we are and what we still need to do.

1. These are the 9 "valid input" test cases that pass:

| Fahrenheit   | Celsius     |    |
|-------------:|------------:|---:|
|       32°F   |       0°C   | 🟩 |
|      212°F   |     100°C   | 🟩 |
|      104°F   |      40°C   | 🟩 |
|       -4°F   |     -20°C   | 🟩 |
|    105.8°F   |      41°C   | 🟩 |
|    105.6°F   |   40.89°C   | 🟩 |
|   36.815°F   |    2.67°C   | 🟩 |
|    221.1°F   |  105.06°C   | 🟩 |
|   50.009°F   |   10.01°C   | 🟩 |

2. Here is the 1 "invalid input" that returns the expected error:

| Fahrenheit   | Scenario                  | Expectation      |    |
|-------------:|--------------------------:|-----------------:|---:|
|  -459.68°F   | Less than absolute zero   | AssertionError   | 🟩 |


### I7-S1: Think (🤔)

To get very thorough with the testing, let's review the boundary-value analysis.

* Invalid Values
  - Extremely low value like -459.68°F is an invalid input, given that it's below absolute zero.
  - Extremely high value like 10000°F is an invalid input, given that the hottest air temperature measured anywhere on Earth was 134°F.
* Maximum and Minimum Values (valid)
  - Maximum valid value, test just _below_ the maximum valid temperature.
  - Minimum valid value, test just _above_ -459.67°F (absolute zero).
* Values on a Boundary (valid)
  - Freezing point of water (just below): 31.9°F =>  -0.06°C
  - Freezing point of water (just above): 32.1°F =>   0.06°C
  - Boiling point of water (just below): 211.9°F =>  99.94°C
  - Boiling point of water (just above): 212.1°F => 100.06°C
* Values Within a Boundary (valid)
  - Just above absolute zero: -459.66°F => -273.14°C
  - Just below a high arbitrary value: 9999.9°F => 5537.77°C
* Values Outside a Boundary (invalid)
  - Slightly below absolute zero: -459.68°F ( 🟩 already checking this scenario)
  - Slightly above a high arbitrary value: 10000.1°F (with 10000°F as the maximum valid temperature)
* Values That Behave Uniquely (valid)
  - Zero Fahrenheit: 0°F => -17.78°C
  - One Fahrenheit: 1°F => -17.22°C
  - Intersection point: -40°F => -40°C (where Fahrenheit equals Celsius)


#### Untested Valid Scenarios

| Fahrenheit   | Scenario                              | Expectation      |    |
|-------------:|:-------------------------------------:|-----------------:|---:|
|    10000°F   | Maximum valid value                   |        5537.78°C | 🤔 |
|  -459.67°F   | Minimum valid value                   |        -273.15°C | 🤔 |
|     31.9°F   | Freezing point of water (just below)  |          -0.06°C | 🤔 |
|     32.1°F   | Freezing point of water (just above)  |           0.06°C | 🤔 |
|    211.9°F   | Boiling point of water (just below)   |          99.94°C | 🤔 |
|    212.1°F   | Boiling point of water (just above)   |         100.06°C | 🤔 |
|  -459.66°F   | Just above absolute zero              |        -273.14°C | 🤔 |
|   9999.9°F   | Just below a high arbitrary value     |        5537.72°C | 🤔 |
|        0°F   | Zero Fahrenheit                       |         -17.78°C | 🤔 |
|        1°F   | One Fahrenheit                        |         -17.22°C | 🤔 |
|      -40°F   | Intersection point                    |            -40°C | 🤔 |

#### Untested Error Scenarios

| Fahrenheit   | Scenario                              | Expectation      |    |
|-------------:|:-------------------------------------:|-----------------:|---:|
|  -459.68°F   | Less than absolute zero               | AssertionError   | 🟩 |
|  10000.1°F   | Slightly above a high arbitrary value | AssertionError   | 🤔 |


### I7-S2: Test (red 🔴)

With parameterized testing, we can check all the valid scenarios very quickly.

```python
@pytest.mark.parametrize("valid_input, expected_result", [
    (32, 0),
    (212, 100),
    (104, 40),
    (-4, -20),
    (105.8, 41),
    (105.6, 40.89),
    (36.815, 2.67),
    (221.1, 105.06),
    (50.009, 10.01),
    (10000, 5537.78),
    (-459.67, -273.15),
    (31.9, -0.06),
    (32.1, 0.06),
    (211.9, 99.94),
    (212.1, 100.06),
    (-459.66, -273.14),
    (9999.9, 5537.72),
    (0, -17.78),
    (1, -17.22),
    (-40, -40)],
)
def test_param_input_expect_result(
        valid_input, 
        expected_result):
    assert convert(valid_input) == expected_result
```

Running:
```zsh
$ pytest --quiet test_temperature_converter.py
```

Returns
```zsh
..........F..........                                                                     [100%]
=========================================== FAILURES ============================================
________________________ test_param_input_expect_result[-459.67--273.15] ________________________

valid_input = -459.67, expected_result = -273.15

    @pytest.mark.parametrize("valid_input, expected_result", [
        (32, 0),
        (212, 100),
        (104, 40),
        (-4, -20),
        (105.8, 41),
        (105.6, 40.89),
        (36.815, 2.67),
        (221.1, 105.06),
        (50.009, 10.01),
        (10000, 5537.78),
        (-459.67, -273.15),
        (31.9, -0.06),
        (32.1, 0.06),
        (211.9, 99.94),
        (212.1, 100.06),
        (-459.66, -273.14),
        (9999.9, 5537.72),
        (0, -17.78),
        (1, -17.22),
        (-40, -40)],
    )
    def test_param_input_expect_result(
            valid_input,
            expected_result):
>       assert convert(valid_input) == expected_result

test_temperature_converter.py:31: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

fahrenheit = -459.67

    def convert(fahrenheit: float) -> float:
>       assert fahrenheit > -459.67
E       AssertionError

temperature_converter.py:4: AssertionError
==================================== short test summary info ====================================
FAILED test_temperature_converter.py::test_param_input_expect_result[-459.67--273.15] - AssertionError
1 failed, 20 passed in 0.02s
```

There's our 1 failed test!

That is the minimum valid value (absolute zero) scenario where -459.67°F should return exactly -273.15°C.

### I7-S3: Code (green 🟩)

Absolute zero is a special, physical constant value that is defined as exactly -273.15°C.

To make this test pass, let return that constant when the input is -459.67°F.

The function now looks like this:
```python
# temperature_converter.py

def convert(fahrenheit: float) -> float:
    if fahrenheit == -459.67:
        return -273.15

    assert fahrenheit > -459.67

    celsius = (5 * (fahrenheit - 32)) / 9

    return float(round(celsius, 2))
```

Running `pytest` confirms that all tests are passing.
```zsh
$ pytest --quiet test_temperature_converter.py
.....................                                                                                                                                                 [100%]
21 passed in 0.01s
```

Bravo! 👏 👏 👏

### I7-S4: Refactor (tidy 🧹)

I don't like that there are two magic _absolute zero_ values in our code:
* Absolute zero in degrees Fahrenheit = -459.67
* Absolute zero in degrees Celsius = -273.15

Let's refactor those into constants, as follows:

```python
# temperature_converter.py

ABS_ZERO_CELSIUS = -273.15
ABS_ZERO_FAHRENHEIT = -459.67

def convert(fahrenheit: float) -> float:
    if fahrenheit == ABS_ZERO_FAHRENHEIT:
        return ABS_ZERO_CELSIUS

    assert fahrenheit > ABS_ZERO_FAHRENHEIT

    celsius = (5 * (fahrenheit - 32)) / 9

    return float(round(celsius, 2))
```

Running `pytest` confirms that all tests are passing.
```zsh
$ pytest --quiet test_temperature_converter.py
.....................                                                                                                                                                 [100%]
21 passed in 0.01s
```

Ready for the next iteration?

## Iteration 8

In this iteration, we'll address more expected errors. Specifically, the slightly above a high arbitrary value.

### I8-S1: Think (🤔)

We've thought about 10000°F as the maximum valid temperature but we don't enforce that in the code. Let's add that behavior.


### I8-S2: Test (red 🔴)

Add this to the bottom of the `test_temperature_converter.py` file and save:
```python

def test_when_passed_10000_pt_1_expect_AssertionError():
    with pytest.raises(AssertionError):
        convert(10000.1)
```

Running `pytest` now results in 1 failed test.
```zsh
$ pytest --quiet test_temperature_converter.py
.....................F                                                                                                                                                [100%]
================================================================================= FAILURES ==================================================================================
_____________________________________________________________ test_when_passed_10000_pt_1_expect_AssertionError _____________________________________________________________

    def test_when_passed_10000_pt_1_expect_AssertionError():
>       with pytest.raises(AssertionError):
E       Failed: DID NOT RAISE <class 'AssertionError'>

test_temperature_converter.py:38: Failed
========================================================================== short test summary info ==========================================================================
FAILED test_temperature_converter.py::test_when_passed_10000_pt_1_expect_AssertionError - Failed: DID NOT RAISE <class 'AssertionError'>
1 failed, 21 passed in 0.02s
```

### I8-S3: Code (green 🟩)

Now, add the input check to the `convert()` function in `temperature_converter.py` and save.

This should pass the test.
```python
# temperature_converter.py

ABS_ZERO_CELSIUS = -273.15
ABS_ZERO_FAHRENHEIT = -459.67

def convert(fahrenheit: float) -> float:
    if fahrenheit == ABS_ZERO_FAHRENHEIT:
        return ABS_ZERO_CELSIUS

    assert fahrenheit <= 10000
    assert fahrenheit > ABS_ZERO_FAHRENHEIT

    celsius = (5 * (fahrenheit - 32)) / 9

    return float(round(celsius, 2))
```

And it does!
```zsh
$ pytest --quiet test_temperature_converter.py
......................                                                                                                                                                [100%]
22 passed in 0.01s
```

### I8-S4: Refactor (tidy 🧹)

Ready to refactor? Let's move the maximum valid input into a constant.

Move the maximum valid input into a constant and save:
```python
# temperature_converter.py

ABS_ZERO_CELSIUS = -273.15
ABS_ZERO_FAHRENHEIT = -459.67

MAX_FAHRENHEIT = 10000

def convert(fahrenheit: float) -> float:
    if fahrenheit == ABS_ZERO_FAHRENHEIT:
        return ABS_ZERO_CELSIUS

    assert fahrenheit <= MAX_FAHRENHEIT
    assert fahrenheit > ABS_ZERO_FAHRENHEIT

    celsius = (5 * (fahrenheit - 32)) / 9

    return float(round(celsius, 2))
```

Run all the tests to make sure nothing fails.
```zsh
$ pytest --quiet test_temperature_converter.py
......................                                                                                                                                                [100%]
22 passed in 0.01s
```

We have 22 passed! All the tests are running. All the tests are passing.

We've improved the code, and we're confident that everything is working as we intended.

## Iteration 9

We have covered a lot of valid and invalid scenarios:

| Fahrenheit   | Scenario                              | Expectation      |    |
|-------------:|:-------------------------------------:|-----------------:|---:|
|    10000°F   | Maximum valid value                   |        5537.78°C | 🟩 |
|  -459.67°F   | Minimum valid value                   |        -273.15°C | 🟩 |
|     31.9°F   | Freezing point of water (just below)  |          -0.06°C | 🟩 |
|     32.1°F   | Freezing point of water (just above)  |           0.06°C | 🟩 |
|    211.9°F   | Boiling point of water (just below)   |          99.94°C | 🟩 |
|    212.1°F   | Boiling point of water (just above)   |         100.06°C | 🟩 |
|  -459.66°F   | Just above absolute zero              |        -273.14°C | 🟩 |
|   9999.9°F   | Just below a high arbitrary value     |        5537.72°C | 🟩 |
|        0°F   | Zero Fahrenheit                       |         -17.78°C | 🟩 |
|        1°F   | One Fahrenheit                        |         -17.22°C | 🟩 |
|      -40°F   | Intersection point                    |            -40°C | 🟩 |
|  -459.68°F   | Less than absolute zero               |   AssertionError | 🟩 |
|  10000.1°F   | Slightly above a high arbitrary value |   AssertionError | 🟩 |

### I9-S1: Think (🤔)

You will notice that the assertion errors don't explain what went wrong. Let's add a message to each of the exceptions so the reason is clear.

When the input value is greater than the maximum temperature in degrees Fahrenheit, we want the message to return as, "Input cannot be greater than 10000".

### I9-S2: Test (red 🔴)

Let's write that test and add it to the end of the `test_temperature_converter.py` file and save:
```python

def test_when_passed_10000_pt_1_expect_raises_message():
    with pytest.raises(AssertionError) as actual_raises:
        convert(10000.1)
    assert 'Input cannot be greater than 10000' == str(actual_raises.value) 
```

Running the test suite:
```zsh
$ pytest --quiet test_temperature_converter.py
```

Returns:
```zsh
......................F                                             [100%]
================================ FAILURES =================================
____________ test_when_passed_10000_pt_1_expect_raises_message ____________

    def test_when_passed_10000_pt_1_expect_raises_message():
        with pytest.raises(AssertionError) as actual_raises:
            convert(10000.1)
>       assert 'Input cannot be greater than 10000' == str(actual_raises.value)
E       AssertionError: assert 'Input cannot...er than 10000' == ''
E         
E         + Input cannot be greater than 10000

test_temperature_converter.py:48: AssertionError
========================= short test summary info =========================
FAILED test_temperature_converter.py::test_when_passed_10000_pt_1_expect_raises_message - AssertionError: assert 'Input cannot...er than 10000' == ''
1 failed, 22 passed in 0.02s
```

We have 1 failed test; just what we're looking for!


### I9-S3: Code (green 🟩)

Add the formatted message string to the `assert` statement as shown and save:
```python
# temperature_converter.py

ABS_ZERO_CELSIUS = -273.15
ABS_ZERO_FAHRENHEIT = -459.67

MAX_FAHRENHEIT = 10000

def convert(fahrenheit: float) -> float:
    if fahrenheit == ABS_ZERO_FAHRENHEIT:
        return ABS_ZERO_CELSIUS

    assert fahrenheit <= MAX_FAHRENHEIT, f'Input cannot be greater than {MAX_FAHRENHEIT}'
    assert fahrenheit > ABS_ZERO_FAHRENHEIT

    celsius = (5 * (fahrenheit - 32)) / 9

    return float(round(celsius, 2))
```

Rerun all the tests to confirm that everything passes.
```zsh
$ pytest --quiet test_temperature_converter.py
.......................                                                                                                                                                                [100%]
23 passed in 0.01s
```

Hurray! 🥳


### I9-S4: Refactor (tidy 🧹)

Let's not refactor anything at this time.


## Iteration 10

We just covered one of two similar behaviors:

| Fahrenheit   | Scenario                              | Expectation      |    |
|-------------:|:-------------------------------------:|-----------------:|---:|
|  10000.1°F   | Slightly above a high arbitrary value |   Proper message | 🟩 |
|  -459.68°F   | Less than absolute zero               |   Proper message | 🤔 |

### I10-S1: Think (🤔)

This second assertion error needs a message so the reason is clear.

When the input value is absolute zero in degrees Fahrenheit, we want the message to return as, "Input cannot be below -459.67".

### I10-S2: Test (red 🔴)


Let's write that test and add it to the end of the `test_temperature_converter.py` file and save:
```python

def test_when_passed_459_pt_68_expect_raises_message():
    with pytest.raises(AssertionError) as actual_raises:
        convert(-459.68)
    assert 'Input cannot be below -459.67' == str(actual_raises.value) 
```

Running the test suite:
```zsh
$ pytest --quiet test_temperature_converter.py
```

Returns:
```zsh
.......................F                                                                                                                                                               [100%]
========================================================================================== FAILURES ==========================================================================================
______________________________________________________________________ test_when_passed_459_pt_68_expect_raises_message ______________________________________________________________________

    def test_when_passed_459_pt_68_expect_raises_message():
        with pytest.raises(AssertionError) as actual_raises:
            convert(-459.68)
>       assert 'Input cannot be below -459.67' == str(actual_raises.value)
E       AssertionError: assert 'Input cannot...below -459.67' == ''
E         
E         + Input cannot be below -459.67

test_temperature_converter.py:53: AssertionError
================================================================================== short test summary info ===================================================================================
FAILED test_temperature_converter.py::test_when_passed_459_pt_68_expect_raises_message - AssertionError: assert 'Input cannot...below -459.67' == ''
1 failed, 23 passed in 0.02s
```

We see the 1 failed happened as expected, and we move to the next step.

### I10-S3: Code (green 🟩)

```python
# temperature_converter.py

ABS_ZERO_CELSIUS = -273.15
ABS_ZERO_FAHRENHEIT = -459.67

MAX_FAHRENHEIT = 10000

def convert(fahrenheit: float) -> float:
    if fahrenheit == ABS_ZERO_FAHRENHEIT:
        return ABS_ZERO_CELSIUS

    assert fahrenheit <= MAX_FAHRENHEIT, f'Input cannot be greater than {MAX_FAHRENHEIT}'
    assert fahrenheit > ABS_ZERO_FAHRENHEIT, f'Input cannot be below {ABS_ZERO_FAHRENHEIT}'

    celsius = (5 * (fahrenheit - 32)) / 9

    return float(round(celsius, 2))
```

Running all the tests ...
```zsh
$ pytest --quiet test_temperature_converter.py
........................                                                                                                                                                               [100%]
24 passed in 0.01s
```

Yes, **24 passed** -- You are awesome! 🤩


### I10-S4: Refactor (tidy 🧹)

Let's comment our code to be sure anyone who reads the code knows what's what.

```python
# temperature_converter.py

# these are physical constants
ABS_ZERO_CELSIUS = -273.15
ABS_ZERO_FAHRENHEIT = -459.67

# limit the input
MAX_FAHRENHEIT = 10000

def convert(fahrenheit: float) -> float:
    # short-circuit for absolute zero
    if fahrenheit == ABS_ZERO_FAHRENHEIT:
        return ABS_ZERO_CELSIUS

    # guard against invalid input
    assert fahrenheit <= MAX_FAHRENHEIT, f'Input cannot be greater than {MAX_FAHRENHEIT}'
    assert fahrenheit > ABS_ZERO_FAHRENHEIT, f'Input cannot be below {ABS_ZERO_FAHRENHEIT}'

    # this is the mathematical formula
    celsius = (5 * (fahrenheit - 32)) / 9

    # be sure to round to 2 decimal places
    return float(round(celsius, 2))
```

Notice that last line? Is that `float()` conversion necessary?

Let's change the line to this and and save:
```python
    return round(celsius, 2)
```

Let's rerun the tests to see if everything still passes.
```zsh
$ pytest --quiet test_temperature_converter.py
........................                                                                                                                                                               [100%]
24 passed in 0.01s
```

Excellent! See how the automated tests liberate refactoring. We changed our code, reran the tests, and we're fully confident that we didn't break anything.

This is how well-written automated tests liberate refactoring.


## Conclusion

In this chapter we learned:
* [provide summary details here]
* Automated tests liberate refactoring.


## Exercises

Try some of the following exercises on your own:
* Think about adding a parameter, such as `precision:int =2`, to the `convert()` function so that the result can be rounded to `precision` digits after the decimal point.
  - Using test-driven development, add a new test to define the behavior.
  - See just that one new test fails, as expected.
  - Add only enough code to get that one test to pass.
  - Make sure that all the existing tests pass with the new parameter.
  - Refactor by using the test suite as a safety net to ensure that everything continues to work as intended.

[^1]: I looked this up on [metric-conversions.org](https://www.metric-conversions.org/temperature/fahrenheit-to-celsius.htm))
[^2]: Read more at [What Every Computer Scientist Should Know About Floating-Point Arithmetic](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html)
