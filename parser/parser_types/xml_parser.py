import xmltodict


class XmlParser:

    def __init__(self, parser_files):
        self.parser_file = parser_files[0]
        self.parsed_content = None
        self.parsing_content()

    def parsing_content(self):
        self.parsed_content = xmltodict.parse(self.parser_file.read())

    def get_content(self):
        return self.parsed_content['Insurance']
