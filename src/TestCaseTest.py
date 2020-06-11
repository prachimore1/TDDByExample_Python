from src.TestCase import TestCase
from src.WasRun import WasRun


class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        self.test = WasRun("testMethod")
        self.test.run()
        assert self.test.log == "setUp testMethod tearDown"


TestCaseTest("testTemplateMethod").run()
