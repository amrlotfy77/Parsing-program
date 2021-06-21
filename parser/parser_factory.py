from .parser_types.xml_parser import XmlParser
from .parser_types.csv_parser import CsvParser


class TypeFactory:
    supported_types = {
        "xml": XmlParser,
        "csv": CsvParser

    }

    def __init__(self, input_type):
        self.type = input_type
        self.check()

    def check(self):
        if self.type not in self.supported_types.keys():
            raise Exception("not supported file types.")

    def get_parser(self):
        return self.supported_types[self.type]
