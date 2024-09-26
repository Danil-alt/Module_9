def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results.update({func.__name__: func(int_list)})
    return results

int_list = [1, 2, 5, 3, 4, 5]

def square_list(int_list):
    return [x ** 2 for x in int_list]


def cube_list(int_list):
    return [x ** 3 for x in int_list]

def sum(int_list):
    result = 0
    for i in int_list:
        result += i
    return result

def max(int_list):
    i = 0
    for i in range(len(int_list)-1):
        if int_list[i] > int_list[i + 1]:
            result = int_list[i]
    return result



print(apply_all_func(int_list, max, sum))

