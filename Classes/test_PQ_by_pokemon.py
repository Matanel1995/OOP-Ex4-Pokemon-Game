from unittest import TestCase

from Classes.PQ_by_pokemon import PQByPokemon
from Classes.Pokemon import Pokemon


def gen_poke_list(k: int):
    poke_list = list()
    for i in range(k):
        poke_list.append(Pokemon(i, i, (i, i, 0)))
    return poke_list


def gen_poke_pq(k: int):
    poke_pq = PQByPokemon()
    for i in range(k):
        poke_pq.add(Pokemon(i, i, (i, i, 0)))
    return poke_pq


class TestPQByPokemon(TestCase):
    def test_add(self):
        poke_list = gen_poke_list(6)
        poke_pq = PQByPokemon()
        self.assertEqual(poke_pq.size(), 0)
        for i in range(6):
            poke_pq.add(poke_list.pop(0))
            self.assertEqual(poke_pq.size(), i + 1)

    def test_pop(self):
        poke_pq = gen_poke_pq(6)
        self.assertEqual(poke_pq.size(), 6)
        for i in range(6):
            self.assertEqual(poke_pq.size(), 6 - i)
            poke_pq.pop()

    def test_is_empty(self):
        poke_pq = PQByPokemon()
        self.assertTrue(poke_pq.is_empty())
        poke_pq = gen_poke_pq(1)
        self.assertFalse(poke_pq.is_empty())

    def test_peek(self):
        self.fail()

    def test_peek_val(self):
        self.fail()

    def test_peek_pos(self):
        self.fail()

    def test_peek_src(self):
        self.fail()

    def test_peek_dest(self):
        self.fail()
