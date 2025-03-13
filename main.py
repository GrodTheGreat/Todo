import sys

todos = []


def init() -> None:
    print("\nWelcome to Todos! (Python Edition)\n")
    fetch_todos()


def fetch_todos() -> None:
    global todos
    try:
        with open(file="./todos.txt", encoding="utf-8") as file:
            todos = [todo.strip() for todo in file.readlines()]
    except FileNotFoundError:
        print("No stored todo data found...\n")


def write_todos() -> None:
    with open(file="./todos.txt", mode="w", encoding="utf-8") as file:
        for todo in todos:
            file.write(todo + "\n")


def prompt_user() -> None:
    print("Please select an option:")
    print("\tList todos: l")
    print("\tCreate todo: c")
    print("\tEdit todo: e")
    print("\tDelete todo: d")
    print("\tQuit: q\n")


def list_todos() -> None:
    print()
    if len(todos) == 0:
        print("No todos!\n")
        return

    for index, todo in enumerate(todos):
        print(f"{index + 1}.) {todo}")
    print()


def edit_todo() -> None:
    while True:
        try:
            user_index = input("\nEnter index of todo to be edited: ")
            index = int(user_index)
            break
        except ValueError:
            print("Invalid index!")

    if index < 1:
        print("Invalid index!")
        print()
        return

    while True:
        new_todo = input("\nEnter updated todo: ")
        if new_todo:
            break
        else:
            print("Invalid todo!")

    try:
        todos[index - 1] = new_todo
    except IndexError:
        print("Invalid index!\n")
        return
    print()


def delete_todo() -> None:
    while True:
        try:
            user_index = input("\nEnter index of todo to be deleted: ")
            index = int(user_index)
            break
        except ValueError:
            print("Invalid index!")

    if index < 1:
        print("Invalid index!")
        print()
        return

    print("Deletion is permanent!")
    confirm = input("Are you sure you want to continue? [y/N] ")
    if confirm.strip().lower() != "y":
        print("Aborting deletion...\n")
        return

    try:
        print("Attempting to delete todo...")
        todos.pop(index - 1)
    except IndexError:
        print("Invalid index!")
        return

    print("Todo deleted!")
    print()


def create_todo() -> None:
    new_todo = input("\nEnter new todo: ")
    todos.append(new_todo)
    print()


def main() -> None:
    init()

    try:
        while True:
            prompt_user()
            user_choice: str = input()
            choice = user_choice.strip().lower()
            match choice:
                case "l":
                    list_todos()
                case "c":
                    create_todo()
                case "e":
                    edit_todo()
                case "d":
                    delete_todo()
                case "q":
                    print("\nExiting Todos...")
                    print("Have a good day!")
                    sys.exit()
                case _:
                    print("Invalid option! Please enter a valid option\n")
    except KeyboardInterrupt:
        print("\nExiting Todos...")
        print("Have a good day!")
        sys.exit()
    finally:
        write_todos()


if __name__ == "__main__":
    main()
