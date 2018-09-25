def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot ] # Подмасив меньших чисел
        great = [i for i in arr[1:] if i > pivot ] # Подмасив больших чисел
        return quicksort(less) + [pivot] + quicksort(great)
