# Функция сортировки пузырьком
def bubble_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Изменяем условие в зависимости от направления сортировки
            if (ascending and arr[j] > arr[j+1]) or (not ascending and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]  # меняем местами

# Запрашиваем у пользователя количество чисел
n = int(input("Введите количество чисел для сортировки: "))

# Запрашиваем у пользователя числа
numbers = []
for _ in range(n):
    number = float(input("Введите число: "))  # используем float для поддержки дробных чисел
    numbers.append(number)

# Запрашиваем направление сортировки
direction = input("Введите '1' для сортировки по возрастанию или '2' для сортировки по убыванию: ")

# Определяем направление сортировки
ascending = True if direction == '1' else False

# Сортируем числа
bubble_sort(numbers, ascending)

# Выводим отсортированный список
print("Отсортированные числа:", numbers)
