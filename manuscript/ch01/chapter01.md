# Chapter 1: Getting Started

To install pytest on a Mac using the zsh shell, you will typically use Python's package manager, pip. Before proceeding, ensure that you have Python and pip installed on your system. Here are the steps to follow:

1. **Open Terminal**: You can open the Terminal application by searching for it using Spotlight (press `Cmd + Space` and type "Terminal"), or by finding it in the Applications > Utilities folder.

2. **Check Python Installation**: Before installing pytest, ensure that Python is installed on your system. You can check this by running the following command in the Terminal:

```zsh
python3 --version
```

This command should return the version of Python installed. If Python is not installed, you will need to install it before proceeding.

**It's important to know that pytest requires Python 3.5 or newer.**

When I run this, here is what I see:

```zsh
sdr:upskill$ python3 --version
Python 3.11.7
```


## Using a virtual environment

To install pytest into a virtual environment using pip, follow these steps. This assumes you already have Python and pip installed on your system. If you're working on a project, it's a good practice to use a virtual environment to manage dependencies separately for each project.

### Step 1: Create a Virtual Environment

First, navigate to your project directory in the terminal. If you haven't already created a virtual environment for your project, do so with the following command:

```zsh
python3 -m venv myenv
```

Replace `myenv` with the name you wish to give to your virtual environment. This command creates a new directory `myenv` within your project directory, where the virtual environment files will be stored.

### Step 2: Activate the Virtual Environment

Before installing pytest or any other package, activate the virtual environment. Activation commands differ slightly depending on your operating system.

- **On macOS or Linux:**

  ```zsh
  source myenv/bin/activate
  ```

- **On Windows:**

  ```cmd
  myenv\Scripts\activate
  ```

You'll know the virtual environment is activated because its name will appear in your shell prompt, indicating that any Python or pip commands will now operate within this isolated environment.

When I run this, here is what I see:
```zsh
sdr:upskill$ python3 -m venv venv
sdr:upskill$ source venv/bin/activate
(venv) sdr:upskill$
```

#### How do I deactivate the virtual environment?

Once you're done working in the virtual environment, you can deactivate it by running:

```zsh
deactivate
```

This command returns you to your system's global Python environment, ensuring that further Python or pip commands do not affect your project's isolated environment.

#### What About virtualenv?
Some people need or want to use virtualenv. I've not tried these commands so beware:
```zsh
$ python3 -m pip install virtualenv
$ python3 -m virtualenv venv
$ source venv/bin/activate
(venv) $ 
```

#### Dropping the (venv) for the rest of the book

The (venv) added before the command prompt is useful to let you know that you are using
a virtual environment.

However, for the rest of the book the use of a virtual environment will be assumed. The `(venv) sdr:upskill$` will not be shown, as such. We’ll shorten it to just `$`.

## Using pip (Python's package installer)

pip is the tool we'll use used to install Python packages, and it is installed as part of
your Python installation.

To check the version of pip and which version of Python it’s tied to by running:

```zsh
$ pip --version
pip 24.0 from /Users/sdr/ ... /venv/lib/python3.11/site-packages/pip (python 3.11)
```

Learning about pip and details on how to use pip is beyond the scope of this book. The [Python Packaging Authority](https://pip.pypa.io) documentation is a great resource for more information on pip.

## Installing pytest

Assuming you've completed the steps above, you are ready to install pytest.

### Step 3: Install pytest

With the virtual environment activated, install pytest using pip by running:

```zsh
$ pip install pytest
```

This command downloads and installs the latest version of pytest and its dependencies into your virtual environment.

### Step 4: Verify Installation

To ensure pytest was installed correctly in your virtual environment, you can check its version:

```zsh
$ pytest --version
pytest 8.0.2
```

This should display the version of pytest that was installed, indicating that the installation was successful. You are now ready to start writing tests with pytest.

## Running pytest

With pytest installed, run it as follows:
```zsh
$ cd code/ch01
$ pytest test_getting_started.py
```

You should see the test fail. Here's the output you should see:

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

## Why start with a failing test?

Test-Driven Development (TDD) is an approach where the developer writes an automated test before coding. TDD starts with a failing test. This first test must fail because no code-under-test exists.

Kent Beck, a pioneer of Extreme Programming (XP) and TDD, emphasizes the importance of small, iterative development steps. In _Extreme Programming Explained: Embrace Change_ he says, "If you're having trouble succeeding, fail"[^1]. This philosophy underpins the TDD approach of writing a failing test before any functional code, promoting simplicity and continuous feedback.

Let's embrace the *fail our way to success* philosophy.

### Do you really _feel the need_ to make that test pass?

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
=============================================== test session starts ===============================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0
rootdir: /Users/sdr/ ... /code/ch01
collected 1 item                                                                                                  

test_getting_started.py .                                                                                   [100%]

================================================ 1 passed in 0.00s ================================================
```

And, there it is ... "1 passed"

[^1]: https://quotefancy.com/kent-beck-quotes

[Continue to Chapter 2](../ch02/chapter02.md)