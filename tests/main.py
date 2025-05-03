from testing_framework.test_loader import TestLoader
from testing_framework.test_suite import TestSuite
from testing_framework.test_runner import TestRunner
from .test_test_case import TestCaseTest
from .test_test_suite import TestSuiteTest
from .test_test_loader import TestLoaderTest


loader = TestLoader()
test_case_suite = loader.make_suite(TestCaseTest)
test_suite_suite = loader.make_suite(TestSuiteTest)
test_load_suite = loader.make_suite(TestLoaderTest)

suite = TestSuite()
suite.add_test(test_case_suite)
suite.add_test(test_suite_suite)
suite.add_test(test_load_suite)

runner = TestRunner()
runner.run(suite)