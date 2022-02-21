
import sys
import json
import clipboard

SAVED_DATA = "clipboard.json"


def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    # create a dictionary with the json keys and values
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        # get whats currently copied on the clipboard gives it a key-value-pair reference
        data[key] = clipboard.paste()
        # loads the referenced key-value-pair into the file
        save_data(SAVED_DATA, data)
    elif command == "load":
        key = input("Enter the key to load data from: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")
    elif command == "list":
        print(f'Clipboard contents: {load_data(SAVED_DATA)}')
    else:
        print("Unknown command")
else:
    print("Please enter ONE command only.")
