# accepts only 2-number-parameter-tuples
class TupleT:
    # EXAMPLE: (1, 1) -> (-1, -1)
    @staticmethod
    def negative(tup):
        return -tup[0], -tup[1]

    @staticmethod
    def add(tup1, tup2):
        return tup1[0]+tup2[0], tup1[1]+tup2[1]

    @staticmethod
    def add_value(tup1, value):
        return tup1[0] + value, tup1[1] + value

    @staticmethod
    def subtract(tup1, tup2):
        return tup1[0]-tup2[0], tup1[1]-tup2[1]

    @staticmethod
    def subtract_value(tup1, value):
        return tup1[0] - value, tup1[1] - value

    @staticmethod
    def multiply(tup1, tup2):
        return tup1[0]*tup2[0], tup1[1]*tup2[1]

    @staticmethod
    def multiply_by_value(tup1, value):
        return tup1[0] * value, tup1[1] * value

    @staticmethod
    def devide(tup1, tup2):
        return tup1[0]/tup2[0], tup1[1]/tup2[1]

    @staticmethod
    def devide_by_value(tup1, value):
        return tup1[0] / value, tup1[1] / value

    @staticmethod
    def round(tup):
        return round(tup[0]), round(tup[1])
