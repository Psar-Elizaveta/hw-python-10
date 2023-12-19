from collections import UserDict
import string


class NameTooShortError(Exception):
    pass
class NameTooLongError(Exception):
    pass
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        # self.name = name
        super().__init__(name)
        if len(name) < 3:
            raise NameTooShortError('Name is too short, need more than 3 symbols. Try again.')
        if len(name) > 10:
            raise NameTooLongError('Name is too long, need only 10 symbols. Try again.')
        return name

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

        if len(value) != 10 or not value.isdigit():
            raise ValueError
                    
class Record:
    def __init__(self, name):
        self.name = Field(name)
        self.phones = []
        
    def __str__(self) -> str:
        return f'Contact name: {self.name.value}, phones: {";".join(str(p) for p in self.phones)}'

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        # phone.validation(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)
    
    
    def remove_phone(self, phone):
        for ph in self.phones:
            if isinstance(ph, Field) and ph.value == phone:
                self.phones.remove(ph)
            

    
    def find_phone(self, search_phone):
        for phone in self.phones:
            if isinstance(phone, Field) and phone.value == search_phone:
                return phone
        return None
    
    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p for p in self.phones)}"

        
    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if old_phone == phone.value:
                self.phones.remove(phone)
                self.phones.append(Phone(new_phone))
                return
        raise ValueError
class AddressBook(UserDict):
    
    def add_record(self, record:Record):
        self.data[record.name.value] = record
    
    def find(self, search_name):
        for name, phone  in self.data.items():
            if name == search_name:
                return phone
        # return self.data.get(name)
        return None
            
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]s
