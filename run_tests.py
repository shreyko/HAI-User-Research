"""Test runner script for OrderFlow Core Service.

Usage:
    python run_tests.py           # Runs all test suites
    python run_tests.py 1         # Runs only test 1
    python run_tests.py 2         # Runs only test 2
    python run_tests.py 3         # Runs only test 3
    python run_tests.py 4         # Runs only test 4
    python run_tests.py 5         # Runs only test 5
"""

import sys
import unittest

def run_tests(target: str = "all"):
    test_mapping = {
        "1": "tests.test_1",
        "test1": "tests.test_1",
        "test_1": "tests.test_1",
        "2": "tests.test_2",
        "test2": "tests.test_2",
        "test_2": "tests.test_2",
        "3": "tests.test_3",
        "test3": "tests.test_3",
        "test_3": "tests.test_3",
        "4": "tests.test_4",
        "test4": "tests.test_4",
        "test_4": "tests.test_4",
        "5": "tests.test_5",
        "test5": "tests.test_5",
        "test_5": "tests.test_5",
    }

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    target_clean = target.lower().strip()
    if target_clean in ("all", ""):
        print("==================================================")
        print(" Running All Test Suites                          ")
        print("==================================================")
        discovered = loader.discover("tests", pattern="test_*.py")
        suite.addTests(discovered)
    elif target_clean in test_mapping:
        module_name = test_mapping[target_clean]
        print(f"--> Running test module: {module_name}")
        loaded = loader.loadTestsFromName(module_name)
        suite.addTests(loaded)
    else:
        print(f"Unknown test target: '{target}'. Use 'all', '1', '2', '3', '4', or '5'.")
        sys.exit(1)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)

if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "all"
    run_tests(arg)
