import json


import os
from models.field import Field
from models.option import Option

from utils.constants import SUCCESS

ALL_PROTOCOl = {
    2: [],
    3: [],
    4: [],
    7: [],
}


class Protocol:
    def __init__(
        self,
        name,
        coucheNumber,
        protocolIdentification,
        fields,
        options,
        maxSize,
        requestTypeSeparator,
        nextProtocolEncapsulated,
        headerSeparator,
        color,

    ) -> None:
        self.name = name
        self.layer = coucheNumber
        self.maxSize = maxSize
        self.protocolIdentification = protocolIdentification
        self.fields = self.loadAllField(fields)
        self.options = self.loadOptions(options)
        self.requestTypeSeparator = requestTypeSeparator
        self.headerSeparator = headerSeparator
        self.nextProtocolEncapsulated = nextProtocolEncapsulated
        self.color = color

    @staticmethod
    def loadModelFromJson(filePath):
        with open(filePath, "r") as json_file:
            data = json.loads(json_file.read())
            return Protocol(**data)

    @staticmethod
    def loadAllProtocol():
        filePath = "models/data"
        res = SUCCESS
        for file in os.listdir(filePath):
            if file.endswith(".json"):
                path = f"{filePath}/{file}"
                model = Protocol.loadModelFromJson(path)
                ALL_PROTOCOl[model.layer].append(model)
        return res

    def loadAllField(self, fields):
        listFields = []

        for idField, field in fields.items():
            f = Field(identification=idField,
                      min=field["min"], max=field['max'], name=field["name"],
                      )
            listFields.append(f)

        return listFields

    def loadOptions(self, options):

        f = Option(**options)
        return f
