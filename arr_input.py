def arr_input_str():
    arr = []

    num = int(input("Enter the number of elements in the list: "))

    for i in range(0,num):
        element = input(f"Enter element number {i+1}: ")
        arr.append(element)

    print(f"The entered list is {arr}")
    
    return arr

def arr_input_num():
    arr = []

    num = int(input("Enter the number of elements in the list: "))

    for i in range(0,num):
        element = int(input(f"Enter element number {i+1}: "))
        arr.append(element)

    print(f"The entered list is {arr}")
    
    return arr