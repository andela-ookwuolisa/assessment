"""
The Single Responsibility Principle requires that each class is 
responsible for only one thing.

Each class should solve one concrete task! No more, no less.
"""


class Order:
    def get_item(self):
        pass

    def set_item(self):
        pass

    def delete_item(self):
        pass


class OrderRepository:
    def load(self):
        pass

    def save(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class OrderViewer:
    def show_items(self):
        pass

    def print_items(self):
        pass
