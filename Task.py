from abc import ABC, abstractmethod


class Task(ABC):
    user = ""

    def __init__(self, userName):
        self.user = userName

    @abstractmethod
    def run(self):
        pass