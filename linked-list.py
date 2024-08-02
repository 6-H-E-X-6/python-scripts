class LinkedList:
    def __init__(self):
        self.Head = None

    class Node:
        def __init__(self, data):

            # The data contained by a node,
            # Whether it be an int, string,
            # or anything else
            self.Data = data

            # The node pointed to by this
            # instance of the node. If it
            # is None, then it denotes
            # the end of the linked list.
            self.Next = None

    class LinkedListIterator:
        def __init__(self, head):
            # This will be used to track
            # the current node being
            # iterated upon.
            self.current = head

        def __iter__(self):
            return self

        def __next__(self):
            if self.current is None:
                raise StopIteration
            else:
                # Set the data to be returned
                # to the current node, then
                # set the current node to the
                # next node in succession.
                item = self.current.Data
                self.current = self.current.Next
                return item

    def __iter__(self):
        return self.LinkedListIterator(self.Head)

    def generate(self, input):
        '''Generated a linked list
           given standard Python
           list comprehensions
           or arrays.'''

        # Do not generate a linked list if
        # this instance already has data.
        if self.Head:
            print("Linked list already exists.")
            return

        self.Head = self.Node(input[0])
        for i in input[1:]:
            self.insert_at_end(i)

    def instantiate(self, input):
        '''Like generate(), but can be
           used during object instantiation'''
        output_list = LinkedList()
        output_list.generate(input)
        return output_list

    def insert_at_beginning(self, data):
        '''Inserts a node containing data at
           the beginning of the linked list.'''

        new_node = self.Node(data)

        # If the linked list has no head,
        # this will become the head.
        if self.Head is None:
            self.Head = new_node
            return

        # Else, set the new node as the head
        # after pointing its next value to
        # the original head.
        else:
            new_node.Next = self.Head
            self.Head = new_node

    def insert_at_index(self, data, index: int):
        '''Inserts  a piece of data
           at any given index in
           the linked list.'''

        # If the given index is 0,
        # just use the function to
        # insert at the beginning.
        if index == 0:
            self.insert_at_beginning(data)
            return

        current_node = self.Head

        # This is the position that
        # will be used to compare
        # our current position to
        # the index.
        position = 0
        while current_node and position + 1 != index:
            current_node = current_node.Next
            position += 1

        if current_node:
            new_node = self.Node(data)

            # Allow the new node to inherit the
            # current node's next value and then
            # point the current node's next value
            # to the new node.
            new_node.Next = current_node.Next
            current_node.Next = new_node
        else:
            print('Index not found')

    def insert_at_end(self, data):
        '''Creates a node with the given
           data at the end of the list.'''

        new_node = self.Node(data)

        if self.Head is None:
            self.Head = new_node
            return

        current_node = self.Head

        while(current_node.Next):
            current_node = current_node.Next

        current_node.Next = new_node

    def update_node(self, data, index: int):
        '''Updates the node at
           a given index.'''

        if self.Head is None:
            print('List does not exist yet. Please create one.')
            return

        current_node = self.Head
        position = 0

        # If the current node exists AND the
        # position is not equal to the index,
        # continue to iterate.
        while current_node and position < index:
            current_node = current_node.Next
            position += 1

        if current_node:
            current_node.Data = data

        # This will trip if and only if the code
        # current_node = current_node.Next
        # points current_node to None
        # (past the end of the list).
        else:
            print('Index out of range')

    def remove_node(self, index: int):
        '''Removes a node at the given index'''

        # If the index is 0, then
        # simply remove the head
        if index == 0:
            self.remove_head()
            return

        position = 0
        current_node = self.Head

        # We check if Next is
        # not None and compare
        # position + 1 to the index
        # because we need to bridge
        # the gap between the removed
        # node, the node before, and
        # the node after, so we have
        # to stop position behind the
        # to-be-removed node.
        while current_node.Next and position + 1 < index:
            current_node = current_node.Next
            position += 1

        if current_node:
            new_connection = current_node.Next.Next
            del(current_node.Next)
            current_node.Next = new_connection
        else:
            print('Index out of range')

    def remove_head(self):
        # Assign the next node to a variable,
        # delete the current head, and then
        # assign that variable as the new head.

        new_head = self.Head.Next
        del(self.Head)
        self.Head = new_head

    def remove_tail(self):

        current_node = self.Head
        # We use the current_node.Next.Next
        # property so we can modify the second
        # to last node in the list and set it's
        # Next variable to None after removing
        # the tail.
        while current_node.Next.Next:
            current_node = current_node.Next

        # We delete all references to
        # the node, and then we set
        # the current_node.Next
        # variable to None to
        # prevent bugs
        del current_node.Next
        current_node.Next = None

    def size(self):
        '''Returns the size of
           the given linked list'''

        if self.Head is None:
            return 0

        size = 0
        current_node = self.Head

        # Iterate through the list
        # until the pointer points
        # to no node while adding
        # 1 size each time
        while current_node:
            size += 1
            current_node = current_node.Next

        return size

    def show_contents(self):
        '''Outputs the list's contents
           in string format.'''

        if self.Head is None:
            return

        current_node = self.Head
        printed_list = ''

        # Iterate while adding
        # each node's data to
        # the string.
        while current_node:
            printed_list += f'{current_node.Data} '
            current_node = current_node.Next

        return printed_list
