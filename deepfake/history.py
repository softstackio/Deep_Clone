class History:
    def __init__(self, limit=20):
        self.limit = limit
        self.entries = []

    def record(self, expression, result):
        self.entries.append((expression, result))
        if len(self.entries) > self.limit:
            self.entries.pop(0)

    def last(self):
        return self.entries[-1] if self.entries else None

    def clear(self):
        self.entries.clear()
