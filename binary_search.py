from arr_input import arr_input_num
import math

def binary_search(search_el, search_arr):
    lower = 0
    upper = len(search_arr)-1
    while lower<=upper:
        mid = (lower + upper)/2        
        if search_arr[int(mid)] == search_el:
            return mid
        elif search_arr[int(mid)] < search_el:
            lower = math.ceil(mid)
        elif search_arr[int(mid)] > search_el:
            upper = math.floor(mid) 
            
    return None
            

inputArr = arr_input_num()
sortedArr = sorted(inputArr)
print(f"The sorted list is {sortedArr}")
search = int(input("Enter the element to be searched: "))

print("Applying binary search...")
result = binary_search(search, sortedArr)

if result == None:
    print(f"The element {search} is not in the given list of elements")
else:
    print(f"The element {search} is at position {int(result+1)} and index {int(result)}")