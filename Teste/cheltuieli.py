from Domeniu.cheltuieli import *
from Service.Cheltuieli.cheltuiala import *


def test_domain_cheltuieli():
    """ Merge, e bun """
    vec = [15, 245, 'mancare']
    assert get_zi(vec) == 15
    assert get_suma(vec) == 245
    assert get_tip(vec) == 'mancare'

    set_zi(vec, 17)
    set_suma(vec, 999)
    set_tip(vec, 'telefon')

    assert get_zi(vec) == 17
    assert get_suma(vec) == 999
    assert get_tip(vec) == 'telefon'


def test_service_cheltuieli():
    vec = []
    vec.append([17, 245, 'mancare'])
    vec.append([27, 555, 'telefon'])
    vec.append([31, 555, 'imbracaminte'])

    assert actualizare_cheltuiala(vec, 27, 555, 'telefon', 1, 111, 'altele') == [
        [17, 245, 'mancare'],
        [1, 111, 'altele'],
        [31, 555, 'imbracaminte']
    ]
    assert cautare_cheltuiala(vec, 31, 555, 'imbracaminte') == 1
    assert tipareste_cheltuieli_suma(vec, 444) == [
        [31, 555, 'imbracaminte']
    ]
    assert tipareste_cheltuieli_tip(vec, 'altele') == [[1, 111, 'altele']]
    assert filtrare_cheltuieli_tip(vec, 'altele') == [[17, 245, 'mancare'], [31, 555, 'imbracaminte']]
    assert filtrare_cheltuieli_suma(vec, 245) == [
        [17, 245, 'mancare'],
        [31, 555, 'imbracaminte']
    ]
    vec.append([5, 889, 'altele'])
    assert tipareste_suma_totala_tip(vec, 'altele') == 1000

    assert gaseste_suma_max_zi(vec) == [5, 889]

    assert tipareste_cheltuieli_suma_fix(vec, 111) == [[1, 111, 'altele']]
    assert tipareste_cheltuieli_sortate_tip(vec) == [
        [1, 111, 'altele'],
        [5, 889, 'altele'],
        [31, 555, 'imbracaminte'],
        [17, 245, 'mancare']
    ]
    assert sterge_toate_cheltuielile_zi(vec, 1) == [
        [17, 245, 'mancare'],
        [31, 555, 'imbracaminte'],
        [5, 889, 'altele']
    ]
    assert sterge_toate_cheltuielile_interval_timp(vec, 1, 15) == [
        [17, 245, 'mancare'],
        [31, 555, 'imbracaminte']
    ]
    assert sterge_toate_cheltuielile_tip(vec, 'altele') == [
        [17, 245, 'mancare'],
        [31, 555, 'imbracaminte']
    ]


def test_service_undo_cheltuieli():
    vec = []
    undo_vec = vec[:]
    vec.append([17, 245, 'mancare'])
    add_undo(undo_vec, vec[:])
    assert undo_vec == [[[17, 245, 'mancare']]]
    vec.append([25, 555, 'altele'])
    add_undo(undo_vec, vec[:])
    assert undo_vec == [[[17, 245, 'mancare']], [[17, 245, 'mancare'], [25, 555, 'altele']]]
    undo(undo_vec)
    assert undo_vec == [[[17, 245, 'mancare']]]
    undo(undo_vec)
    assert undo_vec == []
    """ Trebuie sa fac un artificiu sa-l repar aici, nu stiu ce bug are darr aia e"""
    add_undo(undo_vec, vec[:])
    assert undo_vec == [[[17, 245, 'mancare'], [25, 555, 'altele']]]
    undo(undo_vec)
    assert undo_vec == []
    undo(undo_vec)


test_domain_cheltuieli()
test_service_cheltuieli()
test_service_undo_cheltuieli()
