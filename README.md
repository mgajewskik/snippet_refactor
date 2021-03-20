# Mistakes

- wrong foo constant location, before imports
- wrong foo constant name, should be uppercase
- unused import Expense
- tuple typename in named tuple declaration is non descriptive
- definition name does not meet python standard of lowercase_with_underscores
- input argument in function is a keyword in python
- naming of variables in the function is unclear as what does what
- function does many things and does not have a single responsibility
- there is no exit condition from for loop if item amount is lower than minimum amount
- last print statement does not have parentheses
- when printing we cannot access expense.type_ because we are iterating by dict keys and not MyExpense instances
- reverse argument is False by default so there is no need to use it otherwise it should be True
- all code was refactored according to "clean code" standards in the `refactored.py` file


# Comment

Code overall leaves a lot of room for imprevement and doesn't conform to the Python standards.
It is much easier to refactor leaving more or less similar code structure than to fix the small issues.
The solution is given for this specific piece of code, but I still think that the whole problem could be
solved much easier and integrated into the existing codebase in a more elegant way.


# Solution

Proposed refactored solution can be found in file `refactored.py`
