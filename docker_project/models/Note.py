class Note:
    def __init__(self, title=None, content=None, due_date=None, priority=None):
        self.priority = priority
        self.due_date = due_date
        self.content = content
        self.title = title

    def to_dict(self):
        return {
            'title': self.title,
            'content': self.content,
            'due_date': self.due_date,
            'priority': self.priority
        }
