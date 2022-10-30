from Domeniu.cheltuieli import *


def actualizare_cheltuiala(vector: list, zi: int, suma: int, optiune: str, new_zi: int, new_suma: int,
                           new_optiune: str):
    """
    - Modifica o cheltuiala
    :param vector: vectorul de cheltuieli
    :param zi: O variabila de tip int care reprezinta ziua cand s-a efectuat cheltuiala
    :param suma: O variabila de tip int care reprezinta suma cheltuielii
    :param optiune: O varibila de tip string care reprezinta pe ce s-a cheltuit suma de bani
    :param new_zi: O variabila de tip int care reprezinta noua zi
    :param new_suma: O variabila de tip int care reprezinta noua suma
    :param new_optiune: O variabila de tip string care reprezinta noua optiune
    :return: Lista modificata
    """
    for iterator in vector:
        if get_zi(iterator) == zi and get_suma(iterator) == suma and get_tip(iterator) == optiune:
            try:
                validare_zi_suma_optiune(new_zi, new_suma, new_optiune)
                set_zi(iterator, new_zi)
                set_suma(iterator, new_suma)
                set_tip(iterator, new_optiune)
            except ValueError as e:
                print(e)

    return vector


def cautare_cheltuiala(vector: list, zi, suma, optiune):
    """ Cauta daca o cheltuiala se afla in lista """
    for iterator in vector:
        if get_zi(iterator) == zi and get_suma(iterator) == suma and get_tip(iterator) == optiune:
            return 1
    return 0


def tipareste_cheltuieli_suma(vector: list, suma: int):
    """ Calculeaza si afiseaza cheltuielile in care suma este mai mare decat o variabila citita de la tastatura """
    new_list = []
    for iterator in vector:
        if get_suma(iterator) > suma:
            new_list.append(iterator)
    return new_list


def tipareste_cheltuieli_mai_mici_decat_o_zi_si_suma(vector: list, zi: int, suma: int):
    """ Calculeaza si afiseaza cheltuielile in care ziua este mai mica decat o variabila citita de la tastatura
    dar si suma este mai mica decat o variabila citita de la tastatura """
    new_list = []
    for iterator in vector:
        if get_zi(iterator) < zi and get_suma(iterator) < suma:
            new_list.append(iterator)

    return new_list


def tipareste_cheltuieli_tip(vector: list, tip: str):
    """ Calculeaza si afiseaza cheltuielile in care tipul este la fel ca o variabila citita de la tastatura """
    new_list = []
    for iterator in vector:
        if get_tip(iterator) == tip:
            new_list.append(iterator)

    return new_list


def filtrare_cheltuieli_tip(vector: list, tip: str):
    """
    - Afiseaza cheltuielile care nu sunt de tipul tip
    :param vector: vectorul cu elemente ( cheltuieli )
    :param tip: tipul de cheltuiala care se elimina
    :return: None
    """
    new_list = []
    for iterator in vector:
        if not get_tip(iterator) == tip:
            new_list.append(iterator)

    return new_list


def filtrare_cheltuieli_suma(vector: list, suma: int):
    """
    - Afiseaza cheltuielile care au suma mai mare sau egala cu o suma care se da
    :param vector: vectorul cu cheltuieli
    :param suma: suma care se cere
    :return: None
    """
    new_list = []
    for iterator in vector:
        if not get_suma(iterator) < suma:
            new_list.append(iterator)

    return new_list


def tipareste_suma_totala_tip(vector: list, tip: str):
    """ Calculeaza si afiseaza suma totala la un tip citit de la tastatura """
    suma = 0
    for iterator in vector:
        if get_tip(iterator) == tip:
            suma += get_suma(iterator)

    return suma


def gaseste_suma_max_zi(vector: list):
    """ Calculeaza si afiseaza in ce zi s-au cheltuit mai multi bani """
    max = 0
    zi = ''
    dictionar = {}
    for iterator in vector:
        if str(get_zi(iterator)) in dictionar:
            dictionar[str(get_zi(iterator))] += get_suma(iterator)
        else:
            dictionar[str(get_zi(iterator))] = get_suma(iterator)

        for values in dictionar.keys():
            if dictionar[values] > max:
                max = dictionar[values]
                zi = get_zi(iterator)
    return [zi, max]


