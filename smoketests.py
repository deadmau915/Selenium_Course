from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AsertionsTest
from searchtests import SearchTests

assertions_test = TestLoader().loadTestsFromTestCase(AsertionsTest)
search_tests = TestLoader().loadTestsFromTestCase(SearchTests)

smoke_test = TestSuite([assertions_test, search_tests])

kwargs = {
    "output": "smoke-report"
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)