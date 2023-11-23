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
    def __init__(self, value) -> None:
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

class Phone(Field):
    def validation(self, value):
        super().__init__(value)
        # self.value = value
        if len(value) != 10 and not value.isdigit():
            raise PhoneError('Not a number!')
        
        # elif len(value) == 10 and value.isdigit():
        #     return value
        # else:
        #     return PhoneError
                    
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def __str__(self) -> str:
        return f'Contact name: {self.name.value}, phones: {";".join(str(p) for p in self.phones)}'

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        phone.validation(phone_number)
        if phone not in self.phones:
            self.phones.append(phone_number)
    
    def remove_phone(self, phone):
        for ph in self.phones:
            if str(ph) == phone:
                self.phones.remove(phone)
                break
            
    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if old_phone == phone:
                index_phone = self.phones.index(old_phone)
                self.phones[index_phone] = new_phone
                break 

    
    def find_phone(self, search_phone):
        for phone in self.phones:
            if str(phone) == search_phone:
                return search_phone
        return 'Not such phone'

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


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
                return record
        return 'This name isn\'n here'
            
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print('This name isn\'t here')

if __name__ == "__main__":
# Створення нової адресної книги
    book = AddressBook()

        # Створення запису для John
    john_record = Record("John")
    print(john_record)
    john_record.add_phone("1234567890")
    print(john_record)
    john_record.add_phone("5555555555")
    print(john_record)

        # Додавання запису John до адресної книги
    book.add_record(john_record)

        # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

            # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

            # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")  #'tuple' object has no attribute 'edit_phone'

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

            # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

            # Видалення запису Jane
    book.delete("Jane")



