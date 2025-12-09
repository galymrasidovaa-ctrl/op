import datetime

class Logger:
    _instance = None  # Singleton instance
    _initialized = False  # To prevent re-initialization

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.logs = []
            self._initialized = True

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logs.append(f"{timestamp}: {message}")


# Demonstration
logger1 = Logger()
logger2 = Logger()

logger1.log("System started")

print(logger2.logs)        # ['2025-12-09 00:00:00: System started'] сияқты шығуы керек
print(logger1 is logger2)  # True
