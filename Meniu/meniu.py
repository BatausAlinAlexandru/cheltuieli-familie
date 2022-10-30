from Service.Cheltuieli.cheltuiala import *
from Repo.Repository import *


def print_meniu():
    print("""
              ADAUGARE & MODIFICARE
    1. Agaugare cheltuiala.
    2. Afisare cheltuieli
    3. Actualizare cheltuiala

                    STERGERE
    4. Sterge toate cheltuielile pentru o zi data
    5. Șterge cheltuielile pentru un interval de timp
    6. Șterge toate cheltuielile de un anumit tip

                    CAUTARI
    7. Tipareste toate cheltuielile mai mari decat o suma data
    8. Tipareste toate cheltuielile efectuate inainte de o zi data si mai mici decat o suma
    9. Tipareste toate cheltuielile de un anumit tip

                    RAPOARTE
    10. Tipareste suma totala pentru un anumit tip de cheltuiala
    11. Gaseste ziua in care suma cheltuita e maxima
    12. Tipareste toate cheltuielile ce au o anumita suma
    13. Tipareste cheltuielile sortate dupa tip

                    FILTRARE
    14. Elimina toate cheltuielile de un anumit tip
    15. Elimina toate cheltuielile mai mici decat o suma data
    
                    UNDO
    16. Undo
    x. Iesire
    """)


# 1
def citire_cheltuieli(undo_vec: list, vector: list):  # Plus validări
    """
    - Citeste cheltuieli si le verifica daca sunt corecte, daca sunt le da append in vector
    :param vector: vectorul cu cheltuieli
    :return: vectorul
    """
    try:
        zi_var = int(input('Introduceti ziua: '))
        suma_var = int(input('Introduceti suma: '))
        print("optiuni: mancare, intretinere, imbracaminte, telefon, altele")
        optiune_var = input('Introduceti optiunea: ')

        validare_zi_suma_optiune(zi_var, suma_var, optiune_var)
        vector.append([zi_var, suma_var, optiune_var])
        add_undo(undo_vec, vector[:])
        save(vector)
        return vector
    except ValueError as e:
        print(e)


# 2
def print_cheltuieli(vector: list):
    """ Afiseaza elementele dintr-un vector """
    vector = read_file()
    for i in vector:
        print(f"In ziua de {get_zi(i)} s-a cheltuit suma de {get_suma(i)} pentru {get_tip(i)}.")


# 3
def actualizare_cheltuieli(undo_vec: list, vector: list):
    """ Actualizeaza elementele dintr-un vector """
    try:
        zi_var = int(input('Introduceti ziua pe care vreti s-o modificati: '))
        suma_var = int(input('Introduceti suma pe care vreti s-o modificati: '))
        print("optiuni: mancare, intretinere, imbracaminte, telefon, altele")
        optiune_var = input('Introduceti optiunea pe care vreti s-o modificati: ')
        validare_zi_suma_optiune(zi_var, suma_var, optiune_var)
        if cautare_cheltuiala(vector, zi_var, suma_var, optiune_var):
            noua_zi_var = int(input('Introduceti ziua cu care vreti sa modificati: '))
            noua_suma_var = int(input('Introduceti suma cu care vreti sa modificati: '))
            print("optiuni: mancare, intretinere, imbracaminte, telefon, altele")
            noua_optiune_var = input('Introduceti optiunea cu care vreti sa modificati: ')
            actualizare_cheltuiala(vector, zi_var, suma_var, optiune_var, noua_zi_var, noua_suma_var, noua_optiune_var)
            add_undo(undo_vec, vector[:])
            save(vector)
            return vector
        else:
            print("Nu s-a gasit cheltuiala")
    except ValueError as e:
        print(e)


# 4
def sterge_cheltuieli_zi_ui(undo_vec: list, vector: list):
    """ Sterge cheltuielile dupa o zi data """
    try:
        zi = int(input('Introduceti ziua pe care vreti s-o stergeti: '))
        validare_zi(zi)
        vec = sterge_toate_cheltuielile_zi(vector, zi)
        add_undo(undo_vec, vec[:])
        save(vec)
        return vec
    except ValueError as e:
        print(e)


