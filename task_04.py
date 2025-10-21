def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return 'Contact already exists. Try again.'
    else:
        contacts[name] = phone
        return 'Contact added.'


def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return 'Contact updated.'
    else:
        return 'Contact does not exist. Try again.'


def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return 'Contact does not exist. Try again.'


def show_all(contacts):
    if contacts:
        result = ", ".join([f"{name}: {phone}" for name, phone in contacts.items()])
        return result
    else:
        return "No contacts found."


def main():
    contacts = {}

    print('Welcome to the assistant bot!')

    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        try:
            if command in ['close', 'exit']:
                print('Goodbye!')
                break

            elif command == 'hello':
                print('How can I help you?')

            elif command == 'add':
                print(add_contact(args, contacts))

            elif command == 'change':
                print(change_contact(args, contacts))

            elif command == 'show':
                print(show_phone(args, contacts))

            elif command == 'all':
                print(show_all(contacts))

            else:
                print('Invalid command!')

        except ValueError:
            print('Invalid command. Try again.')


if __name__ == "__main__":
    main()

