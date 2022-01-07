from unittest import TestCase

from Node import *
from Ex3Files.PQ import *
from test_Node import *


class TestPQ(TestCase):
    def test_add(self):
        pq: PQ = PQ()
        self.assertEqual(pq.Q.__len__(), 0)
        n0.set_node_weight(1242145)
        n1.set_node_weight(442142)
        n2.set_node_weight(55)
        n3.set_node_weight(2234235)
        n4.set_node_weight(165654)
        n5.set_node_weight(4545664)
        pq.add(n0)
        self.assertEqual(pq.Q.__len__(), 1)
        pq.add(n1)
        self.assertEqual(pq.Q.__len__(), 2)
        pq.add(n2)
        self.assertEqual(pq.Q.__len__(), 3)
        pq.add(n3)
        self.assertEqual(pq.Q.__len__(), 4)
        pq.add(n4)
        self.assertEqual(pq.Q.__len__(), 5)
        pq.add(n5)
        self.assertEqual(pq.Q.__len__(), 6)

    def test_pop(self):
        pq: PQ = PQ()
        n0.set_node_weight(0)
        n1.set_node_weight(1)
        n2.set_node_weight(2)
        n3.set_node_weight(3)
        n4.set_node_weight(4)
        n5.set_node_weight(4)
        pq.add(n0)
        pq.add(n1)
        pq.add(n2)
        pq.add(n3)
        pq.add(n4)
        pq.add(n5)
        self.assertEqual(pq.get_w(0), 0)
        self.assertEqual(pq.get_id(0), 0)
        self.assertEqual(pq.get_w(1), 1)
        self.assertEqual(pq.get_id(1), 1)
        self.assertEqual(pq.get_w(2), 2)
        self.assertEqual(pq.get_id(2), 2)
        self.assertEqual(pq.get_w(3), 3)
        self.assertEqual(pq.get_id(3), 3)
        self.assertEqual(pq.get_w(4), 4)
        self.assertEqual(pq.get_id(4), 4)
        self.assertEqual(pq.get_w(5), 4)
        self.assertEqual(pq.get_id(5), 5)
        n5.set_node_weight(-1)

        # print(pq)
        # print("Q[0]="+f"{pq.Q[0]}")
        # print("Q.pop="+f"{pq.pop()}")
