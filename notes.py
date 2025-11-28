import json
import os

NOTES_FILE = "notes.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []

    with open(NOTES_FILE, "r") as f:
        return json.load(f)

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)

def add_note(text):
    notes = load_notes()
    notes.append(text)
    save_notes(notes)
    print("Note added.")

def list_notes():
    notes = load_notes()
    if not notes:
        print("No notes yet.")
        return

    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")

def delete_note(index):
    notes = load_notes()
    try:
        removed = notes.pop(index - 1)
        save_notes(notes)
        print(f"Deleted note: {removed}")
    except IndexError:
        print("Invalid note number.")

if __name__ == "__main__":
    while True:
        print("\nNotes CLI")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Select: ")

        if choice == "1":
            add_note(input("Enter note: "))
        elif choice == "2":
            list_notes()
        elif choice == "3":
            delete_note(int(input("Note number to delete: ")))
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
