#!/usr/bin/env python3

import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)


def print_path(path: Path, prefix=""):
    contents = list(path.iterdir())
    contents.sort(key=lambda x: (not x.is_dir(), x.name.lower()))

    for index, sub_path in enumerate(contents):
        connector = "┗ " if index == len(contents) - 1 else "┣ "

        if sub_path.is_dir():
            colored_name = f"📂 {Fore.BLUE}{sub_path.name}{Style.RESET_ALL}"
        else:
            colored_name = f"🗒️ {Fore.GREEN}{sub_path.name}{Style.RESET_ALL}"

        print(f"{prefix}{connector}{colored_name}")

        if sub_path.is_dir():
            new_prefix = prefix + ("  " if index == len(contents) - 1 else "┃ ")
            print_path(sub_path, new_prefix)


def main():
    if len(sys.argv) != 2:
        print("Invalid arguments length. Provide only directory path.")
        exit(1)

    root_path = Path(sys.argv[1])

    if not root_path.exists() or not root_path.is_dir():
        print(f"The path '{root_path}' is not a valid directory.")
        exit(1)

    print(f"{Fore.BLUE}{root_path.name}{Style.RESET_ALL}")
    print_path(root_path)


if __name__ == "__main__":
    main()
