import os
import commands
from collections import OrderedDict


def print_bookmarks(bookmarks):
    for bookmark in bookmarks:
        print("\t".join(str(field) if field else "" for field in bookmark))


def print_options(options):
    for shortcut, option in options.items():
        print(f"{shortcut} {option}")


def option_choice_is_valid(choice, options):
    return choice in options or choice.upper() in options


def get_option_choice(options):
    choice = input("Choose what you want to do: ")
    while not option_choice_is_valid(choice, options):
        print("Choose A, B, T, D, or Q")
        choice = input("Choose what you want to do: ")
    return options[choice.upper()]


def get_user_input(label, required=True):
    value = input(f"{label}: ") or None
    while required and not value:
        value = input(f"{label}: ") or None
    return value


def get_new_bookmark_data():
    return {
        "title": get_user_input("Title"),
        "url": get_user_input("URL"),
        "memo": get_user_input("Memo", required=False),
    }


def clear_screen():
    clear = "cls" if os.name == "nt" else "clear"
    os.system("clear")


def get_bookmark_id_for_deletion():
    return get_user_input("Specify the bookmark ID for deletion")


def get_github_import_options():
    return {
        "github_username": get_user_input("Github User Name"),
        "preserve_timestamps": get_user_input(
            "Do you want to keep the timestamp [Y/n]", required=False
        )
        in {"Y", "y", None},
    }


def loop():
    clear_screen()
    options = OrderedDict(
        {
            "A": Option(
                "Add", commands.AddBookmarkCommand(), prep_call=get_new_bookmark_data
            ),
            "B": Option("Show by Added Date", commands.ListBookmarksCommand()),
            "T": Option(
                "Show by Title", commands.ListBookmarksCommand(order_by="title")
            ),
            "D": Option(
                "Delete",
                commands.DeleteBookmarkCommand(),
                prep_call=get_bookmark_id_for_deletion,
            ),
            "G": Option(
                "Import Github Stars",
                commands.ImportGitHubStarsCommand(),
                prep_call=get_github_import_options,
            ),
            "Q": Option("Quit", commands.QuitCommand()),
        }
    )
    print_options(options)
    chosen_option = get_option_choice(options)
    clear_screen()
    chosen_option.choose()

    _ = input("Go back home screen by entering Enter")


class Option:
    def __init__(self, name, command, prep_call=None):
        self.name = name
        self.command = command
        self.prep_call = prep_call

    def _handle_message(self, message):
        if isinstance(message, list):
            print_bookmarks(message)
        else:
            print(message)

    def choose(self):
        data = self.prep_call() if self.prep_call else None
        message = self.command.execute(data) if data else self.command.execute()
        self._handle_message(message)

    def __str__(self):
        return self.name


if __name__ == "__main__":
    print("Bookmark Management Application - BARK -")
    commands.CreateBookmarksTableCommand().execute()
    while True:
        loop()
