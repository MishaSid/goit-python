''' This is console helper which creates, changes and prints data in format User: Phone number 
    All the saved data is saved in dictionary where the user name is the key and phone number is the value
    The commands are defined in respective functions
    All the data is saved in binary file
'''

import pickle
import sys
import os.path

from classes import AddressBook, Record, Name, Phone, Birthday


def input_error(func): #decorator of errors which may occur when user enters unknown command
    def hundler(data):
        try:
            result = func(data)
        except Exception as e:
            return e
        return result
    return hundler


@input_error
def hello(data):
    print('How can I help you?')


@input_error
def add_ph(data): #add username and his phone to Addressbook
    data = data.replace('add ph ', '')
    if len(data.split()) == 2: # check for 'name phone' input
        name, phone = data.split()

        if name not in phone_book: #add new record
            n = Name(name)
            ph = Phone(phone)
            rec = Record(name=n, phone=ph)
            phone_book.add_record(rec)
        else: #add phone to existing record
            phone = Phone(phone)
            phone_book[name].add_phone(phone)
    else:
        raise Exception('Please enter the name and phone')



@input_error
def change_ph(data):#edit the existing phone in record
    data = data.replace('change ph ', '')
    if len(data.split()) == 3:
        name, phone, new_phone = data.split()
        if name in phone_book:
            phone_book[name].change_phone(Phone(phone), Phone(new_phone))
        else:
            raise Exception('User is not found')
    else:
        raise Exception('Please enter the name and phone')


@input_error
def phone(data):#find the phone in Addressbook
    data = data.replace('phone ', '')
    if len(data.split()) == 1:
        name = data
        if name in phone_book:
            return phone_book[name]
        else:
            raise Exception('User is not found')
    else:
        raise Exception('Please enter only a name')


@input_error
def show_all(data):#print N-quantity records 
    data = data.replace('show all', '')
    if len(data.split()) == 1:
        try:
            N = int(data)
        except:
            N = 1
    else:
        N = len(phone_book.data)

    for el in phone_book.iterator(N):#iterating by Addressbook
        print(el)
        

@input_error
def find(data):
    data = data.replace('find ', '')#search if the pattern is in Addressbook
    if len(data.split()) == 1:
        result = phone_book.full_search(data)
        return result


@input_error
def end_bot(data):
    with open('file.bin', 'wb') as f:
        pickle.dump(phone_book, f)
    return 'Good bye!'


commands = {
    'hello': hello,
    'add ph': add_ph,
    'change ph': change_ph,
    'phone': phone,
    'show all': show_all,
    'find ': find,
    'good bye': end_bot,
    'close': end_bot,
    'exit': end_bot,
    '.': end_bot,
}


@input_error
def choice_action(data):#command parser, check if the entered command is supported
    for command in commands:
        if data.startswith(command):
            return commands[command]
    raise Exception('Give me a correct command please')


if __name__ == '__main__':

    phone_book = AddressBook()
    
    try:#check if file esists
        with open('data.bin', 'rb') as fh:
            phone_book = pickle.load(fh)
    except:#create new file to save the Addressbook
        with open('data.bin', 'wb') as fh:
            pickle.dump(phone_book, fh)


    while True:
        data = input('Enter command: \n')

        func = choice_action(data)
        if isinstance(func, Exception):
            print(func)
            continue
        result = func(data)
        if result:
            print(result)
        if result == 'Good bye!':
            break