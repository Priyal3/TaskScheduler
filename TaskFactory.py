import collections
import datetime
import heapq

from NotifyMe import NotifyMe
from SendEmail import SendEmail


class TaskFactory:
    definedTasks = set(["SendEmail", "NotifyMe"])
    allTasks = collections.defaultdict(list)
    instance = None

    @staticmethod
    def getTaskFactoryInstance():
        if not TaskFactory.instance:
            TaskFactory.instance = TaskFactory()
        return TaskFactory.instance

    def __init__(self):
        if TaskFactory.instance == None:
            TaskFactory.instance = self

    def getTaskList(self):
        print(list(self.definedTasks))
        return self.definedTasks

    def getTaskListForTime(self, time):
        # print(time, self.allTasks)
        if time in self.allTasks:
            tasks = self.allTasks[time]
            del self.allTasks[time]
            return tasks
        return []

    def getTask(self, taskString, user):
        if taskString == "SendEmail":
            return SendEmail(user)
        elif taskString == "NotifyMe":
            return NotifyMe(user)

    def addTask(self, task, time, user):
        discard = datetime.timedelta(seconds=time.second,
                                     microseconds=time.microsecond)
        storetime = time - discard
        print("Adding task ", task, " for time ", str(storetime))
        newTask = self.getTask(task, user)
        heapq.heappush(self.allTasks[str(storetime)], (time, newTask))

