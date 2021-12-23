import sys
import unittest

from tests.test import TestAPI


def suite():
    test_suite = unittest.TestSuite()
    test_loader = unittest.TestLoader()
    test_suite.addTest(test_loader.loadTestsFromTestCase(TestAPI))

    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    result = runner.run(suite())
    sys.exit(not result.wasSuccessful())
