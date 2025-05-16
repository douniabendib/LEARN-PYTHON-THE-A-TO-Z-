# Testing and debugging

# Unit Tests

Unit testing involves taking smaller pieces of a large program and checking that the code behaves as expected under various scenarios. A unit of code can be as simple as a small function or as complex as a large class.

In Python, the unittest framework is a built-in module. It helps developers validate the behavior of their code, piece by piece. By isolating and testing each unit independently, we can verify their functionality and behavior.
A unittest can be as simple as testing that values are the same. We use .assertEqual in unittest to ensure two elements are equal to each other.
```python
assertEqual(a, b)
## a == b
```
To use the unittest framework in a new Python file, we must first import it:
import unittest

