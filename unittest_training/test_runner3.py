import unittest
import utest_calc

testLoad = unittest.TestLoader()
suites = testLoad.loadTestsFromModule(utest_calc)

testResult = unittest.TestResult()

runner = unittest.TextTestRunner(verbosity=1)
testResult = runner.run(suites)
print("errors")
print(len(testResult.errors))
print("failures")
print(len(testResult.failures))
print("skipped")
print(len(testResult.skipped))
print("testsRun")
print(testResult.testsRun)