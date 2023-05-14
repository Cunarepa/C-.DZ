def arithmetic_progress_el(first_el: int, step: int, amount_el: int) -> list:
    return [first_el + (idx - 1) * step for idx in range(1, amount_el + 1)]
n1, d, n = map(int, input("Введите через пробел значения прогрессии\n<первый элемент> <шаг> <количество "
                          "элементов>\n>>> ").split())
print(arithmetic_progress_el(n1, d, n))