from Task import Task


class NotifyMe(Task):

    def run(self):
        print("##############  ", self.user, " is being Notified #################")