# 5
def sterge_cheltuieli_interval_timp_ui(undo_vec: list, vector: list):
    """ Sterge cheltuielile care se incadreaza intr-un interval dat """
    try:
        inceput = int(input("Introduceti de unde sa inceapa: "))
        sfarsit = int(input("Introduceti unde sa se opreasca: "))
        validare_zi(inceput)
        validare_zi(sfarsit)
        vector = sterge_toate_cheltuielile_interval_timp(vector, inceput, sfarsit)
        add_undo(undo_vec, vector[:])
        save(vector)
        return vector
    except ValueError as e:
        print(e)


# 6
def sterge_cheltuieli_tip_ui(undo_vec: list, vector: list):
    """ Sterge cheltuielile care au acelasi tip """
    try:
        tip = input("Introduceti ce tip de cheltuieli vreti sa stergeti: ")
        validare_tip(tip)
        vector = sterge_toate_cheltuielile_tip(vector, tip)
        add_undo(undo_vec, vector[:])
        save(vector)
        return vector
    except ValueError as e:
        print(e)


# E ok pana aici \\\\
# 7
def tipareste_cheltuieli_suma_ui(vector: list):
    """ Afiseaza cheltuielile in care suma este egala cu o variabila citita """
    try:
        suma = int(input('Introduceti suma: '))
        validare_suma(suma)
        tipareste_cheltuieli_suma(vector, suma)
    except ValueError as e:
        print(e)


# 8
def tipareste_cheltuieli_mai_mici_decat_o_zi_si_suma_ui(vector: list):
    """ Afiseaza cheltuielile in care ziua este mai mica decat o variabila citita la fel si suma"""
    try:
        zi = int(input("Introduceti ziua: "))
        suma = int(input("Introduceti suma: "))
        validare_zi(zi)
        validare_suma(suma)
        tipareste_cheltuieli_mai_mici_decat_o_zi_si_suma(vector, zi, suma)
    except ValueError as e:
        print(e)


# 9
def tipareste_cheltuieli_tip_ui(vector: list):
    """ Afiseaza cheltuielile care au acelasi tip citit de la tastatura """
    try:
        tip = input('Introduceti ce tip de cheltuiala vreti sa afisati: ')
        validare_tip(tip)
        tipareste_cheltuieli_tip(vector, tip)
    except ValueError as e:
        print(e)


# e ok pana aici

# 10
def tipareste_suma_totala_tip_ui(vector: list):
    """ Afiseaza cati bani s-au cheltuit pentru un tip citit de la tastatura """
    try:
        tip = input("Introduceti tipul: ")
        validare_tip(tip)
        tipareste_suma_totala_tip(vector, tip)
    except ValueError as e:
        print(e)


# 11
def gaseste_suma_max_zi_ui(vector: list):
    """ Afiseaza cea mai mare suma care s-a cheltuit intr-o zi """
    gaseste_suma_max_zi(vector)


# 12
def tipareste_cheltuieli_suma_fix_ui(vector: list):
    """ Afiseaza cheltuielile in care suma este egala cu o variabila citita de la tastatura """
    try:
        suma = int(input("Introduceti suma: "))
        validare_suma(suma)
        tipareste_cheltuieli_suma_fix(vector, suma)

    except ValueError as e:
        print(e)


# 13
def tipareste_cheltuieli_sortate_tip_ui(vector: list):
    """ Afiseaza cheltuielile in ordinea aflabetica tipului """
    tipareste_cheltuieli_sortate_tip(vector)


# e ok pana aici

# 14
def filtrare_cheltuieli_tip_ui(undo_vec: list, vector: list):
    try:
        tip = input("Introduceti tipul: ")
        vector = filtrare_cheltuieli_tip(vector, tip)
        add_undo(undo_vec, vector[:])
        save(vector)
        return vector
    except ValueError as e:
        print(e)


