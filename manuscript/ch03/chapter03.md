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
* Use the var keyword whenever it is allowed.
* Create a context class to encapsulate repeating arrangement code.
* Write helper classes to hold code that is common to tests across the suite.
* Pass data as arguments into the test method to data-drive the testing.


Here’s a cheat sheet to make your test code better:

- **Naming is important**: Pick the right naming convention for your test functions, classes, modules and folders.
- **Use a consistent pattern for the test method body**: Consistency is key.
- **Short and sweet**: Aim to keep your test methods under ten lines.
- **Limit the test actions to one or two lines of code**: Don’t make your tests run a marathon.
- **One primary assertion rule**: Focus to one primary thing you’re checking per test.
- **Context classes are your friends**: Test code that sets up your tests goes in a context class.
- **Helper classes to the rescue**: Common code across your tests? Offload it into helper classes.
- **Data-drive your tests**: Feeding different data into your tests? Pass them as parameters.


#### Naming Convention

Diving into the jungle of test code naming conventions, you'll find a bunch of different paths, each with its own cheerleaders and naysayers. This book goes with the flow of the [Conventions for Python test discovery](https://docs.pytest.org/en/latest/explanation/goodpractices.html#conventions-for-python-test-discovery) that `pytest` uses.

Here’s the lowdown on how `pytest` finds tests:
- If you don’t tell it otherwise, `pytest` starts looking for tests where you are, in the current directory. You can change things with command line arguments, pointing it at specific directories or files, or set up a `testpaths`.

- It will look in subdirectories, unless the subdirectory is on the `norecursedirs` list.

- Within those directories, it’s looking for files named `test_*.py` or `*_test.py`.

- From those files, `pytest` collects test items:
  - Functions or methods outside classes that start with `test_`.
  - Inside classes that start with a `Test` prefix (and no `__init__` method), it looks for methods that start with `test_`.

The method to naming your test code with `pytest` should follow this convention.

#### Test functions and classes

- For a test function or method, we'll start its name off with `test_`, such as `test_whatchamacallit`
- And if we're testing the `Whatchamacallit` class, start them with a `Test` prefix, such as `TestWhatchamacallit`.


#### Directory and file structure

- For files, we'll be starting with `test`, like `test_whatchamacallit.py`
- Putting tests into an extra directory outside the system-under-test code is useful

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


#### More about names

Test code is a lot different than production code. Test code should never see the light of production. Because of that, we name test code differently.

We need a naming convention for our test code that's clear and makes our lives easier. Why? Because when tests fail, we want to know why without having to decipher the output. Keep it distinct, keep it clear, and make our test code as maintenance-friendly as possible.

The naming convention presented here is helpful in these ways:
- The test directory and filename identifies the modules being tested.
- The test class name identifies the class-under-test, which is the class that the tests are testing.
- The test method (or function) name describes two key aspects of the test:
  - Conditions of the test
  - Expected results of the test

For example, in the `test_temperature_converter.py` file the `test_when_passed_10000_pt_1_expect_raises_message` method:
- tests the temperature converter (we get that from the file name)
- when passed 10000.1 as input
- expect that it raises an error with a message

This example test class tests the `compute_payment()` method of the `Loan` class.
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


That's the idea for now.

**NOTE:** We'll cover the `conftest.py` files and the special `__init__.py` files you see under the `tests` folder in a later section. We'll also revisit the topic of abbreviating test method (or function) names.


## Focus on writing maintainable test code
## Adopt an effective naming convention
## Use the Arrange-Act-Assert (3-As) pattern
## Prefer many short tests over few long tests
## Avoid more than one line of action
## Avoid more than one _primary_ assertion
## Avoid type hints in test code
## Use a _TestsContext_ class to reduce repetition and manage complexity
## Build _TestHelper_ classes to promote reuse
## Data-drive test methods for multiple test cases
## Perform boundary-value analysis to cover all scenarios
## Use stubs to test in isolation
## Use only one mock when testing interaction
