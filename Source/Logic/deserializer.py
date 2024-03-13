import json


class deserializer:
    @staticmethod
    def deserialize(json_data):
        data = json.loads(json_data)
        return deserializer.__process_data(data)

    @staticmethod
    def __process_data(data):
        if isinstance(data, dict):
            processed_data = {}
            for key, value in data.items():
                processed_data[key] = deserializer.__process_data(value)
            return processed_data

        elif isinstance(data, list):
            processed_data = []
            for item in data:
                processed_data.append(deserializer.__process_data(item))
            return processed_data
        else:
            return data
