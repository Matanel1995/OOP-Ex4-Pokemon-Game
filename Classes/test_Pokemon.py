from unittest import TestCase

from Classes.Pokemon import *


class Test(TestCase):

    def test_default_pokemon(self):
        poke_default = Pokemon()
        self.assertEqual(poke_default.value, -1)
        self.assertEqual(poke_default.type_, 0)
        self.assertEqual(poke_default.x_pos, -1)
        self.assertEqual(poke_default.y_pos, -1)
        self.assertEqual(poke_default.z_pos, 0)

    def test_gen_pokemon(self):
        poke_gen = gen_pokemon(1, 2, 3, 4, 0)
        self.assertEqual(poke_gen.value, 1)
        self.assertEqual(poke_gen.type_, 2)
        self.assertEqual(poke_gen.x_pos, 3)
        self.assertEqual(poke_gen.y_pos, 4)
        self.assertEqual(poke_gen.z_pos, 0)
