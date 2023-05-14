# def arithmetic_progress_el(first_el: int, step: int, amount_el: int) -> list:
#     return [first_el + (idx - 1) * step for idx in range(1, amount_el + 1)]
# n1, d, n = map(int, input("Введите через пробел значения прогрессии\n<первый элемент> <шаг> <количество "
#                           "элементов>\n>>> ").split())
# print(arithmetic_progress_el(n1, d, n))




from random import randint
def find_index_range(list_, start, end):
    return [n for n in range(len(list_)) if start <= list_[n] <= end]
def find_in_list(list_, start, end):
    return [(n, list_[n]) for n in range(len(list_)) if start <= list_[n] <= end]
def find_in_list1(list_, start, end):
    return [(idx, el) for idx, el in enumerate(list_) if start <= el <= end]
lst1 = [randint(-20, 20) for el in range(20)]
start_el, end_el = map(int, input(f"Принятый список:\n"
                                  f"{lst1}\n"
                                  f"Введите диапазон чисел для поиска\n"
                                  f"<от> <до>\n").split())
print (f"Индексы чисел в диапазоне: \n{find_index_range(lst1, start_el, end_el)}\n")
   