import math as m

'''
PROBLEM -> formulate 
    -> MATH MODEL -> resolve 
        -> CONCLUSION -> interpret 
            -> PREDICTION -> test
'''


class MathFunction:
    straight_line_equation = ['y=m*x+b', '(y-y1)=m*(x-x1)']
    slope = ['m=y/(x+b)', 'm=(y2-y1)/(x2-x1)']
    circle = 'x**2+y**2=r**2'

    # elements = array
    # image = number
    # domain = string
    # f_range = string
    # independent_var = char
    # dependent_vars = char|array
    # graph = Graph

    def __init__(self, elements):
        self.elements = elements
        self.domain = self.set_domain
        self.f_range = self.set_range

    def find_value(self, dependent_values):
        # return calc(self.elements, dependent_values)
        pass

    def evaluate(self, expression):
        # return simplify(self.elements, expression)
        pass

    def set_domain(self):
        # if self.elements ...
        pass

    def get_domain(self):
        # return self.domain
        pass

    def set_range(self):
        # if self.elements ...
        pass

    def get_range(self):
        # return self.range
        pass

    def graph(self):
        # return self.graph
        pass

    def get_parity(self):
        pass

    def get_increase_type(self, x1, x2):
        if self.find_value(x1) < self.find_value(x2):
            return 'increasing'
        elif self.find_value(x1) > self.find_value(x2):
            return 'decreasing'
        else:
            return 'constant'

    @staticmethod
    def get_value_of_circle(r, x):
        upper = m.sqrt((r**2) - (x**2))
        lower = upper*(-1)
        return [upper, lower]

    @staticmethod
    def get_change_in_x(x1, x2):
        return x2 - x1

    @staticmethod
    def get_change_in_y(y1, y2):
        return y2 - y1

    def get_distance(self, x1, x2, y1, y2):
        horizontal_square = m.pow(self.get_change_in_x(x1, x2), 2)
        vertical_square = m.pow(self.get_change_in_y(y1, y2), 2)
        return m.sqrt(horizontal_square + vertical_square)
