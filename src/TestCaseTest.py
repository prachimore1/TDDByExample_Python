from src.TestCase import TestCase
from src.WasRun import WasRun


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRunFlag)
        test.run()
        assert test.wasRunFlag


TestCaseTest("testRunning").run()
