import os


def load(name):
    return []


def save(name, journal_data):
    filename = os.path.join(name, "User/Desktop", "file.txt")
    print(f" .....saving file to format(filename)")
    fout = open(filename, 'w')
    for entry in journal_data:
        fout.write(entry)
    fout.close()


def add_entry(text, journal_data):
    journal_data.append(text)
