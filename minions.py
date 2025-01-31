from QM import QueueClient
from  task import Task
import numpy as np



class Minion(QueueClient):


    def run_queue(self):
        for i in range(5):
            a_task = self.task_queue.get()
            a_task.work()
            #self.result_queue.put(f"Task {a_task.identifier} done successfully with norm2(ax) = {np.linalg.norm(a_task.a @ a_task.x)}, norm2(b) = {np.linalg.norm(a_task.b)}")
            self.result_queue.put(a_task)


if __name__ == "__main__":
    minion = Minion()
    minion.run_queue()


    

    