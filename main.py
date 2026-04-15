import notes_manager

def main():
    notes_manager.initialize()

    while True:
        print("\n1. Create Note")
        print("2. Read Note")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Title: ")
            content = input("Content: ")
            notes_manager.add_note(title, content)

        elif choice == '2':
            title = input("Title: ")
            notes_manager.read_note(title)

        elif choice == '3':
            title = input("Title: ")
            notes_manager.delete_note(title)

        elif choice == '4':
            break

if __name__ == "__main__":
    main()