# TaskScheduler
Immitates a system which takes in tasks with their execution times ( future or present) and runs them based on the execution times.

Main.py:
  Test to verify the system
  scheduleTask(task, time, user) -> API to schedule a "task" (string) for a "time" (datetime object) for a user ("string")

Task.py:
  Abstract base class that forces the tasks that inherits it to implement the run method
  Has a "user" attribute

  SendEmail.py
    Task to send email

  NotifyMe.py
    Task to notify me

TaskFactory
  Factory class that stores all the task objects that needs to be exceuted with their execution time

TaskExecutor.py
  Runs every minute to query the task table from TaskFactory and executes the task in that minute
  
