import re

import command_handler


def parse(command: str) -> int:
    command = command.strip()

    try:
        if re.search(r"^close$|^exit$", command, re.IGNORECASE):
            print('🤖\tGoodbye!')
            return 1
        
        elif re.search(r"^hello$", command, re.IGNORECASE):
            print("🤖\tHow can I help you?")
        

        elif (match := re.search(r"^add (?P<name>\w+) (?P<phone>[\d\+\-\(\)\s]+)$", command, re.IGNORECASE)):
            name = match.group('name')
            phone_number = match.group('phone')
            command_handler.add_user(name, phone_number)
            print(f"🤖\tUser '{name}' has been added")

        elif (match := re.search(r"^change (?P<name>\w+) (?P<phone>[\d\+\-\(\)\s]+)$", command, re.IGNORECASE)):
            name = match.group("name")
            phone_number = match.group("phone")
            command_handler.change_user(name, phone_number)
            print(f"🤖\tUser '{name}' has been changed")

        elif (match := re.search(r"^phone (?P<name>\w+)$", command, re.IGNORECASE)):
            name = match.group("name")
            phone = command_handler.get_user_phone(name)
            print(f"🤖\tUser phone: '{phone}'")
            
        elif (match := re.search(r"^all$", command, re.IGNORECASE)):
            command_handler.show_all()

        elif (match := re.search(r"^help$", command, re.IGNORECASE)):
            command_handler.show_help()

        else:
            print("🤖\tUnknown command. Please try one more time.")
        
    except ValueError as e:
        print(f"🤖\t{e}")
        return 0
    else:
        return 0
    