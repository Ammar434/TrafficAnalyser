class Option:
    def __init__(self, greatherThanField, valueToBeGreather, fields):
        self.greatherThanField = greatherThanField
        self.valueToBeGreather = valueToBeGreather

        # TODO : NEED TO FIND A WAY TO MANAGE OPTION
        self.fields = fields

    def __str__(self) -> str:
        msgToPrint = str(self.greatherThanField) + ' ' + \
            str(self.valueToBeGreather)
        return msgToPrint
