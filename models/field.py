class Field:
    def __init__(self, identification, name, min=0, max=0, content=""):
        self.name = name
        self.minValue = min
        self.maxValue = max
        self.content = content
        self.id = identification
