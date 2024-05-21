import os
import json

class Setting:
    
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
    
    def to_dict(self):
        return {"key": self.key, "value": self.value}
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["key"], data["value"])

    @staticmethod
    def load_all_settings():
        filepath = "data/settings.json"
        if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            return []
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
                return [Setting.from_dict(pair) for pair in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
        
    @staticmethod
    def find_setting(settings, key):
        for setting in settings:
            if setting.key == key:
                return setting
        return None
    
    @staticmethod
    def set_setting(settings, setting):
        existing_setting = Setting.find_setting(settings, setting.key)
        if existing_setting:
            existing_setting.value = setting.value
        else:
            settings.append(setting)
            
