import time

import numpy as np
import json


class Task:
    def __init__(self, identifier=0, size=None):
        self.identifier = identifier
        self.size = size or 1000 #np.random.randint(300, 3_000)
        self.a = np.random.rand(self.size, self.size)
        self.b = np.random.rand(self.size)
        self.x = np.zeros((self.size))
        self.time = 0
    


    def work(self):
        #start = time.perf_counter()
        start = time.time() 
        self.x = np.linalg.solve(self.a, self.b)
        #self.time = time.perf_counter() - start
        self.time = time.time() - start
        print(f"Task N {self.identifier}, duration : {self.time}, result : {self.x}")
    
    def to_json(self) -> str : 
        dict = {
            "a": self.a.tolist(),
            "b": self.b.tolist(),
            "x": self.x.tolist(),
            "identifier": self.identifier,
            "size": self.size
        }
        return(json.dumps(dict))

    @staticmethod
    def from_json(text: str) -> "Task":
        data =json.loads(text)
        task = Task()
        task.a = np.array(data["a"])
        task.b = np.array(data["b"])
        task.x = np.array(data["x"])
        task.size = np.array(data["size"])
        task.identifier = np.array(data["identifier"])
        task.time = float(data["time"])
        return task
    
    def __eq__(self, other: "Task") -> bool:
        if isinstance(other, Task):
            if (other.identifier == self.identifier) : 
                return True
            else :
                return False
        return False


if __name__== "__main__":

    a = Task(2)
    txt = a.to_json()
    b = Task.from_json(txt)
    print(a.__eq__(b))
    
    