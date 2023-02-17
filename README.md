# Data Engineering Pre-Task

Welcome to the Kaufland e-commerce Team Data Engineering Python Pre-Task! If you have been sent a link to this GitHub repository by one of our technical recruiters, it means we are interested in working with you.

By solving this task, you will give us an indicator for what to talk about in the upcoming tech interview. It is a big support during the recruiting process, so we thank you already for taking your time to take a look at the repository.

## Task

Your task is to write the logic for a new automated cargo robot utilised in one of the Kaufland e-commerce warehouses. The robot's operating system is already in place, all joints are properly oiled up, and it is eager to start working. All that is missing is a tiny bit of software to make sure it does not overextend its maximum load while still being the most effective!

In order to help it, you will implement a function called `maximum_value(orders, maximum_load)` that, for a given list of `orders` and a `maximum_load`, tries to find the best combination of items based on their value; orders are dictionaries of the form

```python
order = {
    'weight': 5,
    'value': 10,
}
```

Because Team Data Engineering is working using [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development), we prepared a test suite for you already. So all you have to do is install the requirements in the [requirements.txt](./requirements.txt) and implement your business logic.

## Test Suite

The tests are implemented using [pytest](https://docs.pytest.org/en/7.2.x/), our test framework of choice. In order to run the test suite, you have to call it like this:

```shell
$ pytest maximum_value_test.py
```

## Evaluation Criteria

We will evaluate your solution based on the following criteria:

- Does your code pass all tests?
- Is it idiomatic Python code?
- Is it readable and properly documented?

## How to hand in your solution

Once you are done coding your solution, please upload it to GitHub and share your repository with your technical recruiter. They will forward it to us.
