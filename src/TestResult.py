class TestResult:
    def __init__(self):
        self.runCount = 0
        self.failCount = 0

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.failCount += 1

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.failCount)
