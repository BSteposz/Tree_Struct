"""

    __5__
   /     \
  3       5__
 / \     /   \
2   5   1     0
             / \
            2   8
                 \
                  5
"""


class Node:
    """"""

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return f'{self.value},{self.left},{self.right}'

    def _get_children_subtree(self):
        """metoda pomocnicza zwracająca liste
        wartości poddrzewa (wartość root + wartość "dzieci")"""
        children = [self.value]
        if self.left:
            children.append(self.left.value)
        if self.right:
            children.append(self.right.value)
        return children

    def sum_in_subtree(self):
        """Zwraca sumę wartości poddrzewa na którym zostanie wywołana """
        return sum(self._get_children_subtree())

    def average_in_subtree(self):
        """Zwraca średnią wartość poddrzewa na którym zostanie wywołana """
        data = self._get_children_subtree()
        return sum(data) / len(data)

    @property
    def median_in_subtree(self):
        """Zwraca medianę poddrzewa na którym zostanie wywołana """
        data = self._get_children_subtree()
        if len(data) % 2 != 0:
            return sorted(data)[(len(data)//2)]
        else:
            return (sorted(data)[len(data)//2 - 1] + sorted(data)[len(data)//2]) / 2

    def _get_subchild(self, node):
        """Metoda pomocnicza do metody get_array_of_all_child(),
         rekurencyjnie znajduje najniższy poziom drzewa i zwraca jego wartość"""
        if not node:
            return 0
        left_sum = self._get_subchild(node.left)
        right_sum = self._get_subchild(node.right)
        self.data.append(node.value)
        return node.value

    def get_array_of_all_child(self, root):
        """ Metoda zwracająca listę wartości drzewa, od wskazanej gałęzi, aż do najniższej (końca)"""
        self.data = []
        self._get_subchild(root)
        return self.data

    def sum_in_all_subtree(self, root):
        """Metoda zwracają sumę wartości drzewa od wskazanego początku, do końca"""
        return sum(self.get_array_of_all_child(root))

    def average_in_all_subtree(self, root):
        """Metoda zwracają średnią wartość drzewa od wskazanego poddrzewa """
        data = self.get_array_of_all_child(root)
        return sum(data) / len(data)

    def median_in_all_subtree(self, root):
        """Metoda zwracają wartość mediany drzewa od wskazanego poddrzewa """
        data = self.get_array_of_all_child(root)
        if len(data) % 2 != 0:
            return sorted(data)[(len(data)//2)]
        else:
            return (sorted(data)[len(data)//2 - 1] + sorted(data)[len(data)//2]) / 2









