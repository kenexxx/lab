# 1. Фільтрація списків за кількістю елементів
def filter_lists_by_count(*lists, k, n):
    """
    Фільтрує списки, де елемент k зустрічається рівно n разів.
    """
    return [lst for lst in lists if lst.count(k) == n]

test_list_1 = [(4, 5, 5, 4), (5, 4, 3)]
filtered_result = filter_lists_by_count(*test_list_1, k=5, n=2)
print("Фільтрація списків за кількістю елементів:", filtered_result)


# 2. Сортування двомірного масиву за стовпцем
def sort_by_column(array, k):
    """
    Сортує двомірний масив за стовпцем k.
    """
    return sorted(array, key=lambda x: x[k])

array_2 = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
sorted_result = sort_by_column(array_2, 1)
print("Сортування за стовпцем:", sorted_result)


# 3. Генерація попарних комбінацій
from itertools import permutations

def generate_combinations(list1, list2):
    """
    Генерує всі можливі попарні комбінації елементів двох списків без повторень.
    """
    return [list(zip(list1, p)) for p in permutations(list2)]

comb_result = generate_combinations(["a", "b"], [1, 2])
print("Генерація попарних комбінацій:", comb_result)


# 4. Унікальні значення словника
def sort_unique_values(dictionary):
    """
    Повертає відсортований список унікальних значень словника.
    """
    unique_values = set()
    for values in dictionary.values():
        unique_values.update(values)
    return sorted(unique_values)

test_dict_4 = {'gfg': [5, 6, 7, 8], 'best': [6, 12, 10, 8]}
unique_sorted = sort_unique_values(test_dict_4)
print("Унікальні значення словника:", unique_sorted)


# 5. Значення зі словника, якщо ключ у списку
def get_value_if_key_in_list(input_list, input_dict, k):
    """
    Повертає значення зі словника за ключем, якщо ключ є в списку.
    """
    return input_dict[k] if k in input_list else None

test_list_5 = ["Gfg", "is", "Good"]
test_dict_5 = {"Gfg": 5, "Best": 6}
value_if_key = get_value_if_key_in_list(test_list_5, test_dict_5, "Gfg")
print("Значення зі словника:", value_if_key)


# 6. Фільтрація словника за значенням
def filter_dict_by_value(input_dict, k):
    """
    Видаляє пари "ключ-значення", де значення більше за k.
    """
    return {key: value for key, value in input_dict.items() if not isinstance(value, (int, float)) or value <= k}

test_dict_6 = {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'}
filtered_dict = filter_dict_by_value(test_dict_6, 7)
print("Фільтрація словника за значенням:", filtered_dict)