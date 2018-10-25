'''
Many client-specific interfaces are better than one general-purpose interface.

Many specialized interfaces are better than one universal.
Adherence to this principle is necessary in order for client classes
the using / implementing interface knew only about the methods they use,
which leads to a decrease in the amount of unused code.
'''
class IItem(object):

    def set_condition(self, condition):
        pass

    def set_price(self, price):
        pass


class ICloses(object):

    def set_color(self, color):
        pass

    def set_size(self, size):
        pass


class IDiscountable(object):

    def set_promocode(self, promo):
        pass

    def set_discount(self, discount):
        pass
