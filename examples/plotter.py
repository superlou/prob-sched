import numpy as np


class Plotter:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def plot(self, plt):
        num_plots = len(self.tasks)

        duration = max([len(task.finish()) for task in self.tasks])

        for i, task in enumerate(self.tasks):
            ax = plt.subplot(num_plots, 1, i + 1)
            finish = task.finish()
            padding = duration - len(finish)
            padded_finish = np.append(finish, np.zeros(padding))
            plt.bar(np.arange(duration), padded_finish, align='center')

            ax.get_yaxis().set_visible(False)
