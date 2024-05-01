from Source.Logics.storage_observer import storage_observer
from Source.Models.event_type import event_type


class LoggingObserver(storage_observer):
    def __init__(self, settings):
        self.settings = settings
        self.log_entries = []

    def update(self, event_type, data):
        if event_type == event_type.LOG_ENTRY:
            self.log_entries.append(data)

    def save_logs(self, filename="logs.txt"):
        with open(filename, "w") as f:
            for entry in self.log_entries:
                f.write(str(entry) + "\n")