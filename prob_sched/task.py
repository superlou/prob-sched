import numpy as np


class Task():
    def __init__(self, pmf, predecessor=None):
        # Note that pmf is the Probabilty Mass Function of finishing on a
        # specific index, not the probability of being finished.
        self.pmf = pmf
        self.predecessor = predecessor

    def finish(self):
        if self.predecessor:
            return np.convolve(self.pmf, self.predecessor.finish())
        else:
            return self.pmf

    def cum_finish(self):
        return np.cumsum(self.finish())