# 15
def filtrare_cheltuieli_suma_ui(undo_vec: list, vector: list):
    try:
        suma = int(input("Introduceti suma: "))
        vector = filtrare_cheltuieli_suma(vector, suma)
        add_undo(undo_vec, vector[:])
        save(vector)
        return vector
    except ValueError as e:
        print(e)


# 16
def undo_vec_ui(undo_vector: list, vector: list):
    try:
        undo(undo_vector)
        vector = undo_vector[len(undo_vector) - 1][:]
        save(vector)
        return vector
    except IndexError as e:
        print("Nu mai poti face undo. ", e)
        return read_file()


def runUI():
    """
    - Meniul
    :return: None
    """

    vec = read_file()

    undo_vector = [vec[:]]
    while True:
        print_meniu()
        cmd = input('Introduceti comanda: ')

        if cmd == '1':
            vec = citire_cheltuieli(undo_vector, vec)
        elif cmd == '2':
            print_cheltuieli(vec)
        elif cmd == '3':
            vec = actualizare_cheltuieli(undo_vector, vec)
        elif cmd == '4':
            vec = sterge_cheltuieli_zi_ui(undo_vector, vec)
        elif cmd == '5':
            vec = sterge_cheltuieli_interval_timp_ui(undo_vector, vec)
        elif cmd == '6':
            vec = sterge_cheltuieli_tip_ui(undo_vector, vec)
        elif cmd == '7':
            tipareste_cheltuieli_suma_ui(vec)
        elif cmd == '8':
            tipareste_cheltuieli_mai_mici_decat_o_zi_si_suma_ui(vec)
        elif cmd == '9':
            tipareste_cheltuieli_tip_ui(vec)
        elif cmd == '10':
            tipareste_suma_totala_tip_ui(vec)
        elif cmd == '11':
            gaseste_suma_max_zi_ui(vec)
        elif cmd == '12':
            tipareste_cheltuieli_suma_fix_ui(vec)
        elif cmd == '13':
            tipareste_cheltuieli_sortate_tip_ui(vec)
        elif cmd == '14':
            vec = filtrare_cheltuieli_tip_ui(undo_vector, vec)
        elif cmd == '15':
            vec = filtrare_cheltuieli_suma_ui(undo_vector, vec)
        elif cmd == '16':
            # undo(undo_vector)
            # vec = undo_vector[len(undo_vector) - 1][:]
            # save(vec)
            vec = undo_vec_ui(undo_vector, vec)
            if not undo_vector:
                undo_vector.append(vec[:])
            print(vec)
            print(undo_vector)

        elif cmd == 'x':
            break
        else:
            print("Introduceti o comanda valida")


runUI()

'''
17 245 telefon
25 445 altele
31 2235 imbracaminte
12 221 intretinere
2 22 altele
1 552 mancare
17 245 telefon
25 445 altele
31 2235 imbracaminte
12 221 intretinere
2 22 altele
1 552 mancare
17 245 telefon
25 445 altele
31 2235 imbracaminte
12 221 intretinere
2 22 altele
1 552 mancare
17 245 telefon
25 445 altele
31 2235 imbracaminte
12 221 intretinere
2 22 altele
1 552 mancare
17 245 telefon
25 445 altele
31 2235 imbracaminte
12 221 intretinere
2 22 altele
1 552 mancare
17 245 telefon
25 445 altele
31 2235 imbracaminte
12 221 intretinere
2 22 altele
1 552 mancare
17 245 telefon
25 445 altele
31 2235 imbracaminte
12 221 intretinere
2 22 altele
1 552 mancare
17 245 telefon
25 445 altele
31 2235 imbracaminte
12 221 intretinere
2 22 altele
1 552 mancare
17 245 telefon
25 445 altele
31 2235 imbracaminte
12 221 intretinere
2 22 altele
1 552 mancare
17 245 telefon
25 445 altele
31 2235 imbracaminte
12 221 intretinere
2 22 altele
1 552 mancare
'''
