import json

class TaskManager:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_tasks(self):
        try:
            with open(self.filepath, "r") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            print("Error: file not found")
            self.tasks = []
    def get_incomplete(self):
        self.incomplete = [t for t in self.tasks if t["done"] == False]
        return self.incomplete
    def summary(self):
        incomplete = self.get_incomplete()
        print(f"You have {len(incomplete)} incomplete tasks:")
        for t in incomplete:
            print("-", t["task"])

manager = TaskManager("tasks.json")
manager.load_tasks()
manager.summary()