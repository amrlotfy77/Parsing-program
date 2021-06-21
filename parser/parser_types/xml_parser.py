import xmltodict

from ..parser_format.xml import XmlDataFormatter


class XmlParser:

    def __init__(self, parser_files):
        self.parser_file = parser_files[0]
        self.parser_formatter = XmlDataFormatter()
        self.parsed_content = None
        self.parsing_content()

    def parsing_content(self):
        self.parsed_content = xmltodict.parse(self.parser_file.read())

    def get_content(self):
        return self.parser_formatter.format_data(self.parsed_content['Insurance'])
