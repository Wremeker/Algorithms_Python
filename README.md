# Разбор базовых алгоритмов и структур данных

Бинарый поиск
------------------------
![](https://github.com/Wremeker/Algorithms_Python/blob/master/images/binary_search.png)
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

Быстрая сортировка 
------------------------
```
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot ] # Подмасив меньших чисел
        great = [i for i in arr[1:] if i > pivot ] # Подмасив больших чисел
        return quicksort(less) + [pivot] + quicksort(great)
```
