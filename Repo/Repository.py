from Domeniu.cheltuieli import *


def save(vector: list):
    with open('../Files/cheltuieli.txt', 'w') as file:
        for iterator in vector:
            file.write(f"{get_zi(iterator)} {get_suma(iterator)} {get_tip(iterator)}\n")


def read_file():
    return_vec = []
    with open('../Files/cheltuieli.txt', 'r') as file:
        if file.readable():
            vec = file.readlines()
            for iterator in vec:
                iterator = iterator.split(' ')
                iterator[0] = int(iterator[0])
                iterator[1] = int(iterator[1])
                iterator[2] = iterator[2][:len(iterator[2]) - 1]
                return_vec.append([get_zi(iterator), get_suma(iterator), get_tip(iterator)])
    return return_vec
