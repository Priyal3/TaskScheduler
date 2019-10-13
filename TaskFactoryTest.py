import datetime
import unittest

from TaskFactory import TaskFactory


class TaskFactoryTest(unittest.TestCase):

    def setUp(self) -> None:
        self.taskFactory = TaskFactory()
        time = datetime.datetime.now()
        discard = datetime.timedelta(seconds=time.second,
                                     microseconds=time.microsecond)
        self.storetime = time - discard

    def test_getTaskList(self):
        self.assertEqual(list(self.taskFactory.getTaskList()), ["SendEmail", "NotifyMe"], "Valid tasks are incorrect")

    def test_getTaskListForTime(self):
        tasks = self.taskFactory.getTaskListForTime(self.storetime)
        ans = ""
        for task in tasks:
            ans += task.user+":"
        tasks = self.taskFactory.getTaskListForTime(self.storetime + datetime.timedelta(minutes=1))
        ans = ""
        for task in tasks:
            ans += task.user + ":"
        self.assertEqual(ans, "Sam:Peter:Dwight:Grey:Mike:", "Task order stored incorrectly for 1st minute")
        self.assertEqual(ans, "Jim:", "Task order stored incorrectly for 2nd minute")

if __name__ == '__main__':
    unittest.main()