
# Функция для поиска наименьшего элемента в массива 
def findSmallElementInArray(arr):
    smallset = arr[0] # Храненение наименьшего значения
    smallset_index = 0 # Хранение наименьшего значения
    for i in range(1, len(arr)): # Проход по массиву
        if arr[i] < smallset: # Если очередной элемент массива меньше наименьшего  
            smallset = arr[i] 
            smallset_index = i
    return smallset_index

# Сортировка выбором 
def selectionSort(arr): 
    newArr = [] 
    for i in range(len(arr)):  # Проход по массиву
        smallset = findSmallElementInArray(arr) # Поиск наименьшего элемента
        newArr.append(arr.pop(smallset)) # Добавление в начало
    return newArr