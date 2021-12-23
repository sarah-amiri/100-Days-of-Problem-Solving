"""
    This problem is available on Leetcode:
    https://leetcode.com/problems/palindrome-linked-list

    In this problem a single linked list is given and it must return True if
    the linked list is palindrome.
    I first use a stack, but then used this method:
    1. find the middle of the linked list
    2. reverse the second half
    3. compare two parts
    4. reverse again the second half
    Time:O(n), space: O(1)
"""
from typing import Optional


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class SingleLinkedList:
    def __init__(self, items=[]):
        self.head = None
        self.middle = None
        self.tail = None
        self.items = items
        self.__create_from_list(items)

    def __create_from_list(self, items: list) -> None:
        if not items:
            return
        self.head = Node(value=items[0])
        node = self.head
        for item in items[1:]:
            new_node = Node(value=item)
            node.next, node = new_node, new_node

    def __find_middle(self) -> None:
        n1, n2 = self.head, self.head
        while n2 and n2.next:
            n1, n2 = n1.next, n2.next.next
        self.middle = n1

    def __reverse(self, start: Optional[Node] = None) -> Node:
        if start is None:
            start = self.head

        node = start.next
        start.next = None
        while node:
            node_next = node.next
            node.next, start, node = start, node, node_next
        return start

    @classmethod
    def compare(cls, start1: Optional[Node], start2: Optional[Node]) -> bool:
        while start1 and start2 and start1 != start2:
            if start1.value != start2.value:
                return False
            start1, start2 = start1.next, start2.next
        return True

    def is_palindrome(self) -> bool:
        if not self.items:
            return True
        self.__find_middle()
        self.tail = self.__reverse(self.middle)
        start1, start2 = self.head, self.tail
        result = self.compare(start1, start2)
        self.__reverse(self.tail)
        return result

    def __str__(self) -> str:
        st = ''
        node = self.head
        while node:
            st += str(node.value)
            if node.next:
                st += ' -> '
            node = node.next
        return st


if __name__ == '__main__':
    # example 1
    print('Example 1')
    linked_list = SingleLinkedList([1, 2])
    print(linked_list.is_palindrome())
    print(linked_list)
    print()

    # example 2
    print('Example 2')
    linked_list = SingleLinkedList([1])
    print(linked_list.is_palindrome())
    print(linked_list)
    print()

    # example 3
    print('Example 3')
    linked_list = SingleLinkedList([])
    print(linked_list.is_palindrome())
    print(linked_list)
    print()

    # example 4
    print('Example 4')
    linked_list = SingleLinkedList([1, 2, 3, 4, 5])
    print(linked_list.is_palindrome())
    print(linked_list)
    print()

    # example 5
    print('Example 5')
    linked_list = SingleLinkedList([i for i in range(1, 101)] + [i for i in range(100, 0, -1)])
    print(linked_list.is_palindrome())
    print(linked_list)
    print()

    # example 6
    print('Example 6')
    linked_list = SingleLinkedList([i for i in range(1, 201)] * 2)
    print(linked_list.is_palindrome())
    print(linked_list)
    print()

    # example 7
    print('Example 7')
    linked_list = SingleLinkedList([1, 1, 2, 1])
    print(linked_list.is_palindrome())
    print(linked_list)
    print()
