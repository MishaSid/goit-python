#Creating classes for managing address book dictionary where key is username and value is a list of his phones

from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record): # add Record object to the address book dictionary
        self.data[record] = record

    def iterator(self):# iterator for AddressBook
        def __iter__(self):
            return self
        
        def __next__(self):
            return self.data.items()
       

class Record:
    def __init__(self, name): #create username field and list oh his phones
        self.name = name
        self.phones = []
        self.birthday = ''
    
    def add_phone(self, phone): #add phone to the phones list
        self.phones.append(phone)

    def edit_record(self, phone, new_phone): #replace phone with new_phone in the phones list
        if phone in self.phones:
            self.phones.remove(phone)    
            self.add_phone(Phone(new_phone))

    def delete_record(self, phone): #remove new phone to the phones list
        self.phones.remove(phone)

    def days_to_birthday(self, birthday): #return days to the next user`s birthday
        from datetime import datetime, timedelta
        self.birthday = birthday
        self.current_date = datetime.now().date()
        self.birthday_datetime = datetime.strptime(birthday, '%d.%m.%Y') #converting of dd.mm.yyyy string to datetime format
        self.birthday_datetime_this_year = datetime(year=self.current_date.year,month=self.birthday_datetime.month,\
        day=self.birthday_datetime.day).date() #amend year of birt to curent year
        self.birthday_datetime_next_year = datetime(year=self.current_date.year+1,month=self.birthday_datetime.month,\
        day=self.birthday_datetime.day).date() #amend year of birt to next year
        self.time_delta = self.birthday_datetime_this_year - self.current_date
        if int(self.time_delta.days) > 0: #if bitrhday will be in current year
            return self.time_delta.days
        else: #if user had a birhday this year
            return (self.birthday_datetime_next_year - self.current_date).days


class Field:
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        print('F setter')
        self.__value = new_value


class Name(Field): # class of username
    def __init__(self, name):
        self.name = name

    
class Phone(Field): #class of user`s phone
    def __init__(self, phone):
        self.__value = phone

    @property
    def value(self):
        return self.__value

    @value.setter #validate the phone number 
    def value(self, new_phone):
        if len(new_phone)==12 and new_phone.isnumeric():
            self.__value = new_phone
        else:
            print(f'Please enter the valid phone number')
    

class Birthday(Field):
    def __init__(self, birthday):
        self.__value = birthday

    @property
    def value(self):
        return self.__value

    @value.setter #validate the birthday date with dd.mm.yyyy format
    def value(self, new_birthday):
        import re
        if re.match(r'\d\d.\d\d.\d{4}', new_birthday) and len(new_birthday) == 10:
            self.__value = new_birthday
        else:
            print(f'Please enter the birthday date in dd.mm.yyyy format')

# for testing purposes
user = Record('Nick')
user.birthday = Birthday('22.03.2000')
user.birthday.value = '245.12.2000'
print(user.birthday.value)
user.phone = Phone('380969891936')
user.phone.value = '3809698919363'
print(user.phone.value)
print(user.days_to_birthday('22.03.2000'))