def tipareste_cheltuieli_suma_fix(vector: list, suma: int):
    """ Calculeaza si afiseaza cheltuielile in care suma este egala cu o variabila citita de la tastatura """
    new_list = []
    for iterator in vector:
        if get_suma(iterator) == suma:
            new_list.append(iterator)

    return new_list


def tipareste_cheltuieli_sortate_tip(vector: list):
    """ Calculeaza si afiseaza elementele in ordine crescatoare dupa tip """
    optiuni = ['mancare', 'intretinere', 'imbracaminte', 'telefon', 'altele']
    optiuni.sort()
    new_list = []
    for opt in optiuni:
        for iterator in vector:
            if opt == get_tip(iterator):
                new_list.append(iterator)

    return new_list


def sterge_toate_cheltuielile_zi(vector: list, zi: int):
    """
    - Sterge toate cheltuielile pentru o zi data
    :param vector: Vectorul care contine cheltuielile
    :param zi: Variabila de tip int care reprezinta ziua care se sterge
    :return:
    """
    lista_noua = []
    for iterator in vector:
        if not get_zi(iterator) == zi:
            lista_noua.append(iterator)

    return lista_noua


def sterge_toate_cheltuielile_interval_timp(vector: list, inceput: int, sfarsit: int):
    """
    - Sterge toate cheltuielile care se afla intr-un interval dat
    :param vector: vactorul cu cheltuielile
    :param inceput: ziua de unde sa inceapa sa stearga
    :param sfarsit: ziua unde sa se opreasca de sters
    :return: vectorul care rezulta in urma operatiilor
    """
    lista_noua = []
    for iterator in vector:
        if not inceput <= get_zi(iterator) <= sfarsit:
            lista_noua.append(iterator)

    return lista_noua


def sterge_toate_cheltuielile_tip(vector: list, optiune: str):
    """
    - Sterge toate cheltuielile de un anumit tip
    :param vector: vectorul cu cheltuieli
    :param optiune: reprezinta tip cheltuiala care trebuie stearsa
    :return: vectorul care rezulta in urma operatiilor
    """
    lista_noua = []
    for iterator in vector:
        if not get_tip(iterator) == optiune:
            lista_noua.append(iterator)

    return lista_noua


def validare_zi(zi: int):
    """ Verifica daca ziua se afla in intervalul 1-31 """
    vec_errors = []
    if zi < 1 or zi > 31:
        vec_errors.append("Ziua nu se afla in intervalul 1-31")
    if vec_errors:
        raise ValueError(vec_errors)


def validare_suma(suma: int):
    """ Verifica daca suma este pozitiva """
    vec_errors = []
    if suma < 0:
        vec_errors.append("Suma nu poate fi negativa.")
    if vec_errors:
        raise ValueError(vec_errors)


def validare_tip(optiune: str):
    """ Verifica daca optiunea se afla in optiunile cerute """
    vec_errors = []
    optiuni = ['mancare', 'intretinere', 'imbracaminte', 'telefon', 'altele']
    if optiune not in optiuni:
        vec_errors.append(f"Optiunea nu este bine aleasa, incercati din {optiuni}.")
    if vec_errors:
        raise ValueError(vec_errors)


def validare_zi_suma_optiune(zi: int, suma: int, optiune: str):
    """
    - Verifica daca datele introduse sunt corecte
    :param zi: O variabila de tip int
    :param suma: O variabila de tip int
    :param optiune: O variabila de tip string
    :return: Daca datele sunt corect introduse nu da raise la ValueError daca exista probleme da raise la ValueError
    """
    vec_errors = []

    if zi < 1 or zi > 31:
        vec_errors.append("Ziua nu se afla in intervalul 1-31")

    if suma < 0:
        vec_errors.append("Suma nu poate fi negativa.")

    optiuni = ['mancare', 'intretinere', 'imbracaminte', 'telefon', 'altele']
    if optiune not in optiuni:
        vec_errors.append(f"Optiunea nu este bine aleasa, incercati din {optiuni}.")

    if vec_errors:
        raise ValueError(vec_errors)


def add_undo(undo_vec: list, vector: list):
    """ Adauga vectorul nostru in vectorul undo. """
    undo_vec.append(vector)
    return undo_vec


def undo(undo_vec: list):
    """ Doar ii face pop la vectorul undo pentru a da un pas in spate. """
    try:
        undo_vec.pop()
    except IndexError as e:
        print(e)
