import dddata


def main():
    print_header()
    run_event_loop()


def print_header():
    print("------------")
    print("JOURNAL APP")
    print("-------------")


def run_event_loop():
    print("What do you want to do with your journal? ")
    cmd = None
    journal_name = 'default'
    journal_data = dddata.load(journal_name)

    while cmd != 'x':
        cmd = input("[L]ist entries,[A]dd an entry,[E]xist")
        # cmd=cmd.lower().strip()
        if cmd.upper().strip() == 'L':
            list_entries(journal_data)
        elif cmd.lower().strip() == 'a':
            add_entry(journal_data)
        elif cmd.lower().strip() != 'x':
            print("sorry we dont understand the command")

    print("Done Goodbye")
    dddata.save(journal_data, journal_name)


def list_entries(journal_data):
    #entries = reversed(data)
    for id ,entry in enumerate(journal_data):
        print(f"{id+1}] {entry}")


def add_entry(journal_data):
    text = input("type your entry")
    dddata.add_entry(text,journal_data)
    journal_data.append(text)

main()
