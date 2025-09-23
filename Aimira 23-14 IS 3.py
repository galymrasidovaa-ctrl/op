lst = [1, 2, 3, 4, 5]
reversed_lst = lst[::-1]
print(reversed_lst)  # Выведет: [5, 4, 3, 2, 1]

def list_sort(lst):
    return sorted(lst, key=abs, reverse=True)

# Пример использования:
numbers = [-10, 2, -30, 4, 5]
sorted_numbers = list_sort(numbers)
print(sorted_numbers)  # Выведет: [-30, -10, 5, 4, 2]

def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]

# Пример использования:
my_list = [1, 2, 3, 4]
change(my_list)
print(my_list)  # Выведет: [4, 2, 3, 1]
