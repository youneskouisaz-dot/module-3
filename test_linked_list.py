from linked_list import LinkedList


def test_add_first():
    linked_list = LinkedList()

    linked_list.addFirst("B")
    linked_list.addFirst("A")

    assert linked_list.toList() == ["A", "B"]


def test_add_last():
    linked_list = LinkedList()

    linked_list.addLast("A")
    linked_list.addLast("B")

    assert linked_list.toList() == ["A", "B"]


def test_remove_first():
    linked_list = LinkedList()

    linked_list.addLast("A")
    linked_list.addLast("B")

    removed = linked_list.removeFirst()

    assert removed == "A"
    assert linked_list.toList() == ["B"]


def test_remove_last():
    linked_list = LinkedList()

    linked_list.addLast("A")
    linked_list.addLast("B")

    removed = linked_list.removeLast()

    assert removed == "B"
    assert linked_list.toList() == ["A"]


def test_peek_first():
    linked_list = LinkedList()

    linked_list.addLast("A")
    linked_list.addLast("B")

    assert linked_list.peekFirst() == "A"


def test_peek_last():
    linked_list = LinkedList()

    linked_list.addLast("A")
    linked_list.addLast("B")

    assert linked_list.peekLast() == "B"


def test_empty_list():
    linked_list = LinkedList()

    assert linked_list.removeFirst() is None
    assert linked_list.removeLast() is None
    assert linked_list.peekFirst() is None
    assert linked_list.peekLast() is None
