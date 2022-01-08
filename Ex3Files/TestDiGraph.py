from unittest import TestCase

from Ex3Files.DiGraph import *


def init_g_empty_nodes():
    g_empty = DiGraph()
    g_empty.add_node(0, (0, 0, 0))
    g_empty.add_node(1, (1, 1, 0))
    g_empty.add_node(2, (2, 2, 0))
    g_empty.add_node(3, (3, 3, 0))
    return g_empty


def init_g_empty_edges():
    g_empty = init_g_empty_nodes()
    g_empty.add_edge(0, 1, 1)
    g_empty.add_edge(1, 0, 1)
    g_empty.add_edge(1, 2, 1)
    g_empty.add_edge(2, 1, 1)
    g_empty.add_edge(2, 3, 1)
    g_empty.add_edge(3, 2, 1)
    return g_empty


class TestDiGraph(TestCase):

    def test_add_node(self):
        g_empty = DiGraph()
        self.assertEqual(g_empty.v_size(), 0)
        self.assertTrue(g_empty.add_node(0, (0, 0, 0)))
        self.assertEqual(g_empty.v_size(), 1)
        self.assertEqual(g_empty.nodes.get(0).id, 0)
        self.assertEqual(g_empty.nodes.get(0).pos, (0, 0, 0))
        self.assertTrue(g_empty.add_node(1, (1, 1, 0)))
        self.assertTrue(g_empty.add_node(2, (2, 2, 0)))
        self.assertEqual(g_empty.v_size(), 3)
        self.assertTrue(g_empty.add_node(3, (3, 3, 0)))
        self.assertEqual(g_empty.nodes.get(1).id, 1)
        self.assertEqual(g_empty.nodes.get(1).pos, (1, 1, 0))
        self.assertEqual(g_empty.nodes.get(2).id, 2)
        self.assertEqual(g_empty.nodes.get(2).pos, (2, 2, 0))
        self.assertEqual(g_empty.nodes.get(3).id, 3)
        self.assertEqual(g_empty.nodes.get(3).pos, (3, 3, 0))
        self.assertEqual(g_empty.v_size(), 4)

    def test_add_edge(self):
        g_empty = init_g_empty_nodes()
        self.assertEqual(g_empty.e_size(), 0)
        self.assertFalse("0to1" in g_empty.edges)
        self.assertTrue(g_empty.add_edge(0, 1, 1))
        self.assertEqual(g_empty.e_size(), 1)
        self.assertTrue("0to1" in g_empty.edges)
        self.assertIsNone(g_empty.add_edge(0, 1, 1))
        self.assertTrue(g_empty.add_edge(1, 0, 1))
        self.assertTrue(g_empty.add_edge(1, 2, 1))
        self.assertTrue(g_empty.add_edge(2, 1, 1))
        self.assertTrue(g_empty.add_edge(2, 3, 1))
        self.assertTrue(g_empty.add_edge(3, 2, 1))
        self.assertEqual(g_empty.e_size(), 6)

    def test_remove_edge(self):
        g_empty = init_g_empty_edges()
        self.assertEqual(g_empty.v_size(), 4)
        self.assertEqual(g_empty.e_size(), 6)
        self.assertTrue(g_empty.remove_edge(0, 1))
        self.assertEqual(g_empty.e_size(), 5)

    def test_remove_node(self):
        g_empty = init_g_empty_edges()
        self.assertEqual(g_empty.v_size(), 4)
        self.assertEqual(g_empty.e_size(), 6)
        self.assertTrue(g_empty.remove_node(0))
        self.assertIsNone(g_empty.remove_node(0))
        self.assertEqual(g_empty.v_size(), 3)
        self.assertEqual(g_empty.e_size(), 4)
        self.assertTrue(g_empty.remove_node(2))
        self.assertIsNone(g_empty.remove_node(2))
        self.assertEqual(g_empty.v_size(), 2)
        self.assertEqual(g_empty.e_size(), 0)

    def test_get_all_v(self):
        g_empty = init_g_empty_edges()
        self.assertEqual(g_empty.v_size(), 4)
        self.assertEqual(g_empty.e_size(), 6)
        self.assertEqual(g_empty.get_all_v(), g_empty.nodes)

    def test_all_in_edges_of_node(self):
        g_empty = init_g_empty_edges()
        self.assertEqual(g_empty.v_size(), 4)
        self.assertEqual(g_empty.e_size(), 6)
        for key in g_empty.nodes.keys():
            self.assertEqual(g_empty.all_in_edges_of_node(key), g_empty.nodes.get(key).edges_in)

    def test_all_out_edges_of_node(self):
        g_empty = init_g_empty_edges()
        self.assertEqual(g_empty.v_size(), 4)
        self.assertEqual(g_empty.e_size(), 6)
        for key in g_empty.nodes.keys():
            self.assertEqual(g_empty.all_out_edges_of_node(key), g_empty.nodes.get(key).edges_out)

    def test_str(self):
        g_empty = init_g_empty_edges()
        self.assertEqual(g_empty.v_size(), 4)
        self.assertEqual(g_empty.e_size(), 6)
        # print(g_empty)
