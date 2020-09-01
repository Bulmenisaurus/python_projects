import yfinance as yf
import matplotlib.pyplot as plt


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
        choice = input()
        if choice.lower() in ('quit', 'done'):
            if len(companies) != 0:
                break
            else:
                print("You can't have 0 companies.\nQuitting bot now...")
                quit()
        else:
            if choice not in companies:
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


#client.trade("GOOG", ita.Action.short, 2)
#client.trade("GOOG", ita.Action.buy, 10, "Limit", 500)
print('GOOG:')
print(ita.get_quote("GOOG"))


#######################################################
#######################################################
# plot data (testing purposes only)