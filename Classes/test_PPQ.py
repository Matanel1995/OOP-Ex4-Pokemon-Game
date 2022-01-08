from unittest import TestCase

from Classes.PPQ import *
from Classes.test_Pokemon import *
from Classes.test_Agent import *


def gen_poke_list(k: int):
    poke_list = list()
    for i in range(k):
        poke_list.append(gen_pokemon(i, i, i, i))
    return poke_list


def gen_poke_pq(k: int):
    poke_pq = PQByPokemon()
    for i in range(k):
        poke_pq.add(gen_pokemon(i, i, i, i))
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
        k: int = 15
        pq_peek = gen_poke_pq(k)
        for i in range(k):
            self.assertEqual(pq_peek.peek()[0], (-1) * (k - 1 - i))
            self.assertEqual(pq_peek.peek()[1], (k - 1 - i))
            temp_poke = gen_pokemon((k - 1 - i), (k - 1 - i), (k - 1 - i), (k - 1 - i))
            pq_peek.pop()

    # def test_peek_pokemon_val_pos_src_dst(self):
    #     k: int = 15
    #     pq_peek_pokemon = gen_poke_pq(k)
    #     for i in range(k):
    #         temp_poke = gen_pokemon((k - 1 - i), (k - 1 - i), (k - 1 - i), (k - 1 - i), 0)
    #         self.assertEqual(pq_peek_pokemon.peek_pokemon().__str__(), temp_poke.__str__())
    #         self.assertEqual(pq_peek_pokemon.peek_val(), temp_poke.value)
    #         self.assertEqual(pq_peek_pokemon.peek_pos(), temp_poke.pos)
    #         self.assertEqual(pq_peek_pokemon.peek_src(), temp_poke.src)
    #         self.assertEqual(pq_peek_pokemon.peek_dst(), temp_poke.dst)
    #         pq_peek_pokemon.pop()
