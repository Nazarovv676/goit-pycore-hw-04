import ast
import json


def parse_user(data):
    try:
        user_dict = json.loads(data)
        
        if isinstance(user_dict, dict) and "name" in user_dict and "phone" in user_dict:
            return user_dict
        else:
            raise ValueError("Parsed data is not a valid user dictionary.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing JSON data: {e}")
    
    
def serialize_user(user_dict):
    try:
        user_json = json.dumps(user_dict)
        return user_json
    except (TypeError, ValueError) as e:
        raise ValueError(f"Error serializing user data: {e}")