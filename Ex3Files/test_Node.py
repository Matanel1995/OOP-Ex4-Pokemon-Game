from unittest import TestCase

from Ex3Files.Node import *

n0 = Node(0, (0, 0, 0))
n1 = Node(1, (1, 1, 0))
n2 = Node(2, (2, 2, 0))
n3 = Node(3, (3, 3, 0))
n4 = Node(4, (4, 4, 0))
n5 = Node(5, (5, 5, 0))
node_list = (n0, n1, n2, n3, n4, n5)


class TestNode(TestCase):

    def test_id(self):
        i = 0
        for n in node_list:
            self.assertEqual(n.id, i)
            i += 1

    def test_pos(self):
        i = 0
        for n in node_list:
            self.assertEqual(n.pos, (i, i, 0))
            i += 1

    def test_add_incoming_edge(self):
        node = Node(0, (0, 0, 0))
        node.add_incoming_edge(1, 1)
        self.assertEqual(node.edges_in[1], 1)
        node.add_incoming_edge(2, 1)
        node.add_incoming_edge(3, 1)
        node.add_incoming_edge(4, 1)
        self.assertEqual(node.edges_in[2], 1)
        self.assertEqual(node.edges_in[3], 1)
        self.assertEqual(node.edges_in[4], 1)

    def test_add_outgoing_edge(self):
        node = Node(0, (0, 0, 0))
        node.add_outgoing_edge(2, 4)
        node.add_outgoing_edge(1, 1)
        node.add_outgoing_edge(3, 1)
        node.add_outgoing_edge(4, 1)
        self.assertTrue(2 in node.edges_out)
        self.assertEqual(node.edges_out[2], 4)
        self.assertTrue(1 in node.edges_out)
        self.assertTrue(3 in node.edges_out)
        self.assertTrue(4 in node.edges_out)

    def test_delete_incoming_edge(self):
        node = Node(0, (0, 0, 0))
        node.add_incoming_edge(1, 1)
        node.add_incoming_edge(2, 1)
        node.add_incoming_edge(3, 1)
        node.add_incoming_edge(4, 1)
        self.assertTrue(1 in node.edges_in)
        node.delete_incoming_edge(1)
        self.assertTrue(1 not in node.edges_in)
        self.assertTrue(2 in node.edges_in)
        node.delete_incoming_edge(2)
        self.assertTrue(2 not in node.edges_in)
        self.assertTrue(3 in node.edges_in)
        node.delete_incoming_edge(3)
        self.assertTrue(3 not in node.edges_in)
        self.assertTrue(4 in node.edges_in)
        node.delete_incoming_edge(4)
        self.assertTrue(4 not in node.edges_in)

    def test_delete_outgoing_edge(self):
        node = Node(0, (0, 0, 0))
        node.add_outgoing_edge(2, 4)
        node.add_outgoing_edge(1, 1)
        node.add_outgoing_edge(3, 1)
        node.add_outgoing_edge(4, 1)
        self.assertTrue(1 in node.edges_out)
        node.delete_outgoing_edge(1)
        self.assertTrue(1 not in node.edges_out)
        self.assertTrue(2 in node.edges_out)
        node.delete_outgoing_edge(2)
        self.assertTrue(2 not in node.edges_out)
        self.assertTrue(3 in node.edges_out)
        node.delete_outgoing_edge(3)
        self.assertTrue(3 not in node.edges_out)
        self.assertTrue(4 in node.edges_out)
        node.delete_outgoing_edge(4)
        self.assertTrue(4 not in node.edges_out)
