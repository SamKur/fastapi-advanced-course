import pytest
from app.logic import is_eligible_for_loan

# activate venv, cd to unit-testing folder
# pytest tests/ -- to run all tests in the 'tests' directory    INSIDE THIS ->
# test_*.py *_test.py (ignores most files including like .venv, .git, or build) INSIDE THIS ->
# def test_*, class Test* without __init__

# special cases-
# also does testing in subclasses of unittest.TestCase
# conftest.py: pytest looks for these files to load local plugins, fixtures, and hooks that apply to tests in that directory and below.

# run test => pytest tests/

# file name should start with test_ and test functions should also start with test_ for pytest to recognize them as tests
def test_eligible_user():
    assert is_eligible_for_loan(60000, 25, 'employed') == True


def test_underage_user():
    assert is_eligible_for_loan(60000, 19, 'employed') == False


def test_low_income():
    assert is_eligible_for_loan(30000, 25, 'employed') == False


def test_unemployed_user():
    assert is_eligible_for_loan(60000, 25, 'unemployed') == False


def test_boundary_case():
    assert is_eligible_for_loan(50000, 21, 'employed') == True