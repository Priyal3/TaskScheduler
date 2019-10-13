import datetime
import heapq
import time

from TaskFactory import TaskFactory


class TaskExecutor:
    taskFactory = None

    def __init__(self):
        self.taskFactory = TaskFactory()

    def excecute(self):
        print("########## Task Executor Starting #########")
        while len(self.taskFactory.allTasks) > 0:
            currentTime = datetime.datetime.now()
            discard = datetime.timedelta(seconds=currentTime.second,
                                         microseconds=currentTime.microsecond)
            storeTime = currentTime - discard
            print("Looking for tasks for time ", str(storeTime))
            tasks = self.taskFactory.getTaskListForTime(str(storeTime))
            print("Number of tasks Found: ", len(tasks))
            for i in range(len(tasks)):
                task = heapq.heappop(tasks)
                task[1].run()
            time.sleep(60)
        print("Executed all tasks")
