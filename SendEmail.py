from Task import Task


class SendEmail(Task):

    def run(self):
        print("############## Sending email for ", self.user, "  ################### ")