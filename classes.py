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


stocks = StonkBots(money=111)
print(stocks.grapher_bot())
stocks = StonkBots(money=40)
print(stocks.percent_bot())
