from tree_struct import Node
import unittest


class TestTree(unittest.TestCase):
    """Klasa testująca struktórę drzewa z wariantu 1


                        __5__
                       /     \
                      3       7__
                     / \     /   \
                    2   5   1     0
                                 / \
                                2   8
                                     \
                                      5

    """
    def setUp(self):
        # wierzchołek drzewa (root)
        self.root = Node(5)
        # Poziom 1
        self.root.left = Node(3)
        self.root.right = Node(7)
        # poziom 2
        self.root.left.left = Node(2)
        self.root.left.right = Node(5)
        self.root.right.left = Node(1)
        self.root.right.right = Node(0)
        # poziom 3
        self.root.right.right.left = Node(2)
        self.root.right.right.right = Node(8)
        # poziom 4
        self.root.right.right.right.right = Node(5)

    def test_is_instance(self):
        self.assertIsInstance(self.root.left, Node)

    def test_sum_in_subtree(self):
        """test sumy wartosci we wskazanym poddrzewie

                        3                       7
                      /  \          &&        /  \
                     2    5                  1    0
        """
        self.assertEqual(self.root.left.sum_in_subtree(), sum([3, 2, 5]))
        self.assertEqual(self.root.right.sum_in_subtree(), sum([7, 1, 0]))


    def test_average_in_subtree(self):
        """test średniej wartosci we wskazanym poddrzewie

                        3                       7
                      /  \          &&        /  \
                     2    5                  1    0
        """
        self.assertAlmostEqual(self.root.left.average_in_subtree(), sum([3, 2, 5])/3)
        self.assertEqual(self.root.right.average_in_subtree(), sum([7, 1, 0])/3)

    def test_mediane_in_subtree(self):
        """test mediany we wskazanym poddrzewie

                        3                       7
                      /  \          &&        /  \
                     2    5                  1    0
        """
        self.assertEqual(self.root.left.median_in_subtree, 3)
        self.assertEqual(self.root.right.median_in_subtree, 1)

    def test_sum_in_all_subtree(self):
        """
        Test sumy wszystkich wartości zaczynając od poddrzewa o wartości 7
                              7__
                             /   \
                            1     0
                                 / \
                                2   8
                                     \
                                      5

        """
        self.assertEqual(self.root.sum_in_all_subtree(self.root.right), sum([7, 1, 0, 2, 8, 5]))

    def test_average_in_all_subtree(self):
        """
        Test mediany wartości zaczynając od poddrzewa o wartości 7
                              7__
                             /   \
                            1     0
                                 / \
                                2   8
                                     \
                                      5

        """
        self.assertEqual(self.root.average_in_all_subtree(self.root.right), sum([7, 1, 0, 2, 8, 5]) / 6)

    def test_median_in_all_subtree(self):
        """
        Test mediany wartości zaczynając od poddrzewa o wartości 7
                              7__
                             /   \
                            1     0
                                 / \
                                2   8
                                     \
                                      5

        """
        self.assertEqual(self.root.median_in_all_subtree(self.root.right), 3.5)

if __name__ == '__main__':
    unittest.main()