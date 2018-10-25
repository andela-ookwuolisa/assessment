'''
High-level modules should not depend on low-level modules. Both should depend on abstractions.
Abstractions should not depend on details. Details should depend on abstractions.

Everything seems quite logical. But there is one problem -
Customer class depends on OrderProcessor class
(moreover, the principle of openness / closeness is not fulfilled).
In order to get rid of dependence on a particular class,
you need to make Customer depend on abstraction,
those. from the IOrderProcessor interface.

'''
class Customer:
    current_order = None

    def buy_items(self):
        processor = OrderProcessor()
        return processor.checkout(self.current_order)


class OrderProcessor:
    def checkout(self, order):
        pass
