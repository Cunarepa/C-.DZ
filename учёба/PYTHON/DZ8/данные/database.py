from view import get_record, user_request, view_notion, show_list_tuple_dict

def create_record(data_phonebook: list):
    return data_phonebook.append(get_record())

def filter_records_surname(data_phonebook) -> list:
    surname_filter = user_request("запрос фамилии").capitalize()
    found_records = []
    for idx, person in enumerate(data_phonebook):
        if person.get("surname").startswith(surname_filter):
            found_records.append((idx, person))
    return found_records 

def change_records(data_phonebook, surname_filter):
    if len(surname_filter) == 1: 
        record_number = surname_filter[0][0]
        view_notion("введите данные")
        data_phonebook[record_number] = get_record()
    elif len(surname_filter) > 1: 
        show_list_tuple_dict(surname_filter)
        record_number = int(user_request("несколько совпадений")) - 1
        data_phonebook[record_number] = get_record()
    else:
        view_notion("человек не найден")

def delete_records(data_phonebook, surname_filter):
    if len(surname_filter) == 1: 
        data_phonebook.pop(surname_filter[0][0])
        return surname_filter
    elif len(surname_filter) > 1:
        show_list_tuple_dict(surname_filter)
        record_number = int(user_request("несколько совпадений")) - 1
        data_phonebook.pop(record_number)
        return data_phonebook[surname_filter]
    else:
        view_notion("человек не найден")

def export_in_file(export_file, data):
    with open(export_file, "w", encoding='utf-8') as file:
        for el in data: 
            file.write(f"{el['surname']},{el['name']},{el['phone']},{el['description']}\n")


def read_file(file_path: str) -> list:
    data = []
    with open(file_path, "r", encoding='utf-8') as file:
        for string in file:
            new_list = string.strip().split(",") 
            data.append({"surname": new_list[0], 'name': new_list[1], 'phone': new_list[2], 'description': new_list[3]})
    return data