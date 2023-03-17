class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_item(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def remove_item(self, data):
        curr_node = self.head
        prev_node = None
        while curr_node:
            if curr_node.data == data:
                if prev_node:
                    prev_node.next = curr_node.next
                else:
                    self.head = curr_node.next
                return True
            prev_node = curr_node
            curr_node = curr_node.next
        return False

    def print_items(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.name} - Rp {self.price}'


class Store:
    def __init__(self):
        self.inventory = LinkedList()

    def add_item(self, item):
        self.inventory.add_item(item)

    def remove_item(self, item):
        return self.inventory.remove_item(item)

    def update_item(self, item, new_name=None, new_price=None):
        curr_node = self.inventory.head
        while curr_node:
            if curr_node.data == item:
                if new_name:
                    curr_node.data.name = new_name
                if new_price:
                    curr_node.data.price = new_price
                return True
            curr_node = curr_node.next
        return False

    def print_inventory(self):
        self.inventory.print_items()


store = Store()
store.add_item(Item('Bola Sepak', 50000))
store.add_item(Item('Bola Basket', 70000))
store.add_item(Item('Bola Voli', 55000))

store.print_inventory()

store.remove_item(Item('Bola Basket', 70000))

store.update_item(Item('Bola Sepak', 50000), new_price=60000)

store.add_item(Item('Bola Tenis', 65000))

store.print_inventory()
