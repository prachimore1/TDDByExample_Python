from src.TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRunFlag = None
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRunFlag = 1
