import numpy as np
import matplotlib.pyplot as plt
from plotter import Plotter
from prob_sched import Task


def spread_uniform(min, max):
    completion = np.zeros(min)
    uniform = np.ones(max - min + 1) / (max - min + 1)
    return np.concatenate([completion, uniform])


if __name__ == '__main__':
    print('Starting...')
    t1 = Task(spread_uniform(3, 5))
    t2 = Task(spread_uniform(3, 5), t1)
    t3 = Task(spread_uniform(3, 5), t2)
    t4 = Task(spread_uniform(3, 5), t3)
    t5 = Task(spread_uniform(3, 5), t4)
    p = Plotter()
    p.add_task(t1)
    p.add_task(t2)
    p.add_task(t3)
    p.add_task(t4)
    p.add_task(t5)
    p.plot(plt)
    plt.show()
