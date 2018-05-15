import journal


def print_header():
    print('Welcome to the Journal App')


def run_event_loop():
    cmd = None
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print('That is not an understood command.')

    print('goodbye.')
    journal.save(journal_name)


def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('{}.{}'.format(idx, entry))


def add_entry(data):
    entry = input('what would you like to add?: ')
    journal.add_entry(entry, data)


def main():
    print_header()
    run_event_loop()


main()
