from multiprocessing.managers import BaseManager
from multiprocessing import Queue

PORT = 50000
KEY = b"Maxoff"

class QueueManager(BaseManager): pass

class QueueClient:
    def __init__(self):
        QueueManager.register('get_result_queue')
        QueueManager.register('get_task_queue')
        client_manager = QueueManager(address=('', PORT), authkey=KEY)
        client_manager.connect()
        self.task_queue = client_manager.get_task_queue()
        self.result_queue = client_manager.get_result_queue()





if __name__ == "__main__":
    
    task_queue = Queue()
    result_queue = Queue()

    QueueManager.register('get_task_queue', callable=lambda:task_queue)
    QueueManager.register('get_result_queue', callable=lambda:result_queue)
    queue_manager = QueueManager(address=('', PORT), authkey=KEY)
    s = queue_manager.get_server()
    s.serve_forever()
