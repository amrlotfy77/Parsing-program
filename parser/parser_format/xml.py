from collections import OrderedDict


class XmlDataFormatter:

    @staticmethod
    def handle_vehicle_data(vehicle_data):
        formatted_data = []
        if not vehicle_data['Transaction']['Customer'].get('Units'):
            return formatted_data

        for vehicle in vehicle_data['Transaction']['Customer']['Units']['Auto']['Vehicle']:
            formatted_data.append(
                {
                    "id": vehicle['@id'],
                    "make": vehicle['Make'],
                    "vin_number": vehicle['VinNumber'],
                }
            )
        return formatted_data

    def format_data(self, data):
        formatted_data = OrderedDict({
            "transaction": {
                "date": data['Transaction']['Date'],
                "customer": {
                    "id": data['Transaction']['Customer']['@id'],
                    "name": data['Transaction']['Customer']['Name'],
                    "address": data['Transaction']['Customer']['Address'],
                    "phone": data['Transaction']['Customer']['Phone']
                },
                "vehicles": self.handle_vehicle_data(data)
            }
        })

        return formatted_data
