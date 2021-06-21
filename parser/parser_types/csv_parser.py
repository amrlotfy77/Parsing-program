import csv

from ..parser_format.csv import CsvDataFormatter


class CsvParser:

    def __init__(self, parser_files):
        self.parser_file_customer = parser_files[0]
        self.parser_file_vehicles = parser_files[1]
        self.parser_formatter = CsvDataFormatter()

        self.parsed_content_vehicles = []
        self.parsed_content = []
        self.parsing_vehicles()
        self.parsing_content()

    def parsing_vehicles(self):
        dict_reader = csv.DictReader(self.parser_file_vehicles)
        for v_data in dict_reader:
            self.parsed_content_vehicles.append(v_data)

    def get_vehicles(self, _id):
        lst = []
        for i, row in enumerate(self.parsed_content_vehicles):
            if row.get('owner_id') == _id:
                del row['owner_id']
                lst.append(row)
        return lst

    def parsing_content(self):
        for line in csv.DictReader(self.parser_file_customer):
            line['vehicles'] = self.get_vehicles(line['id'])
            # print(line)
            self.parsed_content.append(line)

    def get_content(self):
        return self.parser_formatter.format_data(self.parsed_content)

