import copy

def example_shallow_copy():
    old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]]
    new_list = copy.copy(old_list)

    print(old_list)
    print(new_list)

    print("\n-----------------------------------------------\n")

    old_list[1][0] = 555
    old_list[2][2] = 888

    print(old_list)
    print(new_list)

def example_deep_copy():
    old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]]
    new_list = copy.deepcopy(old_list)

    print(old_list)
    print(new_list)

    print("\n-----------------------------------------------\n")

    old_list[1][0] = 555
    old_list[2][2] = 888

    print(old_list)
    print(new_list)

if __name__ == "__main__":
    print(">>> Shallow copy example: ")
    example_shallow_copy()
    print("\n\n+++++++++++++++++++++++++++++++++++++++++++++++\n\n")
    print(">>> Deep copy example: ")
    example_deep_copy()