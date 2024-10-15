import os
import tempfile
import models


_db_path = 'database.txt'
_file_encoding = "UTF-8"
_eol = "\n"

def add(user):
    with open(_db_path, "a", encoding=_file_encoding) as file:
        file.write(models.serialize_user(user) + _eol)


def update(user):
    updated = False

    with open(_db_path, "r", encoding=_file_encoding) as file, \
         tempfile.NamedTemporaryFile('w', delete=False, encoding=_file_encoding) as temp_file:

        for line in file:
            record = models.parse_user(line)
            if record["name"] == user["name"]:
                updated_record = models.serialize_user(user)
                temp_file.write(updated_record + _eol)
                updated = True
            else:
                temp_file.write(line)

    if updated:
        os.replace(temp_file.name, _db_path)
        return user
    else:
        os.remove(temp_file.name)
        raise ValueError(f"User with name '{user['name']}' not found.")
    
def get_by_name(name):
    with open(_db_path, "r", encoding=_file_encoding) as file:
        for line in file:
            record = models.parse_user(line)
            if record["name"] == name:
                return record

        raise ValueError(f"User with name '{name}' not found.")
    
    
def get_all():
    with open(_db_path, "r", encoding=_file_encoding) as file:
        return [models.parse_user(line) for line in file]