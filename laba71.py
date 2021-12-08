import random

def create(size,):
    matrix_keys = []
    for i in range(1, size[0] + 1):
        matrix_keys.append(i)
    matrix = dict.fromkeys(matrix_keys)

    for i in range(size[0]):
        matrix_list = []
        a = int(random.uniform(-34, 26))
        b = int(random.uniform(-34, 26))
        c = int(random.uniform(-34, 26))
        d = int(random.uniform(-34, 26))
        e = int(random.uniform(-34, 26))
        k = int(random.uniform(-34, 26))
        matrix_list.append(a)
        matrix_list.append(b)
        matrix_list.append(c)
        matrix_list.append(d)
        matrix_list.append(e)
        matrix_list.append(k)
        matrix[i + 1] = matrix_list
    return matrix

def print_t(matrix):
    for i in matrix:
        print(matrix[i])

def calc(matrix):
    count = []
    sum = 0
    for i in range(len(matrix)):
        list = matrix[i+1]
        for number in list:
            if number >= 0:
                count.append(number)
                index = list.index(number)
                list[index] = 0
                matrix.update({i + 1: list})
            else:
                pass
    for numbers in count:
        sum += numbers
    print(f'Сума всіх додатніх елементів в матриці: {sum}\nКількість додатніх елементів в матриці: {len(count)}')
    return matrix
def ordering_keys(matrix):
    for i in range(3):
        matrix[i+1] = matrix[i+1][::-1]
    return matrix
def sort(matrix):
    list1 = matrix[1]
    list2 = matrix[2]
    list3 = matrix[3]
    list1 = sorted(list1)
    list1 = list1[::-1]
    list2 = sorted(list2)
    list2 = list2[::-1]
    list3 = sorted(list3)
    list3 = list3[::-1]
    for number in list1:
        if list1.index(number) != 5:
            if number == list1[list1.index(number)+1]:
                if number in list2 and list2.count(number) >= 2:
                    list2[list1.index(number)] = list3[list1.index(number)]
                    list2[list1.index(number)+1] = list3[list1.index(number)]

                else:
                    pass
                if list1.index(number) != 5:
                    list1[(list1.index(number))+1] = list2[list1.index(number)+1]
                    list1[list1.index(number)] = list2[list1.index(number)]


            else:
                pass
    matrix[1] = list1
    matrix[2] = list2
    matrix[3] = list3
    return matrix

def main():
    matrix = create((8,6))
    print_t(matrix)
    print()
    calc(matrix)
    ordering_keys(matrix)
    print()
    sort(matrix)
    print_t(matrix)
main()