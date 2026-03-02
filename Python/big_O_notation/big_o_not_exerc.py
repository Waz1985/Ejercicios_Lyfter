#Exercise #1
#Bubble sort is a O(n2) because it is an iteration inside another iteration, but I'm not pretty sure if will be a O(log n) 
# because of the iteration reduction we used in line 10 
def bubble_sort(list_to_order): #O(n2)
    list_len = len(list_to_order) -1 #O(1)

    for it_num in range(list_len): #O(n)
        swapped = False #O(n)

        for i in range(list_len - it_num): #O(log n) because each iteration it reduces the times it will execute 
            current = i #O(1)
            next = i + 1 #O(1)
            print(list_to_order[current], list_to_order[next]) #O(1)

            if list_to_order[current] > list_to_order[next]: #O(1)
                list_to_order[current], list_to_order[next] = list_to_order[next], list_to_order[current] #O(1)

                swapped = True #O(1)

            print(f"List: {list_to_order}")   #O(1)

        if not swapped: #O(1)
            break #O(1)

        print(f"iterations:{list_len - it_num}") #O(1)
    print(f"Ordered list: {list_to_order}") #O(1)


#Exercise #2
# Alg - 1 / print_numbers_times_2
def print_numbers_times_2(numbers_list): #O(n)
	for number in numbers_list: #O(n)
		print(number * 2) #O(1)
#R/  #O(n) algorithm


# Alg - 2 / check_if_lists_have_an_equal
def check_if_lists_have_an_equal(list_a, list_b): #O(n2)
	for element_a in list_a: #O(n2)
		for element_b in list_b: #O(n)
			if element_a == element_b: #O(1)
				return True #O(1)
				
	return False #O(1)
#R/  #O(n2) algorithm


# Alg - 3 / print_10_or_less_elements
def print_10_or_less_elements(list_to_print): #O(1)
	list_len = len(list_to_print) #O(1)
	for index in range(min(list_len, 10)): #O(1)
		print(list_to_print[index]) #O(1)
#R/  #O(1) algorithm


# Alg - 4 / generate_list_trios
def generate_list_trios(list_a, list_b, list_c): #O(n3)
	result_list = [] #O(1)
	for element_a in list_a: #O(n3)
		for element_b in list_b: #O(n2)
			for element_c in list_c: #O(n)
				result_list.append(f'{element_a} {element_b} {element_c}') #O(1)
				
	return result_list #O(1)
#R/  #O(n3) algorithm