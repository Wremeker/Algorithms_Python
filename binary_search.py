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
