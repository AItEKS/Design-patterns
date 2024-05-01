from datetime import datetime

class LogEntry:
    def __init__(self, category, message, timestamp=None):
        self.category = category
        self.message = message
        self.timestamp = timestamp or datetime.now()

    def __str__(self):
        return f"[{self.timestamp}] {self.category}: {self.message}"