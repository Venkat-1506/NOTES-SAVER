import os

NOTES_DIR = "notes"

def initialize():
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)

def get_path(title):
    return os.path.join(NOTES_DIR, title + ".txt")

def add_note(title, content):
    with open(get_path(title), "w") as file:
        file.write(content)
    print("Note saved")

def read_note(title):
    path = get_path(title)
    if os.path.exists(path):
        with open(path, "r") as file:
            print(file.read())
    else:
        print("Note not found")

def delete_note(title):
    path = get_path(title)
    if os.path.exists(path):
        os.remove(path)
        print("Note deleted")