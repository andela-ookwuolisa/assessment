'''
This interface is bad because it includes too many methods.
And what if our product class cannot have discounts or promo codes,
or it does not make sense for it to establish the material from which it was made (for example, for books).
Thus, in order not to implement in each class methods that are not used in it,
better break the interface into several smaller ones and
implement specific interfaces with each specific class


many client-specific interfaces are better than one general-purpose interface
'''
class IItem(object):

    def apply_discount(self, discount):
        pass
    def apply_promocode(self, promo):
        pass

    def set_color(self, color):
        pass
    def set_size(self, size):
        pass

    def set_condition(self, condition):
        pass
    def set_price(self, price):
        pass
