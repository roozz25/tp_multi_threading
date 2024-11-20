import unittest
import numpy as np
from task import Task


class TestWork(unittest.TestCase):
    def test_task_equals_fail(self):
        _task = Task()

        np.testing.assert_almost_equal(_task.a @ _task.x, _task.b)

    def test_task_equals_pass(self):
        _task = Task()
        _task.work()

        np.testing.assert_almost_equal(_task.a @ _task.x, _task.b)


if __name__ == "__main__":
    unittest.main()
