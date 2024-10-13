from statistics import mean

class InvalidDataFormat(Exception):
    """Exception raised when the data format in the file is invalid."""
    pass

def parse_record(record):
    """
    Parses a record from the file.

    Args:
        record (str): A string representing a single record from the file, 
                      in the format "name,salary".

    Returns:
        tuple: A tuple containing the name (str) and salary (int).

    Raises:
        InvalidDataFormat: If the record is not in the correct format or the salary 
                           cannot be converted to an integer.
    """
    try:
        name, salaryStr = record.split(',')
        salary = int(salaryStr)
    except (ValueError, IndexError):
        raise InvalidDataFormat(f"Invalid record format: {record.strip()}")

    return name, salary

def total_salary(path):
    """
    Reads salary records from a file and calculates the total and average salary.

    Args:
        path (str): The file path to the data file containing salary records.

    Returns:
        tuple: A tuple containing the total salary (int) and average salary (float).

    Raises:
        InvalidDataFormat: If any record in the file has an invalid format.
    """
    with open(path, encoding='UTF-8') as file:
        lines = file.readlines()

        records = [parse_record(line) for line in lines]

        salaries = [salary for _, salary in records]

        total = sum(salaries)
        average = mean(salaries)

        return total, average


# Example usage
try:
    total, average = total_salary('task1_data.txt')
    print(f"Total salary: {total}")
    print(f"Average salary: {average}")
except InvalidDataFormat as e:
    print(e)
