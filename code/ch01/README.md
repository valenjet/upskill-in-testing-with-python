# Getting Started with pytest

## Check Python Installation

Before installing `pytest`, ensure that Python is installed on your system and check it by running:
```zsh
$ python3 --version
Python 3.11.7
```

**It's important to know that pytest requires Python 3.5 or newer.**

This command should return the version of Python installed. If Python is not installed, you will need to install it before proceeding.

## Using a virtual environment

Navigate to your project directory, create a virtual environment and activate it:
```zsh
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $
```

#### Dropping the (venv) for the rest of the book

The `(venv)` added before the command prompt is useful to let you know that you are using
a virtual environment.

However, for the rest of the book the use of a virtual environment will be assumed. The `(venv) $` will not be shown. We’ll shorten it to just `$`.

## Using pip (Python's package installer)

Check the version of `pip`:
```zsh
$ pip --version
pip 24.0 from /Users/sdr/ ... /venv/lib/python3.11/site-packages/pip (python 3.11)
```

## Installing pytest

With the virtual environment activated, install `pytest` using `pip` by running:

```zsh
$ pip install pytest
```

To ensure `pytest` was installed correctly in your virtual environment, you can check its version:

```zsh
$ pytest --version
pytest 8.0.2
```

## Running pytest

With `pytest` installed, run it as follows:
```zsh
$ cd code/ch01
$ pytest test_getting_started.py
```

You should see that one test fail. Here's the output you should see:

```zsh
==================================== test session starts =====================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0
rootdir: /Users/sdr/ ... /code/ch01
collected 1 item                                                                             

test_getting_started.py F                                                              [100%]

========================================== FAILURES ==========================================
_________________________________________ test_start _________________________________________

    def test_start():
>       assert True == False, "You are all set!"
E       AssertionError: You are all set!
E       assert True == False

test_getting_started.py:4: AssertionError
================================== short test summary info ===================================
FAILED test_getting_started.py::test_start - AssertionError: You are all set!
===================================== 1 failed in 0.01s ======================================
```

Notice the "1 failed" message on the last line. That's how pytest tells us that a test failed.

If we look in `test_getting_started.py` file, we see the assertion that `True` is equal to `False`.
```python
def test_start():
    assert True == False, "You are all set!"
```

So, the test failed because we expected it to fail. You are all set!

See [Why start with a failing test?](../manuscript/ch01/chapter01.md#why-start-with-a-failing-test) for more info.

If you feel the need to make the `test_start()` test pass ...

1. Open the `test_getting_started.py` file and change `False` to `True` and save the file.
```python
def test_start():
    assert True == True, "You are all set!"
```

2. Now, rerun pytest, as follows:
```zsh
$ pytest test_getting_started.py
```

3. You should now see the "1 passed" message on the last line.
```zsh
==================================== test session starts =====================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0
rootdir: /Users/sdr/ ... /code/ch01
collected 1 item                                                                                                  

test_getting_started.py .                                                              [100%]

===================================== 1 passed in 0.01s ======================================
```

And, there it is ... "1 passed"

[Back to the table of contents](../README.md)