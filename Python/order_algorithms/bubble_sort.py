import random
my_list = list(range(101))
random.shuffle(my_list)
print(my_list)
def bubble_sort(list_to_order):
    if not isinstance(list_to_order, list):
        raise TypeError("Parameter must be a list")

    list_len = len(list_to_order) -1

    for it_num in range(list_len):
        swapped = False

        for i in range(list_len - it_num):
            current = i
            next = i + 1

            if list_to_order[current] > list_to_order[next]:
                list_to_order[current], list_to_order[next] = list_to_order[next], list_to_order[current]

                swapped = True
            
        if not swapped:
            break

    return list_to_order


def inverted_bubble_sort(list_to_order):
    if not isinstance(list_to_order, list):
        raise TypeError("Parameter must be a list")
    list_len = len(list_to_order)

    for it_num in range(list_len):
        swapped = False

        for i in range(list_len -1, it_num, - 1):
            current = i
            next = i - 1
            
            if list_to_order[current] < list_to_order[next]:
                list_to_order[current], list_to_order[next] = (list_to_order[next], list_to_order[current])
                swapped = True
        
        if not swapped:
            break


print(f"return {bubble_sort(my_list)}")