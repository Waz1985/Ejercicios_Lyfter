from actions import StudentManager
from data import CSVHandler
from menu import Menu

def main():
    manager = StudentManager()
    csv_handler = CSVHandler()
    menu = Menu(manager, csv_handler)
    menu.start()


if __name__ == "__main__":
    main()
