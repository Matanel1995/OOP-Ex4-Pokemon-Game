from unittest import TestCase

from Classes.Agent import *


class TestAgent(TestCase):

    # def test_default_agent(self):
    #     a_default = Agent()
    #     self.assertEqual(a_default.id, -1)
    #     self.assertEqual(a_default.value, -1)
    #     self.assertEqual(a_default.src, -1)
    #     self.assertEqual(a_default.dst, -1)
    #     self.assertEqual(a_default.speed, -1)
    #     self.assertEqual(a_default.x_pos, -1)
    #     self.assertEqual(a_default.y_pos, -1)
    #     self.assertEqual(a_default.z_pos, 0)

    def test_gen_agent(self):
        a_gen = gen_agent(1, 2, 3, 4, 5, 6, 7, 0)
        self.assertEqual(a_gen.id, 1)
        self.assertEqual(a_gen.value, 2)
        self.assertEqual(a_gen.src, 3)
        self.assertEqual(a_gen.dst, 4)
        self.assertEqual(a_gen.speed, 5)
        self.assertEqual(a_gen.x_pos, str(6))
        self.assertEqual(a_gen.y_pos, str(7))
        self.assertEqual(a_gen.z_pos, str(0))


