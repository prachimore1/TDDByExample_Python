from src.TestCase import TestCase
from src.TestResult import TestResult
from src.WasRun import WasRun


class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert test.log == "setUp testMethod tearDown"

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert "1 run, 1 failed" == result.summary()

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert "1 run, 1 failed" == result.summary()


TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
TestCaseTest("testFailedResultFormatting").run()
TestCaseTest("testFailedResult").run()
