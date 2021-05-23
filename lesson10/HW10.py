#Creating classes for managing address book dictionary where key is username and value is a list of his phones

from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record): # add Record object to the address book dictionary
        self.data[record] = record


class Record:
    def __init__(self, name): #create username field and list oh his phones
        self.name = name
        self.phones = []


    def add_phone(self, phone): #add phone to the phones list
        self.phones.append(phone)


    def edit_record(self, phone, new_phone): #replace phone with new_phone in the phones list
        if phone in self.phones:
            self.phones.remove(phone)    
            self.add_phone(Phone(new_phone))
        

    def delete_record(self, phone): #remove new phone to the phones list
        self.phones.remove(phone)


class Field:
    pass

class Name(Field): # class of username
    def __init__(self, name):
        self.name = name


class Phone(Field): #class of user`s phone
    def __init__(self, phone):
        self.phone = phone
    
