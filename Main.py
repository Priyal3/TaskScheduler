import datetime

from TaskExecutor import TaskExecutor
from TaskFactory import TaskFactory


def scheduleTask(task, time, user):
    taskFactory = TaskFactory()
    if task not in taskFactory.getTaskList():
        print(task, " not a valid task")
        return
    if time == "ASAP":
        time = datetime.datetime.now()
    taskFactory.addTask(task, time, user)


if __name__ == '__main__':
    currentTime = datetime.datetime.now()
    timedelta = datetime.timedelta(seconds=2)
    scheduleTask("NotifyMe", currentTime, "Sam") # t
    scheduleTask("OrderFood", currentTime, "Bob") # t
    scheduleTask("SendEmail", currentTime + 1 * timedelta, "Peter") # t + 4
    scheduleTask("NotifyMe", currentTime + 15 * timedelta, "Grey") # t + 30
    scheduleTask("SendEmail", currentTime + 7 * timedelta, "Dwight") # t + 14
    scheduleTask("NotifyMe", currentTime + 40 * timedelta, "Jim") # t + 80
    scheduleTask("SendEmail", currentTime + 21 * timedelta, "Mike") # t + 42
    # Right Order
    # Sam -> Bob -> Peter -> Dwight -> Grey -> Mike -> Jim
    taskExecutor = TaskExecutor()
    taskExecutor.excecute()

