from unittest import TestCase

from Classes.Agent import Agent


class TestAgent(TestCase):

    def test_path(self):
        a=Agent()
        a.path.append(2)
        a.path.append(3)
        a.path.append(4)

