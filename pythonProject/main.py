# Функция сортировки пузырьком
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # меняем местами

# Запрашиваем у пользователя количество чисел
n = int(input("Введите количество чисел для сортировки: "))

# Запрашиваем у пользователя числа
numbers = []
for _ in range(n):
    number = float(input("Введите число: "))  # используем float для поддержки дробных чисел
    numbers.append(number)

# Сортируем числа
bubble_sort(numbers)

# Выводим отсортированный список
print("Отсортированные числа:", numbers)