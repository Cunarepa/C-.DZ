import os

from database import create_record, filter_records_surname, export_in_file, read_file, change_records, delete_records
from view import file_path, menu_buttons, view_notion, show_list_tuple_dict, show_list_dict, create_new_file, \
    user_request


def menu(data_phonebook):
    while True:
        user_input = menu_buttons()

        if user_input == "o":
            if len(data_phonebook) == 0:
                view_notion("данные не найдены", "x", "x")
            else:
                show_list_dict(data_phonebook)
        if user_input == "н":
            if len(data_phonebook) != 0:
                create_record(data_phonebook)
                view_notion("новая запись", separator_end="—")
            else:
                view_notion("ошибка импорта", "x", "x")
        if user_input == "ф":
            surname_filter = filter_records_surname(data_phonebook)
            if len(surname_filter) != 0:
                view_notion("результат поиска", "—", "—")
                show_list_tuple_dict(surname_filter)

            else:
                view_notion("пустой справочник")
        if user_input == "э":
            if len(data_phonebook) != 0:
                export_file_path = file_path()
                if path_check(export_file_path):
                    export_in_file(export_file_path, data_phonebook)
                    view_notion("экспорт", "-", "-")
                else:
                    choice = create_new_file(export_file_path)
                    if choice == "Д":
                        export_in_file(export_file_path, data_phonebook)
                        view_notion("экспорт", "-", "-")
            else:
                view_notion("ошибка экспорта", "-", "-")
        if user_input == "и":
            import_file_path = file_path()
            if path_check(import_file_path):  
                data_phonebook = read_file(import_file_path)
                view_notion("импорт", "-", "-")
            else:
                view_notion("ошибка пути", "-", "-")
        if user_input == "в":
            view_notion("конец программы")
            break
        if user_input == "з":
            if len(data_phonebook) != 0:
                if user_request("вывод словаря").capitalize() == "Д":  
                    show_list_dict(data_phonebook)
                surname_filter = filter_records_surname(data_phonebook)  
                change_records(data_phonebook, surname_filter)
            else:
                view_notion("пустой справочник")
                view_notion("ошибка импорта")
        if user_input == "y":
            if len(data_phonebook) != 0: 
                if user_request("вывод словаря").capitalize() == "Д":  
                    show_list_dict(data_phonebook)  
                surname_filter = filter_records_surname(data_phonebook)
                delete_person = delete_records(data_phonebook, surname_filter)
                view_notion("удален"), show_list_tuple_dict(delete_person)
            else:
                view_notion("пустой справочник", "x")
                view_notion("ошибка импорта", separator_end="x")


def path_check(file_path: str) -> bool:
    if os.path.isfile(file_path):
        return True
    else:
        return False
