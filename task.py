class Task:
    def __init__(self,title,completed=False):
        self.title = title
        self.completed = completed

    def to_dict(self):
            return {
                "title": self.title,
                "completed": self.completed
                }
        
    @staticmethod
    def from_dict(data):
            return Task(title=data["title"], completed=data["completed"])
        

def greet (name):
    return f'Hello, {name}! Welcome to the task manager.'
        

