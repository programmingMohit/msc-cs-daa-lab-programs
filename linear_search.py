from arr_input import arr_input_str

def linear_search(search_el, search_arr):
    for item in search_arr:
        if item == search_el:
            return search_arr.index(item)
            
    return None   

inputArr = arr_input_str()

search = input("Enter the element to be searched: ")

print("Applying linear search...")
result = linear_search(search, inputArr)

if result == None:
    print(f"The element {search} is not in the given list of elements")
else:
    print(f"The element {search} is at position {result+1} and index {result}")
    

    
     