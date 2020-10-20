from math import floor

class StonkBots:
    def __init__(self, money=0):
        self.cash = float(money)

    def __call__(self):
        print("Bot network booting up....")

    def grapher_bot(self):
        if self.cash < 10.0:
            stonks = "Graph stonks = bad :("
        else:
            stonks = 'Graph stonks = good :)'
        self.cash = 10
        return f"Grapher bot has run the calculations, and the result is '{stonks}'"

    def percent_bot(self):
        if floor(self.cash) % 2 == 0:
            stonks = "Percent stonks = bad :("
        else:
            stonks = "Percent stonks = good :)"
        print("stonk")
        return f"Percent bot has run the calculations, and the result is '{stonks}'"

"""
stocks = StonkBots(money=111)
print(stocks.grapher_bot())
stocks = StonkBots(money=40)
print(stocks.percent_bot())
"""


class DividableList(list):
    def __floordiv__(self, divisor):
        return_lists_len = len(self) // divisor
        num_of_full_lists = divisor
        return_list = []
        for x in range(num_of_full_lists):
            return_list.append(self[x*return_lists_len:x*return_lists_len+return_lists_len])
        return return_list

    __truediv__ = __floordiv__  # how would you do decimal with integers???

    def __mod__(self, modulisor):
        modulo = len(self) % modulisor
        return self[-modulo:]


a = DividableList(['x', 'z', 'z', 'a', 'a', 'b', 'a', '2', '3'])
print(a / 3)
print(a % 4)
