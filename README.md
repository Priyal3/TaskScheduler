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
  
  
  
  ################ Sample Output #################

Adding task  NotifyMe  for time  2019-10-13 15:32:00
OrderFood  not a valid task
Adding task  SendEmail  for time  2019-10-13 15:32:00
Adding task  NotifyMe  for time  2019-10-13 15:32:00
Adding task  SendEmail  for time  2019-10-13 15:32:00
Adding task  NotifyMe  for time  2019-10-13 15:33:00
Adding task  SendEmail  for time  2019-10-13 15:32:00
########## Task Executor Starting #########
Looking for tasks for time  2019-10-13 15:32:00
Number of tasks Found:  5
##############   Sam  is being Notified #################
############## Sending email for  Peter   ################### 
############## Sending email for  Dwight   ################### 
##############   Grey  is being Notified #################
############## Sending email for  Mike   ################### 
Looking for tasks for time  2019-10-13 15:33:00
Number of tasks Found:  1
##############   Jim  is being Notified #################
Executed all tasks
  
