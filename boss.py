from QM import QueueClient
from  task import Task


class Boss(QueueClient):
        
    
    def work(self):
        for i in range(5):
            task = Task(i,20)
            self.task_queue.put(task)

    def get_result(self):
        for i in range(5):
            task = self.result_queue.get()
            print(f"Task id : {task.identifier}; Task time : {task.time}")
    

if __name__ == "__main__":
    boss = Boss()
    boss.work()
    boss.get_result()