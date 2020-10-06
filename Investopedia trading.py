import yfinance as yf

import importlib.util
path = "/Users/meow/programming/PycharmProjects/investopedia-trading-api/InvestopediaApi/ita.py"
spec = importlib.util.spec_from_file_location("ita", path)
ita = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ita)


# 1: Select 5-10 companies so you don't spread yourself out too thin.
# 2: Look at more that 1 month and see if there's a positive trend
# 2.5: If there is, buy 1-5, not more than 5 because that's relying too heavily on one stock.
# 3: Put the stop loss at the 10% of the current stock (as a constant)


# log in
# username = how_to_lose_money
with open('/Users/meow/Downloads/InvestopediaAccountInfo.txt', 'r') as file:
    account_info = file.read().splitlines()
client = ita.Account(account_info[0], account_info[1], 1)


companies = []
default_companies = input("Would you like to use the default companies?\n")
if default_companies.lower().strip() in ('no', 'false', 'n', 'f'):
    print("You wil be selecting some companies shortly!")
    print("Remeber, type 'quit' or 'done' to stop selecting tickers.")
    while len(companies) < 5:
        choice = input().upper()
        if choice.lower() in ('quit', 'done'):
            if len(companies) != 0:
                break
            else:
                print("You can't have 0 companies.\nQuitting bot now...")
                quit()
        else:
            if choice not in companies:
                stock = yf.Ticker(choice)
                if len(stock.history()['Open']) == 0:
                    pass  # the len() prints a status, so I'll let it do its thing
                else:
                    companies.append(choice)
                    print(f"{choice} has been added!")
            else:
                print(f"{choice} is already in your list. Remember, type 'quit' or 'done' to finish selecting.")
else:
    companies = ['AMZN', 'MSFT', 'GOOG']
print(f"Thank you for selecting your companies. Here is the full list:\n{', '.join(companies)}")
status = client.get_portfolio_status()
print(status.account_val)
print(status.buying_power)
print(status.cash)
print(status.annual_return)


# client.trade("GOOG", ita.Action.short, 2)
# client.trade("GOOG", ita.Action.buy, 10, "Limit", 500)

######################################################
######################################################
# bots thing

class StonkBots:
    def __init__(self, money, stock_list, shares, last_2_stock, comp):
        self.balance = float(money)
        self.market = stock_list
        self.curr_stock = last_2_stock[1]
        self.prev_stock = last_2_stock[0]
        self.company = comp
        self.num_shares = int(shares)

    # graphs a bezier curve from lst 2-5 points, takes average from all of em

    def grapher_bot(self):
        """Does some things idk what tho"""
        y_average = sum(self.market) / len(self.market)
        next_point = (len(self.market), self.market[-1] + y_average)

    # takes last 2 points, if they're going up, invest, going down, sell

    def percent_bot(self):
        pass

    # takes all tips from avijit and combines it

    def avijit_bot(self):
        """ Combines all of avijits advice into one package.
        (The stop loss will be done outside of the function)"""
        avg = sum(self.market)/len(self.market)
        if self.market[0] < avg < self.market[-1]:  # if market is rising, large scale
            buy_amount = self.balance // self.curr_stock
            if self.curr_stock >= self.prev_stock:  # if market is rising, small scale
                if buy_amount > 5:
                    buy_amount = 5
                if buy_amount > 1:
                    self.balance = buy(self.company, buy_amount, self.balance, self.curr_stock)
                    self.num_shares += buy_amount
            else:
                if self.num_shares > 5:
                    sell_amount = 5
                else:
                    sell_amount = self.num_shares
                if self.num_shares > 1:
                    self.balance = sell(self.company, sell_amount, self.balance, self.curr_stock)
                    self.num_shares -= sell_amount
        else:
            if self.num_shares > 1:
                sell(self.company, self.num_shares, self.balance, self.curr_stock)
                self.num_shares = 0
        return self.balance


def sell(company, amount, money, share_price):
    #client.trade(company, ita.Action.sell, amount)
    print(f"Sold {amount} shares of {company} for ${share_price} each, totaling ${amount * share_price}")
    return money + share_price * amount


def buy(company, amount, money, share_price):
    #client.trade(company, ita.Action.buy, amount)
    print(f"Bought {amount} shares of {company} for ${share_price} each, totaling ${amount * share_price}")
    return money - amount * share_price
#######################################################
#######################################################
# thing


stock_data = yf.download(
    tickers=' '.join(companies),
    period='1mo',
)

stocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
bot = StonkBots(
    money=status.buying_power,
    stock_list=stocks,
    shares=2,
    last_2_stock=[stocks[-2], stocks[-1]],
    comp='GOOG')

calcs = bot.avijit_bot()
print(f"Bots balance = {calcs}")
