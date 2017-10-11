import numpy as np
from prob_sched import Task


def test_task_creation_can_use_numpy_array():
    t = Task(np.array([0, 0, 1]))
    assert np.array_equal(t.finish(), [0, 0, 1])


def test_task_creation_can_use_list():
    t = Task([0, 0, 1])
    assert np.array_equal(t.finish(), [0, 0, 1])


def test_calculate_finish_without_uncertainty():
    t1 = Task([0, 0, 1])
    t2 = Task([0, 1], t1)
    t3 = Task([0, 1], t2)

    assert np.array_equal(t1.finish(), [0, 0, 1])
    assert np.array_equal(t2.finish(), [0, 0, 0, 1])
    assert np.array_equal(t3.finish(), [0, 0, 0, 0, 1])


def test_calculate_cumulative_finish():
    t1 = Task([0, 0.5, 0.5])
    assert np.array_equal(t1.cum_finish(), [0, 0.5, 1.0])

    t2 = Task([0, 0.1, 0.3, 0.6])
    assert np.array_equal(t2.cum_finish(), [0, 0.1, 0.4, 1.0])

    t3 = Task([0, 0.5, 0.5], t1)
    assert np.array_equal(t3.cum_finish(), [0, 0, 0.25, 0.75, 1.0])
