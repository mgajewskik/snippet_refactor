#!/usr/bin/python

from collections import namedtuple
from typing import List, Dict

Expense = namedtuple("Expense", ["item", "amount"])


def get_test_data() -> List[Expense]:
    """ Prepare fake data. """

    foo = []

    foo.append(Expense("food", 4))
    foo.append(Expense("food", 3))
    foo.append(Expense("car", 3))
    foo.append(Expense("dog", 1))

    return foo

def get_summarized_expenses(min_amount: int, expenses: List[Expense]) -> Dict[str, int]:
    """ Print sum of the expenses if expense.amount above the minimum amount. """

    summary = {}
    for expense in expenses:

        if expense.amount < min_amount:
            continue

        if not expense.item in summary:
            summary[expense.item] = 0

        summary[expense.item] = summary[expense.item] + expense.amount

    return summary


def print_summary(summary: Dict[str, int]):
    """ Print summary to stdout. From lowest to biggest amount. """

    for key, value in sorted(summary.items(), key=lambda i: i[1], reverse=True):
        print(key, value)


if __name__ == "__main__":

    print_summary(get_summarized_expenses(2, get_test_data()))
