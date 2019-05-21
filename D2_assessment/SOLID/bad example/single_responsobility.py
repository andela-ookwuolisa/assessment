"""
The Single Responsibility Principle requires that each class
 is responsible for only one thing.

This class solves 3 different tasks: work with db,
work with items, items displaying. It should be separated
to 3 different classes.
"""
class Order:
    def get_item(self):
        pass
    def set_item(self):
        pass
    def delete_item(self):
        pass

    def show_items(self):
        pass
    def print_items(self):
        pass

    def load(self):
        pass
    def save(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass
