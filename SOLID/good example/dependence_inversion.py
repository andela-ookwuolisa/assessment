'''
Dependencies within the system are based on abstractions.
Top level modules are independent of lower level modules.
Abstractions should not depend on the details. Details must depend on abstractions.
This definition can be reduced -
dependencies should be built with respect to abstractions, not details
'''
class Customer:
    current_order = None

    def buy_items(self, order_processor):
        return order_processor.checkout(self.current_order)


class IOrderProcessor:

    def checkout(self, order):
        pass

class OrderProcessor(IOrderProcessor):

    def checkout(self, order):
        "Do some cool stuff"
        pass
