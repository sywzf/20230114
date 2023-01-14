from no_element import NoElement


class BST:
    """A binary search tree."""

    class Node:
        def __init__(self, key, n=1, left=None, right=None):
            self.key = key
            self.n = n
            self.left = left
            self.right = right

    def __init__(self):
        self._root = None

    @staticmethod
    def _size(x: Node):
        if x is None:
            return 0
        else:
            return x.n

    def size(self):
        return BST._size(self._root)

    def is_empty(self):
        return self.size() == 0

    def put(self, key):
        def _put(x: BST.Node):
            if x is None:
                return BST.Node(key)
            if key < x.key:
                x.left = _put(x.left)
            elif key > x.key:
                x.right = _put(x.right)
            x.n = BST._size(x.left) + BST._size(x.right) + 1
            return x
        if key is None:
            raise KeyError
        self._root = _put(self._root)

    def get(self, key):
        def _get(x: BST.Node):
            if x is None or key == x.key:
                return x
            if key < x.key:
                return _get(x.left)
            elif key > x.key:
                return _get(x.right)
        if key is None:
            raise KeyError
        return _get(self._root)

    def contains(self, key):
        return self.get(key) is not None

    @staticmethod
    def _remove_min(x: Node):
        # x is not none
        if x.left is None:
            return x.right
        x.left = BST._remove_min(x.left)
        x.n = BST._size(x.left) + BST._size(x.right) + 1
        return x

    def remove_min(self):
        if self.is_empty():
            raise NoElement
        self._root = BST._remove_min(self._root)

    def remove_max(self):
        def _remove_max(x: BST.Node):
            # x is not null
            if x.right is None:
                return x.left
            x.right = _remove_max(x.right)
            x.n = BST._size(x.left) + BST._size(x.right) + 1
            return x
        if self.is_empty():
            raise NoElement
        self._root = _remove_max(self._root)

    def remove(self, key):
        def _remove(x: BST.Node):
            if x is None:
                return None
            if key < x.key:
                x.left = _remove(x.left)
            elif key > x.key:
                x.right = _remove(x.right)
            else:
                if x.right is None:
                    return x.left
                if x.left is None:
                    return x.right
                t = x
                x = BST._min(t.right)
                x.right = BST._remove_min(t.right)
                x.left = t.left
            x.n = BST._size(x.left) + BST._size(x.right) + 1
            return x
        if key is None:
            raise KeyError
        self._root = _remove(self._root)

    @staticmethod
    def _min(x):
        # x is not None
        if x.left is None:
            return x
        else:
            return BST._min(x.left)

    def min(self):
        if self.is_empty():
            raise NoElement
        return BST._min(self._root).key

    def max(self):
        def _max(x: BST.Node):
            # x is not None
            if x.right is None:
                return x
            else:
                return _max(x.right)
        if self.is_empty():
            return NoElement
        return _max(self._root).key

    def height(self):
        def _height(x: BST.Node):
            if x is None:
                return -1
            else:
                return 1 + max(_height(x.left), _height(x.right))
        return _height(self._root)

    def is_bst(self):
        def _is_bst(node):
            if node == null :
                return True


            if node.left != null and node.key < node.left.key :
                return False


            if node.right != null and node.key > node.right.key:
                return False


            if _is_bst(node.left) == False or _is_bst(node.right) == False :
                return False


            return True
    
        return _is_bst(self._root)