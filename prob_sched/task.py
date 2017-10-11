import numpy as np


class Task():
    def __init__(self, completion=None, parent=None):
        self.completion = completion
        self.parent = parent

    def finish(self):
        if self.parent:
            return np.convolve(self.completion, self.parent.finish())
        else:
            return self.completion
