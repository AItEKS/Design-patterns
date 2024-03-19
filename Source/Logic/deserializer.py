class deserializer:
    def __init__(self):
        pass

    def deserialize(self, json_obj):
        if isinstance(json_obj, dict):
            for key, value in json_obj.items():
                if isinstance(value, dict):
                    json_obj[key] = self.deserialize(value)
                elif isinstance(value, list):
                    json_obj[key] = [self.deserialize(item) for item in value]
                elif '__class__' in value and '__module__' in value:
                    class_name = value['__class__']
                    module_name = value['__module__']
                    module = __import__(module_name, fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    instance = class_()
                    instance.__dict__.update(value)
                    json_obj[key] = instance

        return json_obj

