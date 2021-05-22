''' This is console helper which creates, changes and prints data in format User: Phone number 
    All the saved data is saved in dictionary where the user name is the key and phone number is the value
    The commands are defined in respective functions
'''


def greeting():
    return 'How can I help you?'
    

def add_contact(name, phone): #add username and his phone to dictionary of contacts
    return name_phone.update({name: phone})


def change_phone(name, phone): #amend username and his phone in dictionary of contacts
    name_phone[name] = phone
    

def print_phone(name):
    return name_phone.get(name)


def print_all_contacts():
    return name_phone


def end_bot():
    return 'Good bye!'


def input_error(func): #decorator of errors which may occur when user enters unknown command
    def inner():
        try:
            result = func()
            return result
        except KeyError:
            return "No user with given name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Enter user phone"
        except TypeError:
            return "Unknowm command"
    return inner


def identify_input(user_input): #parcer of user input
    if commands.get(user_input.lower()): #find if user input is one of the existing commands
        return commands.get(user_input.lower())
    elif user_input.lower().startswith('add') or user_input.lower().startswith('change'): #check add and change commands and their arguments
        parcer = user_input.split(' ')
        command = parcer[0].lower()
        name = parcer[1]
        phone = parcer[2]
        return (commands.get(command),name, phone)
    elif user_input.lower().startswith('phone'): #check phone command and username
        parcer = user_input.split(' ')
        command = parcer[0].lower()
        name = parcer[1].lower()
        return (commands.get(command), name)
    else:
        return user_input

@input_error
def handler():
    if isinstance(identify_input(user_input), types.FunctionType): #check for a command without arguments
        return identify_input(user_input)()
    elif len(identify_input(user_input)) == 2: #check for a command with one argument
        return identify_input(user_input)[0](identify_input(user_input)[1])
    else:
        return identify_input(user_input)[0](identify_input(user_input)[1], identify_input(user_input)[2]) #command with two arguments
    

if __name__ == '__main__':
    name_phone = {}
    commands = {'hello': greeting, 'add': add_contact, 'change': change_phone, 'phone': print_phone, 'show all': print_all_contacts,\
    'good bye': end_bot, 'close': end_bot, 'exit': end_bot}

    while True:
        import types #for is function check
        user_input = input('Enter command: \n')
        if handler() == end_bot():
            print(end_bot())
            break
        elif handler() == None:
            continue
        else:
            print(handler())
 