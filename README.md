# Разбор базовых алгоритмов и структур данных

Бинарый поиск
------------------------
```
def binary_search(list, item):
    low = 0 # Нулевой элемент массива
    high = len(list) - 1 # Последний элемент массива

    while low <= high: 
        mid = round((low + high)/2) # Пока часть не сократится до одного элемента
        guess = list[mid] # Выборка индекса элемента в массиве
        if guess == item: # Если элемент найден вернуть его
            return mid
        if guess > item:  # Если много
            high = mid - 1
        else:           # Если мало
            low = mid + 1
    return None
```
Сортировка выбором 
------------------------
```
# Функция для поиска наименьшего элемента в массива 
def findSmallElementInArray(arr):
    smallset = arr[0] # Храненение наименьшего значения
    smallset_index = 0 # Хранение индекса наименьшего значения
    for i in range(1, len(arr)): # Проход по массиву
        if arr[i] < smallset: # Если очередной элемент массива меньше наименьшего  
            smallset = arr[i] 
            smallset_index = i
    return smallset_index

# Функция сортировки выбором 
def selectionSort(arr): 
    newArr = [] 
    for i in range(len(arr)):  # Проход по массиву
        smallset = findSmallElementInArray(arr) # Поиск наименьшего элемента
        newArr.append(arr.pop(smallset)) # Добавление в начало
    return newArr
```
