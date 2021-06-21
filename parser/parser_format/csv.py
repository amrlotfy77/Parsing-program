from collections import OrderedDict


class CsvDataFormatter:

    @staticmethod
    def format_data(data):
        formatted_data = []
        for u_data in data:
            formatted_data.append(OrderedDict({
                "transaction": {
                    "date": u_data['date'],
                    "customer": {
                        "id": u_data['id'],
                        "name": u_data['name'],
                        "address": u_data['address'],
                        "phone": u_data['phone']
                    },
                    "vehicles": u_data['vehicles']
                }
            }))

        return formatted_data
