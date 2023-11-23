# num = '380998764532'
# phone = (num.strip()
#             .replace('(', '')
#             .replace(')', '')
#             .replace('-', '')
#             .replace(' ', '')
#             .removeprefix('+')
#             )
# if len(phone) == 10:
#     print(phone)
# elif len(phone) == 12:
#     print(phone.lstrip('38'))
# else:
#     print('Not a phone')
# phones = ['08746378', '564783920', '657849302', '0507374198']
# def edit_phone(phone, new_phone):
#     index_phone = phones.index(phone)
#     print(index_phone)
#     phones[index_phone] = new_phone
#     print(phones)
#     return phones
# print(edit_phone('0507374198', '7658439202345678'))


new = {'liza': '87654', 'gdhjk':'9876543'}
liza = 'liza'
print(new.get('liza'))
print(new.get(liza))
print(new.get('rytuyiuij'))
search_name = 'stepan'
# for name, phone in new.items():
#     if name == search_name:
#         print(name, phone) 
phones = ['98765', '987654', '09876543']
phone = '98765'   
for el in phones:
    if el.value == phone:
        phones.remove(phone)
print(phones)
print(el.value())
