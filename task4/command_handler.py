from tabulate import tabulate
import user_datasource


def add_user(name, phone):
    user_datasource.add({
        "name": name,
        "phone": phone,
    })


def change_user(name, phone):
    user_datasource.update({
        "name": name,
        "phone": phone,
    })


def get_user_phone(name):
    user = user_datasource.get_by_name(name)
    return user["phone"]


def show_all():
    users = user_datasource.get_all()
    table_data = [(user["name"], user["phone"]) for user in users]
    
    print(tabulate(table_data, headers=["Name", "Phone"], tablefmt="fancy_grid"))
 
def show_help():
    help_text = """
🤖 Command Line Tool

Usage:
    command [options]

Available Commands:
    add <name> <phone>        Adds a new user with the specified name and phone number.
                              Example: `add John 1234567890`

    change <name> <phone>     Updates the phone number of an existing user.
                              Example: `change John 0987654321`

    phone <name>              Retrieves the phone number of the specified user.
                              Example: `phone John`

    all                       Displays all users and their phone numbers.

    hello                     Greets the user and offers assistance.

    help                      Displays this help message.

    close / exit              Exits the application.
"""
    print(help_text)