import sys
from pathlib import Path
from colorama import Fore, init

def display_directory_tree():
    """Show the directory tree of a given directory path."""
    init()

    try:
        path = Path(sys.argv[1])
    except IndexError:
        print("Please enter a valid directory path.")
        return

    if not path.exists():
        print("Directory path does not exist.")
        return

    if not path.is_dir():
        print(f"{path} is not a directory.")
        return

    print(Fore.BLUE + f"{path.name}/")

    def iterate_folder(path: Path, prefix: str = '    '):
        try:
            for item in sorted(path.iterdir()):
                if item.is_dir():
                    print(Fore.BLUE + f"{prefix}{item.name}/")
                    iterate_folder(item, prefix + "    ")
                else:
                    print(Fore.GREEN + f"{prefix}{item.name}")
        except PermissionError:
            print("Access denied.")

    iterate_folder(path)

if __name__ == '__main__':
    display_directory_tree()