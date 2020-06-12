from src.TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRunFlag = None
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRunFlag = 1
        self.log = self.log + " testMethod"

    def testBrokenMethod(self):
        raise IOError

    def setUp(self):
        self.wasRunFlag = None
        self.log = "setUp"

    def tearDown(self):
        self.log = self.log + " tearDown"
