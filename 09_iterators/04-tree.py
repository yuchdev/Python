__doc__ = """Generators shine if you have to work with complicated state
Let's implement tree iterator

Advantage of generator approach over for_each or other callback approach:
- it is lazy 
- we can easily make break
- it is more readable

"""


class BinaryTreeIterator:
    """
    Binary Tree Iterator
    """

    def __init__(self, tree):
        """
        Constructor
        """
        self.tree = tree
        self.stack = []

    def __iter__(self):
        """
        Iterator
        """
        return self

    def __next__(self):
        """
        Next method
        """
        if self.tree is None and len(self.stack) == 0:
            raise StopIteration
        while self.tree is not None:
            self.stack.append(self.tree)
            self.tree = self.tree.left
        self.tree = self.stack.pop()
        result = self.tree.value
        self.tree = self.tree.right
        return result


class BinaryTree:
    """
    Binary Tree
    """

    def __init__(self, value, left=None, right=None):
        """
        Constructor
        """
        self.value = value
        self.left = left
        self.right = right

    def __iter__(self):
        """
        Iterator
        """
        return BinaryTreeIterator(self)

    @property
    def pre_order(self):
        """
        Iterate tree in pre-order
        :return: generator
        """
        yield self.value
        if self.left:
            yield from self.left.pre_order
        if self.right:
            yield from self.right.pre_order

    @property
    def post_order(self):
        """
        Iterate tree in post-order
        :return: generator
        """
        if self.left:
            yield from self.left.post_order
        if self.right:
            yield from self.right.post_order
        yield self.value

    def for_each(self, callback):
        """
        Call callback for each node
        We show different iteration approach than generator
        Advantage of generator approach:
        - it is lazy
        - we can easily make break
        - it is more readable
        :param callback: callable
        """
        callback(self.value)
        if self.left:
            self.left.for_each(callback)
        if self.right:
            self.right.for_each(callback)
