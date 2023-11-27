from collections import UserDict
import string


class NameTooShortError(Exception):
    pass
    # print('Name is too short, need more than 3 symbols. Try again.')

class NameTooLongError(Exception):
    pass
    # print('Name is too long, need only 10 symbols. Try again.')
    
class PhoneError(Exception):
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
        # self.validation(value)
    # def validation(self, value):
    #     super().__init__(value)
    #     # self.value = value
        if len(value) != 10 or not value.isdigit():
            raise ValueError
        
        # elif len(value) == 10 and value.isdigit():
        #     return value
        # else:
        #     return PhoneError
                    
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
                return phone.value
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
    # def __init__(self):
    #     se
    def add_record(self, record:Record):
        self.data[record.name.value] = record
        # self.data.update(record)
        # return self.data
    
    def find(self, search_name):
        for name, phone  in self.data.items():
            if name == search_name:
                return phone
        # return self.data.get(name)
        return None
            
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            
    # def delete(self, name):
    #     return self.data.pop(name)
        

if __name__ == "__main__":

    book = AddressBook()

    john_record = Record("John")
    print(john_record)
    john_record.add_phone("1234567890")
    print(john_record)
    john_record.add_phone("5555555555")
    print(john_record)

    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")  #'tuple' object has no attribute 'edit_phone'

    print(john)  

    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    book.delete("Jane")



