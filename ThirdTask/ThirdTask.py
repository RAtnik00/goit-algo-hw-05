import sys
from pathlib import Path
from colorama import Fore

def show_dir(path_str):
    path = Path(path_str)
    if not path.is_dir():
        print(Fore.RED + "Це не директорія або її не існує!")
        return

    print(Fore.BLUE + str(path.resolve()))
    for item in path.iterdir():
        if item.is_file():
            print(Fore.GREEN + item.name)
        elif item.is_dir():
            show_dir(item)

def main():
    if len(sys.argv) < 2:
        print("Вкажіть шлях до директорії!")
    else:
        show_dir(sys.argv[1])

if __name__ == "__main__":
    main()
