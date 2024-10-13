class InvalidDataFormat(Exception):
    """
    Exception raised when the data format in the file is invalid.
    """

    pass


def parse_record(record):
    """
    Parses a single record string into a dictionary containing 'id', 'name', and 'age'.

    Args:
        record (str): A string containing the record in the format 'id, name, age'.

    Raises:
        InvalidDataFormat: If the record does not conform to the expected format.

    Returns:
        dict: A dictionary with keys 'id', 'name', and 'age', containing the parsed values.
    """
    try:
        id, name, age = record.split(",")
    except (ValueError, IndexError):
        raise InvalidDataFormat(f"Invalid record format: {record.strip()}")

    return {"id": id.strip(), "name": name.strip(), "age": age.strip()}


def get_cats_info(path):
    """
    Reads the file from the given path and parses each line as a record.

    Args:
        path (str): The path to the file containing cat information.

    Returns:
        list: A list of dictionaries, where each dictionary represents a cat's information.
    """
    with open(path, encoding="UTF-8") as file:
        lines = file.readlines()

        records = [parse_record(line) for line in lines]

        return records


# Example usage
cats_info = get_cats_info("task2_data.txt")
print(cats_info)
